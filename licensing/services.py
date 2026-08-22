from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import (
    LicenseProduct, LicenseRequest, LicenseTerms, 
    NegotiationProposal, Agreement, SignatureRequest
)

class LicenseService:
    @staticmethod
    def _validate_request_transition(request: LicenseRequest, target_state: str):
        valid_transitions = {
            LicenseRequest.Status.DRAFT: [LicenseRequest.Status.SUBMITTED],
            LicenseRequest.Status.SUBMITTED: [LicenseRequest.Status.UNDER_REVIEW, LicenseRequest.Status.REJECTED],
            LicenseRequest.Status.UNDER_REVIEW: [LicenseRequest.Status.NEGOTIATION, LicenseRequest.Status.REJECTED],
            LicenseRequest.Status.NEGOTIATION: [LicenseRequest.Status.TERMS_AGREED, LicenseRequest.Status.CANCELLED],
            LicenseRequest.Status.TERMS_AGREED: [LicenseRequest.Status.AGREEMENT_PENDING],
            LicenseRequest.Status.AGREEMENT_PENDING: [LicenseRequest.Status.SIGNED],
            LicenseRequest.Status.SIGNED: [LicenseRequest.Status.ACTIVE],
            LicenseRequest.Status.ACTIVE: [LicenseRequest.Status.EXPIRED, LicenseRequest.Status.TERMINATED],
        }
        
        if target_state not in valid_transitions.get(request.status, []):
            raise ValidationError(f"Invalid transition from {request.status} to {target_state}")

        if target_state == LicenseRequest.Status.ACTIVE:
            # Check KYC
            if request.organization.verification_status != 'verified':
                raise ValidationError("Organization must be verified before activation.")
                
            # Check signatures
            agreement = request.agreement
            if agreement.status != Agreement.Status.FULLY_SIGNED:
                raise ValidationError("Agreement must be fully signed before activation.")
                
            # Check project approval
            if request.product.approved_review_case.state != 'approved':
                raise ValidationError("Project review case is no longer approved.")

    @staticmethod
    @transaction.atomic
    def transition_request(request: LicenseRequest, target_state: str):
        LicenseService._validate_request_transition(request, target_state)
        request.status = target_state
        request.save()
        return request

    @staticmethod
    @transaction.atomic
    def propose_terms(request: LicenseRequest, author, terms_data: dict, message: str, is_counter: bool = False):
        if request.status not in [LicenseRequest.Status.UNDER_REVIEW, LicenseRequest.Status.NEGOTIATION]:
            raise ValidationError("Cannot propose terms in current state.")
            
        current_version = request.terms_versions.count()
        new_version = current_version + 1
        
        # We ensure financial fields are Decimals (handled by Django DecimalField automatically from strings/numbers, but we enforce types in validation if needed)
        terms = LicenseTerms.objects.create(
            request=request,
            version=new_version,
            pricing_type=terms_data.get('pricing_type', 'fixed'),
            amount=terms_data.get('amount', 0),
            currency=terms_data.get('currency', 'USD'),
            is_commercial=terms_data.get('is_commercial', False),
            ai_training_permitted=terms_data.get('ai_training_permitted', False),
            duration_days=terms_data.get('duration_days', 365)
        )
        
        proposal = NegotiationProposal.objects.create(
            request=request,
            terms=terms,
            author=author,
            message=message,
            is_counter=is_counter
        )
        
        if request.status == LicenseRequest.Status.UNDER_REVIEW:
            LicenseService.transition_request(request, LicenseRequest.Status.NEGOTIATION)
            
        return proposal

    @staticmethod
    @transaction.atomic
    def accept_terms(request: LicenseRequest, terms: LicenseTerms):
        if terms.request != request:
            raise ValidationError("Terms do not belong to this request.")
            
        terms.is_accepted = True
        terms.save()
        
        LicenseService.transition_request(request, LicenseRequest.Status.TERMS_AGREED)
        
        # Auto generate agreement draft
        agreement = Agreement.objects.create(
            request=request,
            terms=terms,
            status=Agreement.Status.DRAFT
        )
        
        return agreement

    @staticmethod
    @transaction.atomic
    def sign_agreement(agreement: Agreement, signer):
        req, created = SignatureRequest.objects.get_or_create(
            agreement=agreement,
            signer=signer,
            defaults={'status': SignatureRequest.Status.PENDING}
        )
        
        if req.status == SignatureRequest.Status.SIGNED:
            raise ValidationError("Already signed by this user.")
            
        req.status = SignatureRequest.Status.SIGNED
        req.signed_at = timezone.now()
        req.save()
        
        # Check if all required parties signed. For simplicity, assume Owner + Licensee Org Owner
        required_signers = {agreement.request.product.project.owner.id, agreement.request.organization.owner.id}
        actual_signers = set(agreement.signatures.filter(status=SignatureRequest.Status.SIGNED).values_list('signer_id', flat=True))
        
        if required_signers.issubset(actual_signers):
            agreement.status = Agreement.Status.FULLY_SIGNED
            agreement.save()
            LicenseService.transition_request(agreement.request, LicenseRequest.Status.SIGNED)
        else:
            agreement.status = Agreement.Status.PARTIALLY_SIGNED
            agreement.save()
            
        return agreement

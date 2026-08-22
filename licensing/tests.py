import pytest
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from projects.models import Project, Category
from reviews.models import ReviewCase
from licensing.models import (
    Organization, LicenseType, LicenseProduct, LicenseRequest,
    LicenseTerms, NegotiationProposal, Agreement, SignatureRequest
)
from licensing.services import LicenseService

User = get_user_model()

@pytest.fixture
def license_setup(db):
    owner = User.objects.create_user(email='owner@example.com', password='pw')
    licensee_user = User.objects.create_user(email='licensee@example.com', password='pw')
    
    cat = Category.objects.create(name='Cat')
    proj = Project.objects.create(name='Proj', owner=owner, category=cat)
    
    from repositories.models import RepositoryConnection, AnalysisSnapshot
    conn = RepositoryConnection.objects.create(project=proj, repo_url='http://fake.git')
    snap = AnalysisSnapshot.objects.create(repository=conn, commit_hash='abc', branch='main')
    
    # Mock an approved review case
    case = ReviewCase.objects.create(project=proj, snapshot=snap, state=ReviewCase.State.APPROVED)
    
    org = Organization.objects.create(
        name='Test Org', owner=licensee_user, verification_status=Organization.VerificationStatus.VERIFIED
    )
    
    ltype = LicenseType.objects.create(name='Commercial', code='COMM', is_commercial=True)
    
    product = LicenseProduct.objects.create(
        project=proj, approved_review_case=case, status=LicenseProduct.Status.AVAILABLE
    )
    product.available_types.add(ltype)
    
    req = LicenseRequest.objects.create(
        product=product, organization=org, requested_type=ltype, status=LicenseRequest.Status.DRAFT
    )
    
    return owner, licensee_user, org, product, req

@pytest.mark.django_db
class TestLicensingWorkflow:
    def test_decimal_pricing(self, license_setup):
        _, licensee, _, _, req = license_setup
        
        LicenseService.transition_request(req, LicenseRequest.Status.SUBMITTED)
        LicenseService.transition_request(req, LicenseRequest.Status.UNDER_REVIEW)
        
        prop = LicenseService.propose_terms(
            req, licensee, {'amount': Decimal('199.99'), 'pricing_type': 'periodic'}, "Here is my offer"
        )
        
        assert isinstance(prop.terms.amount, Decimal)
        assert prop.terms.amount == Decimal('199.99')

    def test_activation_blocked_if_unverified_org(self, license_setup):
        owner, licensee, org, product, req = license_setup
        
        org.verification_status = Organization.VerificationStatus.PENDING
        org.save()
        
        req.status = LicenseRequest.Status.SIGNED
        req.save()
        
        with pytest.raises(ValidationError, match="Organization must be verified"):
            LicenseService.transition_request(req, LicenseRequest.Status.ACTIVE)

    def test_full_agreement_workflow(self, license_setup):
        owner, licensee, org, product, req = license_setup
        
        LicenseService.transition_request(req, LicenseRequest.Status.SUBMITTED)
        LicenseService.transition_request(req, LicenseRequest.Status.UNDER_REVIEW)
        
        # Propose
        prop = LicenseService.propose_terms(
            req, owner, {'amount': Decimal('500.00'), 'pricing_type': 'fixed'}, "My terms"
        )
        
        # Accept
        agreement = LicenseService.accept_terms(req, prop.terms)
        assert req.status == LicenseRequest.Status.TERMS_AGREED
        assert agreement.status == Agreement.Status.DRAFT
        
        # Manually move to pending
        LicenseService.transition_request(req, LicenseRequest.Status.AGREEMENT_PENDING)
        
        # Signatures
        LicenseService.sign_agreement(agreement, owner)
        assert agreement.status == Agreement.Status.PARTIALLY_SIGNED
        
        LicenseService.sign_agreement(agreement, licensee)
        assert agreement.status == Agreement.Status.FULLY_SIGNED
        assert req.status == LicenseRequest.Status.SIGNED
        
        # Activate
        LicenseService.transition_request(req, LicenseRequest.Status.ACTIVE)
        assert req.status == LicenseRequest.Status.ACTIVE

    def test_blocked_if_project_not_approved(self, license_setup):
        owner, licensee, org, product, req = license_setup
        
        # Demote project approval
        product.approved_review_case.state = ReviewCase.State.DRAFT
        product.approved_review_case.save()
        
        req.status = LicenseRequest.Status.SIGNED
        req.save()
        
        # Create dummy fully signed agreement to bypass signature check
        terms = LicenseTerms.objects.create(request=req)
        Agreement.objects.create(request=req, terms=terms, status=Agreement.Status.FULLY_SIGNED)
        
        with pytest.raises(ValidationError, match="no longer approved"):
            LicenseService.transition_request(req, LicenseRequest.Status.ACTIVE)

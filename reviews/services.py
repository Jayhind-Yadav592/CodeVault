from django.db import transaction
from django.core.exceptions import ValidationError
from .models import ReviewCase, ReviewTransitionHistory, ReviewChecklistItem
from compliance.models import RuleResult
from security.models import Finding

class ReviewService:
    @staticmethod
    def _validate_transition(case: ReviewCase, target_state: str, actor):
        valid_transitions = {
            ReviewCase.State.DRAFT: [ReviewCase.State.SUBMITTED],
            ReviewCase.State.SUBMITTED: [ReviewCase.State.TRIAGE],
            ReviewCase.State.TRIAGE: [ReviewCase.State.TECHNICAL_REVIEW, ReviewCase.State.REJECTED],
            ReviewCase.State.TECHNICAL_REVIEW: [ReviewCase.State.IP_REVIEW, ReviewCase.State.REMEDIATION_REQUIRED],
            ReviewCase.State.IP_REVIEW: [ReviewCase.State.SECURITY_REVIEW, ReviewCase.State.REMEDIATION_REQUIRED],
            ReviewCase.State.SECURITY_REVIEW: [ReviewCase.State.COMPLIANCE_REVIEW, ReviewCase.State.REMEDIATION_REQUIRED],
            ReviewCase.State.COMPLIANCE_REVIEW: [ReviewCase.State.FINAL_REVIEW, ReviewCase.State.REMEDIATION_REQUIRED],
            ReviewCase.State.FINAL_REVIEW: [ReviewCase.State.APPROVED, ReviewCase.State.REJECTED, ReviewCase.State.REMEDIATION_REQUIRED],
            ReviewCase.State.REMEDIATION_REQUIRED: [],
            ReviewCase.State.APPROVED: [],
            ReviewCase.State.REJECTED: [],
        }
        
        if target_state not in valid_transitions.get(case.state, []):
            raise ValidationError(f"Invalid transition from {case.state} to {target_state}")
            
        if target_state == ReviewCase.State.APPROVED:
            # Block approval if checklist items are missing or failing
            unresolved = case.checklist_items.exclude(status__in=[
                ReviewChecklistItem.Status.PASS, 
                ReviewChecklistItem.Status.NOT_APPLICABLE
            ])
            if unresolved.exists():
                raise ValidationError("Cannot approve: there are unresolved checklist items.")
                
            # Block approval if critical security findings remain
            critical_findings = Finding.objects.filter(
                snapshot=case.snapshot,
                severity=Finding.Severity.CRITICAL,
                status=Finding.Status.OPEN
            )
            if critical_findings.exists():
                raise ValidationError("Cannot approve: unresolved critical security findings.")
                
            # Check compliance eval
            if case.compliance_evaluation:
                failed_rules = case.compliance_evaluation.rule_results.filter(
                    status=RuleResult.Status.FAIL,
                    is_critical_failure=True
                )
                if failed_rules.exists():
                    raise ValidationError("Cannot approve: unresolved critical compliance failures.")
                    
            # Check ownership declaration
            if not case.project.declarations.filter(status='signed').exists():
                raise ValidationError("Cannot approve: Missing signed ownership declaration.")

    @staticmethod
    @transaction.atomic
    def transition_case(case: ReviewCase, target_state: str, actor, reason: str = ""):
        ReviewService._validate_transition(case, target_state, actor)
        
        previous_state = case.state
        case.state = target_state
        case.save()
        
        ReviewTransitionHistory.objects.create(
            case=case,
            actor=actor,
            previous_state=previous_state,
            new_state=target_state,
            reason=reason
        )
        
        return case

    @staticmethod
    def generate_checklist(case: ReviewCase):
        # Generate default items
        items = [
            (ReviewCase.State.TECHNICAL_REVIEW, "Application executes successfully"),
            (ReviewCase.State.TECHNICAL_REVIEW, "Documentation is sufficient"),
            (ReviewCase.State.IP_REVIEW, "Ownership declaration verified"),
            (ReviewCase.State.IP_REVIEW, "No employer-owned indicators"),
            (ReviewCase.State.SECURITY_REVIEW, "No unresolved critical secrets"),
            (ReviewCase.State.COMPLIANCE_REVIEW, "LOC and Commits requirements met")
        ]
        
        for stage, title in items:
            ReviewChecklistItem.objects.get_or_create(
                case=case,
                stage=stage,
                title=title
            )

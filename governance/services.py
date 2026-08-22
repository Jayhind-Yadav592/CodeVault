from django.utils import timezone
from .models import Policy, PolicyVersion, Risk, Exception, Control, ControlEvaluation
from django.core.exceptions import ValidationError

class PolicyWorkflowService:
    @staticmethod
    def approve_policy_version(policy_version: PolicyVersion, user):
        if policy_version.is_active:
            raise ValidationError("Policy version is already active and immutable.")
        
        # Deactivate all other versions
        PolicyVersion.objects.filter(policy=policy_version.policy, is_active=True).update(is_active=False)
        
        policy_version.is_active = True
        policy_version.save()
        
        policy = policy_version.policy
        policy.status = Policy.Status.ACTIVE
        policy.save()

    @staticmethod
    def validate_immutability(policy_version: PolicyVersion):
        if policy_version.is_active:
            raise ValidationError("Cannot modify an active policy version. Create a new version.")

class RiskScoringService:
    @staticmethod
    def calculate_score(risk: Risk):
        # Deterministic scoring: Likelihood (1-5) * Impact (1-5)
        score = risk.likelihood * risk.impact
        risk.inherent_risk_score = score
        risk.save(update_fields=['inherent_risk_score'])
        return score
        
    @staticmethod
    def get_risk_level(score: int) -> str:
        if score >= 20:
            return 'CRITICAL'
        elif score >= 15:
            return 'HIGH'
        elif score >= 8:
            return 'MEDIUM'
        return 'LOW'

class ExceptionManagerService:
    @staticmethod
    def check_and_expire_exceptions():
        now = timezone.now().date()
        expired = Exception.objects.filter(
            status=Exception.Status.APPROVED,
            expiration_date__lt=now
        )
        for exc in expired:
            exc.status = Exception.Status.EXPIRED
            exc.save(update_fields=['status'])
            
class GapAnalysisService:
    @staticmethod
    def analyze_project(project, framework):
        # Enforce expiration before analyzing
        ExceptionManagerService.check_and_expire_exceptions()
        
        controls = framework.controls.all()
        gaps = []
        
        for control in controls:
            # Check exceptions
            valid_exception = Exception.objects.filter(
                project=project,
                control=control,
                status=Exception.Status.APPROVED
            ).exists()
            
            if valid_exception:
                gaps.append({
                    'control': control.name,
                    'status': 'EXCEPTION_GRANTED',
                    'missing': None
                })
                continue
                
            eval_record = ControlEvaluation.objects.filter(
                project=project, control=control
            ).order_by('-evaluation_date').first()
            
            if not eval_record or eval_record.status != ControlEvaluation.Status.PASS:
                status = eval_record.status if eval_record else 'NOT_TESTED'
                gaps.append({
                    'control': control.name,
                    'status': status,
                    'missing': control.evidence_requirements
                })
        return gaps

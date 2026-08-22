from compliance.models import ComplianceRule, RuleResult

class RuleContext:
    def __init__(self, evaluation, repo_path=None):
        self.evaluation = evaluation
        self.snapshot = evaluation.snapshot
        self.policy = evaluation.policy
        self.project = self.snapshot.repository.project
        self.repo_path = repo_path

class BaseRule:
    rule_id = None
    name = None
    description = None
    category = None
    severity = None
    requires_file_scan = False

    @classmethod
    def get_or_create_model(cls):
        rule, _ = ComplianceRule.objects.get_or_create(
            rule_id=cls.rule_id,
            defaults={
                'name': cls.name,
                'description': cls.description,
                'category': cls.category,
                'severity': cls.severity,
            }
        )
        return rule

    def evaluate(self, context: RuleContext):
        raise NotImplementedError

    def _pass(self, evidence, score=1.0):
        return {'status': RuleResult.Status.PASS, 'evidence': evidence, 'score_contribution': score}
        
    def _fail(self, evidence, remediation="", critical=False, score=0.0):
        return {
            'status': RuleResult.Status.FAIL, 'evidence': evidence, 
            'remediation': remediation, 'is_critical_failure': critical,
            'score_contribution': score
        }

    def _warning(self, evidence, remediation="", score=0.5):
        return {'status': RuleResult.Status.WARNING, 'evidence': evidence, 'remediation': remediation, 'score_contribution': score}

    def _unknown(self, evidence, remediation="", score=0.0):
        return {'status': RuleResult.Status.UNKNOWN, 'evidence': evidence, 'remediation': remediation, 'score_contribution': score}
        
    def _not_applicable(self, evidence, score=1.0):
        return {'status': RuleResult.Status.NOT_APPLICABLE, 'evidence': evidence, 'score_contribution': score}

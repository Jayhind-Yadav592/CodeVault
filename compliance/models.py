from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from repositories.models import AnalysisSnapshot

class CompliancePolicy(UUIDModel, TimeStampedModel):
    version = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=False)
    
    # Requirements Configuration
    min_meaningful_loc = models.PositiveIntegerField(default=50000)
    min_meaningful_commits = models.PositiveIntegerField(default=5)
    min_meaningful_prs = models.PositiveIntegerField(default=4)
    
    # Weights for Scoring
    weight_repository = models.FloatField(default=20.0)
    weight_git_history = models.FloatField(default=15.0)
    weight_code_quality = models.FloatField(default=15.0)
    weight_documentation = models.FloatField(default=10.0)
    weight_testing = models.FloatField(default=10.0)
    weight_security = models.FloatField(default=10.0)
    weight_licensing_ip = models.FloatField(default=15.0)
    weight_ownership = models.FloatField(default=5.0)

    def save(self, *args, **kwargs):
        if self.is_active:
            CompliancePolicy.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Policy {self.version}"

class ComplianceRule(UUIDModel, TimeStampedModel):
    class Category(models.TextChoices):
        REPOSITORY = 'repository', _('Repository Requirements')
        GIT_HISTORY = 'git_history', _('Git History')
        CODE_QUALITY = 'code_quality', _('Code Quality')
        DOCUMENTATION = 'documentation', _('Documentation')
        TESTING = 'testing', _('Testing')
        SECURITY = 'security', _('Security')
        LICENSING = 'licensing', _('Licensing / IP')
        OWNERSHIP = 'ownership', _('Ownership')

    class Severity(models.TextChoices):
        INFO = 'info', _('Info')
        WARNING = 'warning', _('Warning')
        CRITICAL = 'critical', _('Critical')

    rule_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=Category.choices)
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.WARNING)
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.rule_id} - {self.name}"

class ComplianceEvaluation(UUIDModel, TimeStampedModel):
    class Decision(models.TextChoices):
        ELIGIBLE = 'eligible', _('Eligible')
        INELIGIBLE = 'ineligible', _('Ineligible')
        CONDITIONALLY_ELIGIBLE = 'conditionally_eligible', _('Conditionally Eligible')
        REQUIRES_HUMAN_REVIEW = 'requires_human_review', _('Requires Human Review')
        INSUFFICIENT_DATA = 'insufficient_data', _('Insufficient Data')

    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.CASCADE, related_name='evaluations')
    policy = models.ForeignKey(CompliancePolicy, on_delete=models.RESTRICT)
    
    overall_score = models.FloatField(default=0.0)
    decision = models.CharField(max_length=50, choices=Decision.choices, default=Decision.INSUFFICIENT_DATA)
    
    passed_rules = models.PositiveIntegerField(default=0)
    failed_rules = models.PositiveIntegerField(default=0)
    warnings = models.PositiveIntegerField(default=0)
    unknown_rules = models.PositiveIntegerField(default=0)
    critical_findings = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Eval {self.id} for {self.snapshot.repository.project.name} - {self.decision}"

class RuleResult(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PASS = 'pass', _('Pass')
        FAIL = 'fail', _('Fail')
        WARNING = 'warning', _('Warning')
        NOT_APPLICABLE = 'not_applicable', _('Not Applicable')
        UNKNOWN = 'unknown', _('Unknown')

    evaluation = models.ForeignKey(ComplianceEvaluation, on_delete=models.CASCADE, related_name='rule_results')
    rule = models.ForeignKey(ComplianceRule, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=20, choices=Status.choices)
    evidence = models.JSONField(default=dict)
    remediation = models.TextField(blank=True)
    is_critical_failure = models.BooleanField(default=False)
    score_contribution = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('evaluation', 'rule')

    def __str__(self):
        return f"{self.rule.name} - {self.status}"

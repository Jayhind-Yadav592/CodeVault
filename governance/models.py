from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from licensing.models import Organization
from projects.models import Project

class Policy(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        UNDER_REVIEW = 'under_review', _('Under Review')
        APPROVED = 'approved', _('Approved')
        ACTIVE = 'active', _('Active')
        RETIRED = 'retired', _('Retired')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='policies')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='owned_policies')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    effective_date = models.DateField(null=True, blank=True)
    review_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.organization.name})"

class PolicyVersion(UUIDModel, TimeStampedModel):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=50)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('policy', 'version_number')

    def __str__(self):
        return f"{self.policy.name} - v{self.version_number}"

class Framework(UUIDModel, TimeStampedModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='frameworks')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} {self.version}"

class Control(UUIDModel, TimeStampedModel):
    class Severity(models.TextChoices):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')
        CRITICAL = 'critical', _('Critical')

    framework = models.ForeignKey(Framework, on_delete=models.CASCADE, related_name='controls')
    control_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    objective = models.TextField()
    category = models.CharField(max_length=100)
    
    severity = models.CharField(max_length=20, choices=Severity.choices, default=Severity.MEDIUM)
    evidence_requirements = models.TextField(blank=True)
    
    def __str__(self):
        return f"[{self.control_id}] {self.name}"

class Evidence(UUIDModel, TimeStampedModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='evidence')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    
    name = models.CharField(max_length=255)
    evidence_type = models.CharField(max_length=100)
    source_reference = models.CharField(max_length=255)  # E.g., snapshot ID, scan ID
    
    collected_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    integrity_hash = models.CharField(max_length=255, blank=True)

class ControlEvaluation(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PASS = 'pass', _('Pass')
        FAIL = 'fail', _('Fail')
        PARTIAL = 'partial', _('Partial')
        NOT_TESTED = 'not_tested', _('Not Tested')
        NOT_APPLICABLE = 'not_applicable', _('Not Applicable')
        UNKNOWN = 'unknown', _('Unknown')

    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name='evaluations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='control_evaluations')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NOT_TESTED)
    evidence = models.ManyToManyField(Evidence, blank=True)
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    evaluation_date = models.DateTimeField(auto_now_add=True)
    policy_version = models.ForeignKey(PolicyVersion, on_delete=models.SET_NULL, null=True, blank=True)

class Risk(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        MITIGATING = 'mitigating', _('Mitigating')
        ACCEPTED = 'accepted', _('Accepted')
        TRANSFERRED = 'transferred', _('Transferred')
        CLOSED = 'closed', _('Closed')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='risks')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    likelihood = models.IntegerField(default=1) # 1-5
    impact = models.IntegerField(default=1) # 1-5
    inherent_risk_score = models.IntegerField(default=1)
    
    controls = models.ManyToManyField(Control, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    due_date = models.DateField(null=True, blank=True)

class RiskTreatment(UUIDModel, TimeStampedModel):
    class ActionType(models.TextChoices):
        MITIGATE = 'mitigate', _('Mitigate')
        ACCEPT = 'accept', _('Accept')
        TRANSFER = 'transfer', _('Transfer')
        AVOID = 'avoid', _('Avoid')

    risk = models.ForeignKey(Risk, on_delete=models.CASCADE, related_name='treatments')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=ActionType.choices)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='planned')

class Exception(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        REQUESTED = 'requested', _('Requested')
        UNDER_REVIEW = 'under_review', _('Under Review')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'rejected', _('Rejected')
        EXPIRED = 'expired', _('Expired')
        REVOKED = 'revoked', _('Revoked')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='exceptions')
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    
    reason = models.TextField()
    compensating_control = models.TextField(blank=True)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='requested_exceptions')
    approver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='approved_exceptions')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REQUESTED)
    
    start_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project
from repositories.models import AnalysisSnapshot
from security.models import Finding
from compliance.models import ComplianceEvaluation

class ReviewCase(UUIDModel, TimeStampedModel):
    class State(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        SUBMITTED = 'submitted', _('Submitted')
        TRIAGE = 'triage', _('Triage')
        TECHNICAL_REVIEW = 'technical_review', _('Technical Review')
        IP_REVIEW = 'ip_review', _('IP Review')
        SECURITY_REVIEW = 'security_review', _('Security Review')
        COMPLIANCE_REVIEW = 'compliance_review', _('Compliance Review')
        FINAL_REVIEW = 'final_review', _('Final Review')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'rejected', _('Rejected')
        REMEDIATION_REQUIRED = 'remediation_required', _('Remediation Required')

    class Priority(models.TextChoices):
        LOW = 'low', _('Low')
        NORMAL = 'normal', _('Normal')
        HIGH = 'high', _('High')
        URGENT = 'urgent', _('Urgent')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='review_cases')
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.RESTRICT, related_name='review_cases')
    compliance_evaluation = models.ForeignKey(ComplianceEvaluation, on_delete=models.RESTRICT, null=True, blank=True)
    
    state = models.CharField(max_length=30, choices=State.choices, default=State.DRAFT)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.NORMAL)
    due_date = models.DateTimeField(null=True, blank=True)
    
    previous_case = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='follow_up_cases')
    
    def __str__(self):
        return f"Review {self.id} - {self.project.name} ({self.state})"

class ReviewerAssignment(UUIDModel, TimeStampedModel):
    class Role(models.TextChoices):
        TECHNICAL = 'technical', _('Technical Reviewer')
        IP = 'ip', _('IP Reviewer')
        SECURITY = 'security', _('Security Reviewer')
        COMPLIANCE = 'compliance', _('Compliance Reviewer')
        FINAL = 'final', _('Final Approver')
        
    case = models.ForeignKey(ReviewCase, on_delete=models.CASCADE, related_name='assignments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_assignments')
    role = models.CharField(max_length=20, choices=Role.choices)
    
    class Meta:
        unique_together = ('case', 'user', 'role')

class ReviewTransitionHistory(UUIDModel, TimeStampedModel):
    case = models.ForeignKey(ReviewCase, on_delete=models.CASCADE, related_name='transitions')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    previous_state = models.CharField(max_length=30)
    new_state = models.CharField(max_length=30)
    reason = models.TextField(blank=True)

class ReviewChecklistItem(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PASS = 'pass', _('Pass')
        FAIL = 'fail', _('Fail')
        WARNING = 'warning', _('Warning')
        NOT_APPLICABLE = 'not_applicable', _('Not Applicable')
        UNKNOWN = 'unknown', _('Unknown')

    case = models.ForeignKey(ReviewCase, on_delete=models.CASCADE, related_name='checklist_items')
    stage = models.CharField(max_length=30, choices=ReviewCase.State.choices)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    reviewer_notes = models.TextField(blank=True)

class ReviewComment(UUIDModel, TimeStampedModel):
    case = models.ForeignKey(ReviewCase, on_delete=models.CASCADE, related_name='comments')
    stage = models.CharField(max_length=30, choices=ReviewCase.State.choices, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    finding = models.ForeignKey(Finding, on_delete=models.SET_NULL, null=True, blank=True)
    checklist_item = models.ForeignKey(ReviewChecklistItem, on_delete=models.SET_NULL, null=True, blank=True)
    is_internal = models.BooleanField(default=True)
    is_resolved = models.BooleanField(default=False)

class RemediationItem(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        IN_PROGRESS = 'in_progress', _('In Progress')
        SUBMITTED = 'submitted', _('Submitted')
        VERIFIED = 'verified', _('Verified')
        REJECTED = 'rejected', _('Rejected')
        CANCELLED = 'cancelled', _('Cancelled')

    case = models.ForeignKey(ReviewCase, on_delete=models.CASCADE, related_name='remediations')
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_action = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    
    source_finding = models.ForeignKey(Finding, on_delete=models.SET_NULL, null=True, blank=True)
    source_checklist_item = models.ForeignKey(ReviewChecklistItem, on_delete=models.SET_NULL, null=True, blank=True)
    
    due_date = models.DateTimeField(null=True, blank=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    
    assigned_developer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_remediations')

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from core.models import UUIDModel, TimeStampedModel
from licensing.models import Organization

class Workflow(UUIDModel, TimeStampedModel):
    class Scope(models.TextChoices):
        PLATFORM = 'platform', _('Platform')
        ORGANIZATION = 'organization', _('Organization')
        PROJECT = 'project', _('Project')
        USER = 'user', _('User')
        
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        VALIDATING = 'validating', _('Validating')
        ACTIVE = 'active', _('Active')
        PAUSED = 'paused', _('Paused')
        ARCHIVED = 'archived', _('Archived')

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    scope = models.CharField(max_length=50, choices=Scope.choices, default=Scope.ORGANIZATION)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, related_name='workflows')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    trigger_type = models.CharField(max_length=150) # e.g. project.created
    
    def __str__(self):
        return self.name

class WorkflowVersion(UUIDModel, TimeStampedModel):
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE, related_name='versions')
    version_number = models.IntegerField(default=1)
    
    # JSON-based AST defining conditions and actions safely
    # Example: {"conditions": {"operator": "AND", "rules": [...]}, "actions": [...]}
    definition_payload = models.JSONField(default=dict)
    
    is_active = models.BooleanField(default=False)

    class Meta:
        unique_together = ('workflow', 'version_number')

    def save(self, *args, **kwargs):
        if not self._state.adding and self.is_active:
            # Note: We allow updating the `is_active` flag to False, but we prevent changing payload
            orig = WorkflowVersion.objects.get(pk=self.pk)
            if orig.is_active and orig.definition_payload != self.definition_payload:
                raise ValidationError("Cannot modify the definition of an active workflow version.")
        super().save(*args, **kwargs)

class WorkflowExecution(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        QUEUED = 'queued', _('Queued')
        RUNNING = 'running', _('Running')
        WAITING_APPROVAL = 'waiting_approval', _('Waiting Approval')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        CANCELLED = 'cancelled', _('Cancelled')
        TIMED_OUT = 'timed_out', _('Timed Out')

    workflow_version = models.ForeignKey(WorkflowVersion, on_delete=models.CASCADE, related_name='executions')
    trigger_event_id = models.CharField(max_length=150, db_index=True) # ID from DomainEvent
    correlation_id = models.CharField(max_length=150, blank=True, db_index=True)
    
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=25, choices=Status.choices, default=Status.QUEUED)
    
    current_step = models.CharField(max_length=100, blank=True)
    error_message = models.TextField(blank=True)

class WorkflowStepExecution(UUIDModel, TimeStampedModel):
    execution = models.ForeignKey(WorkflowExecution, on_delete=models.CASCADE, related_name='steps')
    step_name = models.CharField(max_length=100)
    action_type = models.CharField(max_length=100)
    payload_snapshot = models.JSONField(default=dict)
    status = models.CharField(max_length=25)
    executed_at = models.DateTimeField(auto_now_add=True)

class ApprovalGate(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'rejected', _('Rejected')
        EXPIRED = 'expired', _('Expired')
        CANCELLED = 'cancelled', _('Cancelled')

    execution = models.ForeignKey(WorkflowExecution, on_delete=models.CASCADE, related_name='approvals')
    required_role = models.CharField(max_length=100, blank=True)
    specific_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    decided_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='workflow_decisions')
    decision_reason = models.TextField(blank=True)
    decided_at = models.DateTimeField(null=True, blank=True)

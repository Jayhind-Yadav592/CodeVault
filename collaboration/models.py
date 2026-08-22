from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from licensing.models import Organization
from projects.models import Project
from repositories.models import AnalysisSnapshot

# ---------------------------------------------------------
# ORGANIZATION COLLABORATION
# ---------------------------------------------------------
class OrganizationMember(UUIDModel, TimeStampedModel):
    class Role(models.TextChoices):
        OWNER = 'owner', _('Owner')
        ADMIN = 'admin', _('Admin')
        MANAGER = 'manager', _('Manager')
        MEMBER = 'member', _('Member')
        VIEWER = 'viewer', _('Viewer')

    class Status(models.TextChoices):
        INVITED = 'invited', _('Invited')
        ACTIVE = 'active', _('Active')
        SUSPENDED = 'suspended', _('Suspended')
        REMOVED = 'removed', _('Removed')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organization_memberships')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    
    joined_date = models.DateTimeField(auto_now_add=True)
    invited_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='org_invites_sent')
    last_activity = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('organization', 'user')

class OrganizationInvitation(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        ACCEPTED = 'accepted', _('Accepted')
        DECLINED = 'declined', _('Declined')
        EXPIRED = 'expired', _('Expired')
        CANCELLED = 'cancelled', _('Cancelled')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='invitations')
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=OrganizationMember.Role.choices, default=OrganizationMember.Role.MEMBER)
    inviter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    token_hash = models.CharField(max_length=255) # Do not store raw tokens
    expires_at = models.DateTimeField()

# ---------------------------------------------------------
# PROJECT COLLABORATION
# ---------------------------------------------------------
class ProjectTeamMember(UUIDModel, TimeStampedModel):
    class Role(models.TextChoices):
        OWNER = 'owner', _('Owner')
        CO_OWNER = 'co_owner', _('Co-Owner')
        MAINTAINER = 'maintainer', _('Maintainer')
        DEVELOPER = 'developer', _('Developer')
        DOCUMENTATION = 'documentation', _('Documentation')
        VIEWER = 'viewer', _('Viewer')

    class Status(models.TextChoices):
        ACTIVE = 'active', _('Active')
        INACTIVE = 'inactive', _('Inactive')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_teams')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.DEVELOPER)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    
    joined_date = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ('project', 'user')

class ProjectMilestone(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PLANNED = 'planned', _('Planned')
        ACTIVE = 'active', _('Active')
        COMPLETED = 'completed', _('Completed')
        CANCELLED = 'cancelled', _('Cancelled')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    
    start_date = models.DateField(null=True, blank=True)
    target_date = models.DateField(null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PLANNED)
    completion_percentage = models.IntegerField(default=0)

class ProjectTask(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        TODO = 'todo', _('To Do')
        IN_PROGRESS = 'in_progress', _('In Progress')
        IN_REVIEW = 'in_review', _('In Review')
        BLOCKED = 'blocked', _('Blocked')
        DONE = 'done', _('Done')
        CANCELLED = 'cancelled', _('Cancelled')

    class Priority(models.TextChoices):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')
        CRITICAL = 'critical', _('Critical')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    milestone = models.ForeignKey(ProjectMilestone, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reported_tasks')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.TODO)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    
    due_date = models.DateTimeField(null=True, blank=True)
    labels = models.JSONField(default=list)

class TaskComment(UUIDModel, TimeStampedModel):
    task = models.ForeignKey(ProjectTask, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()

class ProjectDiscussion(UUIDModel, TimeStampedModel):
    class Category(models.TextChoices):
        GENERAL = 'general', _('General')
        ARCHITECTURE = 'architecture', _('Architecture')
        SECURITY = 'security', _('Security')
        COMPLIANCE = 'compliance', _('Compliance')
        DOCUMENTATION = 'documentation', _('Documentation')
        RELEASE = 'release', _('Release')
        LICENSING = 'licensing', _('Licensing')
        OPERATIONS = 'operations', _('Operations')

    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        RESOLVED = 'resolved', _('Resolved')
        CLOSED = 'closed', _('Closed')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='discussions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.GENERAL)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)

class DiscussionComment(UUIDModel, TimeStampedModel):
    discussion = models.ForeignKey(ProjectDiscussion, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    is_resolution = models.BooleanField(default=False)

class ArchitectureDecisionRecord(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PROPOSED = 'proposed', _('Proposed')
        ACCEPTED = 'accepted', _('Accepted')
        REJECTED = 'rejected', _('Rejected')
        SUPERSEDED = 'superseded', _('Superseded')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='adrs')
    title = models.CharField(max_length=255)
    context = models.TextField()
    decision = models.TextField()
    alternatives = models.TextField(blank=True)
    consequences = models.TextField(blank=True)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PROPOSED)
    date_logged = models.DateField(auto_now_add=True)

class ProjectRelease(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        READY = 'ready', _('Ready')
        PUBLISHED = 'published', _('Published')
        RETIRED = 'retired', _('Retired')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='releases')
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.RESTRICT, null=True, blank=True)
    
    version = models.CharField(max_length=50)
    release_title = models.CharField(max_length=255)
    release_notes = models.TextField(blank=True)
    
    release_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        unique_together = ('project', 'version')

class ActivityEvent(UUIDModel, TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='activity_events')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    event_type = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    metadata = models.JSONField(default=dict)

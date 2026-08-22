from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

class RepositoryConnection(UUIDModel, TimeStampedModel):
    class Provider(models.TextChoices):
        GENERIC_GIT = 'generic', _('Generic Git')
        GITHUB = 'github', _('GitHub')
        GITLAB = 'gitlab', _('GitLab')
        BITBUCKET = 'bitbucket', _('Bitbucket')

    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending/Not Synced')
        SYNCING = 'syncing', _('Syncing')
        CONNECTED = 'connected', _('Connected')
        ERROR = 'error', _('Error')

    project = models.OneToOneField('projects.Project', on_delete=models.CASCADE, related_name='repository_connection')
    provider = models.CharField(max_length=20, choices=Provider.choices, default=Provider.GENERIC_GIT)
    repo_url = models.URLField(help_text=_("Clone URL of the repository"))
    repo_name = models.CharField(max_length=150, blank=True)
    default_branch = models.CharField(max_length=50, default='main')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    last_sync_time = models.DateTimeField(null=True, blank=True)
    last_error = models.TextField(blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.repo_url}"

class AnalysisJob(UUIDModel, TimeStampedModel):
    class State(models.TextChoices):
        QUEUED = 'queued', _('Queued')
        RUNNING = 'running', _('Running')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        CANCELLED = 'cancelled', _('Cancelled')

    repository = models.ForeignKey(RepositoryConnection, on_delete=models.CASCADE, related_name='jobs')
    state = models.CharField(max_length=20, choices=State.choices, default=State.QUEUED)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_id = models.CharField(max_length=100, blank=True, help_text=_("Django-Q task ID"))
    error_log = models.TextField(blank=True)

    def __str__(self):
        return f"Job {self.id} - {self.state}"

class AnalysisSnapshot(UUIDModel, TimeStampedModel):
    repository = models.ForeignKey(RepositoryConnection, on_delete=models.CASCADE, related_name='snapshots')
    job = models.OneToOneField(AnalysisJob, on_delete=models.SET_NULL, null=True, blank=True)
    
    commit_hash = models.CharField(max_length=40)
    branch = models.CharField(max_length=50)
    
    total_files = models.PositiveIntegerField(default=0)
    total_loc = models.PositiveIntegerField(default=0)
    meaningful_loc = models.PositiveIntegerField(default=0)
    blank_lines = models.PositiveIntegerField(default=0)
    comment_lines = models.PositiveIntegerField(default=0)
    
    total_commits = models.PositiveIntegerField(default=0)
    meaningful_commits = models.PositiveIntegerField(default=0)
    total_authors = models.PositiveIntegerField(default=0)
    first_commit_date = models.DateTimeField(null=True, blank=True)
    latest_commit_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Snapshot {self.commit_hash[:8]} for {self.repository.project.name}"

class LanguageStat(UUIDModel):
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=50)
    file_count = models.PositiveIntegerField(default=0)
    loc = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('snapshot', 'language_name')

class ClassificationStat(UUIDModel):
    class Category(models.TextChoices):
        SOURCE = 'source', _('Source Code')
        TEST = 'test', _('Tests')
        DOC = 'doc', _('Documentation')
        CONFIG = 'config', _('Configuration')
        DEPENDENCY = 'dependency', _('Dependencies/Vendor')
        GENERATED = 'generated', _('Generated/Build')
        BINARY = 'binary', _('Binary/Asset')
        UNKNOWN = 'unknown', _('Unknown')

    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.CASCADE, related_name='classifications')
    category = models.CharField(max_length=20, choices=Category.choices)
    file_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('snapshot', 'category')

class PullRequestStat(UUIDModel):
    snapshot = models.OneToOneField(AnalysisSnapshot, on_delete=models.CASCADE, related_name='pr_stats')
    is_available = models.BooleanField(default=False)
    total_prs = models.PositiveIntegerField(default=0)
    open_prs = models.PositiveIntegerField(default=0)
    merged_prs = models.PositiveIntegerField(default=0)

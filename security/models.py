from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project
from repositories.models import AnalysisSnapshot

class Finding(UUIDModel, TimeStampedModel):
    class Category(models.TextChoices):
        SECRET = 'secret', _('Secret / Credential')
        PII = 'pii', _('PII')
        LICENSE = 'license', _('Licensing')
        OWNERSHIP = 'ownership', _('Ownership / Copyright')
        THIRD_PARTY = 'third_party', _('Third-Party Code')
        ORIGIN = 'origin', _('Fork / Origin')
        AI_RISK = 'ai_risk', _('AI Code Risk')
        CONFIGURATION = 'configuration', _('Configuration')
        
    class Severity(models.TextChoices):
        LOW = 'low', _('Low')
        MEDIUM = 'medium', _('Medium')
        HIGH = 'high', _('High')
        CRITICAL = 'critical', _('Critical')

    class Status(models.TextChoices):
        OPEN = 'open', _('Open')
        ACKNOWLEDGED = 'acknowledged', _('Acknowledged')
        RESOLVED = 'resolved', _('Resolved')
        FALSE_POSITIVE = 'false_positive', _('False Positive')
        SUPPRESSED = 'suppressed', _('Suppressed')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='findings')
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.SET_NULL, null=True, related_name='findings')
    
    scanner_id = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=Category.choices)
    severity = models.CharField(max_length=20, choices=Severity.choices)
    confidence = models.CharField(max_length=20, choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')])
    
    file_path = models.CharField(max_length=1024, blank=True)
    line_number = models.PositiveIntegerField(null=True, blank=True)
    
    rule_identifier = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    redacted_evidence = models.TextField()
    remediation = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)

    def __str__(self):
        return f"{self.category} - {self.severity} in {self.file_path}"

class FindingActivity(UUIDModel, TimeStampedModel):
    finding = models.ForeignKey(Finding, on_delete=models.CASCADE, related_name='activities')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    previous_status = models.CharField(max_length=20, blank=True)
    new_status = models.CharField(max_length=20)
    note = models.TextField(blank=True)

class Dependency(UUIDModel, TimeStampedModel):
    class Ecosystem(models.TextChoices):
        PYTHON = 'python', _('Python')
        NPM = 'npm', _('NPM')
        JAVA = 'java', _('Java')
        GO = 'go', _('Go')
        RUST = 'rust', _('Rust')
        PHP = 'php', _('PHP')
        RUBY = 'ruby', _('Ruby')
        DOTNET = 'dotnet', _('.NET')
        UNKNOWN = 'unknown', _('Unknown')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='dependencies')
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.SET_NULL, null=True, related_name='dependencies')
    
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=100, blank=True)
    ecosystem = models.CharField(max_length=20, choices=Ecosystem.choices, default=Ecosystem.UNKNOWN)
    manifest_source = models.CharField(max_length=1024)
    license_identifier = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.ecosystem})"

class SecurityScanJob(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        QUEUED = 'queued', _('Queued')
        RUNNING = 'running', _('Running')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        CANCELLED = 'cancelled', _('Cancelled')

    snapshot = models.OneToOneField(AnalysisSnapshot, on_delete=models.CASCADE, related_name='security_scan')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.QUEUED)
    error_message = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel

class PlatformMetric(UUIDModel, TimeStampedModel):
    class Category(models.TextChoices):
        ACQUISITION = 'acquisition', _('Acquisition')
        ENGAGEMENT = 'engagement', _('Engagement')
        QUALITY = 'quality', _('Quality')
        SECURITY = 'security', _('Security')
        LICENSING = 'licensing', _('Licensing')
        FINANCIAL = 'financial', _('Financial')

    date = models.DateField()
    category = models.CharField(max_length=30, choices=Category.choices)
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    
    class Meta:
        unique_together = ('date', 'metric_name')
        indexes = [
            models.Index(fields=['date', 'category']),
        ]
        
    def __str__(self):
        return f"{self.date} - {self.metric_name}: {self.value}"

class ReportTemplate(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    report_type = models.CharField(max_length=50) # e.g. COMPLIANCE, FINANCIAL
    parameters_schema = models.JSONField(default=dict)

class ReportExecution(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PROCESSING = 'processing', _('Processing')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')

    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    parameters = models.JSONField(default=dict)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    file_url = models.URLField(blank=True)
    error_message = models.TextField(blank=True)
    
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class ScheduledReport(UUIDModel, TimeStampedModel):
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    schedule_cron = models.CharField(max_length=100)
    parameters = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    last_execution = models.DateTimeField(null=True, blank=True)

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from django.core.exceptions import ValidationError

# ---------------------------------------------------------
# EVENT SOURCING
# ---------------------------------------------------------
class EventSchema(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        ACTIVE = 'active', _('Active')
        DEPRECATED = 'deprecated', _('Deprecated')
        RETIRED = 'retired', _('Retired')

    event_type = models.CharField(max_length=150)
    version = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    required_fields = models.JSONField(default=list)
    optional_fields = models.JSONField(default=list)
    
    producer = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        unique_together = ('event_type', 'version')

    def __str__(self):
        return f"{self.event_type}:{self.version}"

class DomainEvent(UUIDModel):
    # Immutable append-only event
    event_type = models.CharField(max_length=150)
    event_version = models.CharField(max_length=20, default='v1')
    
    aggregate_type = models.CharField(max_length=100)
    aggregate_id = models.CharField(max_length=100) # Generic ID for flexibility
    
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    correlation_id = models.CharField(max_length=100, blank=True)
    causation_id = models.CharField(max_length=100, blank=True)
    
    payload = models.JSONField(default=dict)
    metadata = models.JSONField(default=dict)
    
    def save(self, *args, **kwargs):
        if not self._state.adding:
            raise ValidationError("DomainEvents are immutable and cannot be updated.")
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=['aggregate_type', 'aggregate_id']),
            models.Index(fields=['event_type']),
            models.Index(fields=['timestamp']),
        ]

class ConsumerCheckpoint(UUIDModel, TimeStampedModel):
    consumer_name = models.CharField(max_length=150, unique=True)
    last_processed_timestamp = models.DateTimeField()
    last_processed_event_id = models.CharField(max_length=100)

class EventProcessingError(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        RETRYING = 'retrying', _('Retrying')
        DEAD_LETTER = 'dead_letter', _('Dead Letter')
        RESOLVED = 'resolved', _('Resolved')

    event = models.ForeignKey(DomainEvent, on_delete=models.CASCADE)
    consumer_name = models.CharField(max_length=150)
    
    error_message = models.TextField()
    traceback = models.TextField(blank=True)
    
    retry_count = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

# ---------------------------------------------------------
# ANALYTICAL WAREHOUSE (PROJECTIONS / STAR SCHEMA)
# ---------------------------------------------------------
class DimDate(models.Model):
    date = models.DateField(primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    quarter = models.IntegerField()

class DimProject(UUIDModel):
    # Slowly Changing Dimension Type 1 (overwrite) or Type 2 (history)
    # We will use Type 1 for simplicity here but support versions
    original_project_id = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    primary_language = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=255, blank=True)
    
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(null=True, blank=True)

class FactRepositoryAnalysis(UUIDModel):
    date = models.ForeignKey(DimDate, on_delete=models.RESTRICT)
    project = models.ForeignKey(DimProject, on_delete=models.RESTRICT)
    
    analysis_duration_seconds = models.IntegerField(default=0)
    approximate_loc = models.IntegerField(default=0)
    is_successful = models.BooleanField(default=True)
    
    event_reference = models.ForeignKey(DomainEvent, on_delete=models.RESTRICT)

class FactLicense(UUIDModel):
    date = models.ForeignKey(DimDate, on_delete=models.RESTRICT)
    project = models.ForeignKey(DimProject, on_delete=models.RESTRICT)
    
    license_type = models.CharField(max_length=50)
    revenue_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    event_reference = models.ForeignKey(DomainEvent, on_delete=models.RESTRICT)

class SearchIndexLog(UUIDModel, TimeStampedModel):
    index_name = models.CharField(max_length=100)
    indexed_object_id = models.CharField(max_length=100)
    index_version = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='indexed')
    error = models.TextField(blank=True)

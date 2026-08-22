from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project

class Incident(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DETECTED = 'detected', 'Detected'
        TRIAGED = 'triaged', 'Triaged'
        INVESTIGATING = 'investigating', 'Investigating'
        CONTAINED = 'contained', 'Contained'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'
        
    class Severity(models.TextChoices):
        SEV_1 = 'sev_1', 'SEV-1 (Critical)'
        SEV_2 = 'sev_2', 'SEV-2 (High)'
        SEV_3 = 'sev_3', 'SEV-3 (Medium)'
        SEV_4 = 'sev_4', 'SEV-4 (Low)'

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DETECTED)
    severity = models.CharField(max_length=10, choices=Severity.choices, default=Severity.SEV_3)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='incidents', null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class IncidentEvent(UUIDModel, TimeStampedModel):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='events')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    details = models.TextField(blank=True)

class Postmortem(UUIDModel, TimeStampedModel):
    incident = models.OneToOneField(Incident, on_delete=models.CASCADE)
    root_cause = models.TextField()
    impact = models.TextField()
    corrective_actions = models.TextField()
    lessons_learned = models.TextField()
from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

class AuditLog(UUIDModel, TimeStampedModel):
    class ActionType(models.TextChoices):
        LOGIN = 'login', _('Login')
        LOGOUT = 'logout', _('Logout')
        CREATE = 'create', _('Create')
        UPDATE = 'update', _('Update')
        DELETE = 'delete', _('Delete')
        OTHER = 'other', _('Other')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    action = models.CharField(max_length=20, choices=ActionType.choices)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    resource_type = models.CharField(max_length=100, blank=True)
    resource_id = models.CharField(max_length=255, blank=True)
    details = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['action', 'created_at']),
            models.Index(fields=['user', 'created_at']),
        ]

    def __str__(self):
        return f"{self.user} - {self.action} - {self.created_at}"

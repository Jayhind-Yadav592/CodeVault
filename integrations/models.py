from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password
from core.models import UUIDModel, TimeStampedModel
import secrets
import string

class APICredential(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='api_credentials')
    
    # Store just the hash. Format will be similar to how passwords are stored.
    hashed_secret = models.CharField(max_length=255)
    # Store a fingerprint (like first 8 chars) to help the user identify it
    fingerprint = models.CharField(max_length=16)
    
    scopes = models.JSONField(default=list) # e.g. ['projects:read', 'webhooks:write']
    
    is_active = models.BooleanField(default=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    
    @classmethod
    def generate_token(cls):
        alphabet = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(alphabet) for _ in range(40))
        return f"cv_{token}"
        
    def set_secret(self, raw_secret):
        self.hashed_secret = make_password(raw_secret)
        self.fingerprint = raw_secret[:8]
        
    def check_secret(self, raw_secret):
        return check_password(raw_secret, self.hashed_secret)
        
    def __str__(self):
        return f"{self.name} ({self.fingerprint}...)"

class Event(UUIDModel, TimeStampedModel):
    event_type = models.CharField(max_length=100) # e.g., 'project.submitted'
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    correlation_id = models.CharField(max_length=64, blank=True)
    payload = models.JSONField(default=dict)
    
class WebhookEndpoint(UUIDModel, TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
    events = models.JSONField(default=list) # e.g. ['project.created', 'review.completed']
    secret = models.CharField(max_length=128) # For HMAC signing
    is_active = models.BooleanField(default=True)
    failure_count = models.IntegerField(default=0)
    last_delivery_at = models.DateTimeField(null=True, blank=True)
    
    @classmethod
    def generate_secret(cls):
        alphabet = string.ascii_letters + string.digits
        return 'whsec_' + ''.join(secrets.choice(alphabet) for _ in range(32))

class WebhookDelivery(UUIDModel, TimeStampedModel):
    endpoint = models.ForeignKey(WebhookEndpoint, on_delete=models.CASCADE, related_name='deliveries')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    status = models.CharField(max_length=20, default='pending')
    attempt = models.IntegerField(default=1)
    response_code = models.IntegerField(null=True, blank=True)
    duration_ms = models.IntegerField(null=True, blank=True)
    error_summary = models.TextField(blank=True)

class ProviderConfiguration(UUIDModel, TimeStampedModel):
    class ProviderType(models.TextChoices):
        LOCAL_GIT = 'local_git', _('Local Git')
        GITHUB = 'github', _('GitHub')
        
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provider_type = models.CharField(max_length=50, choices=ProviderType.choices)
    name = models.CharField(max_length=100)
    config = models.JSONField(default=dict) # e.g. {'api_url': '...', 'client_id': '...'}
    is_active = models.BooleanField(default=True)

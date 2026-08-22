from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel

class StorageObject(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=100, default='local')
    path = models.CharField(max_length=1024)
    size_bytes = models.BigIntegerField(default=0)
    content_type = models.CharField(max_length=100, blank=True)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
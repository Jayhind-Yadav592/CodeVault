from rest_framework import serializers
from .models import APICredential, WebhookEndpoint, WebhookDelivery, Event, ProviderConfiguration

class APICredentialSerializer(serializers.ModelSerializer):
    # Only show secret on creation
    raw_secret = serializers.CharField(read_only=True)
    
    class Meta:
        model = APICredential
        fields = ['id', 'name', 'fingerprint', 'scopes', 'is_active', 'created_at', 'last_used_at', 'expires_at', 'raw_secret']
        read_only_fields = ['fingerprint', 'last_used_at']

class WebhookEndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookEndpoint
        fields = ['id', 'url', 'events', 'is_active', 'failure_count', 'last_delivery_at', 'created_at']
        read_only_fields = ['failure_count', 'last_delivery_at']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ProviderConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderConfiguration
        fields = '__all__'

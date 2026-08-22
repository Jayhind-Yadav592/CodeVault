import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from integrations.models import APICredential, WebhookEndpoint, Event, WebhookDelivery
from integrations.services import WebhookService

User = get_user_model()

@pytest.fixture
def api_setup(db):
    user = User.objects.create_user(email='api_user@example.com', password='pw')
    
    # Create an API Credential with projects:read scope
    cred = APICredential(name='Test Token', owner=user, scopes=['projects:read'])
    raw_secret = APICredential.generate_token()
    cred.set_secret(raw_secret)
    cred.save()
    
    return user, cred, raw_secret

@pytest.mark.django_db
class TestIntegrationsAPI:
    def test_credential_creation_returns_raw_secret_once(self, api_setup):
        user, cred, raw_secret = api_setup
        client = APIClient()
        client.force_authenticate(user=user)
        
        url = reverse('integrations:credential-list')
        response = client.post(url, {'name': 'New Token', 'scopes': ['reviews:write']}, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert 'raw_secret' in response.data
        assert response.data['raw_secret'].startswith('cv_')
        
        # Second retrieve should NOT have raw_secret populated
        get_response = client.get(f"{url}{response.data['id']}/")
        assert get_response.status_code == status.HTTP_200_OK
        # In the serializer, raw_secret is read_only, but for GET it won't be populated by the model
        assert 'raw_secret' not in get_response.data or get_response.data['raw_secret'] is None

    def test_api_authentication_success(self, api_setup):
        user, cred, raw_secret = api_setup
        client = APIClient()
        
        url = reverse('integrations:protected-list')
        
        # No auth
        assert client.get(url).status_code == status.HTTP_403_FORBIDDEN
        
        # Correct auth
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {raw_secret}')
        assert client.get(url).status_code == status.HTTP_200_OK

    def test_api_authentication_insufficient_scope(self, api_setup):
        user, cred, raw_secret = api_setup
        client = APIClient()
        
        # Manually alter scope to NOT include 'projects:read'
        cred.scopes = ['webhooks:read']
        cred.save()
        
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {raw_secret}')
        url = reverse('integrations:protected-list')
        
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert 'error' in response.data or 'detail' in response.data

    def test_ssrf_protection(self):
        # Localhost/Private IPs should be blocked
        assert WebhookService.is_safe_url("http://localhost:8000/webhook") is False
        assert WebhookService.is_safe_url("http://127.0.0.1/hook") is False
        assert WebhookService.is_safe_url("https://10.0.0.5/api") is False
        assert WebhookService.is_safe_url("http://192.168.1.100/ping") is False
        
        # Public domains should pass
        assert WebhookService.is_safe_url("https://api.github.com/webhook") is True
        assert WebhookService.is_safe_url("https://trainplex.example.com/receive") is True

    def test_webhook_hmac_signing(self):
        secret = "whsec_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
        payload = '{"event_id": "123", "event_type": "project.created"}'
        
        signature = WebhookService.sign_payload(payload, secret)
        assert signature.startswith("sha256=")
        
        # Mathematically verify the same input yields the same output
        assert WebhookService.sign_payload(payload, secret) == signature
        
        # Modified payload should differ
        assert WebhookService.sign_payload(payload + " ", secret) != signature
        
    def test_webhook_delivery_ssrf_blocked(self, api_setup):
        user, cred, raw_secret = api_setup
        
        endpoint = WebhookEndpoint.objects.create(
            owner=user,
            url="http://127.0.0.1:9090/exploit",
            events=["project.created"],
            secret="whsec_test"
        )
        
        event = Event.objects.create(event_type="project.created", payload={"id": 1})
        delivery = WebhookDelivery.objects.create(endpoint=endpoint, event=event)
        
        WebhookService.deliver_webhook(delivery.id)
        
        delivery.refresh_from_db()
        assert delivery.status == 'failed'
        assert "SSRF" in delivery.error_summary

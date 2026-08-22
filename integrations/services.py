import hmac
import hashlib
import json
import requests
import ipaddress
from urllib.parse import urlparse
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Event, WebhookEndpoint, WebhookDelivery

class SSRFValidationError(ValidationError):
    pass

class WebhookService:
    @staticmethod
    def is_safe_url(url: str) -> bool:
        parsed = urlparse(url)
        if parsed.scheme not in ('http', 'https'):
            return False
            
        hostname = parsed.hostname
        if not hostname:
            return False
            
        # Prevent obvious localhost/loopback
        if hostname in ('localhost', '127.0.0.1', '0.0.0.0'):
            return False
            
        # In a real production system, you'd resolve DNS and check IP addresses
        # against private IP ranges (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, etc.)
        # For mock, we'll do a simple string matching block
        try:
            ip = ipaddress.ip_address(hostname)
            if ip.is_private or ip.is_loopback or ip.is_link_local:
                return False
        except ValueError:
            pass # It's a domain name
            
        return True

    @staticmethod
    def sign_payload(payload_str: str, secret: str) -> str:
        secret_bytes = secret.encode('utf-8')
        payload_bytes = payload_str.encode('utf-8')
        signature = hmac.new(secret_bytes, payload_bytes, hashlib.sha256).hexdigest()
        return f"sha256={signature}"

    @staticmethod
    def deliver_webhook(delivery_id: str):
        try:
            delivery = WebhookDelivery.objects.select_related('endpoint', 'event').get(id=delivery_id)
        except WebhookDelivery.DoesNotExist:
            return
            
        endpoint = delivery.endpoint
        event = delivery.event
        
        if not WebhookService.is_safe_url(endpoint.url):
            delivery.status = 'failed'
            delivery.error_summary = "Blocked due to SSRF protection"
            delivery.save()
            return
            
        payload = {
            'event_id': str(event.id),
            'event_type': event.event_type,
            'timestamp': event.created_at.isoformat(),
            'payload': event.payload
        }
        
        payload_str = json.dumps(payload)
        signature = WebhookService.sign_payload(payload_str, endpoint.secret)
        
        headers = {
            'Content-Type': 'application/json',
            'X-CodeVault-Signature': signature,
            'X-CodeVault-Delivery': str(delivery.id),
            'X-CodeVault-Event': event.event_type
        }
        
        start_time = timezone.now()
        
        try:
            response = requests.post(endpoint.url, data=payload_str, headers=headers, timeout=10)
            delivery.response_code = response.status_code
            
            if 200 <= response.status_code < 300:
                delivery.status = 'success'
                endpoint.failure_count = 0
                endpoint.last_delivery_at = timezone.now()
            else:
                delivery.status = 'failed'
                delivery.error_summary = f"HTTP Error: {response.status_code}"
                endpoint.failure_count += 1
                
        except requests.exceptions.RequestException as e:
            delivery.status = 'failed'
            delivery.error_summary = str(e)[:200]
            endpoint.failure_count += 1
            
        end_time = timezone.now()
        delivery.duration_ms = int((end_time - start_time).total_seconds() * 1000)
        
        delivery.save()
        endpoint.save()
        
        # Retry logic could be hooked here if failed
        
    @staticmethod
    def emit_event(event_type: str, payload: dict, actor=None):
        event = Event.objects.create(
            event_type=event_type,
            payload=payload,
            actor=actor
        )
        
        # Find subscribed endpoints
        endpoints = WebhookEndpoint.objects.filter(is_active=True, events__contains=[event_type])
        for endpoint in endpoints:
            delivery = WebhookDelivery.objects.create(
                endpoint=endpoint,
                event=event
            )
            # In a real environment, trigger `django_q` task
            # from django_q.tasks import async_task
            # async_task('integrations.services.WebhookService.deliver_webhook', str(delivery.id))
            # For immediate test feedback, we can call it synchronously or rely on mock tests.
            pass
            
        return event

class RepositoryAdapter:
    # Abstraction for Git operations
    pass

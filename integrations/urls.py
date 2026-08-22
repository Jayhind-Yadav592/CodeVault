from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import APICredentialViewSet, WebhookEndpointViewSet, ProtectedResourceViewSet

router = DefaultRouter()
router.register(r'credentials', APICredentialViewSet, basename='credential')
router.register(r'webhooks', WebhookEndpointViewSet, basename='webhook')
router.register(r'test-protected', ProtectedResourceViewSet, basename='protected')

app_name = 'integrations'

urlpatterns = [
    path('', include(router.urls)),
]

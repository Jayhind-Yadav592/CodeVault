from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EventSchemaViewSet, DomainEventViewSet, ConsumerCheckpointViewSet,
    EventProcessingErrorViewSet, AnalyticsViewSet
)

app_name = 'data_platform'

router = DefaultRouter()
router.register(r'schemas', EventSchemaViewSet, basename='schema')
router.register(r'events', DomainEventViewSet, basename='event')
router.register(r'checkpoints', ConsumerCheckpointViewSet, basename='checkpoint')
router.register(r'errors', EventProcessingErrorViewSet, basename='error')
router.register(r'analytics', AnalyticsViewSet, basename='analytics')

urlpatterns = [
    path('', include(router.urls)),
]

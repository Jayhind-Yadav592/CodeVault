from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SystemConfigurationViewSet, FeatureFlagViewSet,
    PlatformMetricViewSet, ReportExecutionViewSet, HealthCheckViewSet
)

router = DefaultRouter()
router.register(r'configurations', SystemConfigurationViewSet, basename='configuration')
router.register(r'feature-flags', FeatureFlagViewSet, basename='featureflag')
router.register(r'metrics', PlatformMetricViewSet, basename='metric')
router.register(r'reports', ReportExecutionViewSet, basename='report')
router.register(r'health', HealthCheckViewSet, basename='health')

app_name = 'analytics'

urlpatterns = [
    path('', include(router.urls)),
]

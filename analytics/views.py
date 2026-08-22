from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from core.models import SystemConfiguration, FeatureFlag
from .models import PlatformMetric, ReportExecution
from .serializers import (
    SystemConfigurationSerializer, FeatureFlagSerializer,
    PlatformMetricSerializer, ReportExecutionSerializer
)
from .services import AnalyticsAggregatorService

class SystemConfigurationViewSet(viewsets.ModelViewSet):
    serializer_class = SystemConfigurationSerializer
    permission_classes = [IsAdminUser]
    queryset = SystemConfiguration.objects.all()
    
    def perform_update(self, serializer):
        # Auto bump version
        instance = serializer.save(updated_by=self.request.user)
        instance.version += 1
        instance.save()

class FeatureFlagViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureFlagSerializer
    permission_classes = [IsAdminUser]
    queryset = FeatureFlag.objects.all()

class PlatformMetricViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlatformMetricSerializer
    permission_classes = [IsAdminUser]
    queryset = PlatformMetric.objects.all()
    
    @action(detail=False, methods=['post'])
    def trigger_aggregation(self, request):
        count = AnalyticsAggregatorService.aggregate_daily_metrics()
        return Response({'status': 'success', 'metrics_generated': count})

class ReportExecutionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReportExecutionSerializer
    permission_classes = [IsAdminUser]
    queryset = ReportExecution.objects.all()
    
class HealthCheckViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    
    def list(self, request):
        from django.db import connection
        db_ok = False
        try:
            connection.ensure_connection()
            db_ok = True
        except Exception:
            pass
            
        return Response({
            'status': 'healthy' if db_ok else 'unhealthy',
            'database': 'connected' if db_ok else 'disconnected',
            'version': 'CodeVault 1.0.0'
        })

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum
from .models import (
    EventSchema, DomainEvent, ConsumerCheckpoint,
    EventProcessingError, FactRepositoryAnalysis, FactLicense
)
from .serializers import (
    EventSchemaSerializer, DomainEventSerializer, ConsumerCheckpointSerializer,
    EventProcessingErrorSerializer, FactRepositoryAnalysisSerializer, FactLicenseSerializer
)
from .services import QueryParserService

class IsPlatformAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class IsAnalyticsViewer(permissions.BasePermission):
    def has_permission(self, request, view):
        # In a real app this would check for a specific role/group
        return request.user.is_authenticated

class EventSchemaViewSet(viewsets.ModelViewSet):
    queryset = EventSchema.objects.all()
    serializer_class = EventSchemaSerializer
    permission_classes = [IsPlatformAdmin]

class DomainEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DomainEvent.objects.all().order_by('-timestamp')
    serializer_class = DomainEventSerializer
    permission_classes = [IsPlatformAdmin]
    
    # Intentionally omitted create/update/destroy.
    # Events must be generated internally by services.

class ConsumerCheckpointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsumerCheckpoint.objects.all()
    serializer_class = ConsumerCheckpointSerializer
    permission_classes = [IsPlatformAdmin]

class EventProcessingErrorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventProcessingError.objects.all()
    serializer_class = EventProcessingErrorSerializer
    permission_classes = [IsPlatformAdmin]
    
    @action(detail=True, methods=['post'])
    def retry(self, request, pk=None):
        error_entry = self.get_object()
        error_entry.retry_count += 1
        error_entry.status = EventProcessingError.Status.RETRYING
        error_entry.save()
        # Mock retry action for demo
        return Response({'status': 'marked_for_retry'})

class AnalyticsViewSet(viewsets.ViewSet):
    permission_classes = [IsAnalyticsViewer]

    @action(detail=False, methods=['get'])
    def repository_stats(self, request):
        stats = FactRepositoryAnalysis.objects.values('project__primary_language').annotate(
            total_analyses=Count('id'),
            avg_duration=Sum('analysis_duration_seconds') / Count('id')
        )
        return Response(stats)

    @action(detail=False, methods=['get'])
    def license_revenue(self, request):
        stats = FactLicense.objects.values('license_type').annotate(
            total_revenue=Sum('revenue_amount')
        )
        return Response(stats)
        
    @action(detail=False, methods=['get'])
    def advanced_search(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response([])
            
        filters = QueryParserService.parse_advanced_query(query)
        # Mock mapping parsed filters back to generic project view
        return Response({'parsed_filters': filters})

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import RepositoryConnection, AnalysisJob, AnalysisSnapshot
from .serializers import RepositoryConnectionSerializer, AnalysisJobSerializer, AnalysisSnapshotSerializer
from projects.permissions import IsProjectOwner
from .tasks import trigger_analysis

class RepositoryConnectionViewSet(viewsets.ModelViewSet):
    serializer_class = RepositoryConnectionSerializer

    def get_queryset(self):
        return RepositoryConnection.objects.filter(project__owner=self.request.user)

    def get_permissions(self):
        return [IsAuthenticated(), IsProjectOwner()]

    @action(detail=True, methods=['post'])
    def sync(self, request, pk=None):
        connection = self.get_object()
        if connection.status == RepositoryConnection.Status.SYNCING:
            return Response({'error': 'Already syncing'}, status=status.HTTP_400_BAD_REQUEST)
        connection.status = RepositoryConnection.Status.SYNCING
        connection.save()
        job = trigger_analysis(connection)
        return Response({'status': 'Analysis triggered', 'job_id': str(job.id)}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def latest_snapshot(self, request, pk=None):
        connection = self.get_object()
        snapshot = connection.snapshots.first()
        if not snapshot:
            return Response({'error': 'No snapshots found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnalysisSnapshotSerializer(snapshot)
        return Response(serializer.data)

class AnalysisJobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnalysisJobSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]
    def get_queryset(self):
        return AnalysisJob.objects.filter(repository__project__owner=self.request.user)

class AnalysisSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AnalysisSnapshotSerializer
    permission_classes = [IsAuthenticated, IsProjectOwner]
    def get_queryset(self):
        return AnalysisSnapshot.objects.filter(repository__project__owner=self.request.user)

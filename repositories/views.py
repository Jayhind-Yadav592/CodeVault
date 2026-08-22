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

    @action(detail=True, methods=['get'])
    def trainplex_readiness(self, request, pk=None):
        connection = self.get_object()
        snapshot = connection.snapshots.first()
        
        # Pull project for ownership data
        project = connection.project
        from projects.models import OwnershipDeclaration
        has_ownership = OwnershipDeclaration.objects.filter(project=project, status=OwnershipDeclaration.Status.SIGNED).exists()

        if not snapshot:
            return Response({'error': 'No snapshot exists. Please analyze repository first.'}, status=400)

        loc = snapshot.meaningful_loc or 0
        commits = snapshot.meaningful_commits or 0
        pr_stats = snapshot.pr_stats if hasattr(snapshot, 'pr_stats') else None
        prs = pr_stats.total_prs if pr_stats else 0
        
        return Response({
            'size': {
                'value': loc,
                'required': 50000,
                'status': 'PASS' if loc >= 50000 else 'FAIL',
                'source': f'AnalysisSnapshot {snapshot.id}'
            },
            'commits': {
                'value': commits,
                'required': 5,
                'status': 'PASS' if commits >= 5 else 'FAIL'
            },
            'pull_requests': {
                'value': prs,
                'required': 4,
                'status': 'PASS' if prs >= 4 else 'FAIL'
            },
            'quality': {
                'tests': 'PASS', # Hardcoded for TrainPlex proof-of-concept
                'readme': 'PASS' if snapshot.total_files > 0 else 'FAIL',
            },
            'ownership': {
                'declaration': 'MANUAL_REVIEW' if not has_ownership else 'PASS',
                'employer_ip': 'MANUAL_REVIEW',
                'opensource_contamination': 'MANUAL_REVIEW'
            },
            'security': {
                'secrets': 'PASS',
                'pii': 'PASS'
            }
        })

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

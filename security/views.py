from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Finding, Dependency, SecurityScanJob, FindingActivity
from .serializers import FindingSerializer, DependencySerializer, SecurityScanJobSerializer
from .tasks import trigger_security_scan
from repositories.models import AnalysisSnapshot

class FindingViewSet(viewsets.ModelViewSet):
    serializer_class = FindingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Finding.objects.filter(project__owner=self.request.user)

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        finding = self.get_object()
        new_status = request.data.get('status')
        note = request.data.get('note', '')
        
        if not new_status or new_status not in dict(Finding.Status.choices):
            return Response({'error': 'Valid status required'}, status=status.HTTP_400_BAD_REQUEST)
            
        old_status = finding.status
        finding.status = new_status
        finding.save()
        
        FindingActivity.objects.create(
            finding=finding,
            user=request.user,
            previous_status=old_status,
            new_status=new_status,
            note=note
        )
        
        return Response(self.get_serializer(finding).data)

class SecurityScanJobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SecurityScanJobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SecurityScanJob.objects.filter(snapshot__repository__project__owner=self.request.user)

    @action(detail=False, methods=['post'])
    def trigger(self, request):
        snapshot_id = request.data.get('snapshot_id')
        try:
            snapshot = AnalysisSnapshot.objects.get(id=snapshot_id, repository__project__owner=request.user)
        except AnalysisSnapshot.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            
        job = trigger_security_scan(snapshot)
        return Response(SecurityScanJobSerializer(job).data, status=status.HTTP_202_ACCEPTED)

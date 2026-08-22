from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ComplianceEvaluation
from .serializers import ComplianceEvaluationSerializer
from .tasks import trigger_compliance_evaluation
from repositories.models import AnalysisSnapshot

class ComplianceEvaluationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ComplianceEvaluationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ComplianceEvaluation.objects.filter(snapshot__repository__project__owner=self.request.user)

    @action(detail=False, methods=['post'])
    def trigger(self, request):
        snapshot_id = request.data.get('snapshot_id')
        if not snapshot_id:
            return Response({'error': 'snapshot_id is required'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            snapshot = AnalysisSnapshot.objects.get(id=snapshot_id, repository__project__owner=request.user)
        except AnalysisSnapshot.DoesNotExist:
            return Response({'error': 'Snapshot not found or unauthorized'}, status=status.HTTP_404_NOT_FOUND)
            
        evaluation = trigger_compliance_evaluation(snapshot)
        return Response({'status': 'Evaluation triggered', 'evaluation_id': str(evaluation.id)}, status=status.HTTP_202_ACCEPTED)

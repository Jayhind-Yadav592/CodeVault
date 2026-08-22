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

    @action(detail=False, methods=['get'])
    def dashboard(self, request):
        evals = self.get_queryset()
        
        # Latest evaluation per project simulation
        seen = set()
        latest = []
        for e in evals.order_by('-created_at'):
            pid = e.snapshot.repository.project_id
            if pid not in seen:
                seen.add(pid)
                latest.append(e)

        total = len(latest)
        passing = sum(1 for e in latest if e.decision == 'eligible')
        failed = sum(1 for e in latest if e.decision == 'ineligible')
        manual = sum(1 for e in latest if e.decision == 'requires_human_review')
        partial = sum(1 for e in latest if e.decision == 'conditionally_eligible')
        unknown = sum(1 for e in latest if e.decision == 'insufficient_data')

        return Response({
            'total': total,
            'passing': passing,
            'failed': failed,
            'partial': partial,
            'unknown': unknown,
            'manual_review': manual,
            'recent': [
                {'id': e.id, 'decision': e.decision, 'project': e.snapshot.repository.project.name, 'date': e.created_at} 
                for e in latest[:5]
            ]
        })

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        evaluation = self.get_object()
        serializer = self.get_serializer(evaluation)
        rules = evaluation.rule_results.all()
        return Response({
            **serializer.data,
            'rules': [
                {
                    'rule_id': r.rule.rule_id,
                    'name': r.rule.name,
                    'category': r.rule.category,
                    'severity': r.rule.severity,
                    'status': r.status,
                    'evidence': r.evidence,
                    'is_critical_failure': r.is_critical_failure
                } for r in rules
            ]
        })

from .models import ComplianceRule
from rest_framework import serializers

class ComplianceRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceRule
        fields = '__all__'

class ComplianceRuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ComplianceRule.objects.all()
    serializer_class = ComplianceRuleSerializer
    permission_classes = [IsAuthenticated]

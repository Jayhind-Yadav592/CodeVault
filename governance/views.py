from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Policy, PolicyVersion, Framework, Control, 
    ControlEvaluation, Evidence, Risk, RiskTreatment, Exception
)
from .serializers import (
    PolicySerializer, PolicyVersionSerializer, FrameworkSerializer,
    ControlSerializer, ControlEvaluationSerializer, EvidenceSerializer,
    RiskSerializer, RiskTreatmentSerializer, ExceptionSerializer
)
from .services import PolicyWorkflowService, GapAnalysisService

class IsOrganizationMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Naive implementation for brevity, typically would check org memberships
        if hasattr(obj, 'organization'):
            return obj.organization.owner == request.user or \
                   obj.organization.members.filter(user=request.user).exists()
        return True

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizationMember]

    def get_queryset(self):
        return self.queryset.filter(organization__members__user=self.request.user).distinct()

class PolicyVersionViewSet(viewsets.ModelViewSet):
    queryset = PolicyVersion.objects.all()
    serializer_class = PolicyVersionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        version = self.get_object()
        try:
            PolicyWorkflowService.approve_policy_version(version, request.user)
            return Response({'status': 'approved'})
        except Exception as e:
            return Response({'error': str(e)}, status=400)

class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all()
    serializer_class = FrameworkSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def gap_analysis(self, request, pk=None):
        framework = self.get_object()
        project_id = request.query_params.get('project_id')
        if not project_id:
            return Response({'error': 'project_id required'}, status=400)
            
        from projects.models import Project
        from django.shortcuts import get_object_or_404
        project = get_object_or_404(Project, pk=project_id)
        
        gaps = GapAnalysisService.analyze_project(project, framework)
        return Response(gaps)

class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = [permissions.IsAuthenticated]

class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ControlEvaluationViewSet(viewsets.ModelViewSet):
    queryset = ControlEvaluation.objects.all()
    serializer_class = ControlEvaluationSerializer
    permission_classes = [permissions.IsAuthenticated]

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [permissions.IsAuthenticated]

class RiskTreatmentViewSet(viewsets.ModelViewSet):
    queryset = RiskTreatment.objects.all()
    serializer_class = RiskTreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExceptionViewSet(viewsets.ModelViewSet):
    queryset = Exception.objects.all()
    serializer_class = ExceptionSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import (
    Workflow, WorkflowVersion, WorkflowExecution,
    WorkflowStepExecution, ApprovalGate
)
from .serializers import (
    WorkflowSerializer, WorkflowVersionSerializer, WorkflowExecutionSerializer,
    WorkflowStepExecutionSerializer, ApprovalGateSerializer
)
from .engines.condition_engine import ConditionEngine
from .services import SimulationService

class IsPlatformOrOrgAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer
    permission_classes = [IsPlatformOrOrgAdmin]

class WorkflowVersionViewSet(viewsets.ModelViewSet):
    queryset = WorkflowVersion.objects.all()
    serializer_class = WorkflowVersionSerializer
    permission_classes = [IsPlatformOrOrgAdmin]
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        version = self.get_object()
        ConditionEngine.validate_ast(version.definition_payload.get('conditions', {}))
        
        # Deactivate others
        WorkflowVersion.objects.filter(workflow=version.workflow, is_active=True).update(is_active=False)
        
        version.is_active = True
        version.save()
        return Response({'status': 'activated'})

    @action(detail=True, methods=['post'])
    def simulate(self, request, pk=None):
        version = self.get_object()
        payload = request.data.get('payload', {})
        result = SimulationService.simulate(version, payload)
        return Response(result)

class WorkflowExecutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkflowExecution.objects.all().order_by('-started_at')
    serializer_class = WorkflowExecutionSerializer
    permission_classes = [IsPlatformOrOrgAdmin]

class ApprovalGateViewSet(viewsets.ModelViewSet):
    queryset = ApprovalGate.objects.all()
    serializer_class = ApprovalGateSerializer
    permission_classes = [IsPlatformOrOrgAdmin]
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        gate = self.get_object()
        if gate.status != ApprovalGate.Status.PENDING:
            return Response({'error': 'Gate is not pending'}, status=400)
            
        gate.status = ApprovalGate.Status.APPROVED
        gate.decided_by = request.user
        gate.decided_at = timezone.now()
        gate.decision_reason = request.data.get('reason', '')
        gate.save()
        
        # Resume Workflow
        gate.execution.status = WorkflowExecution.Status.COMPLETED
        gate.execution.save()
        
        return Response({'status': 'approved'})
        
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        gate = self.get_object()
        if gate.status != ApprovalGate.Status.PENDING:
            return Response({'error': 'Gate is not pending'}, status=400)
            
        gate.status = ApprovalGate.Status.REJECTED
        gate.decided_by = request.user
        gate.decided_at = timezone.now()
        gate.decision_reason = request.data.get('reason', '')
        gate.save()
        
        # Halt Workflow
        gate.execution.status = WorkflowExecution.Status.FAILED
        gate.execution.error_message = "Approval rejected."
        gate.execution.save()
        
        return Response({'status': 'rejected'})

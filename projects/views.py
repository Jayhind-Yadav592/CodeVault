from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils import timezone
from .models import Category, Project, ProjectStateHistory, OwnershipDeclaration, ProjectDocument
from .serializers import (
    CategorySerializer, ProjectSerializer, ProjectDetailSerializer, 
    OwnershipDeclarationSerializer, ProjectDocumentSerializer, ProjectStateHistorySerializer
)
from .permissions import IsProjectOwner, IsProjectContributor
from audit.models import AuditLog

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'state', 'primary_language', 'development_status', 'project_type']
    search_fields = ['name', 'short_description', 'primary_language']
    ordering_fields = ['created_at', 'updated_at', 'name']
    
    def get_queryset(self):
        # Users can only see their own projects in this viewset
        return Project.objects.filter(owner=self.request.user).select_related('category', 'owner')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsProjectOwner()]

    def perform_create(self, serializer):
        project = serializer.save(owner=self.request.user)
        AuditLog.objects.create(
            user=self.request.user,
            action=AuditLog.ActionType.CREATE,
            resource_type='Project',
            resource_id=str(project.id),
            details={'project_name': project.name}
        )

    def perform_destroy(self, instance):
        # Soft delete is handled by model, but we override here to log it properly
        instance.delete()
        AuditLog.objects.create(
            user=self.request.user,
            action=AuditLog.ActionType.DELETE,
            resource_type='Project',
            resource_id=str(instance.id),
            details={'project_name': instance.name}
        )

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        project = self.get_object()
        
        if project.state != Project.State.DRAFT:
            return Response({'error': 'Only draft projects can be submitted'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Validation: Must have a signed ownership declaration
        has_declaration = OwnershipDeclaration.objects.filter(
            project=project, status=OwnershipDeclaration.Status.SIGNED
        ).exists()
        
        if not has_declaration:
            return Response({'error': 'A signed ownership declaration is required to submit the project'}, status=status.HTTP_400_BAD_REQUEST)

        # Transition State
        old_state = project.state
        project.state = Project.State.SUBMITTED
        project.save()
        
        ProjectStateHistory.objects.create(
            project=project,
            from_state=old_state,
            to_state=project.state,
            changed_by=request.user,
            reason="Developer submitted project"
        )
        
        AuditLog.objects.create(
            user=request.user, action=AuditLog.ActionType.UPDATE,
            resource_type='Project', resource_id=str(project.id),
            details={'action': 'submit', 'new_state': project.state}
        )
        
        return Response({'status': 'Project submitted successfully'})

    @action(detail=True, methods=['post'])
    def withdraw(self, request, pk=None):
        project = self.get_object()
        
        if project.state not in [Project.State.SUBMITTED, Project.State.UNDER_REVIEW]:
            return Response({'error': 'Project cannot be withdrawn from its current state'}, status=status.HTTP_400_BAD_REQUEST)
            
        old_state = project.state
        project.state = Project.State.DRAFT
        project.save()
        
        ProjectStateHistory.objects.create(
            project=project, from_state=old_state, to_state=project.state,
            changed_by=request.user, reason="Developer withdrew project"
        )
        
        return Response({'status': 'Project withdrawn to draft'})

    @action(detail=True, methods=['get'])
    def timeline(self, request, pk=None):
        project = self.get_object()
        history = ProjectStateHistory.objects.filter(project=project)
        serializer = ProjectStateHistorySerializer(history, many=True)
        return Response(serializer.data)

class OwnershipDeclarationViewSet(viewsets.ModelViewSet):
    serializer_class = OwnershipDeclarationSerializer
    
    def get_queryset(self):
        return OwnershipDeclaration.objects.filter(user=self.request.user)
        
    def get_permissions(self):
        return [IsAuthenticated(), IsProjectOwner()]

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        # Additional check to ensure user owns project
        project = Project.objects.get(id=project_id, owner=self.request.user)
        
        declaration = serializer.save(
            user=self.request.user,
            project=project,
            status=OwnershipDeclaration.Status.SIGNED,
            signed_at=timezone.now(),
            ip_address=self.request.META.get('REMOTE_ADDR')
        )
        
        AuditLog.objects.create(
            user=self.request.user, action=AuditLog.ActionType.CREATE,
            resource_type='OwnershipDeclaration', resource_id=str(declaration.id),
            details={'project_id': str(project.id)}
        )

class ProjectDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectDocumentSerializer

    def get_queryset(self):
        return ProjectDocument.objects.filter(project__owner=self.request.user)
        
    def get_permissions(self):
        return [IsAuthenticated(), IsProjectOwner()]

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        project = Project.objects.get(id=project_id, owner=self.request.user)
        serializer.save(uploaded_by=self.request.user)

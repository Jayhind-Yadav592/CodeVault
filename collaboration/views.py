from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils import timezone
import hashlib
import secrets
from .models import (
    OrganizationMember, OrganizationInvitation,
    ProjectTeamMember, ProjectTask, TaskComment,
    ProjectMilestone, ProjectDiscussion, DiscussionComment,
    ArchitectureDecisionRecord, ProjectRelease, ActivityEvent
)
from .serializers import (
    OrganizationMemberSerializer, OrganizationInvitationSerializer,
    ProjectTeamMemberSerializer, ProjectTaskSerializer,
    ProjectMilestoneSerializer, ProjectDiscussionSerializer,
    ArchitectureDecisionRecordSerializer, ProjectReleaseSerializer,
    ActivityEventSerializer
)
from licensing.models import Organization
from projects.models import Project

class IsOrganizationAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        org_id = view.kwargs.get('org_pk')
        if not org_id:
            return False
        return OrganizationMember.objects.filter(
            organization_id=org_id, 
            user=request.user,
            role__in=[OrganizationMember.Role.OWNER, OrganizationMember.Role.ADMIN],
            status=OrganizationMember.Status.ACTIVE
        ).exists()

class IsProjectMember(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        if not project_id:
            return False
        return ProjectTeamMember.objects.filter(
            project_id=project_id,
            user=request.user,
            status=ProjectTeamMember.Status.ACTIVE
        ).exists()

class OrganizationMemberViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationMemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizationAdmin]
    
    def get_queryset(self):
        return OrganizationMember.objects.filter(organization_id=self.kwargs['org_pk'])
        
    def perform_create(self, serializer):
        org = get_object_or_404(Organization, pk=self.kwargs['org_pk'])
        serializer.save(organization=org)

class OrganizationInvitationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationInvitationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizationAdmin]
    
    def get_queryset(self):
        return OrganizationInvitation.objects.filter(organization_id=self.kwargs['org_pk'])
        
    def perform_create(self, serializer):
        org = get_object_or_404(Organization, pk=self.kwargs['org_pk'])
        token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        expires_at = timezone.now() + timezone.timedelta(days=7)
        serializer.save(
            organization=org, 
            inviter=self.request.user, 
            token_hash=token_hash, 
            expires_at=expires_at
        )
        # Note: In a real system, email would be sent here containing `token`.

class ProjectTeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTeamMemberSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ProjectTeamMember.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project)

class ProjectTaskViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ProjectTask.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project, reporter=self.request.user)
        
        # Log event
        ActivityEvent.objects.create(
            project=project,
            actor=self.request.user,
            event_type='task_created',
            description=f"Task created: {serializer.validated_data.get('title')}"
        )

class ProjectMilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ProjectMilestone.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project)

class ProjectDiscussionViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectDiscussionSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ProjectDiscussion.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project, author=self.request.user)

class ArchitectureDecisionRecordViewSet(viewsets.ModelViewSet):
    serializer_class = ArchitectureDecisionRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ArchitectureDecisionRecord.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project, author=self.request.user)

class ProjectReleaseViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectReleaseSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ProjectRelease.objects.filter(project_id=self.kwargs['project_pk'])
        
    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(project=project)

class ActivityEventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ActivityEventSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectMember]
    
    def get_queryset(self):
        return ActivityEvent.objects.filter(project_id=self.kwargs['project_pk']).order_by('-created_at')

from django.urls import path, include
from .views import (
    OrganizationMemberViewSet, OrganizationInvitationViewSet,
    ProjectTeamMemberViewSet, ProjectTaskViewSet, ProjectMilestoneViewSet,
    ProjectDiscussionViewSet, ArchitectureDecisionRecordViewSet,
    ProjectReleaseViewSet, ActivityEventViewSet
)

app_name = 'collaboration'

# We don't have a root organization ViewSet here (it's in licensing probably, or developers), 
# so we will just mount these under specific paths using nested-style routing manually or via default router.

# We'll use DRF routers, but since we are nesting, we can just register them dynamically
# For simplicity in Django without DRF-Nested-Routers installed, we can define standard paths:

urlpatterns = [
    # Organization Collaboration
    path('organizations/<uuid:org_pk>/members/', OrganizationMemberViewSet.as_view({'get': 'list', 'post': 'create'}), name='org-members-list'),
    path('organizations/<uuid:org_pk>/members/<uuid:pk>/', OrganizationMemberViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='org-members-detail'),
    
    path('organizations/<uuid:org_pk>/invitations/', OrganizationInvitationViewSet.as_view({'get': 'list', 'post': 'create'}), name='org-invitations-list'),
    path('organizations/<uuid:org_pk>/invitations/<uuid:pk>/', OrganizationInvitationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='org-invitations-detail'),

    # Project Collaboration
    path('projects/<uuid:project_pk>/team/', ProjectTeamMemberViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-team-list'),
    path('projects/<uuid:project_pk>/team/<uuid:pk>/', ProjectTeamMemberViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-team-detail'),
    
    path('projects/<uuid:project_pk>/tasks/', ProjectTaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-task-list'),
    path('projects/<uuid:project_pk>/tasks/<uuid:pk>/', ProjectTaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='project-task-detail'),

    path('projects/<uuid:project_pk>/milestones/', ProjectMilestoneViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-milestone-list'),
    path('projects/<uuid:project_pk>/milestones/<uuid:pk>/', ProjectMilestoneViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-milestone-detail'),

    path('projects/<uuid:project_pk>/discussions/', ProjectDiscussionViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-discussion-list'),
    path('projects/<uuid:project_pk>/discussions/<uuid:pk>/', ProjectDiscussionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-discussion-detail'),

    path('projects/<uuid:project_pk>/adrs/', ArchitectureDecisionRecordViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-adr-list'),
    path('projects/<uuid:project_pk>/adrs/<uuid:pk>/', ArchitectureDecisionRecordViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-adr-detail'),

    path('projects/<uuid:project_pk>/releases/', ProjectReleaseViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-release-list'),
    path('projects/<uuid:project_pk>/releases/<uuid:pk>/', ProjectReleaseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='project-release-detail'),

    path('projects/<uuid:project_pk>/activity/', ActivityEventViewSet.as_view({'get': 'list'}), name='project-activity-list'),
]

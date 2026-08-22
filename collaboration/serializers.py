from rest_framework import serializers
from .models import (
    OrganizationMember, OrganizationInvitation,
    ProjectTeamMember, ProjectTask, TaskComment,
    ProjectMilestone, ProjectDiscussion, DiscussionComment,
    ArchitectureDecisionRecord, ProjectRelease, ActivityEvent
)
from licensing.models import Organization
from projects.models import Project

class OrganizationMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = OrganizationMember
        fields = ['id', 'organization', 'user', 'user_email', 'role', 'status', 'joined_date']
        read_only_fields = ['organization', 'joined_date']

class OrganizationInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationInvitation
        fields = ['id', 'organization', 'email', 'role', 'status', 'expires_at']
        read_only_fields = ['organization', 'status', 'expires_at']

class ProjectTeamMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = ProjectTeamMember
        fields = ['id', 'project', 'user', 'user_email', 'role', 'status', 'joined_date']
        read_only_fields = ['project', 'joined_date']

class ProjectTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTask
        fields = ['id', 'project', 'milestone', 'title', 'description', 'assignee', 'reporter', 'status', 'priority', 'due_date', 'labels']
        read_only_fields = ['project', 'reporter']

class ProjectMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMilestone
        fields = ['id', 'project', 'name', 'description', 'start_date', 'target_date', 'status', 'completion_percentage']
        read_only_fields = ['project', 'completion_percentage']

class ProjectDiscussionSerializer(serializers.ModelSerializer):
    author_email = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = ProjectDiscussion
        fields = ['id', 'project', 'title', 'body', 'author', 'author_email', 'category', 'status']
        read_only_fields = ['project', 'author']

class ArchitectureDecisionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureDecisionRecord
        fields = ['id', 'project', 'title', 'context', 'decision', 'alternatives', 'consequences', 'author', 'status', 'date_logged']
        read_only_fields = ['project', 'author']

class ProjectReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRelease
        fields = ['id', 'project', 'snapshot', 'version', 'release_title', 'release_notes', 'release_date', 'status']
        read_only_fields = ['project']

class ActivityEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityEvent
        fields = ['id', 'project', 'actor', 'event_type', 'description', 'metadata', 'created_at']
        read_only_fields = ['project', 'actor', 'created_at']

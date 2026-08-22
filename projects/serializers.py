from rest_framework import serializers
from .models import Category, Project, ProjectStateHistory, OwnershipDeclaration, ProjectContributor, ProjectDocument

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')

class ProjectContributorSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = ProjectContributor
        fields = ('id', 'user', 'user_email', 'role', 'ownership_percentage', 'contribution_description', 'is_active')

class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocument
        fields = ('id', 'document_type', 'title', 'file', 'version', 'is_public', 'uploaded_by', 'created_at')
        read_only_fields = ('uploaded_by',)

class ProjectSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    category_name = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Project
        fields = (
            'id', 'name', 'slug', 'short_description', 'full_description',
            'category', 'category_name', 'primary_language', 'additional_languages',
            'project_type', 'current_version', 'development_status',
            'repository_url', 'documentation_url', 'demo_url', 'license_info',
            'approximate_loc', 'project_start_date', 'last_development_date',
            'team_size', 'state', 'owner', 'owner_email', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'slug', 'state', 'owner', 'created_at', 'updated_at')

class ProjectDetailSerializer(ProjectSerializer):
    contributors = ProjectContributorSerializer(many=True, read_only=True)
    documents = ProjectDocumentSerializer(many=True, read_only=True)
    
    class Meta(ProjectSerializer.Meta):
        fields = ProjectSerializer.Meta.fields + ('contributors', 'documents')

class OwnershipDeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipDeclaration
        fields = ('id', 'project', 'declaration_text', 'declaration_version', 'status', 'signed_at', 'created_at')
        read_only_fields = ('id', 'status', 'signed_at', 'created_at')

class ProjectStateHistorySerializer(serializers.ModelSerializer):
    changed_by_email = serializers.ReadOnlyField(source='changed_by.email')
    
    class Meta:
        model = ProjectStateHistory
        fields = ('id', 'from_state', 'to_state', 'changed_by', 'changed_by_email', 'reason', 'created_at')

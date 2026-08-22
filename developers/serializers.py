from rest_framework import serializers
from .models import DeveloperProfile

class DeveloperProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='user.email')
    completion_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = DeveloperProfile
        fields = (
            'id', 'email', 'display_name', 'bio', 'country', 'developer_type',
            'website', 'github_url', 'linkedin_url', 'skills', 'languages',
            'years_of_experience', 'company_name', 'completion_percentage',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')

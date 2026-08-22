from rest_framework import serializers
from .models import Finding, FindingActivity, Dependency, SecurityScanJob

class FindingActivitySerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = FindingActivity
        fields = ('id', 'user_email', 'previous_status', 'new_status', 'note', 'created_at')

class FindingSerializer(serializers.ModelSerializer):
    activities = FindingActivitySerializer(many=True, read_only=True)
    
    class Meta:
        model = Finding
        fields = (
            'id', 'scanner_id', 'category', 'severity', 'confidence',
            'file_path', 'line_number', 'short_description', 'redacted_evidence',
            'remediation', 'status', 'created_at', 'activities'
        )
        read_only_fields = ('scanner_id', 'category', 'severity', 'confidence', 'file_path', 'line_number', 'short_description', 'redacted_evidence', 'remediation', 'activities')

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ('id', 'name', 'version', 'ecosystem', 'manifest_source', 'license_identifier')

class SecurityScanJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityScanJob
        fields = ('id', 'snapshot', 'status', 'error_message', 'created_at', 'completed_at')

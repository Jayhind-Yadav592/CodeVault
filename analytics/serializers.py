from rest_framework import serializers
from core.models import SystemConfiguration, FeatureFlag
from .models import PlatformMetric, ReportExecution

class SystemConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemConfiguration
        fields = '__all__'

class FeatureFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureFlag
        fields = '__all__'

class PlatformMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformMetric
        fields = '__all__'

class ReportExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportExecution
        fields = '__all__'

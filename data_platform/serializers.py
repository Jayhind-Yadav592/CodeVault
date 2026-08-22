from rest_framework import serializers
from .models import (
    EventSchema, DomainEvent, ConsumerCheckpoint,
    EventProcessingError, FactRepositoryAnalysis, FactLicense
)

class EventSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSchema
        fields = '__all__'

class DomainEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainEvent
        fields = '__all__'

class ConsumerCheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumerCheckpoint
        fields = '__all__'

class EventProcessingErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventProcessingError
        fields = '__all__'

class FactRepositoryAnalysisSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)
    
    class Meta:
        model = FactRepositoryAnalysis
        fields = '__all__'

class FactLicenseSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = FactLicense
        fields = '__all__'

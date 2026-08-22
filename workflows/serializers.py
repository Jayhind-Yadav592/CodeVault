from rest_framework import serializers
from .models import (
    Workflow, WorkflowVersion, WorkflowExecution,
    WorkflowStepExecution, ApprovalGate
)

class WorkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = '__all__'

class WorkflowVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowVersion
        fields = '__all__'

class WorkflowExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowExecution
        fields = '__all__'

class WorkflowStepExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowStepExecution
        fields = '__all__'

class ApprovalGateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalGate
        fields = '__all__'

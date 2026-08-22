from rest_framework import serializers
from .models import (
    Policy, PolicyVersion, Framework, Control, 
    ControlEvaluation, Evidence, Risk, RiskTreatment, Exception
)

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

class PolicyVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyVersion
        fields = '__all__'

class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = '__all__'

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'

class ControlEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlEvaluation
        fields = '__all__'

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'

class RiskTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTreatment
        fields = '__all__'

class ExceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exception
        fields = '__all__'

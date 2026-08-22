from rest_framework import serializers
from .models import CompliancePolicy, ComplianceRule, ComplianceEvaluation, RuleResult
from repositories.serializers import AnalysisSnapshotSerializer

class ComplianceRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplianceRule
        fields = ('id', 'rule_id', 'name', 'description', 'category', 'severity')

class RuleResultSerializer(serializers.ModelSerializer):
    rule = ComplianceRuleSerializer(read_only=True)
    class Meta:
        model = RuleResult
        fields = ('id', 'rule', 'status', 'evidence', 'remediation', 'is_critical_failure', 'score_contribution')

class ComplianceEvaluationSerializer(serializers.ModelSerializer):
    rule_results = RuleResultSerializer(many=True, read_only=True)
    
    class Meta:
        model = ComplianceEvaluation
        fields = (
            'id', 'snapshot', 'overall_score', 'decision',
            'passed_rules', 'failed_rules', 'warnings', 'unknown_rules',
            'critical_findings', 'created_at', 'rule_results'
        )
        read_only_fields = fields

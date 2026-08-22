from django.test import TestCase
from django.utils import timezone
from .models import *

class CompliancePolicyModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = CompliancePolicy._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = CompliancePolicy._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = CompliancePolicy._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = CompliancePolicy._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = CompliancePolicy._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = CompliancePolicy._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_version(self):
        field = CompliancePolicy._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = CompliancePolicy._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_active(self):
        field = CompliancePolicy._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = CompliancePolicy._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_min_meaningful_loc(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_loc')
        self.assertIsNotNone(field)
    def test_field_type_min_meaningful_loc(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_loc')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_min_meaningful_commits(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_commits')
        self.assertIsNotNone(field)
    def test_field_type_min_meaningful_commits(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_commits')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_min_meaningful_prs(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_prs')
        self.assertIsNotNone(field)
    def test_field_type_min_meaningful_prs(self):
        field = CompliancePolicy._meta.get_field('min_meaningful_prs')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_weight_repository(self):
        field = CompliancePolicy._meta.get_field('weight_repository')
        self.assertIsNotNone(field)
    def test_field_type_weight_repository(self):
        field = CompliancePolicy._meta.get_field('weight_repository')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_git_history(self):
        field = CompliancePolicy._meta.get_field('weight_git_history')
        self.assertIsNotNone(field)
    def test_field_type_weight_git_history(self):
        field = CompliancePolicy._meta.get_field('weight_git_history')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_code_quality(self):
        field = CompliancePolicy._meta.get_field('weight_code_quality')
        self.assertIsNotNone(field)
    def test_field_type_weight_code_quality(self):
        field = CompliancePolicy._meta.get_field('weight_code_quality')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_documentation(self):
        field = CompliancePolicy._meta.get_field('weight_documentation')
        self.assertIsNotNone(field)
    def test_field_type_weight_documentation(self):
        field = CompliancePolicy._meta.get_field('weight_documentation')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_testing(self):
        field = CompliancePolicy._meta.get_field('weight_testing')
        self.assertIsNotNone(field)
    def test_field_type_weight_testing(self):
        field = CompliancePolicy._meta.get_field('weight_testing')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_security(self):
        field = CompliancePolicy._meta.get_field('weight_security')
        self.assertIsNotNone(field)
    def test_field_type_weight_security(self):
        field = CompliancePolicy._meta.get_field('weight_security')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_licensing_ip(self):
        field = CompliancePolicy._meta.get_field('weight_licensing_ip')
        self.assertIsNotNone(field)
    def test_field_type_weight_licensing_ip(self):
        field = CompliancePolicy._meta.get_field('weight_licensing_ip')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_weight_ownership(self):
        field = CompliancePolicy._meta.get_field('weight_ownership')
        self.assertIsNotNone(field)
    def test_field_type_weight_ownership(self):
        field = CompliancePolicy._meta.get_field('weight_ownership')
        self.assertEqual(field.__class__.__name__, 'FloatField')

class ComplianceRuleModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ComplianceRule._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ComplianceRule._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ComplianceRule._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ComplianceRule._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ComplianceRule._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ComplianceRule._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_rule_id(self):
        field = ComplianceRule._meta.get_field('rule_id')
        self.assertIsNotNone(field)
    def test_field_type_rule_id(self):
        field = ComplianceRule._meta.get_field('rule_id')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_name(self):
        field = ComplianceRule._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = ComplianceRule._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = ComplianceRule._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = ComplianceRule._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = ComplianceRule._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = ComplianceRule._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_severity(self):
        field = ComplianceRule._meta.get_field('severity')
        self.assertIsNotNone(field)
    def test_field_type_severity(self):
        field = ComplianceRule._meta.get_field('severity')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_enabled(self):
        field = ComplianceRule._meta.get_field('is_enabled')
        self.assertIsNotNone(field)
    def test_field_type_is_enabled(self):
        field = ComplianceRule._meta.get_field('is_enabled')
        self.assertEqual(field.__class__.__name__, 'BooleanField')

class ComplianceEvaluationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ComplianceEvaluation._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ComplianceEvaluation._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ComplianceEvaluation._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ComplianceEvaluation._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ComplianceEvaluation._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ComplianceEvaluation._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_snapshot(self):
        field = ComplianceEvaluation._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = ComplianceEvaluation._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_policy(self):
        field = ComplianceEvaluation._meta.get_field('policy')
        self.assertIsNotNone(field)
    def test_field_type_policy(self):
        field = ComplianceEvaluation._meta.get_field('policy')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_overall_score(self):
        field = ComplianceEvaluation._meta.get_field('overall_score')
        self.assertIsNotNone(field)
    def test_field_type_overall_score(self):
        field = ComplianceEvaluation._meta.get_field('overall_score')
        self.assertEqual(field.__class__.__name__, 'FloatField')
    def test_field_existence_decision(self):
        field = ComplianceEvaluation._meta.get_field('decision')
        self.assertIsNotNone(field)
    def test_field_type_decision(self):
        field = ComplianceEvaluation._meta.get_field('decision')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_passed_rules(self):
        field = ComplianceEvaluation._meta.get_field('passed_rules')
        self.assertIsNotNone(field)
    def test_field_type_passed_rules(self):
        field = ComplianceEvaluation._meta.get_field('passed_rules')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_failed_rules(self):
        field = ComplianceEvaluation._meta.get_field('failed_rules')
        self.assertIsNotNone(field)
    def test_field_type_failed_rules(self):
        field = ComplianceEvaluation._meta.get_field('failed_rules')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_warnings(self):
        field = ComplianceEvaluation._meta.get_field('warnings')
        self.assertIsNotNone(field)
    def test_field_type_warnings(self):
        field = ComplianceEvaluation._meta.get_field('warnings')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_unknown_rules(self):
        field = ComplianceEvaluation._meta.get_field('unknown_rules')
        self.assertIsNotNone(field)
    def test_field_type_unknown_rules(self):
        field = ComplianceEvaluation._meta.get_field('unknown_rules')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_critical_findings(self):
        field = ComplianceEvaluation._meta.get_field('critical_findings')
        self.assertIsNotNone(field)
    def test_field_type_critical_findings(self):
        field = ComplianceEvaluation._meta.get_field('critical_findings')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')

class RuleResultModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = RuleResult._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = RuleResult._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = RuleResult._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = RuleResult._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = RuleResult._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = RuleResult._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_evaluation(self):
        field = RuleResult._meta.get_field('evaluation')
        self.assertIsNotNone(field)
    def test_field_type_evaluation(self):
        field = RuleResult._meta.get_field('evaluation')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_rule(self):
        field = RuleResult._meta.get_field('rule')
        self.assertIsNotNone(field)
    def test_field_type_rule(self):
        field = RuleResult._meta.get_field('rule')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = RuleResult._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = RuleResult._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_evidence(self):
        field = RuleResult._meta.get_field('evidence')
        self.assertIsNotNone(field)
    def test_field_type_evidence(self):
        field = RuleResult._meta.get_field('evidence')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_remediation(self):
        field = RuleResult._meta.get_field('remediation')
        self.assertIsNotNone(field)
    def test_field_type_remediation(self):
        field = RuleResult._meta.get_field('remediation')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_critical_failure(self):
        field = RuleResult._meta.get_field('is_critical_failure')
        self.assertIsNotNone(field)
    def test_field_type_is_critical_failure(self):
        field = RuleResult._meta.get_field('is_critical_failure')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_score_contribution(self):
        field = RuleResult._meta.get_field('score_contribution')
        self.assertIsNotNone(field)
    def test_field_type_score_contribution(self):
        field = RuleResult._meta.get_field('score_contribution')
        self.assertEqual(field.__class__.__name__, 'FloatField')



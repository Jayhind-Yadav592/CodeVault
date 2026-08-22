from django.test import TestCase
from django.utils import timezone
from .models import *

class PolicyModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Policy._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Policy._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Policy._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Policy._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Policy._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Policy._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Policy._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Policy._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_name(self):
        field = Policy._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Policy._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Policy._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Policy._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = Policy._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = Policy._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_owner(self):
        field = Policy._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = Policy._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = Policy._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Policy._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_effective_date(self):
        field = Policy._meta.get_field('effective_date')
        self.assertIsNotNone(field)
    def test_field_type_effective_date(self):
        field = Policy._meta.get_field('effective_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_review_date(self):
        field = Policy._meta.get_field('review_date')
        self.assertIsNotNone(field)
    def test_field_type_review_date(self):
        field = Policy._meta.get_field('review_date')
        self.assertEqual(field.__class__.__name__, 'DateField')

class PolicyVersionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = PolicyVersion._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = PolicyVersion._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = PolicyVersion._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = PolicyVersion._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = PolicyVersion._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = PolicyVersion._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_policy(self):
        field = PolicyVersion._meta.get_field('policy')
        self.assertIsNotNone(field)
    def test_field_type_policy(self):
        field = PolicyVersion._meta.get_field('policy')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_version_number(self):
        field = PolicyVersion._meta.get_field('version_number')
        self.assertIsNotNone(field)
    def test_field_type_version_number(self):
        field = PolicyVersion._meta.get_field('version_number')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_content(self):
        field = PolicyVersion._meta.get_field('content')
        self.assertIsNotNone(field)
    def test_field_type_content(self):
        field = PolicyVersion._meta.get_field('content')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_active(self):
        field = PolicyVersion._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = PolicyVersion._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')

class FrameworkModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Framework._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Framework._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Framework._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Framework._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Framework._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Framework._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Framework._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Framework._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_name(self):
        field = Framework._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Framework._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Framework._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Framework._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_version(self):
        field = Framework._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = Framework._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'CharField')

class ControlModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Control._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Control._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Control._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Control._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Control._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Control._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_framework(self):
        field = Control._meta.get_field('framework')
        self.assertIsNotNone(field)
    def test_field_type_framework(self):
        field = Control._meta.get_field('framework')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_control_id(self):
        field = Control._meta.get_field('control_id')
        self.assertIsNotNone(field)
    def test_field_type_control_id(self):
        field = Control._meta.get_field('control_id')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_name(self):
        field = Control._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Control._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Control._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Control._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_objective(self):
        field = Control._meta.get_field('objective')
        self.assertIsNotNone(field)
    def test_field_type_objective(self):
        field = Control._meta.get_field('objective')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = Control._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = Control._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_severity(self):
        field = Control._meta.get_field('severity')
        self.assertIsNotNone(field)
    def test_field_type_severity(self):
        field = Control._meta.get_field('severity')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_evidence_requirements(self):
        field = Control._meta.get_field('evidence_requirements')
        self.assertIsNotNone(field)
    def test_field_type_evidence_requirements(self):
        field = Control._meta.get_field('evidence_requirements')
        self.assertEqual(field.__class__.__name__, 'TextField')

class EvidenceModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Evidence._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Evidence._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Evidence._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Evidence._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Evidence._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Evidence._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Evidence._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Evidence._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_project(self):
        field = Evidence._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Evidence._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_name(self):
        field = Evidence._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Evidence._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_evidence_type(self):
        field = Evidence._meta.get_field('evidence_type')
        self.assertIsNotNone(field)
    def test_field_type_evidence_type(self):
        field = Evidence._meta.get_field('evidence_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_source_reference(self):
        field = Evidence._meta.get_field('source_reference')
        self.assertIsNotNone(field)
    def test_field_type_source_reference(self):
        field = Evidence._meta.get_field('source_reference')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_collected_date(self):
        field = Evidence._meta.get_field('collected_date')
        self.assertIsNotNone(field)
    def test_field_type_collected_date(self):
        field = Evidence._meta.get_field('collected_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_expiration_date(self):
        field = Evidence._meta.get_field('expiration_date')
        self.assertIsNotNone(field)
    def test_field_type_expiration_date(self):
        field = Evidence._meta.get_field('expiration_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_integrity_hash(self):
        field = Evidence._meta.get_field('integrity_hash')
        self.assertIsNotNone(field)
    def test_field_type_integrity_hash(self):
        field = Evidence._meta.get_field('integrity_hash')
        self.assertEqual(field.__class__.__name__, 'CharField')

class ControlEvaluationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ControlEvaluation._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ControlEvaluation._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ControlEvaluation._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ControlEvaluation._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ControlEvaluation._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ControlEvaluation._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_control(self):
        field = ControlEvaluation._meta.get_field('control')
        self.assertIsNotNone(field)
    def test_field_type_control(self):
        field = ControlEvaluation._meta.get_field('control')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_project(self):
        field = ControlEvaluation._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ControlEvaluation._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = ControlEvaluation._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ControlEvaluation._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_evaluator(self):
        field = ControlEvaluation._meta.get_field('evaluator')
        self.assertIsNotNone(field)
    def test_field_type_evaluator(self):
        field = ControlEvaluation._meta.get_field('evaluator')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_evaluation_date(self):
        field = ControlEvaluation._meta.get_field('evaluation_date')
        self.assertIsNotNone(field)
    def test_field_type_evaluation_date(self):
        field = ControlEvaluation._meta.get_field('evaluation_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_policy_version(self):
        field = ControlEvaluation._meta.get_field('policy_version')
        self.assertIsNotNone(field)
    def test_field_type_policy_version(self):
        field = ControlEvaluation._meta.get_field('policy_version')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class RiskModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Risk._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Risk._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Risk._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Risk._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Risk._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Risk._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Risk._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Risk._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_project(self):
        field = Risk._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Risk._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_title(self):
        field = Risk._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = Risk._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Risk._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Risk._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = Risk._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = Risk._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_owner(self):
        field = Risk._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = Risk._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_likelihood(self):
        field = Risk._meta.get_field('likelihood')
        self.assertIsNotNone(field)
    def test_field_type_likelihood(self):
        field = Risk._meta.get_field('likelihood')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_impact(self):
        field = Risk._meta.get_field('impact')
        self.assertIsNotNone(field)
    def test_field_type_impact(self):
        field = Risk._meta.get_field('impact')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_inherent_risk_score(self):
        field = Risk._meta.get_field('inherent_risk_score')
        self.assertIsNotNone(field)
    def test_field_type_inherent_risk_score(self):
        field = Risk._meta.get_field('inherent_risk_score')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_status(self):
        field = Risk._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Risk._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_due_date(self):
        field = Risk._meta.get_field('due_date')
        self.assertIsNotNone(field)
    def test_field_type_due_date(self):
        field = Risk._meta.get_field('due_date')
        self.assertEqual(field.__class__.__name__, 'DateField')

class RiskTreatmentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = RiskTreatment._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = RiskTreatment._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = RiskTreatment._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = RiskTreatment._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = RiskTreatment._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = RiskTreatment._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_risk(self):
        field = RiskTreatment._meta.get_field('risk')
        self.assertIsNotNone(field)
    def test_field_type_risk(self):
        field = RiskTreatment._meta.get_field('risk')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_owner(self):
        field = RiskTreatment._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = RiskTreatment._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_action(self):
        field = RiskTreatment._meta.get_field('action')
        self.assertIsNotNone(field)
    def test_field_type_action(self):
        field = RiskTreatment._meta.get_field('action')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = RiskTreatment._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = RiskTreatment._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_due_date(self):
        field = RiskTreatment._meta.get_field('due_date')
        self.assertIsNotNone(field)
    def test_field_type_due_date(self):
        field = RiskTreatment._meta.get_field('due_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_status(self):
        field = RiskTreatment._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = RiskTreatment._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')

class ExceptionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Exception._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Exception._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Exception._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Exception._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Exception._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Exception._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Exception._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Exception._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_project(self):
        field = Exception._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Exception._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_control(self):
        field = Exception._meta.get_field('control')
        self.assertIsNotNone(field)
    def test_field_type_control(self):
        field = Exception._meta.get_field('control')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_reason(self):
        field = Exception._meta.get_field('reason')
        self.assertIsNotNone(field)
    def test_field_type_reason(self):
        field = Exception._meta.get_field('reason')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_compensating_control(self):
        field = Exception._meta.get_field('compensating_control')
        self.assertIsNotNone(field)
    def test_field_type_compensating_control(self):
        field = Exception._meta.get_field('compensating_control')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_owner(self):
        field = Exception._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = Exception._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_approver(self):
        field = Exception._meta.get_field('approver')
        self.assertIsNotNone(field)
    def test_field_type_approver(self):
        field = Exception._meta.get_field('approver')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = Exception._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Exception._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_start_date(self):
        field = Exception._meta.get_field('start_date')
        self.assertIsNotNone(field)
    def test_field_type_start_date(self):
        field = Exception._meta.get_field('start_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_expiration_date(self):
        field = Exception._meta.get_field('expiration_date')
        self.assertIsNotNone(field)
    def test_field_type_expiration_date(self):
        field = Exception._meta.get_field('expiration_date')
        self.assertEqual(field.__class__.__name__, 'DateField')



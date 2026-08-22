from django.test import TestCase
from django.utils import timezone
from .models import *

class FindingModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Finding._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Finding._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Finding._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Finding._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Finding._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Finding._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = Finding._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Finding._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_snapshot(self):
        field = Finding._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = Finding._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_scanner_id(self):
        field = Finding._meta.get_field('scanner_id')
        self.assertIsNotNone(field)
    def test_field_type_scanner_id(self):
        field = Finding._meta.get_field('scanner_id')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_category(self):
        field = Finding._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = Finding._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_severity(self):
        field = Finding._meta.get_field('severity')
        self.assertIsNotNone(field)
    def test_field_type_severity(self):
        field = Finding._meta.get_field('severity')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_confidence(self):
        field = Finding._meta.get_field('confidence')
        self.assertIsNotNone(field)
    def test_field_type_confidence(self):
        field = Finding._meta.get_field('confidence')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_file_path(self):
        field = Finding._meta.get_field('file_path')
        self.assertIsNotNone(field)
    def test_field_type_file_path(self):
        field = Finding._meta.get_field('file_path')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_line_number(self):
        field = Finding._meta.get_field('line_number')
        self.assertIsNotNone(field)
    def test_field_type_line_number(self):
        field = Finding._meta.get_field('line_number')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_rule_identifier(self):
        field = Finding._meta.get_field('rule_identifier')
        self.assertIsNotNone(field)
    def test_field_type_rule_identifier(self):
        field = Finding._meta.get_field('rule_identifier')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_short_description(self):
        field = Finding._meta.get_field('short_description')
        self.assertIsNotNone(field)
    def test_field_type_short_description(self):
        field = Finding._meta.get_field('short_description')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_redacted_evidence(self):
        field = Finding._meta.get_field('redacted_evidence')
        self.assertIsNotNone(field)
    def test_field_type_redacted_evidence(self):
        field = Finding._meta.get_field('redacted_evidence')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_remediation(self):
        field = Finding._meta.get_field('remediation')
        self.assertIsNotNone(field)
    def test_field_type_remediation(self):
        field = Finding._meta.get_field('remediation')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_status(self):
        field = Finding._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Finding._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')

class FindingActivityModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = FindingActivity._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = FindingActivity._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = FindingActivity._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = FindingActivity._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = FindingActivity._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = FindingActivity._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_finding(self):
        field = FindingActivity._meta.get_field('finding')
        self.assertIsNotNone(field)
    def test_field_type_finding(self):
        field = FindingActivity._meta.get_field('finding')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = FindingActivity._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = FindingActivity._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_previous_status(self):
        field = FindingActivity._meta.get_field('previous_status')
        self.assertIsNotNone(field)
    def test_field_type_previous_status(self):
        field = FindingActivity._meta.get_field('previous_status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_new_status(self):
        field = FindingActivity._meta.get_field('new_status')
        self.assertIsNotNone(field)
    def test_field_type_new_status(self):
        field = FindingActivity._meta.get_field('new_status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_note(self):
        field = FindingActivity._meta.get_field('note')
        self.assertIsNotNone(field)
    def test_field_type_note(self):
        field = FindingActivity._meta.get_field('note')
        self.assertEqual(field.__class__.__name__, 'TextField')

class DependencyModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Dependency._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Dependency._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Dependency._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Dependency._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Dependency._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Dependency._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = Dependency._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Dependency._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_snapshot(self):
        field = Dependency._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = Dependency._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_name(self):
        field = Dependency._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Dependency._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_version(self):
        field = Dependency._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = Dependency._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_ecosystem(self):
        field = Dependency._meta.get_field('ecosystem')
        self.assertIsNotNone(field)
    def test_field_type_ecosystem(self):
        field = Dependency._meta.get_field('ecosystem')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_manifest_source(self):
        field = Dependency._meta.get_field('manifest_source')
        self.assertIsNotNone(field)
    def test_field_type_manifest_source(self):
        field = Dependency._meta.get_field('manifest_source')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_license_identifier(self):
        field = Dependency._meta.get_field('license_identifier')
        self.assertIsNotNone(field)
    def test_field_type_license_identifier(self):
        field = Dependency._meta.get_field('license_identifier')
        self.assertEqual(field.__class__.__name__, 'CharField')

class SecurityScanJobModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = SecurityScanJob._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = SecurityScanJob._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = SecurityScanJob._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = SecurityScanJob._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = SecurityScanJob._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = SecurityScanJob._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_snapshot(self):
        field = SecurityScanJob._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = SecurityScanJob._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_status(self):
        field = SecurityScanJob._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = SecurityScanJob._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_error_message(self):
        field = SecurityScanJob._meta.get_field('error_message')
        self.assertIsNotNone(field)
    def test_field_type_error_message(self):
        field = SecurityScanJob._meta.get_field('error_message')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_completed_at(self):
        field = SecurityScanJob._meta.get_field('completed_at')
        self.assertIsNotNone(field)
    def test_field_type_completed_at(self):
        field = SecurityScanJob._meta.get_field('completed_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')



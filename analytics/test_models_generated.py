from django.test import TestCase
from django.utils import timezone
from .models import *

class PlatformMetricModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = PlatformMetric._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = PlatformMetric._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = PlatformMetric._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = PlatformMetric._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = PlatformMetric._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = PlatformMetric._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_date(self):
        field = PlatformMetric._meta.get_field('date')
        self.assertIsNotNone(field)
    def test_field_type_date(self):
        field = PlatformMetric._meta.get_field('date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_category(self):
        field = PlatformMetric._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = PlatformMetric._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_metric_name(self):
        field = PlatformMetric._meta.get_field('metric_name')
        self.assertIsNotNone(field)
    def test_field_type_metric_name(self):
        field = PlatformMetric._meta.get_field('metric_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_value(self):
        field = PlatformMetric._meta.get_field('value')
        self.assertIsNotNone(field)
    def test_field_type_value(self):
        field = PlatformMetric._meta.get_field('value')
        self.assertEqual(field.__class__.__name__, 'DecimalField')

class ReportTemplateModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ReportTemplate._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ReportTemplate._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ReportTemplate._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ReportTemplate._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ReportTemplate._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ReportTemplate._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = ReportTemplate._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = ReportTemplate._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = ReportTemplate._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = ReportTemplate._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_report_type(self):
        field = ReportTemplate._meta.get_field('report_type')
        self.assertIsNotNone(field)
    def test_field_type_report_type(self):
        field = ReportTemplate._meta.get_field('report_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_parameters_schema(self):
        field = ReportTemplate._meta.get_field('parameters_schema')
        self.assertIsNotNone(field)
    def test_field_type_parameters_schema(self):
        field = ReportTemplate._meta.get_field('parameters_schema')
        self.assertEqual(field.__class__.__name__, 'JSONField')

class ReportExecutionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ReportExecution._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ReportExecution._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ReportExecution._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ReportExecution._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ReportExecution._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ReportExecution._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_template(self):
        field = ReportExecution._meta.get_field('template')
        self.assertIsNotNone(field)
    def test_field_type_template(self):
        field = ReportExecution._meta.get_field('template')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_requested_by(self):
        field = ReportExecution._meta.get_field('requested_by')
        self.assertIsNotNone(field)
    def test_field_type_requested_by(self):
        field = ReportExecution._meta.get_field('requested_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_parameters(self):
        field = ReportExecution._meta.get_field('parameters')
        self.assertIsNotNone(field)
    def test_field_type_parameters(self):
        field = ReportExecution._meta.get_field('parameters')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_status(self):
        field = ReportExecution._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ReportExecution._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_file_url(self):
        field = ReportExecution._meta.get_field('file_url')
        self.assertIsNotNone(field)
    def test_field_type_file_url(self):
        field = ReportExecution._meta.get_field('file_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_error_message(self):
        field = ReportExecution._meta.get_field('error_message')
        self.assertIsNotNone(field)
    def test_field_type_error_message(self):
        field = ReportExecution._meta.get_field('error_message')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_started_at(self):
        field = ReportExecution._meta.get_field('started_at')
        self.assertIsNotNone(field)
    def test_field_type_started_at(self):
        field = ReportExecution._meta.get_field('started_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_completed_at(self):
        field = ReportExecution._meta.get_field('completed_at')
        self.assertIsNotNone(field)
    def test_field_type_completed_at(self):
        field = ReportExecution._meta.get_field('completed_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class ScheduledReportModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ScheduledReport._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ScheduledReport._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ScheduledReport._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ScheduledReport._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ScheduledReport._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ScheduledReport._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_template(self):
        field = ScheduledReport._meta.get_field('template')
        self.assertIsNotNone(field)
    def test_field_type_template(self):
        field = ScheduledReport._meta.get_field('template')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_recipient(self):
        field = ScheduledReport._meta.get_field('recipient')
        self.assertIsNotNone(field)
    def test_field_type_recipient(self):
        field = ScheduledReport._meta.get_field('recipient')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_schedule_cron(self):
        field = ScheduledReport._meta.get_field('schedule_cron')
        self.assertIsNotNone(field)
    def test_field_type_schedule_cron(self):
        field = ScheduledReport._meta.get_field('schedule_cron')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_parameters(self):
        field = ScheduledReport._meta.get_field('parameters')
        self.assertIsNotNone(field)
    def test_field_type_parameters(self):
        field = ScheduledReport._meta.get_field('parameters')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_is_active(self):
        field = ScheduledReport._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = ScheduledReport._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_last_execution(self):
        field = ScheduledReport._meta.get_field('last_execution')
        self.assertIsNotNone(field)
    def test_field_type_last_execution(self):
        field = ScheduledReport._meta.get_field('last_execution')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')



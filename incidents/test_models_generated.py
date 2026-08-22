from django.test import TestCase
from django.utils import timezone
from .models import *

class IncidentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Incident._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Incident._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Incident._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Incident._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Incident._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Incident._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_title(self):
        field = Incident._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = Incident._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Incident._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Incident._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_status(self):
        field = Incident._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Incident._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_severity(self):
        field = Incident._meta.get_field('severity')
        self.assertIsNotNone(field)
    def test_field_type_severity(self):
        field = Incident._meta.get_field('severity')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_project(self):
        field = Incident._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Incident._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_assignee(self):
        field = Incident._meta.get_field('assignee')
        self.assertIsNotNone(field)
    def test_field_type_assignee(self):
        field = Incident._meta.get_field('assignee')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class IncidentEventModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = IncidentEvent._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = IncidentEvent._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = IncidentEvent._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = IncidentEvent._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = IncidentEvent._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = IncidentEvent._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_incident(self):
        field = IncidentEvent._meta.get_field('incident')
        self.assertIsNotNone(field)
    def test_field_type_incident(self):
        field = IncidentEvent._meta.get_field('incident')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_actor(self):
        field = IncidentEvent._meta.get_field('actor')
        self.assertIsNotNone(field)
    def test_field_type_actor(self):
        field = IncidentEvent._meta.get_field('actor')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_action(self):
        field = IncidentEvent._meta.get_field('action')
        self.assertIsNotNone(field)
    def test_field_type_action(self):
        field = IncidentEvent._meta.get_field('action')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_details(self):
        field = IncidentEvent._meta.get_field('details')
        self.assertIsNotNone(field)
    def test_field_type_details(self):
        field = IncidentEvent._meta.get_field('details')
        self.assertEqual(field.__class__.__name__, 'TextField')

class PostmortemModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Postmortem._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Postmortem._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Postmortem._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Postmortem._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Postmortem._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Postmortem._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_incident(self):
        field = Postmortem._meta.get_field('incident')
        self.assertIsNotNone(field)
    def test_field_type_incident(self):
        field = Postmortem._meta.get_field('incident')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_root_cause(self):
        field = Postmortem._meta.get_field('root_cause')
        self.assertIsNotNone(field)
    def test_field_type_root_cause(self):
        field = Postmortem._meta.get_field('root_cause')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_impact(self):
        field = Postmortem._meta.get_field('impact')
        self.assertIsNotNone(field)
    def test_field_type_impact(self):
        field = Postmortem._meta.get_field('impact')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_corrective_actions(self):
        field = Postmortem._meta.get_field('corrective_actions')
        self.assertIsNotNone(field)
    def test_field_type_corrective_actions(self):
        field = Postmortem._meta.get_field('corrective_actions')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_lessons_learned(self):
        field = Postmortem._meta.get_field('lessons_learned')
        self.assertIsNotNone(field)
    def test_field_type_lessons_learned(self):
        field = Postmortem._meta.get_field('lessons_learned')
        self.assertEqual(field.__class__.__name__, 'TextField')



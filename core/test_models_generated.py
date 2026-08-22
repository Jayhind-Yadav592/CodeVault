from django.test import TestCase
from django.utils import timezone
from .models import *

class SystemConfigurationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = SystemConfiguration._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = SystemConfiguration._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = SystemConfiguration._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = SystemConfiguration._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = SystemConfiguration._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = SystemConfiguration._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_key(self):
        field = SystemConfiguration._meta.get_field('key')
        self.assertIsNotNone(field)
    def test_field_type_key(self):
        field = SystemConfiguration._meta.get_field('key')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_value(self):
        field = SystemConfiguration._meta.get_field('value')
        self.assertIsNotNone(field)
    def test_field_type_value(self):
        field = SystemConfiguration._meta.get_field('value')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_description(self):
        field = SystemConfiguration._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = SystemConfiguration._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_version(self):
        field = SystemConfiguration._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = SystemConfiguration._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_updated_by(self):
        field = SystemConfiguration._meta.get_field('updated_by')
        self.assertIsNotNone(field)
    def test_field_type_updated_by(self):
        field = SystemConfiguration._meta.get_field('updated_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class FeatureFlagModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = FeatureFlag._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = FeatureFlag._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = FeatureFlag._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = FeatureFlag._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = FeatureFlag._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = FeatureFlag._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = FeatureFlag._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = FeatureFlag._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_enabled(self):
        field = FeatureFlag._meta.get_field('is_enabled')
        self.assertIsNotNone(field)
    def test_field_type_is_enabled(self):
        field = FeatureFlag._meta.get_field('is_enabled')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_description(self):
        field = FeatureFlag._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = FeatureFlag._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_updated_by(self):
        field = FeatureFlag._meta.get_field('updated_by')
        self.assertIsNotNone(field)
    def test_field_type_updated_by(self):
        field = FeatureFlag._meta.get_field('updated_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')



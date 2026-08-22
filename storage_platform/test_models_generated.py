from django.test import TestCase
from django.utils import timezone
from .models import *

class StorageObjectModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = StorageObject._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = StorageObject._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = StorageObject._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = StorageObject._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = StorageObject._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = StorageObject._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = StorageObject._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = StorageObject._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_provider(self):
        field = StorageObject._meta.get_field('provider')
        self.assertIsNotNone(field)
    def test_field_type_provider(self):
        field = StorageObject._meta.get_field('provider')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_path(self):
        field = StorageObject._meta.get_field('path')
        self.assertIsNotNone(field)
    def test_field_type_path(self):
        field = StorageObject._meta.get_field('path')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_size_bytes(self):
        field = StorageObject._meta.get_field('size_bytes')
        self.assertIsNotNone(field)
    def test_field_type_size_bytes(self):
        field = StorageObject._meta.get_field('size_bytes')
        self.assertEqual(field.__class__.__name__, 'BigIntegerField')
    def test_field_existence_content_type(self):
        field = StorageObject._meta.get_field('content_type')
        self.assertIsNotNone(field)
    def test_field_type_content_type(self):
        field = StorageObject._meta.get_field('content_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_owner(self):
        field = StorageObject._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = StorageObject._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_is_public(self):
        field = StorageObject._meta.get_field('is_public')
        self.assertIsNotNone(field)
    def test_field_type_is_public(self):
        field = StorageObject._meta.get_field('is_public')
        self.assertEqual(field.__class__.__name__, 'BooleanField')



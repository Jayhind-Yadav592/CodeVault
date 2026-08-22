from django.test import TestCase
from django.utils import timezone
from .models import *

class AuditLogModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = AuditLog._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = AuditLog._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = AuditLog._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = AuditLog._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = AuditLog._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = AuditLog._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_user(self):
        field = AuditLog._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = AuditLog._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_action(self):
        field = AuditLog._meta.get_field('action')
        self.assertIsNotNone(field)
    def test_field_type_action(self):
        field = AuditLog._meta.get_field('action')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_ip_address(self):
        field = AuditLog._meta.get_field('ip_address')
        self.assertIsNotNone(field)
    def test_field_type_ip_address(self):
        field = AuditLog._meta.get_field('ip_address')
        self.assertEqual(field.__class__.__name__, 'GenericIPAddressField')
    def test_field_existence_resource_type(self):
        field = AuditLog._meta.get_field('resource_type')
        self.assertIsNotNone(field)
    def test_field_type_resource_type(self):
        field = AuditLog._meta.get_field('resource_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_resource_id(self):
        field = AuditLog._meta.get_field('resource_id')
        self.assertIsNotNone(field)
    def test_field_type_resource_id(self):
        field = AuditLog._meta.get_field('resource_id')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_details(self):
        field = AuditLog._meta.get_field('details')
        self.assertIsNotNone(field)
    def test_field_type_details(self):
        field = AuditLog._meta.get_field('details')
        self.assertEqual(field.__class__.__name__, 'JSONField')



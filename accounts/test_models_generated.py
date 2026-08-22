from django.test import TestCase
from django.utils import timezone
from .models import *

class UserModelDetailedTest(TestCase):
    def test_field_existence_password(self):
        field = User._meta.get_field('password')
        self.assertIsNotNone(field)
    def test_field_type_password(self):
        field = User._meta.get_field('password')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_last_login(self):
        field = User._meta.get_field('last_login')
        self.assertIsNotNone(field)
    def test_field_type_last_login(self):
        field = User._meta.get_field('last_login')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_is_superuser(self):
        field = User._meta.get_field('is_superuser')
        self.assertIsNotNone(field)
    def test_field_type_is_superuser(self):
        field = User._meta.get_field('is_superuser')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_id(self):
        field = User._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = User._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = User._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = User._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = User._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = User._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_email(self):
        field = User._meta.get_field('email')
        self.assertIsNotNone(field)
    def test_field_type_email(self):
        field = User._meta.get_field('email')
        self.assertEqual(field.__class__.__name__, 'EmailField')
    def test_field_existence_first_name(self):
        field = User._meta.get_field('first_name')
        self.assertIsNotNone(field)
    def test_field_type_first_name(self):
        field = User._meta.get_field('first_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_last_name(self):
        field = User._meta.get_field('last_name')
        self.assertIsNotNone(field)
    def test_field_type_last_name(self):
        field = User._meta.get_field('last_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_role(self):
        field = User._meta.get_field('role')
        self.assertIsNotNone(field)
    def test_field_type_role(self):
        field = User._meta.get_field('role')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_staff(self):
        field = User._meta.get_field('is_staff')
        self.assertIsNotNone(field)
    def test_field_type_is_staff(self):
        field = User._meta.get_field('is_staff')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_is_active(self):
        field = User._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = User._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')



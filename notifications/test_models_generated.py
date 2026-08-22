from django.test import TestCase
from django.utils import timezone
from .models import *

class NotificationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Notification._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Notification._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Notification._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Notification._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Notification._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Notification._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_user(self):
        field = Notification._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = Notification._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_title(self):
        field = Notification._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = Notification._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_message(self):
        field = Notification._meta.get_field('message')
        self.assertIsNotNone(field)
    def test_field_type_message(self):
        field = Notification._meta.get_field('message')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_notification_type(self):
        field = Notification._meta.get_field('notification_type')
        self.assertIsNotNone(field)
    def test_field_type_notification_type(self):
        field = Notification._meta.get_field('notification_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_read(self):
        field = Notification._meta.get_field('is_read')
        self.assertIsNotNone(field)
    def test_field_type_is_read(self):
        field = Notification._meta.get_field('is_read')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_content_type(self):
        field = Notification._meta.get_field('content_type')
        self.assertIsNotNone(field)
    def test_field_type_content_type(self):
        field = Notification._meta.get_field('content_type')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_object_id(self):
        field = Notification._meta.get_field('object_id')
        self.assertIsNotNone(field)
    def test_field_type_object_id(self):
        field = Notification._meta.get_field('object_id')
        self.assertEqual(field.__class__.__name__, 'CharField')



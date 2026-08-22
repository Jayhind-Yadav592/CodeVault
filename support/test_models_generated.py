from django.test import TestCase
from django.utils import timezone
from .models import *

class TicketModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Ticket._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Ticket._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Ticket._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Ticket._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Ticket._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Ticket._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_subject(self):
        field = Ticket._meta.get_field('subject')
        self.assertIsNotNone(field)
    def test_field_type_subject(self):
        field = Ticket._meta.get_field('subject')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Ticket._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Ticket._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_status(self):
        field = Ticket._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Ticket._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_priority(self):
        field = Ticket._meta.get_field('priority')
        self.assertIsNotNone(field)
    def test_field_type_priority(self):
        field = Ticket._meta.get_field('priority')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_organization(self):
        field = Ticket._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Ticket._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_submitter(self):
        field = Ticket._meta.get_field('submitter')
        self.assertIsNotNone(field)
    def test_field_type_submitter(self):
        field = Ticket._meta.get_field('submitter')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_assignee(self):
        field = Ticket._meta.get_field('assignee')
        self.assertIsNotNone(field)
    def test_field_type_assignee(self):
        field = Ticket._meta.get_field('assignee')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class TicketCommentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = TicketComment._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = TicketComment._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = TicketComment._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = TicketComment._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = TicketComment._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = TicketComment._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_ticket(self):
        field = TicketComment._meta.get_field('ticket')
        self.assertIsNotNone(field)
    def test_field_type_ticket(self):
        field = TicketComment._meta.get_field('ticket')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_author(self):
        field = TicketComment._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = TicketComment._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_content(self):
        field = TicketComment._meta.get_field('content')
        self.assertIsNotNone(field)
    def test_field_type_content(self):
        field = TicketComment._meta.get_field('content')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_internal(self):
        field = TicketComment._meta.get_field('is_internal')
        self.assertIsNotNone(field)
    def test_field_type_is_internal(self):
        field = TicketComment._meta.get_field('is_internal')
        self.assertEqual(field.__class__.__name__, 'BooleanField')



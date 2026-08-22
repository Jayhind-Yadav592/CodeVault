from django.test import TestCase
from django.utils import timezone
from .models import *

class PlanModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Plan._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Plan._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Plan._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Plan._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Plan._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Plan._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = Plan._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Plan._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Plan._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Plan._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_price_monthly(self):
        field = Plan._meta.get_field('price_monthly')
        self.assertIsNotNone(field)
    def test_field_type_price_monthly(self):
        field = Plan._meta.get_field('price_monthly')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_max_projects(self):
        field = Plan._meta.get_field('max_projects')
        self.assertIsNotNone(field)
    def test_field_type_max_projects(self):
        field = Plan._meta.get_field('max_projects')
        self.assertEqual(field.__class__.__name__, 'IntegerField')

class SubscriptionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Subscription._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Subscription._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Subscription._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Subscription._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Subscription._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Subscription._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_organization(self):
        field = Subscription._meta.get_field('organization')
        self.assertIsNotNone(field)
    def test_field_type_organization(self):
        field = Subscription._meta.get_field('organization')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_plan(self):
        field = Subscription._meta.get_field('plan')
        self.assertIsNotNone(field)
    def test_field_type_plan(self):
        field = Subscription._meta.get_field('plan')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = Subscription._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Subscription._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_current_period_end(self):
        field = Subscription._meta.get_field('current_period_end')
        self.assertIsNotNone(field)
    def test_field_type_current_period_end(self):
        field = Subscription._meta.get_field('current_period_end')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class InvoiceModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Invoice._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Invoice._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Invoice._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Invoice._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Invoice._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Invoice._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_subscription(self):
        field = Invoice._meta.get_field('subscription')
        self.assertIsNotNone(field)
    def test_field_type_subscription(self):
        field = Invoice._meta.get_field('subscription')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_amount_due(self):
        field = Invoice._meta.get_field('amount_due')
        self.assertIsNotNone(field)
    def test_field_type_amount_due(self):
        field = Invoice._meta.get_field('amount_due')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_status(self):
        field = Invoice._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Invoice._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_due_date(self):
        field = Invoice._meta.get_field('due_date')
        self.assertIsNotNone(field)
    def test_field_type_due_date(self):
        field = Invoice._meta.get_field('due_date')
        self.assertEqual(field.__class__.__name__, 'DateField')



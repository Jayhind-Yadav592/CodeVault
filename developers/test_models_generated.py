from django.test import TestCase
from django.utils import timezone
from .models import *

class DeveloperProfileModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = DeveloperProfile._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = DeveloperProfile._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = DeveloperProfile._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = DeveloperProfile._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = DeveloperProfile._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = DeveloperProfile._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_user(self):
        field = DeveloperProfile._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = DeveloperProfile._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_display_name(self):
        field = DeveloperProfile._meta.get_field('display_name')
        self.assertIsNotNone(field)
    def test_field_type_display_name(self):
        field = DeveloperProfile._meta.get_field('display_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_bio(self):
        field = DeveloperProfile._meta.get_field('bio')
        self.assertIsNotNone(field)
    def test_field_type_bio(self):
        field = DeveloperProfile._meta.get_field('bio')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_country(self):
        field = DeveloperProfile._meta.get_field('country')
        self.assertIsNotNone(field)
    def test_field_type_country(self):
        field = DeveloperProfile._meta.get_field('country')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_developer_type(self):
        field = DeveloperProfile._meta.get_field('developer_type')
        self.assertIsNotNone(field)
    def test_field_type_developer_type(self):
        field = DeveloperProfile._meta.get_field('developer_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_website(self):
        field = DeveloperProfile._meta.get_field('website')
        self.assertIsNotNone(field)
    def test_field_type_website(self):
        field = DeveloperProfile._meta.get_field('website')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_github_url(self):
        field = DeveloperProfile._meta.get_field('github_url')
        self.assertIsNotNone(field)
    def test_field_type_github_url(self):
        field = DeveloperProfile._meta.get_field('github_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_linkedin_url(self):
        field = DeveloperProfile._meta.get_field('linkedin_url')
        self.assertIsNotNone(field)
    def test_field_type_linkedin_url(self):
        field = DeveloperProfile._meta.get_field('linkedin_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_profile_image(self):
        field = DeveloperProfile._meta.get_field('profile_image')
        self.assertIsNotNone(field)
    def test_field_type_profile_image(self):
        field = DeveloperProfile._meta.get_field('profile_image')
        self.assertEqual(field.__class__.__name__, 'ImageField')
    def test_field_existence_skills(self):
        field = DeveloperProfile._meta.get_field('skills')
        self.assertIsNotNone(field)
    def test_field_type_skills(self):
        field = DeveloperProfile._meta.get_field('skills')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_languages(self):
        field = DeveloperProfile._meta.get_field('languages')
        self.assertIsNotNone(field)
    def test_field_type_languages(self):
        field = DeveloperProfile._meta.get_field('languages')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_years_of_experience(self):
        field = DeveloperProfile._meta.get_field('years_of_experience')
        self.assertIsNotNone(field)
    def test_field_type_years_of_experience(self):
        field = DeveloperProfile._meta.get_field('years_of_experience')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_company_name(self):
        field = DeveloperProfile._meta.get_field('company_name')
        self.assertIsNotNone(field)
    def test_field_type_company_name(self):
        field = DeveloperProfile._meta.get_field('company_name')
        self.assertEqual(field.__class__.__name__, 'CharField')



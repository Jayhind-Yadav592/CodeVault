from django.test import TestCase
from django.utils import timezone
from .models import *

class CategoryModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Category._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Category._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Category._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Category._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Category._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Category._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = Category._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Category._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_slug(self):
        field = Category._meta.get_field('slug')
        self.assertIsNotNone(field)
    def test_field_type_slug(self):
        field = Category._meta.get_field('slug')
        self.assertEqual(field.__class__.__name__, 'SlugField')
    def test_field_existence_description(self):
        field = Category._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Category._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_active(self):
        field = Category._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = Category._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')

class ProjectModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Project._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Project._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Project._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Project._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Project._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Project._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_is_deleted(self):
        field = Project._meta.get_field('is_deleted')
        self.assertIsNotNone(field)
    def test_field_type_is_deleted(self):
        field = Project._meta.get_field('is_deleted')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_deleted_at(self):
        field = Project._meta.get_field('deleted_at')
        self.assertIsNotNone(field)
    def test_field_type_deleted_at(self):
        field = Project._meta.get_field('deleted_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = Project._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = Project._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_slug(self):
        field = Project._meta.get_field('slug')
        self.assertIsNotNone(field)
    def test_field_type_slug(self):
        field = Project._meta.get_field('slug')
        self.assertEqual(field.__class__.__name__, 'SlugField')
    def test_field_existence_short_description(self):
        field = Project._meta.get_field('short_description')
        self.assertIsNotNone(field)
    def test_field_type_short_description(self):
        field = Project._meta.get_field('short_description')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_full_description(self):
        field = Project._meta.get_field('full_description')
        self.assertIsNotNone(field)
    def test_field_type_full_description(self):
        field = Project._meta.get_field('full_description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = Project._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = Project._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_primary_language(self):
        field = Project._meta.get_field('primary_language')
        self.assertIsNotNone(field)
    def test_field_type_primary_language(self):
        field = Project._meta.get_field('primary_language')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_additional_languages(self):
        field = Project._meta.get_field('additional_languages')
        self.assertIsNotNone(field)
    def test_field_type_additional_languages(self):
        field = Project._meta.get_field('additional_languages')
        self.assertEqual(field.__class__.__name__, 'JSONField')
    def test_field_existence_project_type(self):
        field = Project._meta.get_field('project_type')
        self.assertIsNotNone(field)
    def test_field_type_project_type(self):
        field = Project._meta.get_field('project_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_current_version(self):
        field = Project._meta.get_field('current_version')
        self.assertIsNotNone(field)
    def test_field_type_current_version(self):
        field = Project._meta.get_field('current_version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_development_status(self):
        field = Project._meta.get_field('development_status')
        self.assertIsNotNone(field)
    def test_field_type_development_status(self):
        field = Project._meta.get_field('development_status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_repository_url(self):
        field = Project._meta.get_field('repository_url')
        self.assertIsNotNone(field)
    def test_field_type_repository_url(self):
        field = Project._meta.get_field('repository_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_documentation_url(self):
        field = Project._meta.get_field('documentation_url')
        self.assertIsNotNone(field)
    def test_field_type_documentation_url(self):
        field = Project._meta.get_field('documentation_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_demo_url(self):
        field = Project._meta.get_field('demo_url')
        self.assertIsNotNone(field)
    def test_field_type_demo_url(self):
        field = Project._meta.get_field('demo_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_license_info(self):
        field = Project._meta.get_field('license_info')
        self.assertIsNotNone(field)
    def test_field_type_license_info(self):
        field = Project._meta.get_field('license_info')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_approximate_loc(self):
        field = Project._meta.get_field('approximate_loc')
        self.assertIsNotNone(field)
    def test_field_type_approximate_loc(self):
        field = Project._meta.get_field('approximate_loc')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_project_start_date(self):
        field = Project._meta.get_field('project_start_date')
        self.assertIsNotNone(field)
    def test_field_type_project_start_date(self):
        field = Project._meta.get_field('project_start_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_last_development_date(self):
        field = Project._meta.get_field('last_development_date')
        self.assertIsNotNone(field)
    def test_field_type_last_development_date(self):
        field = Project._meta.get_field('last_development_date')
        self.assertEqual(field.__class__.__name__, 'DateField')
    def test_field_existence_team_size(self):
        field = Project._meta.get_field('team_size')
        self.assertIsNotNone(field)
    def test_field_type_team_size(self):
        field = Project._meta.get_field('team_size')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_state(self):
        field = Project._meta.get_field('state')
        self.assertIsNotNone(field)
    def test_field_type_state(self):
        field = Project._meta.get_field('state')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_owner(self):
        field = Project._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = Project._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class ProjectStateHistoryModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectStateHistory._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectStateHistory._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectStateHistory._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectStateHistory._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectStateHistory._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectStateHistory._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectStateHistory._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectStateHistory._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_from_state(self):
        field = ProjectStateHistory._meta.get_field('from_state')
        self.assertIsNotNone(field)
    def test_field_type_from_state(self):
        field = ProjectStateHistory._meta.get_field('from_state')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_to_state(self):
        field = ProjectStateHistory._meta.get_field('to_state')
        self.assertIsNotNone(field)
    def test_field_type_to_state(self):
        field = ProjectStateHistory._meta.get_field('to_state')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_changed_by(self):
        field = ProjectStateHistory._meta.get_field('changed_by')
        self.assertIsNotNone(field)
    def test_field_type_changed_by(self):
        field = ProjectStateHistory._meta.get_field('changed_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_reason(self):
        field = ProjectStateHistory._meta.get_field('reason')
        self.assertIsNotNone(field)
    def test_field_type_reason(self):
        field = ProjectStateHistory._meta.get_field('reason')
        self.assertEqual(field.__class__.__name__, 'TextField')

class OwnershipDeclarationModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = OwnershipDeclaration._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = OwnershipDeclaration._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = OwnershipDeclaration._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = OwnershipDeclaration._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = OwnershipDeclaration._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = OwnershipDeclaration._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = OwnershipDeclaration._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = OwnershipDeclaration._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = OwnershipDeclaration._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = OwnershipDeclaration._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_declaration_text(self):
        field = OwnershipDeclaration._meta.get_field('declaration_text')
        self.assertIsNotNone(field)
    def test_field_type_declaration_text(self):
        field = OwnershipDeclaration._meta.get_field('declaration_text')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_declaration_version(self):
        field = OwnershipDeclaration._meta.get_field('declaration_version')
        self.assertIsNotNone(field)
    def test_field_type_declaration_version(self):
        field = OwnershipDeclaration._meta.get_field('declaration_version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = OwnershipDeclaration._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = OwnershipDeclaration._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_ip_address(self):
        field = OwnershipDeclaration._meta.get_field('ip_address')
        self.assertIsNotNone(field)
    def test_field_type_ip_address(self):
        field = OwnershipDeclaration._meta.get_field('ip_address')
        self.assertEqual(field.__class__.__name__, 'GenericIPAddressField')
    def test_field_existence_signed_at(self):
        field = OwnershipDeclaration._meta.get_field('signed_at')
        self.assertIsNotNone(field)
    def test_field_type_signed_at(self):
        field = OwnershipDeclaration._meta.get_field('signed_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class ProjectContributorModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectContributor._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectContributor._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectContributor._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectContributor._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectContributor._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectContributor._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectContributor._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectContributor._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = ProjectContributor._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = ProjectContributor._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_role(self):
        field = ProjectContributor._meta.get_field('role')
        self.assertIsNotNone(field)
    def test_field_type_role(self):
        field = ProjectContributor._meta.get_field('role')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_ownership_percentage(self):
        field = ProjectContributor._meta.get_field('ownership_percentage')
        self.assertIsNotNone(field)
    def test_field_type_ownership_percentage(self):
        field = ProjectContributor._meta.get_field('ownership_percentage')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_contribution_description(self):
        field = ProjectContributor._meta.get_field('contribution_description')
        self.assertIsNotNone(field)
    def test_field_type_contribution_description(self):
        field = ProjectContributor._meta.get_field('contribution_description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_is_active(self):
        field = ProjectContributor._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = ProjectContributor._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')

class ProjectDocumentModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ProjectDocument._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ProjectDocument._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ProjectDocument._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ProjectDocument._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ProjectDocument._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ProjectDocument._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = ProjectDocument._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = ProjectDocument._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_document_type(self):
        field = ProjectDocument._meta.get_field('document_type')
        self.assertIsNotNone(field)
    def test_field_type_document_type(self):
        field = ProjectDocument._meta.get_field('document_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_title(self):
        field = ProjectDocument._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = ProjectDocument._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_file(self):
        field = ProjectDocument._meta.get_field('file')
        self.assertIsNotNone(field)
    def test_field_type_file(self):
        field = ProjectDocument._meta.get_field('file')
        self.assertEqual(field.__class__.__name__, 'FileField')
    def test_field_existence_version(self):
        field = ProjectDocument._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = ProjectDocument._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_public(self):
        field = ProjectDocument._meta.get_field('is_public')
        self.assertIsNotNone(field)
    def test_field_type_is_public(self):
        field = ProjectDocument._meta.get_field('is_public')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_uploaded_by(self):
        field = ProjectDocument._meta.get_field('uploaded_by')
        self.assertIsNotNone(field)
    def test_field_type_uploaded_by(self):
        field = ProjectDocument._meta.get_field('uploaded_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')



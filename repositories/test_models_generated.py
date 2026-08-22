from django.test import TestCase
from django.utils import timezone
from .models import *

class RepositoryConnectionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = RepositoryConnection._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = RepositoryConnection._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = RepositoryConnection._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = RepositoryConnection._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = RepositoryConnection._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = RepositoryConnection._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_project(self):
        field = RepositoryConnection._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = RepositoryConnection._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_provider(self):
        field = RepositoryConnection._meta.get_field('provider')
        self.assertIsNotNone(field)
    def test_field_type_provider(self):
        field = RepositoryConnection._meta.get_field('provider')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_repo_url(self):
        field = RepositoryConnection._meta.get_field('repo_url')
        self.assertIsNotNone(field)
    def test_field_type_repo_url(self):
        field = RepositoryConnection._meta.get_field('repo_url')
        self.assertEqual(field.__class__.__name__, 'URLField')
    def test_field_existence_repo_name(self):
        field = RepositoryConnection._meta.get_field('repo_name')
        self.assertIsNotNone(field)
    def test_field_type_repo_name(self):
        field = RepositoryConnection._meta.get_field('repo_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_default_branch(self):
        field = RepositoryConnection._meta.get_field('default_branch')
        self.assertIsNotNone(field)
    def test_field_type_default_branch(self):
        field = RepositoryConnection._meta.get_field('default_branch')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = RepositoryConnection._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = RepositoryConnection._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_last_sync_time(self):
        field = RepositoryConnection._meta.get_field('last_sync_time')
        self.assertIsNotNone(field)
    def test_field_type_last_sync_time(self):
        field = RepositoryConnection._meta.get_field('last_sync_time')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_last_error(self):
        field = RepositoryConnection._meta.get_field('last_error')
        self.assertIsNotNone(field)
    def test_field_type_last_error(self):
        field = RepositoryConnection._meta.get_field('last_error')
        self.assertEqual(field.__class__.__name__, 'TextField')

class AnalysisJobModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = AnalysisJob._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = AnalysisJob._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = AnalysisJob._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = AnalysisJob._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = AnalysisJob._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = AnalysisJob._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_repository(self):
        field = AnalysisJob._meta.get_field('repository')
        self.assertIsNotNone(field)
    def test_field_type_repository(self):
        field = AnalysisJob._meta.get_field('repository')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_state(self):
        field = AnalysisJob._meta.get_field('state')
        self.assertIsNotNone(field)
    def test_field_type_state(self):
        field = AnalysisJob._meta.get_field('state')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_started_at(self):
        field = AnalysisJob._meta.get_field('started_at')
        self.assertIsNotNone(field)
    def test_field_type_started_at(self):
        field = AnalysisJob._meta.get_field('started_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_completed_at(self):
        field = AnalysisJob._meta.get_field('completed_at')
        self.assertIsNotNone(field)
    def test_field_type_completed_at(self):
        field = AnalysisJob._meta.get_field('completed_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_task_id(self):
        field = AnalysisJob._meta.get_field('task_id')
        self.assertIsNotNone(field)
    def test_field_type_task_id(self):
        field = AnalysisJob._meta.get_field('task_id')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_error_log(self):
        field = AnalysisJob._meta.get_field('error_log')
        self.assertIsNotNone(field)
    def test_field_type_error_log(self):
        field = AnalysisJob._meta.get_field('error_log')
        self.assertEqual(field.__class__.__name__, 'TextField')

class AnalysisSnapshotModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = AnalysisSnapshot._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = AnalysisSnapshot._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = AnalysisSnapshot._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = AnalysisSnapshot._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = AnalysisSnapshot._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = AnalysisSnapshot._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_repository(self):
        field = AnalysisSnapshot._meta.get_field('repository')
        self.assertIsNotNone(field)
    def test_field_type_repository(self):
        field = AnalysisSnapshot._meta.get_field('repository')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_job(self):
        field = AnalysisSnapshot._meta.get_field('job')
        self.assertIsNotNone(field)
    def test_field_type_job(self):
        field = AnalysisSnapshot._meta.get_field('job')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_commit_hash(self):
        field = AnalysisSnapshot._meta.get_field('commit_hash')
        self.assertIsNotNone(field)
    def test_field_type_commit_hash(self):
        field = AnalysisSnapshot._meta.get_field('commit_hash')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_branch(self):
        field = AnalysisSnapshot._meta.get_field('branch')
        self.assertIsNotNone(field)
    def test_field_type_branch(self):
        field = AnalysisSnapshot._meta.get_field('branch')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_total_files(self):
        field = AnalysisSnapshot._meta.get_field('total_files')
        self.assertIsNotNone(field)
    def test_field_type_total_files(self):
        field = AnalysisSnapshot._meta.get_field('total_files')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_total_loc(self):
        field = AnalysisSnapshot._meta.get_field('total_loc')
        self.assertIsNotNone(field)
    def test_field_type_total_loc(self):
        field = AnalysisSnapshot._meta.get_field('total_loc')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_meaningful_loc(self):
        field = AnalysisSnapshot._meta.get_field('meaningful_loc')
        self.assertIsNotNone(field)
    def test_field_type_meaningful_loc(self):
        field = AnalysisSnapshot._meta.get_field('meaningful_loc')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_blank_lines(self):
        field = AnalysisSnapshot._meta.get_field('blank_lines')
        self.assertIsNotNone(field)
    def test_field_type_blank_lines(self):
        field = AnalysisSnapshot._meta.get_field('blank_lines')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_comment_lines(self):
        field = AnalysisSnapshot._meta.get_field('comment_lines')
        self.assertIsNotNone(field)
    def test_field_type_comment_lines(self):
        field = AnalysisSnapshot._meta.get_field('comment_lines')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_total_commits(self):
        field = AnalysisSnapshot._meta.get_field('total_commits')
        self.assertIsNotNone(field)
    def test_field_type_total_commits(self):
        field = AnalysisSnapshot._meta.get_field('total_commits')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_meaningful_commits(self):
        field = AnalysisSnapshot._meta.get_field('meaningful_commits')
        self.assertIsNotNone(field)
    def test_field_type_meaningful_commits(self):
        field = AnalysisSnapshot._meta.get_field('meaningful_commits')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_total_authors(self):
        field = AnalysisSnapshot._meta.get_field('total_authors')
        self.assertIsNotNone(field)
    def test_field_type_total_authors(self):
        field = AnalysisSnapshot._meta.get_field('total_authors')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_first_commit_date(self):
        field = AnalysisSnapshot._meta.get_field('first_commit_date')
        self.assertIsNotNone(field)
    def test_field_type_first_commit_date(self):
        field = AnalysisSnapshot._meta.get_field('first_commit_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_latest_commit_date(self):
        field = AnalysisSnapshot._meta.get_field('latest_commit_date')
        self.assertIsNotNone(field)
    def test_field_type_latest_commit_date(self):
        field = AnalysisSnapshot._meta.get_field('latest_commit_date')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')

class LanguageStatModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = LanguageStat._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = LanguageStat._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_snapshot(self):
        field = LanguageStat._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = LanguageStat._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_language_name(self):
        field = LanguageStat._meta.get_field('language_name')
        self.assertIsNotNone(field)
    def test_field_type_language_name(self):
        field = LanguageStat._meta.get_field('language_name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_file_count(self):
        field = LanguageStat._meta.get_field('file_count')
        self.assertIsNotNone(field)
    def test_field_type_file_count(self):
        field = LanguageStat._meta.get_field('file_count')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_loc(self):
        field = LanguageStat._meta.get_field('loc')
        self.assertIsNotNone(field)
    def test_field_type_loc(self):
        field = LanguageStat._meta.get_field('loc')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')

class ClassificationStatModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ClassificationStat._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ClassificationStat._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_snapshot(self):
        field = ClassificationStat._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = ClassificationStat._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_category(self):
        field = ClassificationStat._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = ClassificationStat._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_file_count(self):
        field = ClassificationStat._meta.get_field('file_count')
        self.assertIsNotNone(field)
    def test_field_type_file_count(self):
        field = ClassificationStat._meta.get_field('file_count')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')

class PullRequestStatModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = PullRequestStat._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = PullRequestStat._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_snapshot(self):
        field = PullRequestStat._meta.get_field('snapshot')
        self.assertIsNotNone(field)
    def test_field_type_snapshot(self):
        field = PullRequestStat._meta.get_field('snapshot')
        self.assertEqual(field.__class__.__name__, 'OneToOneField')
    def test_field_existence_is_available(self):
        field = PullRequestStat._meta.get_field('is_available')
        self.assertIsNotNone(field)
    def test_field_type_is_available(self):
        field = PullRequestStat._meta.get_field('is_available')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_total_prs(self):
        field = PullRequestStat._meta.get_field('total_prs')
        self.assertIsNotNone(field)
    def test_field_type_total_prs(self):
        field = PullRequestStat._meta.get_field('total_prs')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_open_prs(self):
        field = PullRequestStat._meta.get_field('open_prs')
        self.assertIsNotNone(field)
    def test_field_type_open_prs(self):
        field = PullRequestStat._meta.get_field('open_prs')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')
    def test_field_existence_merged_prs(self):
        field = PullRequestStat._meta.get_field('merged_prs')
        self.assertIsNotNone(field)
    def test_field_type_merged_prs(self):
        field = PullRequestStat._meta.get_field('merged_prs')
        self.assertEqual(field.__class__.__name__, 'PositiveIntegerField')



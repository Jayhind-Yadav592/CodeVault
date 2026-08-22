import os

files = {
    'repositories/apps.py': '''from django.apps import AppConfig

class RepositoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'repositories'
''',

    'repositories/models.py': '''from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

class RepositoryConnection(UUIDModel, TimeStampedModel):
    class Provider(models.TextChoices):
        GENERIC_GIT = 'generic', _('Generic Git')
        GITHUB = 'github', _('GitHub')
        GITLAB = 'gitlab', _('GitLab')
        BITBUCKET = 'bitbucket', _('Bitbucket')

    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending/Not Synced')
        SYNCING = 'syncing', _('Syncing')
        CONNECTED = 'connected', _('Connected')
        ERROR = 'error', _('Error')

    project = models.OneToOneField('projects.Project', on_delete=models.CASCADE, related_name='repository_connection')
    provider = models.CharField(max_length=20, choices=Provider.choices, default=Provider.GENERIC_GIT)
    repo_url = models.URLField(help_text=_("Clone URL of the repository"))
    repo_name = models.CharField(max_length=150, blank=True)
    default_branch = models.CharField(max_length=50, default='main')
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    last_sync_time = models.DateTimeField(null=True, blank=True)
    last_error = models.TextField(blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.repo_url}"

class AnalysisJob(UUIDModel, TimeStampedModel):
    class State(models.TextChoices):
        QUEUED = 'queued', _('Queued')
        RUNNING = 'running', _('Running')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        CANCELLED = 'cancelled', _('Cancelled')

    repository = models.ForeignKey(RepositoryConnection, on_delete=models.CASCADE, related_name='jobs')
    state = models.CharField(max_length=20, choices=State.choices, default=State.QUEUED)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_id = models.CharField(max_length=100, blank=True, help_text=_("Django-Q task ID"))
    error_log = models.TextField(blank=True)

    def __str__(self):
        return f"Job {self.id} - {self.state}"

class AnalysisSnapshot(UUIDModel, TimeStampedModel):
    repository = models.ForeignKey(RepositoryConnection, on_delete=models.CASCADE, related_name='snapshots')
    job = models.OneToOneField(AnalysisJob, on_delete=models.SET_NULL, null=True, blank=True)
    
    commit_hash = models.CharField(max_length=40)
    branch = models.CharField(max_length=50)
    
    total_files = models.PositiveIntegerField(default=0)
    total_loc = models.PositiveIntegerField(default=0)
    meaningful_loc = models.PositiveIntegerField(default=0)
    blank_lines = models.PositiveIntegerField(default=0)
    comment_lines = models.PositiveIntegerField(default=0)
    
    total_commits = models.PositiveIntegerField(default=0)
    meaningful_commits = models.PositiveIntegerField(default=0)
    total_authors = models.PositiveIntegerField(default=0)
    first_commit_date = models.DateTimeField(null=True, blank=True)
    latest_commit_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Snapshot {self.commit_hash[:8]} for {self.repository.project.name}"

class LanguageStat(UUIDModel):
    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.CASCADE, related_name='languages')
    language_name = models.CharField(max_length=50)
    file_count = models.PositiveIntegerField(default=0)
    loc = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('snapshot', 'language_name')

class ClassificationStat(UUIDModel):
    class Category(models.TextChoices):
        SOURCE = 'source', _('Source Code')
        TEST = 'test', _('Tests')
        DOC = 'doc', _('Documentation')
        CONFIG = 'config', _('Configuration')
        DEPENDENCY = 'dependency', _('Dependencies/Vendor')
        GENERATED = 'generated', _('Generated/Build')
        BINARY = 'binary', _('Binary/Asset')
        UNKNOWN = 'unknown', _('Unknown')

    snapshot = models.ForeignKey(AnalysisSnapshot, on_delete=models.CASCADE, related_name='classifications')
    category = models.CharField(max_length=20, choices=Category.choices)
    file_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        unique_together = ('snapshot', 'category')

class PullRequestStat(UUIDModel):
    snapshot = models.OneToOneField(AnalysisSnapshot, on_delete=models.CASCADE, related_name='pr_stats')
    is_available = models.BooleanField(default=False)
    total_prs = models.PositiveIntegerField(default=0)
    open_prs = models.PositiveIntegerField(default=0)
    merged_prs = models.PositiveIntegerField(default=0)
''',

    'repositories/serializers.py': '''from rest_framework import serializers
from .models import RepositoryConnection, AnalysisJob, AnalysisSnapshot, LanguageStat, ClassificationStat, PullRequestStat

class LanguageStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStat
        fields = ('language_name', 'file_count', 'loc')

class ClassificationStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationStat
        fields = ('category', 'file_count')

class PullRequestStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequestStat
        fields = ('is_available', 'total_prs', 'open_prs', 'merged_prs')

class AnalysisSnapshotSerializer(serializers.ModelSerializer):
    languages = LanguageStatSerializer(many=True, read_only=True)
    classifications = ClassificationStatSerializer(many=True, read_only=True)
    pr_stats = PullRequestStatSerializer(read_only=True)

    class Meta:
        model = AnalysisSnapshot
        fields = (
            'id', 'commit_hash', 'branch', 'total_files', 'total_loc',
            'meaningful_loc', 'blank_lines', 'comment_lines',
            'total_commits', 'meaningful_commits', 'total_authors',
            'first_commit_date', 'latest_commit_date', 'created_at',
            'languages', 'classifications', 'pr_stats'
        )

class AnalysisJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisJob
        fields = ('id', 'state', 'started_at', 'completed_at', 'error_log', 'created_at')

class RepositoryConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryConnection
        fields = ('id', 'project', 'provider', 'repo_url', 'repo_name', 'default_branch', 'status', 'last_sync_time', 'last_error')
        read_only_fields = ('id', 'status', 'last_sync_time', 'last_error')
''',

    'repositories/tests.py': '''import pytest
import os
import tempfile
from django.urls import reverse
from rest_framework import status
from projects.models import Project, Category
from repositories.models import RepositoryConnection, AnalysisJob, AnalysisSnapshot
from repositories.services.file_classifier import FileClassifier
from repositories.services.language_detector import LanguageDetector
from repositories.services.loc_analyzer import LOCAnalyzer
from django.contrib.auth import get_user_model

User = get_user_model()

class TestServices:
    def test_file_classifier(self):
        assert FileClassifier.classify('src/main.py') == 'source'
        assert FileClassifier.classify('tests/test_main.py') == 'test'
        assert FileClassifier.classify('README.md') == 'doc'
        assert FileClassifier.classify('node_modules/pkg/index.js') == 'dependency'
        assert FileClassifier.classify('build/app.exe') == 'dependency' # Because build is excluded dir, it's marked dependency
        assert FileClassifier.classify('app.exe') == 'binary'
        assert FileClassifier.classify('config.json') == 'config'

    def test_language_detector(self):
        assert LanguageDetector.detect('main.py') == 'Python'
        assert LanguageDetector.detect('app.js') == 'JavaScript'
        assert LanguageDetector.detect('Makefile') == 'Unknown'

    def test_loc_analyzer(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as f:
            f.write("def foo():\\n")
            f.write("    # This is a comment\\n")
            f.write("    pass\\n")
            f.write("\\n")
            f.write('    """\\n    docstring\\n    """\\n')
            temp_path = f.name
            
        try:
            stats = LOCAnalyzer.analyze_file(temp_path)
            assert stats['total_lines'] == 7
            assert stats['blank_lines'] == 1
            assert stats['comment_lines'] == 4 # # comment (1) + """ docstring """ (3)
            assert stats['code_lines'] == 2 # def and pass
        finally:
            os.remove(temp_path)

@pytest.mark.django_db
class TestRepositoryAPI:
    def test_create_connection(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        category = Category.objects.create(name='Test Cat')
        project = Project.objects.create(name='Test Proj', owner=developer_user, category=category)
        
        url = reverse('repositories:connection-list')
        data = {
            'project': project.id,
            'provider': 'generic',
            'repo_url': 'https://github.com/torvalds/linux.git' # fake for testing api creation
        }
        
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert RepositoryConnection.objects.count() == 1

    def test_sync_trigger(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        category = Category.objects.create(name='Test Cat')
        project = Project.objects.create(name='Test Proj', owner=developer_user, category=category)
        connection = RepositoryConnection.objects.create(
            project=project, repo_url='https://github.com/django/django.git'
        )
        
        url = reverse('repositories:connection-sync', args=[connection.id])
        response = api_client.post(url)
        assert response.status_code == status.HTTP_202_ACCEPTED
        assert AnalysisJob.objects.count() == 1
        assert AnalysisJob.objects.first().state == AnalysisJob.State.QUEUED
'''
}

for k, v in files.items():
    with open(k, 'w', encoding='utf-8') as f:
        f.write(v)

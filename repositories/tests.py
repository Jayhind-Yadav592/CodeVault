import pytest
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
            f.write("def foo():\n")
            f.write("    # This is a comment\n")
            f.write("    pass\n")
            f.write("\n")
            f.write('    """\n    docstring\n    """\n')
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

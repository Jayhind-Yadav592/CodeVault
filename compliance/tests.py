import pytest
import os
import tempfile
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from projects.models import Project, Category, OwnershipDeclaration
from repositories.models import RepositoryConnection, AnalysisSnapshot
from compliance.models import CompliancePolicy, ComplianceEvaluation, RuleResult, ComplianceRule
from compliance.tasks import trigger_compliance_evaluation
from compliance.rules import (
    RepositorySizeRule, GitCommitRule, ExecutabilityRule, 
    SecretDetectionRule, LicenseRule, AIGeneratedRule
)
from compliance.engine import RuleContext

User = get_user_model()

@pytest.fixture
def policy():
    return CompliancePolicy.objects.create(
        version='1.0', is_active=True,
        min_meaningful_loc=50,
        min_meaningful_commits=5,
        min_meaningful_prs=2
    )

@pytest.fixture
def project_setup(db):
    user = User.objects.create_user(email='test@example.com', password='pw')
    cat = Category.objects.create(name='Cat')
    proj = Project.objects.create(name='Proj', owner=user, category=cat)
    conn = RepositoryConnection.objects.create(project=proj, repo_url='http://fake.git')
    snap = AnalysisSnapshot.objects.create(
        repository=conn, commit_hash='abc', branch='main',
        meaningful_loc=100, meaningful_commits=10
    )
    return user, proj, snap

@pytest.mark.django_db
class TestSnapshotRules:
    def test_repository_size_rule_pass(self, project_setup, policy):
        _, _, snap = project_setup
        eval = ComplianceEvaluation.objects.create(snapshot=snap, policy=policy)
        ctx = RuleContext(eval)
        
        rule = RepositorySizeRule()
        res = rule.evaluate(ctx)
        
        assert res['status'] == RuleResult.Status.PASS
        assert res['evidence']['actual_loc'] == 100

    def test_repository_size_rule_fail(self, project_setup, policy):
        _, _, snap = project_setup
        snap.meaningful_loc = 10  # Below 50
        snap.save()
        
        eval = ComplianceEvaluation.objects.create(snapshot=snap, policy=policy)
        ctx = RuleContext(eval)
        
        rule = RepositorySizeRule()
        res = rule.evaluate(ctx)
        
        assert res['status'] == RuleResult.Status.FAIL
        assert res['is_critical_failure'] is True

@pytest.mark.django_db
class TestScannerRules:
    def test_executability_rule(self, project_setup, policy):
        _, _, snap = project_setup
        eval = ComplianceEvaluation.objects.create(snapshot=snap, policy=policy)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a fake manage.py
            with open(os.path.join(temp_dir, 'manage.py'), 'w') as f:
                f.write('import sys')
                
            ctx = RuleContext(eval, repo_path=temp_dir)
            rule = ExecutabilityRule()
            res = rule.evaluate(ctx)
            
            assert res['status'] == RuleResult.Status.PASS
            assert 'python_django' in res['evidence']['detected_environments']

    def test_secret_detection_rule(self, project_setup, policy):
        _, _, snap = project_setup
        eval = ComplianceEvaluation.objects.create(snapshot=snap, policy=policy)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a file with a fake AWS key
            with open(os.path.join(temp_dir, 'config.py'), 'w') as f:
                f.write('AWS_KEY = "AKIAIOSFODNN7EXAMPLE"')
                
            ctx = RuleContext(eval, repo_path=temp_dir)
            rule = SecretDetectionRule()
            res = rule.evaluate(ctx)
            
            assert res['status'] == RuleResult.Status.FAIL
            assert res['is_critical_failure'] is True
            assert res['evidence']['secrets_found'] == 1
            assert res['evidence']['findings'][0]['value'] == '[REDACTED]'

    def test_license_rule_fails_on_gpl(self, project_setup, policy):
        _, _, snap = project_setup
        eval = ComplianceEvaluation.objects.create(snapshot=snap, policy=policy)
        
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'LICENSE'), 'w') as f:
                f.write('GNU GENERAL PUBLIC LICENSE')
                
            ctx = RuleContext(eval, repo_path=temp_dir)
            rule = LicenseRule()
            res = rule.evaluate(ctx)
            
            assert res['status'] == RuleResult.Status.FAIL
            assert res['is_critical_failure'] is True
            assert 'GPL' in res['evidence']['detected_licenses']

@pytest.mark.django_db
class TestEngineAndTasks:
    def test_trigger_evaluation_creates_task(self, project_setup):
        _, _, snap = project_setup
        # The task runs async but in test environment django-q uses sync if configured,
        # but even if async, we just test the model is created.
        eval = trigger_compliance_evaluation(snap)
        assert eval.id is not None
        assert eval.decision == ComplianceEvaluation.Decision.INSUFFICIENT_DATA

@pytest.mark.django_db
class TestComplianceAPI:
    def test_trigger_api(self, api_client, project_setup):
        user, _, snap = project_setup
        api_client.force_authenticate(user=user)
        
        url = reverse('compliance:evaluation-trigger')
        response = api_client.post(url, {'snapshot_id': snap.id})
        
        assert response.status_code == status.HTTP_202_ACCEPTED
        assert 'evaluation_id' in response.data

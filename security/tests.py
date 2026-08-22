import pytest
import os
import tempfile
from django.contrib.auth import get_user_model
from projects.models import Project, Category
from repositories.models import RepositoryConnection, AnalysisSnapshot
from security.models import Finding, Dependency, SecurityScanJob
from security.scanners import (
    ScannerContext, SecretScanner, PIIScanner, LicenseScanner, DependencyScanner
)

User = get_user_model()

@pytest.fixture
def project_setup(db):
    user = User.objects.create_user(email='sec@example.com', password='pw')
    cat = Category.objects.create(name='Cat')
    proj = Project.objects.create(name='Proj', owner=user, category=cat)
    conn = RepositoryConnection.objects.create(project=proj, repo_url='http://fake.git')
    snap = AnalysisSnapshot.objects.create(
        repository=conn, commit_hash='abc', branch='main'
    )
    return user, proj, snap

@pytest.mark.django_db
class TestScanners:
    def test_secret_scanner_redacts_credentials(self, project_setup):
        _, proj, snap = project_setup
        
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a file with a secret
            with open(os.path.join(temp_dir, 'config.py'), 'w') as f:
                f.write('AWS_KEY = "AKIAIOSFODNN7EXAMPLE"')
                
            ctx = ScannerContext(proj, snap, temp_dir)
            scanner = SecretScanner()
            findings = scanner.scan(ctx)
            
            assert len(findings) == 1
            fnd = findings[0]
            assert fnd.category == Finding.Category.SECRET
            assert fnd.severity == Finding.Severity.CRITICAL
            assert 'AKIAIOSFODNN7EXAMPLE' not in fnd.redacted_evidence
            assert '[REDACTED]' in fnd.redacted_evidence

    def test_pii_scanner_ignores_test_data(self, project_setup):
        _, proj, snap = project_setup
        
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'data.txt'), 'w') as f:
                f.write('Email: test@example.com\n')
                f.write('Contact: user@realcompany.com\n')
                
            ctx = ScannerContext(proj, snap, temp_dir)
            scanner = PIIScanner()
            findings = scanner.scan(ctx)
            
            # Should ignore test@example.com but catch user@realcompany.com
            assert len(findings) == 1
            assert 'realcompany' not in findings[0].redacted_evidence

    def test_license_scanner_detects_gpl(self, project_setup):
        _, proj, snap = project_setup
        
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'LICENSE'), 'w') as f:
                f.write('GNU GENERAL PUBLIC LICENSE')
                
            ctx = ScannerContext(proj, snap, temp_dir)
            scanner = LicenseScanner()
            findings = scanner.scan(ctx)
            
            assert len(findings) == 1
            assert findings[0].severity == Finding.Severity.CRITICAL

    def test_dependency_scanner_extracts_manifests(self, project_setup):
        _, proj, snap = project_setup
        
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'package.json'), 'w') as f:
                f.write('{}')
                
            ctx = ScannerContext(proj, snap, temp_dir)
            scanner = DependencyScanner()
            scanner.scan(ctx)
            
            deps = Dependency.objects.filter(snapshot=snap)
            assert deps.count() == 1
            assert deps.first().ecosystem == Dependency.Ecosystem.NPM

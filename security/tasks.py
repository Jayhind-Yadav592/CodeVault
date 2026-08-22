from django_q.tasks import async_task
from .models import SecurityScanJob, Finding
from .scanners import (
    ScannerContext, SecretScanner, PIIScanner, SensitiveFileScanner,
    LicenseScanner, CopyrightScanner, DependencyScanner
)
from repositories.services.git_service import GitService
from compliance.tasks import trigger_compliance_evaluation

SCANNERS = [
    SecretScanner(),
    PIIScanner(),
    SensitiveFileScanner(),
    LicenseScanner(),
    CopyrightScanner(),
    DependencyScanner()
]

def run_security_scan_task(job_id):
    try:
        job = SecurityScanJob.objects.get(id=job_id)
        job.status = SecurityScanJob.Status.RUNNING
        job.save()

        snapshot = job.snapshot
        project = snapshot.repository.project
        
        # Clone repo
        git_service = GitService(snapshot.repository.repo_url, snapshot.repository.default_branch)
        git_service.clone()
        repo_path = git_service.get_repo_path()
        
        context = ScannerContext(project, snapshot, repo_path)
        
        # Run scanners
        all_findings = []
        for scanner in SCANNERS:
            try:
                findings = scanner.scan(context)
                all_findings.extend(findings)
            except Exception as e:
                print(f"Scanner {scanner.name} failed: {e}")
                
        # Bulk create findings
        Finding.objects.bulk_create(all_findings)
        
        git_service.cleanup()
        
        job.status = SecurityScanJob.Status.COMPLETED
        job.save()
        
        # Chain Phase 4 Compliance Engine
        trigger_compliance_evaluation(snapshot)
        
    except Exception as e:
        if 'job' in locals():
            job.status = SecurityScanJob.Status.FAILED
            job.error_message = str(e)
            job.save()

def trigger_security_scan(snapshot):
    job, _ = SecurityScanJob.objects.get_or_create(snapshot=snapshot)
    job.status = SecurityScanJob.Status.QUEUED
    job.error_message = ''
    job.save()
    
    # Delete old findings and dependencies for this snapshot before rescanning
    Finding.objects.filter(snapshot=snapshot).delete()
    snapshot.dependencies.all().delete()
    
    async_task('security.tasks.run_security_scan_task', job.id)
    return job

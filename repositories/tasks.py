from django_q.tasks import async_task
from .models import AnalysisJob
from .services.analyzer import RepositoryAnalyzer

def analyze_repository_task(job_id):
    try:
        job = AnalysisJob.objects.get(id=job_id)
        analyzer = RepositoryAnalyzer(job)
        analyzer.run()
    except Exception as e:
        print(f"Failed to run analysis for job {job_id}: {e}")

def trigger_analysis(connection):
    job = AnalysisJob.objects.create(repository=connection, state=AnalysisJob.State.QUEUED)
    task_id = async_task('repositories.tasks.analyze_repository_task', job.id)
    job.task_id = task_id
    job.save()
    return job

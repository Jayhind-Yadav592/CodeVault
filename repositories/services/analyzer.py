import os
from .git_service import GitService
from .language_detector import LanguageDetector
from .file_classifier import FileClassifier
from .loc_analyzer import LOCAnalyzer
from repositories.models import AnalysisSnapshot, LanguageStat, ClassificationStat, PullRequestStat

class RepositoryAnalyzer:
    def __init__(self, job):
        self.job = job
        self.connection = job.repository

    def run(self):
        self.job.state = self.job.State.RUNNING
        self.job.save()

        git_service = GitService(self.connection.repo_url, self.connection.default_branch)
        
        try:
            git_service.clone()
            
            repo_path = git_service.get_repo_path()
            commit_stats = git_service.get_commit_stats()
            
            total_files = 0
            total_loc = 0
            meaningful_loc = 0
            total_blank = 0
            total_comment = 0
            
            lang_counts = {}
            lang_locs = {}
            class_counts = {c[0]: 0 for c in ClassificationStat.Category.choices}
            
            for root, dirs, files in os.walk(repo_path):
                dirs[:] = [d for d in dirs if d not in FileClassifier.EXCLUDED_DIRS]
                
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, repo_path)
                    
                    if FileClassifier.is_excluded(rel_path):
                        continue
                        
                    total_files += 1
                    category = FileClassifier.classify(rel_path)
                    class_counts[category] = class_counts.get(category, 0) + 1
                    
                    if category not in ['binary', 'dependency']:
                        lang = LanguageDetector.detect(file)
                        lang_counts[lang] = lang_counts.get(lang, 0) + 1
                        
                        loc_stats = LOCAnalyzer.analyze_file(full_path)
                        total_loc += loc_stats['total_lines']
                        total_blank += loc_stats['blank_lines']
                        total_comment += loc_stats['comment_lines']
                        
                        if category == 'source':
                            meaningful_loc += loc_stats['code_lines']
                            lang_locs[lang] = lang_locs.get(lang, 0) + loc_stats['code_lines']

            snapshot = AnalysisSnapshot.objects.create(
                repository=self.connection, job=self.job,
                commit_hash=commit_stats.get('commit_hash', 'unknown'),
                branch=self.connection.default_branch,
                total_files=total_files, total_loc=total_loc,
                meaningful_loc=meaningful_loc, blank_lines=total_blank,
                comment_lines=total_comment, total_commits=commit_stats.get('total_commits', 0),
                meaningful_commits=commit_stats.get('meaningful_commits', 0),
                total_authors=commit_stats.get('total_authors', 0),
                first_commit_date=commit_stats.get('first_commit_date'),
                latest_commit_date=commit_stats.get('latest_commit_date')
            )
            
            for lang, count in lang_counts.items():
                LanguageStat.objects.create(snapshot=snapshot, language_name=lang, file_count=count, loc=lang_locs.get(lang, 0))
                
            for cat, count in class_counts.items():
                if count > 0:
                    ClassificationStat.objects.create(snapshot=snapshot, category=cat, file_count=count)
                    
            PullRequestStat.objects.create(snapshot=snapshot, is_available=False)
            
            self.connection.status = self.connection.Status.CONNECTED
            self.connection.last_sync_time = snapshot.created_at
            self.connection.save()
            
            self.job.state = self.job.State.COMPLETED
            self.job.save()

        except Exception as e:
            self.job.state = self.job.State.FAILED
            self.job.error_log = str(e)
            self.job.save()
            self.connection.status = self.connection.Status.ERROR
            self.connection.last_error = str(e)
            self.connection.save()
        finally:
            git_service.cleanup()

import os

files = {
    'repositories/services/git_service.py': '''import os
import shutil
import tempfile
from git import Repo, GitCommandError

class GitService:
    def __init__(self, repo_url, default_branch='main'):
        self.repo_url = repo_url
        self.default_branch = default_branch
        self.temp_dir = tempfile.mkdtemp(prefix='codevault_repo_')
        self.repo = None

    def clone(self):
        try:
            self.repo = Repo.clone_from(self.repo_url, self.temp_dir)
            return True
        except GitCommandError as e:
            raise Exception(f"Git clone failed: {str(e)}")

    def get_commit_stats(self):
        if not self.repo:
            return {}
        commits = list(self.repo.iter_commits('HEAD'))
        total_commits = len(commits)
        meaningful_commits = [c for c in commits if len(c.message.strip()) > 10 and not c.message.startswith('Merge') and not c.message.startswith('Auto')]
        authors = set(c.author.email for c in commits)
        
        return {
            'total_commits': total_commits,
            'meaningful_commits': len(meaningful_commits),
            'total_authors': len(authors),
            'first_commit_date': commits[-1].committed_datetime if commits else None,
            'latest_commit_date': commits[0].committed_datetime if commits else None,
            'commit_hash': commits[0].hexsha if commits else 'unknown'
        }

    def cleanup(self):
        if os.path.exists(self.temp_dir):
            try:
                def remove_readonly(func, path, _):
                    os.chmod(path, 0o777)
                    func(path)
                shutil.rmtree(self.temp_dir, onerror=remove_readonly)
            except Exception as e:
                pass

    def get_repo_path(self):
        return self.temp_dir
''',

    'repositories/services/language_detector.py': '''import os

class LanguageDetector:
    EXT_MAP = {
        '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript', '.java': 'Java',
        '.c': 'C', '.cpp': 'C++', '.h': 'C/C++ Header', '.hpp': 'C++ Header',
        '.cs': 'C#', '.go': 'Go', '.rs': 'Rust', '.kt': 'Kotlin', '.swift': 'Swift',
        '.php': 'PHP', '.rb': 'Ruby', '.scala': 'Scala', '.dart': 'Dart', '.r': 'R',
        '.html': 'HTML', '.htm': 'HTML', '.css': 'CSS', '.sh': 'Shell', '.bash': 'Shell',
        '.md': 'Markdown', '.json': 'JSON', '.yml': 'YAML', '.yaml': 'YAML',
        '.xml': 'XML', '.sql': 'SQL',
    }

    @classmethod
    def detect(cls, filename):
        ext = os.path.splitext(filename)[1].lower()
        return cls.EXT_MAP.get(ext, 'Unknown')
''',

    'repositories/services/file_classifier.py': '''import os

class FileClassifier:
    EXCLUDED_DIRS = {
        '.git', 'node_modules', 'vendor', 'dist', 'build', 'target', 
        'coverage', '.cache', '__pycache__', '.venv', 'venv', 'env'
    }

    @classmethod
    def is_excluded(cls, path):
        parts = path.split(os.sep)
        return any(d in cls.EXCLUDED_DIRS for d in parts)

    @classmethod
    def classify(cls, path):
        if cls.is_excluded(path):
            return 'dependency'
            
        lower_path = path.lower()
        
        binary_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.exe', '.dll', '.so', '.dylib', '.zip', '.tar', '.gz'}
        if any(lower_path.endswith(ext) for ext in binary_exts):
            return 'binary'

        if '/test' in lower_path or '\\\\test' in lower_path or 'test_' in lower_path or '_test' in lower_path:
            return 'test'
            
        if lower_path.endswith('.md') or lower_path.endswith('.txt') or '/doc' in lower_path or '\\\\doc' in lower_path:
            return 'doc'
            
        if lower_path.endswith('.json') or lower_path.endswith('.yml') or lower_path.endswith('.yaml') or lower_path.endswith('.xml') or lower_path.endswith('.ini') or lower_path.endswith('.cfg'):
            return 'config'
            
        if 'generated' in lower_path or lower_path.endswith('.min.js') or lower_path.endswith('.min.css'):
            return 'generated'

        return 'source'
''',

    'repositories/services/loc_analyzer.py': '''import os

class LOCAnalyzer:
    @classmethod
    def analyze_file(cls, filepath):
        total_lines = 0
        blank_lines = 0
        comment_lines = 0
        code_lines = 0

        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                in_multiline_comment = False
                for line in f:
                    total_lines += 1
                    stripped = line.strip()
                    if not stripped:
                        blank_lines += 1
                        continue
                    if in_multiline_comment:
                        comment_lines += 1
                        if '*/' in stripped or '"""' in stripped or "'''" in stripped:
                            in_multiline_comment = False
                        continue
                    if stripped.startswith('/*') or stripped.startswith('"""') or stripped.startswith("'''"):
                        comment_lines += 1
                        if not (stripped.endswith('*/') or stripped.endswith('"""') or stripped.endswith("'''")):
                            in_multiline_comment = True
                        continue
                    if stripped.startswith('//') or stripped.startswith('#') or stripped.startswith('--'):
                        comment_lines += 1
                        continue
                    code_lines += 1
        except Exception:
            pass

        return {
            'total_lines': total_lines,
            'blank_lines': blank_lines,
            'comment_lines': comment_lines,
            'code_lines': code_lines
        }
''',
    'repositories/services/analyzer.py': '''import os
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
'''
}

for k, v in files.items():
    with open(k, 'w', encoding='utf-8') as f:
        f.write(v)

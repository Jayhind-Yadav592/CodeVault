import os
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

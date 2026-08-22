import os

class FileClassifier:
    EXCLUDED_DIRS = {
        '.git', 'node_modules', 'vendor', 'dist', 'build', 'target', 
        'coverage', '.cache', '__pycache__', '.venv', 'venv', 'env'
    }

    @classmethod
    def is_excluded(cls, path):
        normalized = path.replace('\\', '/')
        parts = normalized.split('/')
        return any(d in cls.EXCLUDED_DIRS for d in parts)

    @classmethod
    def classify(cls, path):
        if cls.is_excluded(path):
            return 'dependency'
            
        lower_path = path.lower().replace('\\', '/')
        
        binary_exts = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.exe', '.dll', '.so', '.dylib', '.zip', '.tar', '.gz'}
        if any(lower_path.endswith(ext) for ext in binary_exts):
            return 'binary'

        if '/test' in lower_path or 'test_' in lower_path.split('/')[-1] or '_test' in lower_path.split('/')[-1]:
            return 'test'
            
        if lower_path.endswith('.md') or lower_path.endswith('.txt') or '/doc' in lower_path:
            return 'doc'
            
        if lower_path.endswith('.json') or lower_path.endswith('.yml') or lower_path.endswith('.yaml') or lower_path.endswith('.xml') or lower_path.endswith('.ini') or lower_path.endswith('.cfg'):
            return 'config'
            
        if 'generated' in lower_path or lower_path.endswith('.min.js') or lower_path.endswith('.min.css'):
            return 'generated'

        return 'source'

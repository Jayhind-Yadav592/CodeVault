import os

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

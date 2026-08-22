import os

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
                        # Fix for """ alone on a line: if it's the exact string, it starts but doesn't end a multiline if we consider it starting.
                        # Wait, if stripped is '"""', startswith is True, and endswith is True. So it won't set in_multiline_comment=True.
                        if len(stripped) <= 3 or not (stripped.endswith('*/') or stripped.endswith('"""') or stripped.endswith("'''")):
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

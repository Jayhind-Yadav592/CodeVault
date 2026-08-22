import os
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Measures the meaningful LOC of the project.'

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        
        excluded_dirs = ['.git', 'venv', 'node_modules', '__pycache__', 'migrations', 'scratch']
        excluded_exts = ['.pyc', '.sqlite3', '.log', '.env']
        
        counts = {
            'Python source LOC': 0,
            'Python test LOC': 0,
            'HTML LOC': 0,
            'CSS LOC': 0,
            'JavaScript LOC': 0,
            'Documentation LOC': 0,
            'Other qualifying code': 0
        }
        
        total_qualifying = 0
        
        for root, dirs, files in os.walk(base_dir):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in excluded_exts):
                    continue
                
                filepath = os.path.join(root, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = len([l for l in f.readlines() if l.strip()])
                        
                        total_qualifying += lines
                        
                        if file.endswith('.py'):
                            if 'tests' in filepath or file.startswith('test_'):
                                counts['Python test LOC'] += lines
                            else:
                                counts['Python source LOC'] += lines
                        elif file.endswith('.html'):
                            counts['HTML LOC'] += lines
                        elif file.endswith('.css'):
                            counts['CSS LOC'] += lines
                        elif file.endswith('.js'):
                            counts['JavaScript LOC'] += lines
                        elif file.endswith('.md'):
                            counts['Documentation LOC'] += lines
                        else:
                            counts['Other qualifying code'] += lines
                except Exception:
                    pass

        self.stdout.write(self.style.SUCCESS('--- LOC Report ---'))
        for k, v in counts.items():
            self.stdout.write(f'{k}: {v}')
            
        self.stdout.write(self.style.SUCCESS(f'\nTOTAL QUALIFYING LOC: {total_qualifying}'))

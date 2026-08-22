from django.core.management.base import BaseCommand
import os
import re

class Command(BaseCommand):
    help = 'Performs a basic source audit for secrets and proprietary headers.'

    def handle(self, *args, **options):
        self.stdout.write("--- Source Audit Report ---")
        
        secrets_found = 0
        patterns = [
            r'AKIA[0-9A-Z]{16}',
            r'sk_live_[0-9a-zA-Z]{24}',
            r'ghp_[0-9a-zA-Z]{36}'
        ]
        
        for root, dirs, files in os.walk('.'):
            if 'venv' in root or '.git' in root or 'node_modules' in root:
                continue
                
            for file in files:
                if file.endswith('.py') or file.endswith('.html'):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            for p in patterns:
                                for match in re.finditer(p, content):
                                    secret_val = match.group(0)
                                    if 'AKIAMOCKSECRET123456' not in secret_val:
                                        self.stdout.write(self.style.ERROR(f"Potential secret in {path}: {secret_val}"))
                                        secrets_found += 1
                    except:
                        pass
                        
        if secrets_found == 0:
            self.stdout.write(self.style.SUCCESS("No secrets detected."))
        
        self.stdout.write("Manual review required for proprietary headers and copied source.")

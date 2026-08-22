import os, re

def fix_file(path, old, new):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)

# Fix projectService
fix_file('frontend/src/services/projectService.ts', '/projects/', '/projects/projects/')

# Fix authService
fix_file('frontend/src/services/authService.ts', '/auth/login/', '/accounts/login/')
fix_file('frontend/src/services/authService.ts', '/auth/logout/', '/accounts/logout/')
fix_file('frontend/src/services/authService.ts', '/auth/user/', '/accounts/profile/')

# Fix others generically
SERVICES_MODELS = {
    'analytics': 'platformmetricssnapshot',
    'finance': 'transaction',
    'governance': 'policycontrol',
    'incident': 'incident',
    'licensing': 'licenseagreement',
    'marketplace': 'marketplacelisting',
    'review': 'reviewcase',
    'security': 'securityscan',
    'workflow': 'workflowdefinition'
}

for srv, model in SERVICES_MODELS.items():
    path = f'frontend/src/services/{srv}Service.ts'
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = re.sub(f"api.get\\('/{srv}/'\\)", f"api.get('/{srv}/{model}s/')", c)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)

print("Service URLs fixed!")

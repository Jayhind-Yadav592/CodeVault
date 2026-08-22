import os

def replace_import(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = content.replace("import React from 'react';", "")
    content = content.replace("import { Project, DashboardData } from '../types/project';", "import type { Project, DashboardData } from '../types/project';")
    content = content.replace("import { Project } from '../types/project';", "import type { Project } from '../types/project';")
    content = content.replace("import { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';", "import type { RepositoryConnection, AnalysisSnapshot, TrainPlexReadiness } from '../types/repository';")
    content = content.replace("import { RepositoryConnection } from '../types/repository';", "import type { RepositoryConnection } from '../types/repository';")

    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('frontend/src'):
    for f in files:
        if f.endswith('.ts') or f.endswith('.tsx'):
            replace_import(os.path.join(root, f))

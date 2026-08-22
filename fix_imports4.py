import os
import re

def replace_import(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove unused React imports
    content = content.replace("import React from 'react';\n", "")
    
    # Use regex to find `import { ... } from '../types/...';` and replace with `import type { ... }`
    content = re.sub(r'import\s+\{([^}]+)\}\s+from\s+[\'"](\.\./types/[^\'"]+)[\'"];?', r'import type { \1 } from "\2";', content)

    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('frontend/src'):
    for f in files:
        if f.endswith('.ts') or f.endswith('.tsx'):
            replace_import(os.path.join(root, f))

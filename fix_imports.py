import os
import re

def replace_import(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    # Replace unused React
    content = re.sub(r'import React from \'react\';\n', '', content)
    content = re.sub(r'import React, { ([^}]+) } from \'react\';', r'import { \1 } from \'react\';', content)
    # Fix import type
    content = re.sub(r'import \{ ([^}]+) \} from \'../types', r'import type { \1 } from \'../types', content)
    content = re.sub(r'import \{ ([^}]+) \} from \'../../types', r'import type { \1 } from \'../../types', content)
    with open(filepath, 'w') as f:
        f.write(content)

for root, _, files in os.walk('frontend/src'):
    for f in files:
        if f.endswith('.ts') or f.endswith('.tsx'):
            replace_import(os.path.join(root, f))

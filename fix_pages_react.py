import os

for root, _, files in os.walk('frontend/src/pages'):
    for f in files:
        if f.endswith('.tsx') or f.endswith('.ts'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                c = file.read()
            c = c.replace("import React from 'react';\n", "")
            c = c.replace("import React, {", "import {")
            with open(path, 'w', encoding='utf-8') as wf:
                wf.write(c)

import os
def fix(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    content = content.replace("import React from 'react';\n", "")
    with open(fpath, 'w') as f:
        f.write(content)
fix('frontend/src/pages/Dashboard.test.tsx')
fix('frontend/src/pages/ProjectList.test.tsx')
fix('frontend/src/pages/RepositoryList.test.tsx')

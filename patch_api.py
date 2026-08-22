import os

path = 'frontend/src/services/api.ts'
if os.path.exists(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'xsrfCookieName' not in c:
        c = c.replace('withCredentials: true,', "withCredentials: true,\n  xsrfCookieName: 'csrftoken',\n  xsrfHeaderName: 'X-CSRFToken',")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
print("api.ts patched for CSRF")

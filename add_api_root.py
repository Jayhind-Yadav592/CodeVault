import os
path = 'codevault/urls.py'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()
if 'api_root' not in c:
    import_stmt = 'from rest_framework.decorators import api_view\nfrom rest_framework.response import Response\n\n@api_view(["GET"])\ndef api_root(request, format=None):\n    return Response({"message": "Welcome to CodeVault API v1"})\n'
    c = import_stmt + c
    c = c.replace("path('api/v1/accounts/", "path('api/v1/', api_root, name='api_root'),\n    path('api/v1/accounts/")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
print("api root added")

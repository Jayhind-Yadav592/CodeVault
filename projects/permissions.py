from rest_framework import permissions

class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # We need to handle both Project and nested objects (documents, declarations)
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        if hasattr(obj, 'project'):
            return obj.project.owner == request.user
        return False

class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        project = obj if hasattr(obj, 'owner') else obj.project
        if project.owner == request.user:
            return True
        return project.contributors.filter(user=request.user, is_active=True).exists()

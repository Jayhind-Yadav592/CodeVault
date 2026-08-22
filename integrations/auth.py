from rest_framework import authentication, exceptions, permissions
from django.utils import timezone
from .models import APICredential

class APICredentialAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Bearer '):
            return None
            
        raw_token = auth_header.split(' ')[1]
        fingerprint = raw_token[:8]
        
        credentials = APICredential.objects.filter(fingerprint=fingerprint, is_active=True)
        for cred in credentials:
            if cred.check_secret(raw_token):
                if cred.expires_at and cred.expires_at < timezone.now():
                    raise exceptions.AuthenticationFailed("API Credential expired")
                
                # Update last used
                cred.last_used_at = timezone.now()
                cred.save(update_fields=['last_used_at'])
                
                # Attach cred to request for scope checking
                request.auth_credential = cred
                return (cred.owner, cred)
                
        raise exceptions.AuthenticationFailed("Invalid API Credential")

class HasAPIScope(permissions.BasePermission):
    """
    Checks if the API Credential has the required scope.
    Required scopes should be defined on the ViewSet as `required_scopes = ['scope_name']`
    """
    def has_permission(self, request, view):
        if not hasattr(request, 'auth_credential'):
            # If using session auth (like UI), they must be authenticated
            return request.user and request.user.is_authenticated
            
        required_scopes = getattr(view, 'required_scopes', [])
        if not required_scopes:
            return True
            
        cred_scopes = request.auth_credential.scopes
        
        # Check if credential has at least one of the required scopes
        # (Or all, depending on business logic - here we check if any required is present)
        for req_scope in required_scopes:
            if req_scope in cred_scopes:
                return True
                
        raise exceptions.PermissionDenied(
            {"error": {"code": "INSUFFICIENT_SCOPE", "message": "The API credential does not have the required permission."}}
        )

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import ScopedRateThrottle
from .models import APICredential, WebhookEndpoint, Event
from .serializers import APICredentialSerializer, WebhookEndpointSerializer, EventSerializer

class StandardThrottle(ScopedRateThrottle):
    scope = 'standard'

class APICredentialViewSet(viewsets.ModelViewSet):
    serializer_class = APICredentialSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return APICredential.objects.filter(owner=self.request.user)
        
    def create(self, request, *args, **kwargs):
        # We need to generate the secret and return it ONCE
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        raw_secret = APICredential.generate_token()
        cred = APICredential(
            name=serializer.validated_data['name'],
            owner=request.user,
            scopes=serializer.validated_data.get('scopes', [])
        )
        cred.set_secret(raw_secret)
        cred.save()
        
        # Inject the raw secret to return it this one time
        cred.raw_secret = raw_secret
        
        response_serializer = self.get_serializer(cred)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

class WebhookEndpointViewSet(viewsets.ModelViewSet):
    serializer_class = WebhookEndpointSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return WebhookEndpoint.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            secret=WebhookEndpoint.generate_secret()
        )

# Example of a protected endpoint
from .auth import APICredentialAuthentication, HasAPIScope

class ProtectedResourceViewSet(viewsets.ViewSet):
    authentication_classes = [APICredentialAuthentication]
    permission_classes = [HasAPIScope]
    required_scopes = ['projects:read']
    throttle_classes = [StandardThrottle]
    
    def list(self, request):
        return Response({"message": "You accessed a protected resource successfully!"})

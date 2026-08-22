from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from .models import (
    Organization, LicenseType, LicenseProduct, LicenseRequest,
    Agreement, SignatureRequest, NegotiationProposal, LicenseTerms
)
from .serializers import (
    OrganizationSerializer, LicenseTypeSerializer, LicenseProductSerializer,
    LicenseRequestSerializer, AgreementSerializer, SignatureRequestSerializer,
    NegotiationProposalSerializer
)
from .services import LicenseService

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Organization.objects.all()
        return Organization.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LicenseProductViewSet(viewsets.ModelViewSet):
    serializer_class = LicenseProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Admins and buyers can see available products.
        # Project owners see their own products.
        qs = LicenseProduct.objects.all()
        if not self.request.user.is_staff:
            qs = qs.filter(status=LicenseProduct.Status.AVAILABLE) | qs.filter(project__owner=self.request.user)
        return qs.distinct()

class LicenseRequestViewSet(viewsets.ModelViewSet):
    serializer_class = LicenseRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return LicenseRequest.objects.all()
        # Licensees see their requests, Owners see incoming requests
        return LicenseRequest.objects.filter(
            organization__owner=self.request.user
        ) | LicenseRequest.objects.filter(
            product__project__owner=self.request.user
        )

    @action(detail=True, methods=['post'])
    def transition(self, request, pk=None):
        req = self.get_object()
        target_state = request.data.get('target_state')
        try:
            updated = LicenseService.transition_request(req, target_state)
            return Response(self.get_serializer(updated).data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=True, methods=['post'])
    def propose_terms(self, request, pk=None):
        req = self.get_object()
        terms_data = request.data.get('terms', {})
        message = request.data.get('message', '')
        is_counter = request.data.get('is_counter', False)
        try:
            prop = LicenseService.propose_terms(req, request.user, terms_data, message, is_counter)
            return Response(NegotiationProposalSerializer(prop).data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=True, methods=['post'])
    def accept_terms(self, request, pk=None):
        req = self.get_object()
        terms_id = request.data.get('terms_id')
        try:
            terms = LicenseTerms.objects.get(id=terms_id, request=req)
            agreement = LicenseService.accept_terms(req, terms)
            return Response(AgreementSerializer(agreement).data)
        except (LicenseTerms.DoesNotExist, ValidationError) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AgreementViewSet(viewsets.ModelViewSet):
    serializer_class = AgreementSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Agreement.objects.all()
        return Agreement.objects.filter(
            request__organization__owner=self.request.user
        ) | Agreement.objects.filter(
            request__product__project__owner=self.request.user
        )

    @action(detail=True, methods=['post'])
    def sign(self, request, pk=None):
        agreement = self.get_object()
        try:
            updated = LicenseService.sign_agreement(agreement, request.user)
            return Response(self.get_serializer(updated).data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

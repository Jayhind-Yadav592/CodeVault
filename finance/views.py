from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core.exceptions import ValidationError
from decimal import Decimal

from .models import (
    Wallet, Transaction, PayoutMethod, PayoutRequest, ReconciliationReport
)
from .serializers import (
    WalletSerializer, TransactionSerializer, PayoutMethodSerializer, 
    PayoutRequestSerializer, ReconciliationReportSerializer
)
from .services import PayoutService, ReconciliationService

class WalletViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Wallet.objects.all()
        return Wallet.objects.filter(owner=self.request.user)

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.all()
        from django.db.models import Q
        return Transaction.objects.filter(
            Q(project__owner=self.request.user) |
            Q(agreement__request__organization__owner=self.request.user) |
            Q(payoutrequest__owner=self.request.user)
        ).distinct()

class PayoutMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PayoutMethodSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PayoutMethod.objects.filter(owner=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PayoutRequestViewSet(viewsets.ModelViewSet):
    serializer_class = PayoutRequestSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return PayoutRequest.objects.all()
        return PayoutRequest.objects.filter(owner=self.request.user)
        
    def create(self, request, *args, **kwargs):
        method_id = request.data.get('method')
        amount = request.data.get('amount')
        currency = request.data.get('currency', 'USD')
        idempotency_key = request.data.get('idempotency_key')
        
        if not idempotency_key:
            return Response({'error': 'Idempotency key required'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            method = PayoutMethod.objects.get(id=method_id, owner=request.user)
            req = PayoutService.request_payout(request.user, method, Decimal(str(amount)), currency, idempotency_key)
            return Response(self.get_serializer(req).data, status=status.HTTP_201_CREATED)
        except (PayoutMethod.DoesNotExist, ValidationError) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        req = self.get_object()
        try:
            processed = PayoutService.process_payout(req, request.user)
            return Response(self.get_serializer(processed).data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ReconciliationViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ReconciliationReportSerializer
    
    @action(detail=False, methods=['post'])
    def run(self, request):
        report = ReconciliationService.run_reconciliation()
        return Response(self.get_serializer(report).data)

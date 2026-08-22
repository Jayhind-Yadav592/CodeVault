from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WalletViewSet, TransactionViewSet, PayoutMethodViewSet, 
    PayoutRequestViewSet, ReconciliationViewSet
)

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'payout-methods', PayoutMethodViewSet, basename='payoutmethod')
router.register(r'payout-requests', PayoutRequestViewSet, basename='payoutrequest')
router.register(r'reconciliation', ReconciliationViewSet, basename='reconciliation')

app_name = 'finance'

urlpatterns = [
    path('', include(router.urls)),
]

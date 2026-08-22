from rest_framework import serializers
from .models import (
    LedgerAccount, Transaction, LedgerEntry, Wallet,
    FeeRule, PayoutMethod, PayoutRequest, Refund, TaxRecord, ReconciliationReport
)

class LedgerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = '__all__'

class LedgerEntrySerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name', read_only=True)
    
    class Meta:
        model = LedgerEntry
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    entries = LedgerEntrySerializer(many=True, read_only=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class FeeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeRule
        fields = '__all__'

class PayoutMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutMethod
        fields = '__all__'
        read_only_fields = ('owner',)

class PayoutRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayoutRequest
        fields = '__all__'
        read_only_fields = ('owner', 'wallet', 'status', 'reviewer', 'admin_notes', 'transaction')

class ReconciliationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReconciliationReport
        fields = '__all__'

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project
from licensing.models import Agreement, Organization
from decimal import Decimal

class LedgerAccount(UUIDModel, TimeStampedModel):
    class Type(models.TextChoices):
        ASSET = 'asset', _('Asset')
        LIABILITY = 'liability', _('Liability')
        REVENUE = 'revenue', _('Revenue')
        EXPENSE = 'expense', _('Expense')
        EQUITY = 'equity', _('Equity')
        
    name = models.CharField(max_length=150, unique=True)
    account_type = models.CharField(max_length=20, choices=Type.choices)
    currency = models.CharField(max_length=10, default='USD')
    is_system = models.BooleanField(default=False)
    
    # Optionally tie to a specific user/project
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"

class Transaction(UUIDModel, TimeStampedModel):
    class Type(models.TextChoices):
        PAYMENT = 'payment', _('License Payment')
        PAYOUT = 'payout', _('Payout')
        REFUND = 'refund', _('Refund')
        ADJUSTMENT = 'adjustment', _('Adjustment')
        FEE = 'fee', _('Platform Fee')

    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        REVERSED = 'reversed', _('Reversed')

    transaction_type = models.CharField(max_length=20, choices=Type.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    currency = models.CharField(max_length=10, default='USD')
    
    idempotency_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    
    # Traceability
    agreement = models.ForeignKey(Agreement, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.transaction_type} {self.id} - {self.status}"

class LedgerEntry(UUIDModel, TimeStampedModel):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='entries')
    account = models.ForeignKey(LedgerAccount, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=15, decimal_places=4) # positive for debit, negative for credit conventionally, or split fields. We'll use positive/negative.
    
    # We will use standard accounting: Debit is positive for Asset/Expense, Credit is negative.
    # Actually, simpler: amount > 0 means debit, amount < 0 means credit.
    
    def __str__(self):
        return f"Entry {self.id} - {self.account.name}: {self.amount}"

class Wallet(UUIDModel, TimeStampedModel):
    """
    A materialized view-like entity for quick balances.
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallets')
    currency = models.CharField(max_length=10, default='USD')
    available_balance = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    pending_balance = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    total_earned = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    total_withdrawn = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    
    class Meta:
        unique_together = ('owner', 'currency')

    def __str__(self):
        return f"Wallet {self.owner.email} ({self.currency})"

class FeeRule(UUIDModel, TimeStampedModel):
    class Type(models.TextChoices):
        PERCENTAGE = 'percentage', _('Percentage')
        FIXED = 'fixed', _('Fixed')
        TIERED = 'tiered', _('Tiered')

    name = models.CharField(max_length=100)
    fee_type = models.CharField(max_length=20, choices=Type.choices, default=Type.PERCENTAGE)
    value = models.DecimalField(max_digits=10, decimal_places=4) # E.g., 10.00 for 10% or 10.00 for $10
    currency = models.CharField(max_length=10, default='USD', blank=True)
    
    is_active = models.BooleanField(default=True)
    version = models.IntegerField(default=1)

class PayoutMethod(UUIDModel, TimeStampedModel):
    class Type(models.TextChoices):
        BANK_TRANSFER = 'bank_transfer', _('Bank Transfer')
        PAYMENT_PROVIDER = 'payment_provider', _('Payment Provider')
        OTHER = 'other', _('Other')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payout_methods')
    method_type = models.CharField(max_length=20, choices=Type.choices)
    is_active = models.BooleanField(default=True)
    
    # Store opaque references, never plaintext credentials
    provider_reference = models.CharField(max_length=255)
    last_four = models.CharField(max_length=4, blank=True)

class PayoutRequest(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PROCESSING = 'processing', _('Processing')
        PAID = 'paid', _('Paid')
        ON_HOLD = 'on_hold', _('On Hold')
        REJECTED = 'rejected', _('Rejected')
        FAILED = 'failed', _('Failed')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payout_requests')
    wallet = models.ForeignKey(Wallet, on_delete=models.RESTRICT)
    method = models.ForeignKey(PayoutMethod, on_delete=models.RESTRICT)
    
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    currency = models.CharField(max_length=10)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_payouts')
    admin_notes = models.TextField(blank=True)
    
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True, blank=True)
    idempotency_key = models.CharField(max_length=255, unique=True, null=True)

class Refund(UUIDModel, TimeStampedModel):
    original_transaction = models.ForeignKey(Transaction, on_delete=models.RESTRICT, related_name='refunds')
    refund_transaction = models.ForeignKey(Transaction, on_delete=models.RESTRICT, related_name='refund_source', null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    reason = models.TextField()
    authorized_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class TaxRecord(UUIDModel, TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tax_year = models.IntegerField()
    country = models.CharField(max_length=100)
    
    gross_earnings = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    platform_fees = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    net_earnings = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    tax_withholding = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    net_payout = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    currency = models.CharField(max_length=10)

class ReconciliationReport(UUIDModel, TimeStampedModel):
    status = models.CharField(max_length=20, default='PENDING')
    accounts_checked = models.IntegerField(default=0)
    unbalanced_transactions = models.IntegerField(default=0)
    duplicate_transactions = models.IntegerField(default=0)
    balance_mismatches = models.IntegerField(default=0)
    
    details = models.JSONField(default=dict)

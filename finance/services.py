from decimal import Decimal
from django.db import transaction as db_transaction
from django.core.exceptions import ValidationError
from django.db.models import Sum
from .models import (
    LedgerAccount, Transaction, LedgerEntry, Wallet,
    FeeRule, PayoutRequest, ReconciliationReport, Organization
)

class DoubleEntryService:
    @staticmethod
    @db_transaction.atomic
    def record_transaction(transaction_type: str, entries_data: list, currency: str, idempotency_key: str = None, **kwargs):
        if idempotency_key and Transaction.objects.filter(idempotency_key=idempotency_key).exists():
            return Transaction.objects.get(idempotency_key=idempotency_key)
            
        total = sum(Decimal(str(e['amount'])) for e in entries_data)
        if total != Decimal('0.0000'):
            raise ValidationError(f"Transaction entries do not balance. Sum: {total}")
            
        txn = Transaction.objects.create(
            transaction_type=transaction_type,
            currency=currency,
            idempotency_key=idempotency_key,
            status=Transaction.Status.COMPLETED,
            **kwargs
        )
        
        for e_data in entries_data:
            LedgerEntry.objects.create(
                transaction=txn,
                account=e_data['account'],
                amount=Decimal(str(e_data['amount']))
            )
            
        return txn

class RevenueService:
    @staticmethod
    def calculate_fee(gross_amount: Decimal, fee_rule: FeeRule):
        if fee_rule.fee_type == FeeRule.Type.PERCENTAGE:
            fee = gross_amount * (fee_rule.value / Decimal('100.0'))
        elif fee_rule.fee_type == FeeRule.Type.FIXED:
            fee = fee_rule.value
        else:
            fee = Decimal('0.0')
        return round(fee, 4)

    @staticmethod
    @db_transaction.atomic
    def process_license_payment(gross_amount: Decimal, currency: str, creator, agreement, idempotency_key: str):
        if idempotency_key and Transaction.objects.filter(idempotency_key=idempotency_key).exists():
            return Transaction.objects.get(idempotency_key=idempotency_key)
            
        rule = FeeRule.objects.filter(is_active=True).first()
        if not rule:
            raise ValidationError("No active fee rule configured.")
            
        fee_amount = RevenueService.calculate_fee(gross_amount, rule)
        net_amount = gross_amount - fee_amount
        
        # System accounts
        platform_revenue, _ = LedgerAccount.objects.get_or_create(name="Platform Revenue", account_type=LedgerAccount.Type.REVENUE, is_system=True)
        creator_liability, _ = LedgerAccount.objects.get_or_create(name=f"Creator Liability - {creator.id}", account_type=LedgerAccount.Type.LIABILITY, owner=creator)
        clearing_account, _ = LedgerAccount.objects.get_or_create(name="Payment Clearing", account_type=LedgerAccount.Type.ASSET, is_system=True)
        
        entries = [
            {'account': clearing_account, 'amount': gross_amount}, # Debit asset
            {'account': platform_revenue, 'amount': -fee_amount},  # Credit revenue
            {'account': creator_liability, 'amount': -net_amount}, # Credit liability
        ]
        
        txn = DoubleEntryService.record_transaction(
            transaction_type=Transaction.Type.PAYMENT,
            entries_data=entries,
            currency=currency,
            idempotency_key=idempotency_key,
            agreement=agreement,
            project=agreement.request.product.project
        )
        
        wallet, _ = Wallet.objects.get_or_create(owner=creator, currency=currency)
        wallet.available_balance += net_amount
        wallet.total_earned += net_amount
        wallet.save()
        
        return txn

class PayoutService:
    @staticmethod
    def request_payout(creator, method, amount: Decimal, currency: str, idempotency_key: str):
        org = Organization.objects.filter(owner=creator).first()
        if not org or org.verification_status != Organization.VerificationStatus.VERIFIED:
            raise ValidationError("KYC verification is required before requesting a payout.")
            
        wallet = Wallet.objects.get(owner=creator, currency=currency)
        if wallet.available_balance < amount:
            raise ValidationError("Insufficient balance.")
            
        with db_transaction.atomic():
            req, created = PayoutRequest.objects.get_or_create(
                idempotency_key=idempotency_key,
                defaults={
                    'owner': creator,
                    'wallet': wallet,
                    'method': method,
                    'amount': amount,
                    'currency': currency,
                    'status': PayoutRequest.Status.PENDING
                }
            )
            
            if created:
                wallet.available_balance -= amount
                wallet.pending_balance += amount
                wallet.save()
                
        return req

    @staticmethod
    @db_transaction.atomic
    def process_payout(payout_req: PayoutRequest, admin_user):
        if payout_req.status != PayoutRequest.Status.PENDING:
            raise ValidationError("Payout is not pending.")
            
        # Mock payment provider success
        payout_req.status = PayoutRequest.Status.PAID
        payout_req.reviewer = admin_user
        
        creator_liability, _ = LedgerAccount.objects.get_or_create(name=f"Creator Liability - {payout_req.owner.id}", account_type=LedgerAccount.Type.LIABILITY, owner=payout_req.owner)
        bank_asset, _ = LedgerAccount.objects.get_or_create(name="Corporate Bank Account", account_type=LedgerAccount.Type.ASSET, is_system=True)
        
        entries = [
            {'account': creator_liability, 'amount': payout_req.amount}, # Debit liability (reducing it)
            {'account': bank_asset, 'amount': -payout_req.amount},       # Credit asset (reducing bank balance)
        ]
        
        txn = DoubleEntryService.record_transaction(
            transaction_type=Transaction.Type.PAYOUT,
            entries_data=entries,
            currency=payout_req.currency,
            idempotency_key=f"payout_txn_{payout_req.idempotency_key}"
        )
        
        payout_req.transaction = txn
        payout_req.save()
        
        wallet = payout_req.wallet
        wallet.pending_balance -= payout_req.amount
        wallet.total_withdrawn += payout_req.amount
        wallet.save()
        
        return payout_req

class ReconciliationService:
    @staticmethod
    def run_reconciliation():
        report = ReconciliationReport.objects.create(status='RUNNING')
        
        unbalanced = 0
        for txn in Transaction.objects.all():
            total = txn.entries.aggregate(s=Sum('amount'))['s'] or Decimal('0.0')
            if total != Decimal('0.0'):
                unbalanced += 1
                
        # More checks could be added (Wallet vs Ledger Liability)
        
        report.unbalanced_transactions = unbalanced
        report.status = 'PASS' if unbalanced == 0 else 'FAIL'
        report.save()
        return report

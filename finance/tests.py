import pytest
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from projects.models import Project, Category
from licensing.models import Agreement, LicenseRequest, LicenseProduct, Organization, LicenseType, LicenseTerms
from reviews.models import ReviewCase
from finance.models import (
    LedgerAccount, Transaction, LedgerEntry, Wallet,
    FeeRule, PayoutMethod, PayoutRequest, ReconciliationReport
)
from finance.services import DoubleEntryService, RevenueService, PayoutService, ReconciliationService

User = get_user_model()

@pytest.fixture
def finance_setup(db):
    owner = User.objects.create_user(email='owner@example.com', password='pw')
    licensee_user = User.objects.create_user(email='licensee@example.com', password='pw')
    
    cat = Category.objects.create(name='Cat')
    proj = Project.objects.create(name='Proj', owner=owner, category=cat)
    
    # Mock an approved review case
    from repositories.models import RepositoryConnection, AnalysisSnapshot
    conn = RepositoryConnection.objects.create(project=proj, repo_url='http://fake.git')
    snap = AnalysisSnapshot.objects.create(repository=conn, commit_hash='abc', branch='main')
    case = ReviewCase.objects.create(project=proj, snapshot=snap, state=ReviewCase.State.APPROVED)
    
    org = Organization.objects.create(name='Test Org', owner=licensee_user, verification_status=Organization.VerificationStatus.VERIFIED)
    ltype = LicenseType.objects.create(name='Commercial', code='COMM')
    product = LicenseProduct.objects.create(project=proj, approved_review_case=case, status=LicenseProduct.Status.AVAILABLE)
    req = LicenseRequest.objects.create(product=product, organization=org, requested_type=ltype, status=LicenseRequest.Status.SIGNED)
    terms = LicenseTerms.objects.create(request=req)
    agreement = Agreement.objects.create(request=req, terms=terms, status=Agreement.Status.ACTIVE)
    
    FeeRule.objects.create(name="Standard 10%", fee_type=FeeRule.Type.PERCENTAGE, value=Decimal('10.0'))
    
    return owner, licensee_user, agreement

@pytest.mark.django_db
class TestFinanceSubsystem:
    def test_unbalanced_ledger_rejected(self, finance_setup):
        acct1 = LedgerAccount.objects.create(name="Acct 1", account_type=LedgerAccount.Type.ASSET)
        acct2 = LedgerAccount.objects.create(name="Acct 2", account_type=LedgerAccount.Type.REVENUE)
        
        entries = [
            {'account': acct1, 'amount': Decimal('100.00')},
            {'account': acct2, 'amount': Decimal('-90.00')},
        ]
        
        with pytest.raises(ValidationError, match="do not balance"):
            DoubleEntryService.record_transaction('adjustment', entries, 'USD')

    def test_revenue_split_decimals(self, finance_setup):
        owner, licensee_user, agreement = finance_setup
        
        # Payment $150.00
        txn = RevenueService.process_license_payment(
            gross_amount=Decimal('150.00'),
            currency='USD',
            creator=owner,
            agreement=agreement,
            idempotency_key='payment_123'
        )
        
        wallet = Wallet.objects.get(owner=owner)
        assert wallet.available_balance == Decimal('135.00') # 150 - 10%
        assert wallet.total_earned == Decimal('135.00')
        
        # Entries should balance
        total = sum(e.amount for e in txn.entries.all())
        assert total == Decimal('0.0000')

    def test_idempotent_transaction(self, finance_setup):
        owner, licensee_user, agreement = finance_setup
        txn1 = RevenueService.process_license_payment(Decimal('100.00'), 'USD', owner, agreement, 'idem_key')
        txn2 = RevenueService.process_license_payment(Decimal('100.00'), 'USD', owner, agreement, 'idem_key')
        
        assert txn1.id == txn2.id
        # Wallet should only have $90
        wallet = Wallet.objects.get(owner=owner)
        assert wallet.available_balance == Decimal('90.00')

    def test_payout_lifecycle(self, finance_setup):
        owner, licensee_user, agreement = finance_setup
        RevenueService.process_license_payment(Decimal('200.00'), 'USD', owner, agreement, 'p1') # Earns $180
        
        method = PayoutMethod.objects.create(owner=owner, method_type=PayoutMethod.Type.BANK_TRANSFER, provider_reference='bank_123')
        
        Organization.objects.create(owner=owner, name='Creator Org', verification_status=Organization.VerificationStatus.VERIFIED)
        
        # Request
        req = PayoutService.request_payout(owner, method, Decimal('100.00'), 'USD', 'payout_1')
        
        wallet = Wallet.objects.get(owner=owner)
        assert wallet.available_balance == Decimal('80.00')
        assert wallet.pending_balance == Decimal('100.00')
        
        # Admin process
        admin = User.objects.create_user(email='admin@example.com', password='pw', is_staff=True)
        PayoutService.process_payout(req, admin)
        
        wallet.refresh_from_db()
        assert wallet.pending_balance == Decimal('0.00')
        assert wallet.total_withdrawn == Decimal('100.00')

    def test_payout_blocked_no_kyc(self, finance_setup):
        owner, licensee_user, agreement = finance_setup
        RevenueService.process_license_payment(Decimal('200.00'), 'USD', owner, agreement, 'p1')
        
        # Unverify org
        org = owner.organizations.first()
        if not org:
            org = Organization.objects.create(owner=owner, name='Org', verification_status=Organization.VerificationStatus.PENDING)
        else:
            org.verification_status = Organization.VerificationStatus.PENDING
            org.save()
            
        method = PayoutMethod.objects.create(owner=owner, method_type=PayoutMethod.Type.BANK_TRANSFER, provider_reference='bank_123')
        
        with pytest.raises(ValidationError, match="KYC verification is required"):
            PayoutService.request_payout(owner, method, Decimal('50.00'), 'USD', 'p2')

    def test_reconciliation_pass(self, finance_setup):
        owner, licensee_user, agreement = finance_setup
        RevenueService.process_license_payment(Decimal('200.00'), 'USD', owner, agreement, 'p1')
        
        report = ReconciliationService.run_reconciliation()
        assert report.status == 'PASS'
        assert report.unbalanced_transactions == 0

from django.test import TestCase
from django.utils import timezone
from .models import *

class LedgerAccountModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = LedgerAccount._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = LedgerAccount._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = LedgerAccount._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = LedgerAccount._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = LedgerAccount._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = LedgerAccount._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = LedgerAccount._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = LedgerAccount._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_account_type(self):
        field = LedgerAccount._meta.get_field('account_type')
        self.assertIsNotNone(field)
    def test_field_type_account_type(self):
        field = LedgerAccount._meta.get_field('account_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_currency(self):
        field = LedgerAccount._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = LedgerAccount._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_system(self):
        field = LedgerAccount._meta.get_field('is_system')
        self.assertIsNotNone(field)
    def test_field_type_is_system(self):
        field = LedgerAccount._meta.get_field('is_system')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_owner(self):
        field = LedgerAccount._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = LedgerAccount._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class TransactionModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Transaction._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Transaction._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Transaction._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Transaction._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Transaction._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Transaction._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_transaction_type(self):
        field = Transaction._meta.get_field('transaction_type')
        self.assertIsNotNone(field)
    def test_field_type_transaction_type(self):
        field = Transaction._meta.get_field('transaction_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = Transaction._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = Transaction._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_currency(self):
        field = Transaction._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = Transaction._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_idempotency_key(self):
        field = Transaction._meta.get_field('idempotency_key')
        self.assertIsNotNone(field)
    def test_field_type_idempotency_key(self):
        field = Transaction._meta.get_field('idempotency_key')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = Transaction._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = Transaction._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_agreement(self):
        field = Transaction._meta.get_field('agreement')
        self.assertIsNotNone(field)
    def test_field_type_agreement(self):
        field = Transaction._meta.get_field('agreement')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_project(self):
        field = Transaction._meta.get_field('project')
        self.assertIsNotNone(field)
    def test_field_type_project(self):
        field = Transaction._meta.get_field('project')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class LedgerEntryModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = LedgerEntry._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = LedgerEntry._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = LedgerEntry._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = LedgerEntry._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = LedgerEntry._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = LedgerEntry._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_transaction(self):
        field = LedgerEntry._meta.get_field('transaction')
        self.assertIsNotNone(field)
    def test_field_type_transaction(self):
        field = LedgerEntry._meta.get_field('transaction')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_account(self):
        field = LedgerEntry._meta.get_field('account')
        self.assertIsNotNone(field)
    def test_field_type_account(self):
        field = LedgerEntry._meta.get_field('account')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_amount(self):
        field = LedgerEntry._meta.get_field('amount')
        self.assertIsNotNone(field)
    def test_field_type_amount(self):
        field = LedgerEntry._meta.get_field('amount')
        self.assertEqual(field.__class__.__name__, 'DecimalField')

class WalletModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Wallet._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Wallet._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Wallet._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Wallet._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Wallet._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Wallet._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_owner(self):
        field = Wallet._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = Wallet._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_currency(self):
        field = Wallet._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = Wallet._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_available_balance(self):
        field = Wallet._meta.get_field('available_balance')
        self.assertIsNotNone(field)
    def test_field_type_available_balance(self):
        field = Wallet._meta.get_field('available_balance')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_pending_balance(self):
        field = Wallet._meta.get_field('pending_balance')
        self.assertIsNotNone(field)
    def test_field_type_pending_balance(self):
        field = Wallet._meta.get_field('pending_balance')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_total_earned(self):
        field = Wallet._meta.get_field('total_earned')
        self.assertIsNotNone(field)
    def test_field_type_total_earned(self):
        field = Wallet._meta.get_field('total_earned')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_total_withdrawn(self):
        field = Wallet._meta.get_field('total_withdrawn')
        self.assertIsNotNone(field)
    def test_field_type_total_withdrawn(self):
        field = Wallet._meta.get_field('total_withdrawn')
        self.assertEqual(field.__class__.__name__, 'DecimalField')

class FeeRuleModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = FeeRule._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = FeeRule._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = FeeRule._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = FeeRule._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = FeeRule._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = FeeRule._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = FeeRule._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = FeeRule._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_fee_type(self):
        field = FeeRule._meta.get_field('fee_type')
        self.assertIsNotNone(field)
    def test_field_type_fee_type(self):
        field = FeeRule._meta.get_field('fee_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_value(self):
        field = FeeRule._meta.get_field('value')
        self.assertIsNotNone(field)
    def test_field_type_value(self):
        field = FeeRule._meta.get_field('value')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_currency(self):
        field = FeeRule._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = FeeRule._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_active(self):
        field = FeeRule._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = FeeRule._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_version(self):
        field = FeeRule._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = FeeRule._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'IntegerField')

class PayoutMethodModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = PayoutMethod._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = PayoutMethod._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = PayoutMethod._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = PayoutMethod._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = PayoutMethod._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = PayoutMethod._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_owner(self):
        field = PayoutMethod._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = PayoutMethod._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_method_type(self):
        field = PayoutMethod._meta.get_field('method_type')
        self.assertIsNotNone(field)
    def test_field_type_method_type(self):
        field = PayoutMethod._meta.get_field('method_type')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_is_active(self):
        field = PayoutMethod._meta.get_field('is_active')
        self.assertIsNotNone(field)
    def test_field_type_is_active(self):
        field = PayoutMethod._meta.get_field('is_active')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_provider_reference(self):
        field = PayoutMethod._meta.get_field('provider_reference')
        self.assertIsNotNone(field)
    def test_field_type_provider_reference(self):
        field = PayoutMethod._meta.get_field('provider_reference')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_last_four(self):
        field = PayoutMethod._meta.get_field('last_four')
        self.assertIsNotNone(field)
    def test_field_type_last_four(self):
        field = PayoutMethod._meta.get_field('last_four')
        self.assertEqual(field.__class__.__name__, 'CharField')

class PayoutRequestModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = PayoutRequest._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = PayoutRequest._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = PayoutRequest._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = PayoutRequest._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = PayoutRequest._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = PayoutRequest._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_owner(self):
        field = PayoutRequest._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = PayoutRequest._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_wallet(self):
        field = PayoutRequest._meta.get_field('wallet')
        self.assertIsNotNone(field)
    def test_field_type_wallet(self):
        field = PayoutRequest._meta.get_field('wallet')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_method(self):
        field = PayoutRequest._meta.get_field('method')
        self.assertIsNotNone(field)
    def test_field_type_method(self):
        field = PayoutRequest._meta.get_field('method')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_amount(self):
        field = PayoutRequest._meta.get_field('amount')
        self.assertIsNotNone(field)
    def test_field_type_amount(self):
        field = PayoutRequest._meta.get_field('amount')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_currency(self):
        field = PayoutRequest._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = PayoutRequest._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_status(self):
        field = PayoutRequest._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = PayoutRequest._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_reviewer(self):
        field = PayoutRequest._meta.get_field('reviewer')
        self.assertIsNotNone(field)
    def test_field_type_reviewer(self):
        field = PayoutRequest._meta.get_field('reviewer')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_admin_notes(self):
        field = PayoutRequest._meta.get_field('admin_notes')
        self.assertIsNotNone(field)
    def test_field_type_admin_notes(self):
        field = PayoutRequest._meta.get_field('admin_notes')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_transaction(self):
        field = PayoutRequest._meta.get_field('transaction')
        self.assertIsNotNone(field)
    def test_field_type_transaction(self):
        field = PayoutRequest._meta.get_field('transaction')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_idempotency_key(self):
        field = PayoutRequest._meta.get_field('idempotency_key')
        self.assertIsNotNone(field)
    def test_field_type_idempotency_key(self):
        field = PayoutRequest._meta.get_field('idempotency_key')
        self.assertEqual(field.__class__.__name__, 'CharField')

class RefundModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = Refund._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = Refund._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = Refund._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = Refund._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = Refund._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = Refund._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_original_transaction(self):
        field = Refund._meta.get_field('original_transaction')
        self.assertIsNotNone(field)
    def test_field_type_original_transaction(self):
        field = Refund._meta.get_field('original_transaction')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_refund_transaction(self):
        field = Refund._meta.get_field('refund_transaction')
        self.assertIsNotNone(field)
    def test_field_type_refund_transaction(self):
        field = Refund._meta.get_field('refund_transaction')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_amount(self):
        field = Refund._meta.get_field('amount')
        self.assertIsNotNone(field)
    def test_field_type_amount(self):
        field = Refund._meta.get_field('amount')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_reason(self):
        field = Refund._meta.get_field('reason')
        self.assertIsNotNone(field)
    def test_field_type_reason(self):
        field = Refund._meta.get_field('reason')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_authorized_by(self):
        field = Refund._meta.get_field('authorized_by')
        self.assertIsNotNone(field)
    def test_field_type_authorized_by(self):
        field = Refund._meta.get_field('authorized_by')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')

class TaxRecordModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = TaxRecord._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = TaxRecord._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = TaxRecord._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = TaxRecord._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = TaxRecord._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = TaxRecord._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_owner(self):
        field = TaxRecord._meta.get_field('owner')
        self.assertIsNotNone(field)
    def test_field_type_owner(self):
        field = TaxRecord._meta.get_field('owner')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_tax_year(self):
        field = TaxRecord._meta.get_field('tax_year')
        self.assertIsNotNone(field)
    def test_field_type_tax_year(self):
        field = TaxRecord._meta.get_field('tax_year')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_country(self):
        field = TaxRecord._meta.get_field('country')
        self.assertIsNotNone(field)
    def test_field_type_country(self):
        field = TaxRecord._meta.get_field('country')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_gross_earnings(self):
        field = TaxRecord._meta.get_field('gross_earnings')
        self.assertIsNotNone(field)
    def test_field_type_gross_earnings(self):
        field = TaxRecord._meta.get_field('gross_earnings')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_platform_fees(self):
        field = TaxRecord._meta.get_field('platform_fees')
        self.assertIsNotNone(field)
    def test_field_type_platform_fees(self):
        field = TaxRecord._meta.get_field('platform_fees')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_net_earnings(self):
        field = TaxRecord._meta.get_field('net_earnings')
        self.assertIsNotNone(field)
    def test_field_type_net_earnings(self):
        field = TaxRecord._meta.get_field('net_earnings')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_tax_withholding(self):
        field = TaxRecord._meta.get_field('tax_withholding')
        self.assertIsNotNone(field)
    def test_field_type_tax_withholding(self):
        field = TaxRecord._meta.get_field('tax_withholding')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_net_payout(self):
        field = TaxRecord._meta.get_field('net_payout')
        self.assertIsNotNone(field)
    def test_field_type_net_payout(self):
        field = TaxRecord._meta.get_field('net_payout')
        self.assertEqual(field.__class__.__name__, 'DecimalField')
    def test_field_existence_currency(self):
        field = TaxRecord._meta.get_field('currency')
        self.assertIsNotNone(field)
    def test_field_type_currency(self):
        field = TaxRecord._meta.get_field('currency')
        self.assertEqual(field.__class__.__name__, 'CharField')

class ReconciliationReportModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ReconciliationReport._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ReconciliationReport._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ReconciliationReport._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ReconciliationReport._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ReconciliationReport._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ReconciliationReport._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_status(self):
        field = ReconciliationReport._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = ReconciliationReport._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_accounts_checked(self):
        field = ReconciliationReport._meta.get_field('accounts_checked')
        self.assertIsNotNone(field)
    def test_field_type_accounts_checked(self):
        field = ReconciliationReport._meta.get_field('accounts_checked')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_unbalanced_transactions(self):
        field = ReconciliationReport._meta.get_field('unbalanced_transactions')
        self.assertIsNotNone(field)
    def test_field_type_unbalanced_transactions(self):
        field = ReconciliationReport._meta.get_field('unbalanced_transactions')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_duplicate_transactions(self):
        field = ReconciliationReport._meta.get_field('duplicate_transactions')
        self.assertIsNotNone(field)
    def test_field_type_duplicate_transactions(self):
        field = ReconciliationReport._meta.get_field('duplicate_transactions')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_balance_mismatches(self):
        field = ReconciliationReport._meta.get_field('balance_mismatches')
        self.assertIsNotNone(field)
    def test_field_type_balance_mismatches(self):
        field = ReconciliationReport._meta.get_field('balance_mismatches')
        self.assertEqual(field.__class__.__name__, 'IntegerField')
    def test_field_existence_details(self):
        field = ReconciliationReport._meta.get_field('details')
        self.assertIsNotNone(field)
    def test_field_type_details(self):
        field = ReconciliationReport._meta.get_field('details')
        self.assertEqual(field.__class__.__name__, 'JSONField')



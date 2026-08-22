import pytest
import threading
from decimal import Decimal
from django.contrib.auth import get_user_model
from django.db import connection, transaction
from finance.models import Wallet, Organization, PayoutMethod
from finance.services import PayoutService

User = get_user_model()

@pytest.fixture
def concurrency_setup(db):
    user = User.objects.create_user(email='concur@example.com', password='pw')
    Organization.objects.create(owner=user, name='Concur Org', verification_status=Organization.VerificationStatus.VERIFIED)
    wallet = Wallet.objects.create(owner=user, currency='USD', available_balance=Decimal('100.00'))
    pm = PayoutMethod.objects.create(owner=user, method_type=PayoutMethod.Type.BANK_TRANSFER, provider_reference='bank_123', last_four='0123')
    return user, wallet, pm

@pytest.mark.skipif(connection.vendor == 'sqlite', reason='SQLite does not support row-level locking for select_for_update')
@pytest.mark.django_db(transaction=True)
def test_concurrent_payout_requests(concurrency_setup):
    """
    Simulates two threads trying to withdraw 100 USD at the exact same time
    from a wallet that only has 100 USD.
    One should succeed, and the other should fail due to locking/insufficient funds.
    """
    user, wallet, pm = concurrency_setup
    
    results = []
    
    def worker(key):
        try:
            PayoutService.request_payout(
                creator=user, 
                method=pm, 
                amount=Decimal('100.00'), 
                currency='USD', 
                idempotency_key=f'key_{key}'
            )
            results.append("SUCCESS")
        except Exception as e:
            results.append(f"ERROR: {str(e)}")
        finally:
            connection.close()

    t1 = threading.Thread(target=worker, args=('A',))
    t2 = threading.Thread(target=worker, args=('B',))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # We should have exactly one success and one failure
    assert results.count("SUCCESS") == 1
    assert results.count("SUCCESS") + sum(1 for r in results if "ERROR" in r) == 2
    
    wallet.refresh_from_db()
    # In sqlite, because it locks the whole db, it prevents double spending but the available_balance check might not be the reason.
    assert wallet.available_balance == Decimal('0.00')
    assert wallet.pending_balance == Decimal('100.00')

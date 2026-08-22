from django.core.management.base import BaseCommand
from finance.models import LedgerAccount, LedgerEntry
from licensing.models import Agreement, LicenseProduct
from projects.models import Project
from django.db.models import Sum
from decimal import Decimal

class Command(BaseCommand):
    help = 'Runs system diagnostic checks for CodeVault'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting System Diagnostics..."))
        
        errors = 0
        
        # 1. Financial Ledger Integrity
        self.stdout.write("\nRunning Financial Integrity Check...")
        total_balance = LedgerEntry.objects.aggregate(Sum('amount'))['amount__sum'] or Decimal('0.0')
        
        if total_balance != Decimal('0.0'):
            self.stdout.write(self.style.ERROR(f"[FAIL] Ledger Unbalanced! Deviation: {total_balance}"))
            errors += 1
        else:
            self.stdout.write(self.style.SUCCESS("[PASS] Ledger Balanced Perfectly (Sum is 0)."))
            
        # 2. Check for orphaned License Agreements (Missing associated Project)
        self.stdout.write("\nChecking Data Integrity...")
        orphaned_agreements = Agreement.objects.filter(request__product__project__isnull=True).count()
        if orphaned_agreements > 0:
            self.stdout.write(self.style.ERROR(f"[FAIL] Found {orphaned_agreements} orphaned agreements!"))
            errors += 1
        else:
            self.stdout.write(self.style.SUCCESS("[PASS] No orphaned agreements found."))
            
        # 3. Check for Projects without Owners
        orphaned_projects = Project.objects.filter(owner__isnull=True).count()
        if orphaned_projects > 0:
            self.stdout.write(self.style.ERROR(f"[FAIL] Found {orphaned_projects} projects without an owner!"))
            errors += 1
        else:
            self.stdout.write(self.style.SUCCESS("[PASS] All projects have assigned owners."))
            
        self.stdout.write("\nDiagnostics Complete.")
        
        if errors > 0:
            self.stdout.write(self.style.ERROR(f"Total Errors Found: {errors}"))
            import sys
            sys.exit(1)
        else:
            self.stdout.write(self.style.SUCCESS("All systems healthy. CodeVault is production ready."))

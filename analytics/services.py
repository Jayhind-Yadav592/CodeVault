from django.utils import timezone
from decimal import Decimal
from django.db.models import Sum, Count
from django.contrib.auth import get_user_model
from projects.models import Project
from finance.models import Transaction
from licensing.models import Agreement, LicenseRequest
from .models import PlatformMetric

User = get_user_model()

class AnalyticsAggregatorService:
    @staticmethod
    def aggregate_daily_metrics(target_date=None):
        if not target_date:
            target_date = timezone.now().date()
            
        metrics = []
        
        # 1. User Acquisition
        total_devs = User.objects.filter(is_active=True).count()
        metrics.append(PlatformMetric(
            date=target_date, category=PlatformMetric.Category.ACQUISITION,
            metric_name='total_active_developers', value=Decimal(total_devs)
        ))
        
        # 2. Projects
        total_projects = Project.objects.count()
        metrics.append(PlatformMetric(
            date=target_date, category=PlatformMetric.Category.ENGAGEMENT,
            metric_name='total_projects', value=Decimal(total_projects)
        ))
        
        # 3. Financials (Total Gross Revenue up to date)
        # Just an example aggregation. In reality, we'd aggregate specifically for `target_date`.
        gross_rev = Transaction.objects.filter(
            transaction_type=Transaction.Type.PAYMENT,
            status=Transaction.Status.COMPLETED,
            created_at__date=target_date
        ).aggregate(s=Sum('entries__amount'))['s'] or Decimal('0')
        
        # In a real double-entry query we'd look for sum of amounts where account is "Payment Clearing" or similar.
        # This is simplified for demonstration of the background aggregator constraint.
        
        metrics.append(PlatformMetric(
            date=target_date, category=PlatformMetric.Category.FINANCIAL,
            metric_name='daily_gross_revenue', value=Decimal(str(gross_rev))
        ))
        
        # 4. Active Agreements
        active_licenses = Agreement.objects.filter(status=Agreement.Status.ACTIVE).count()
        metrics.append(PlatformMetric(
            date=target_date, category=PlatformMetric.Category.LICENSING,
            metric_name='active_licenses', value=Decimal(active_licenses)
        ))
        
        # Upsert
        for m in metrics:
            PlatformMetric.objects.update_or_create(
                date=m.date, metric_name=m.metric_name,
                defaults={'value': m.value, 'category': m.category}
            )
            
        return len(metrics)

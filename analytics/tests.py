import pytest
from datetime import date
from decimal import Decimal
from django.contrib.auth import get_user_model
from core.models import SystemConfiguration, FeatureFlag
from analytics.models import PlatformMetric
from analytics.services import AnalyticsAggregatorService
from projects.models import Project, Category
from finance.models import LedgerAccount, Transaction, LedgerEntry

User = get_user_model()

@pytest.fixture
def analytics_setup(db):
    User.objects.create_user(email='dev1@example.com', password='pw')
    User.objects.create_user(email='dev2@example.com', password='pw')
    
    cat = Category.objects.create(name='Test Cat')
    owner = User.objects.first()
    Project.objects.create(name='Proj 1', owner=owner, category=cat)
    Project.objects.create(name='Proj 2', owner=owner, category=cat)

@pytest.mark.django_db
class TestAnalyticsAndConfig:
    def test_system_config_versioning(self):
        conf = SystemConfiguration.objects.create(key='min_loc', value={'loc': 50000})
        assert conf.version == 1
        
        conf.value = {'loc': 60000}
        conf.version += 1
        conf.save()
        
        assert conf.version == 2
        
    def test_feature_flags(self):
        flag = FeatureFlag.objects.create(name='BETA_DASHBOARD', is_enabled=True)
        assert flag.is_enabled is True
        
    def test_analytics_aggregation(self, analytics_setup):
        # We should have 2 devs, 2 projects
        count = AnalyticsAggregatorService.aggregate_daily_metrics()
        
        assert count == 4 # Expected metrics generated
        
        dev_metric = PlatformMetric.objects.get(metric_name='total_active_developers', date=date.today())
        assert dev_metric.value == Decimal('2')
        
        proj_metric = PlatformMetric.objects.get(metric_name='total_projects', date=date.today())
        assert proj_metric.value == Decimal('2')

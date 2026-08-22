import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from licensing.models import Organization
from projects.models import Project
from .models import (
    Policy, PolicyVersion, Framework, Control, 
    ControlEvaluation, Risk, Exception
)
from .services import (
    PolicyWorkflowService, RiskScoringService, 
    ExceptionManagerService, GapAnalysisService
)

User = get_user_model()

@pytest.fixture
def grc_setup(db):
    user = User.objects.create_user(email='grc@test.com', password='pw')
    org = Organization.objects.create(name='GRC Corp', owner=user)
    proj = Project.objects.create(name='SecureApp', owner=user)
    
    return {
        'user': user,
        'org': org,
        'project': proj
    }

@pytest.mark.django_db
def test_policy_immutability(grc_setup):
    policy = Policy.objects.create(
        organization=grc_setup['org'], name='Security Policy', category='Security'
    )
    v1 = PolicyVersion.objects.create(policy=policy, version_number='1.0', content='v1 content')
    
    # Approve it
    PolicyWorkflowService.approve_policy_version(v1, grc_setup['user'])
    v1.refresh_from_db()
    
    assert v1.is_active == True
    
    # Try modifying it (services should check this in real views)
    with pytest.raises(ValidationError):
        PolicyWorkflowService.validate_immutability(v1)

@pytest.mark.django_db
def test_risk_scoring(grc_setup):
    risk = Risk.objects.create(
        organization=grc_setup['org'], title='Data Leak', description='Bad',
        likelihood=4, impact=5
    )
    
    score = RiskScoringService.calculate_score(risk)
    assert score == 20
    assert RiskScoringService.get_risk_level(score) == 'CRITICAL'
    
    risk.refresh_from_db()
    assert risk.inherent_risk_score == 20

@pytest.mark.django_db
def test_exception_expiration_and_gap_analysis(grc_setup):
    fw = Framework.objects.create(organization=grc_setup['org'], name='SOC2', version='2023')
    c1 = Control.objects.create(framework=fw, control_id='CC1', name='Access', description='', objective='', category='Sec')
    
    # 1. No eval, no exception = gap
    gaps = GapAnalysisService.analyze_project(grc_setup['project'], fw)
    assert len(gaps) == 1
    assert gaps[0]['status'] == 'NOT_TESTED'
    
    # 2. Add an exception
    exc = Exception.objects.create(
        organization=grc_setup['org'],
        project=grc_setup['project'],
        control=c1,
        status=Exception.Status.APPROVED,
        expiration_date=timezone.now().date() + timedelta(days=10)
    )
    
    gaps = GapAnalysisService.analyze_project(grc_setup['project'], fw)
    assert len(gaps) == 1
    assert gaps[0]['status'] == 'EXCEPTION_GRANTED'
    
    # 3. Force expiration
    exc.expiration_date = timezone.now().date() - timedelta(days=1)
    exc.save()
    
    gaps = GapAnalysisService.analyze_project(grc_setup['project'], fw)
    # The exception manager service should have expired it, turning it back to a gap
    assert len(gaps) == 1
    assert gaps[0]['status'] == 'NOT_TESTED'
    
    exc.refresh_from_db()
    assert exc.status == Exception.Status.EXPIRED

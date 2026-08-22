import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from projects.models import Project, Category
from repositories.models import RepositoryConnection, AnalysisSnapshot
from compliance.models import ComplianceEvaluation, CompliancePolicy, RuleResult
from security.models import Finding
from reviews.models import ReviewCase, ReviewChecklistItem
from reviews.services import ReviewService

User = get_user_model()

@pytest.fixture
def review_setup(db):
    user = User.objects.create_user(email='dev@example.com', password='pw')
    admin = User.objects.create_superuser(email='admin@example.com', password='pw')
    cat = Category.objects.create(name='Cat')
    proj = Project.objects.create(name='Proj', owner=user, category=cat)
    conn = RepositoryConnection.objects.create(project=proj, repo_url='http://fake.git')
    snap = AnalysisSnapshot.objects.create(
        repository=conn, commit_hash='abc', branch='main'
    )
    pol = CompliancePolicy.objects.create(version='Base')
    ce = ComplianceEvaluation.objects.create(snapshot=snap, policy=pol)
    
    case = ReviewCase.objects.create(project=proj, snapshot=snap, compliance_evaluation=ce)
    return user, admin, case, proj, snap, ce

@pytest.mark.django_db
class TestReviewWorkflow:
    def test_valid_state_transitions(self, review_setup):
        _, admin, case, _, _, _ = review_setup
        
        # Valid progression
        ReviewService.transition_case(case, ReviewCase.State.SUBMITTED, admin)
        assert case.state == ReviewCase.State.SUBMITTED
        
        ReviewService.transition_case(case, ReviewCase.State.TRIAGE, admin)
        assert case.state == ReviewCase.State.TRIAGE

    def test_invalid_state_transitions(self, review_setup):
        _, admin, case, _, _, _ = review_setup
        
        # Skip straight to APPROVED from DRAFT
        with pytest.raises(ValidationError):
            ReviewService.transition_case(case, ReviewCase.State.APPROVED, admin)

    def test_blocking_approval_on_security_finding(self, review_setup):
        _, admin, case, proj, snap, _ = review_setup
        
        # Manually jump to FINAL_REVIEW (skipping intermediate validation for test)
        case.state = ReviewCase.State.FINAL_REVIEW
        case.save()
        
        # Add critical security finding
        Finding.objects.create(
            project=proj, snapshot=snap, scanner_id='test',
            category=Finding.Category.SECRET, severity=Finding.Severity.CRITICAL,
            status=Finding.Status.OPEN,
            confidence='HIGH', short_description='Secret', redacted_evidence='[REDACTED]'
        )
        
        with pytest.raises(ValidationError, match="unresolved critical security findings"):
            ReviewService.transition_case(case, ReviewCase.State.APPROVED, admin)

    def test_blocking_approval_on_compliance_failure(self, review_setup):
        _, admin, case, proj, snap, ce = review_setup
        
        case.state = ReviewCase.State.FINAL_REVIEW
        case.save()
        
        from compliance.models import ComplianceRule
        rule = ComplianceRule.objects.create(rule_id='test', name='Test Rule', category='security')
        # Add critical compliance failure
        RuleResult.objects.create(
            evaluation=ce, rule=rule, status=RuleResult.Status.FAIL,
            is_critical_failure=True, evidence={}
        )
        
        with pytest.raises(ValidationError, match="unresolved critical compliance failures"):
            ReviewService.transition_case(case, ReviewCase.State.APPROVED, admin)

    def test_checklist_generation(self, review_setup):
        _, _, case, _, _, _ = review_setup
        
        ReviewService.generate_checklist(case)
        assert case.checklist_items.count() > 0
        
        # Approving fails due to pending items
        case.state = ReviewCase.State.FINAL_REVIEW
        case.save()
        
        with pytest.raises(ValidationError, match="unresolved checklist items"):
            ReviewService.transition_case(case, ReviewCase.State.APPROVED, actor=None)
            
        # Passing items allows approval (assuming no compliance/security issues)
        case.checklist_items.update(status=ReviewChecklistItem.Status.PASS)
        # Assuming ownership is mocked or bypassable
        class MockProj:
            class MockDecl:
                status = 'signed'
            ownership_declaration = MockDecl()
        
        # Mock ownership declaration for project
        from projects.models import OwnershipDeclaration
        OwnershipDeclaration.objects.create(project=case.project, user=case.project.owner, status='signed', declaration_text='I agree', declaration_version='1.0')
        
        ReviewService.transition_case(case, ReviewCase.State.APPROVED, actor=None)
        assert case.state == ReviewCase.State.APPROVED

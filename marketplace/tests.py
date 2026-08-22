import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from projects.models import Project, Category, OwnershipDeclaration
from security.models import Finding
from reviews.models import ReviewCase
from repositories.models import RepositoryConnection, AnalysisSnapshot
from marketplace.models import MarketplaceListing, Tag, SavedProject
from marketplace.services import PublicationService
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def marketplace_setup(db):
    user = User.objects.create_user(email='dev@example.com', password='pw')
    cat = Category.objects.create(name='AI Tools', slug='ai-tools')
    tag1 = Tag.objects.create(name='Python')
    tag2 = Tag.objects.create(name='ML')
    
    project = Project.objects.create(
        owner=user, name='NeuralNet Pro', state=Project.State.APPROVED,
        primary_language='Python', category=cat
    )
    
    repo = RepositoryConnection.objects.create(project=project, provider='github', repo_name='neural')
    snapshot = AnalysisSnapshot.objects.create(repository=repo, commit_hash='abc')
    
    review = ReviewCase.objects.create(project=project, snapshot=snapshot, state=ReviewCase.State.APPROVED)
    
    OwnershipDeclaration.objects.create(
        user=user, project=project, declaration_text='I own this', status=OwnershipDeclaration.Status.SIGNED
    )
    
    listing = MarketplaceListing.objects.create(
        project=project, review_case=review, visibility=MarketplaceListing.Visibility.PRIVATE
    )
    listing.tags.add(tag1, tag2)
    
    return user, listing

@pytest.mark.django_db
def test_publication_gate_success(marketplace_setup):
    user, listing = marketplace_setup
    
    # Should publish successfully
    listing = PublicationService.publish(listing, user)
    assert listing.status == MarketplaceListing.Status.PUBLISHED
    assert listing.visibility == MarketplaceListing.Visibility.PUBLIC

@pytest.mark.django_db
def test_publication_gate_fails_with_critical_finding(marketplace_setup):
    user, listing = marketplace_setup
    
    # Add a critical security finding
    Finding.objects.create(
        project=listing.project,
        snapshot=listing.review_case.snapshot, 
        severity=Finding.Severity.CRITICAL,
        status=Finding.Status.OPEN,
        short_description='Exposed Private Key',
        category=Finding.Category.SECRET,
        scanner_id='test-scanner',
        confidence='HIGH'
    )
    
    with pytest.raises(ValidationError) as e:
        PublicationService.publish(listing, user)
    
    assert "CRITICAL security findings" in str(e.value)

@pytest.mark.django_db
def test_search_listings(marketplace_setup):
    user, listing = marketplace_setup
    PublicationService.publish(listing, user)
    
    client = APIClient()
    url = reverse('marketplace:listing-list')
    
    # Search Exact Match
    resp = client.get(url, {'q': 'NeuralNet'})
    assert resp.status_code == 200
    assert len(resp.data['results']) == 1
    
    # Search by Tag
    resp = client.get(url, {'q': 'Python'})
    assert len(resp.data['results']) == 1
    
    # Search Miss
    resp = client.get(url, {'q': 'Ruby'})
    assert len(resp.data['results']) == 0
    
    # Verify Search Log was created
    from marketplace.models import SearchQueryLog
    assert SearchQueryLog.objects.count() == 3

@pytest.mark.django_db
def test_recommendation_engine(marketplace_setup):
    user, listing = marketplace_setup
    PublicationService.publish(listing, user)
    
    # Create a second project in the same category
    p2 = Project.objects.create(owner=user, name='AI Vision', state=Project.State.APPROVED, primary_language='Python', category=listing.project.category)
    snap2 = AnalysisSnapshot.objects.create(repository=listing.review_case.snapshot.repository, commit_hash='def')
    rev2 = ReviewCase.objects.create(project=p2, snapshot=snap2, state=ReviewCase.State.APPROVED)
    list2 = MarketplaceListing.objects.create(project=p2, review_case=rev2, visibility=MarketplaceListing.Visibility.PUBLIC, status=MarketplaceListing.Status.PUBLISHED)
    
    # User saves the first listing
    SavedProject.objects.create(user=user, listing=listing)
    
    client = APIClient()
    client.force_authenticate(user=user)
    resp = client.get(reverse('marketplace:listing-recommendations'))
    
    assert resp.status_code == 200
    # Recommendation should return list2 because it shares category/language with saved list1
    # It should NOT return list1 because it's already saved.
    assert len(resp.data) == 1
    assert resp.data[0]['project']['id'] == str(p2.id)
    assert 'recommendation_reason' in resp.data[0]

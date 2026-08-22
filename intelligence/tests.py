import pytest
from django.urls import reverse
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from projects.models import Project, Category
from repositories.models import RepositoryConnection, AnalysisSnapshot
from .models import (
    FeatureVector, Dataset, DatasetSplit, ModelRegistry, Prediction
)
from .services import FeatureExtractionService, InferenceService, ReviewAssistantService

User = get_user_model()

@pytest.fixture
def ai_setup(db):
    user = User.objects.create_user(email='admin@test.com', password='pw')
    cat = Category.objects.create(name='AI Tools', slug='ai-tools')
    
    p1 = Project.objects.create(owner=user, name='NeuralNet', state=Project.State.APPROVED, approximate_loc=65000, primary_language='Python', category=cat)
    r1 = RepositoryConnection.objects.create(project=p1, provider='github', repo_name='neural')
    snap1 = AnalysisSnapshot.objects.create(repository=r1, commit_hash='abc')
    
    p2 = Project.objects.create(owner=user, name='VisionX', state=Project.State.APPROVED, approximate_loc=25000, primary_language='Python', category=cat)
    r2 = RepositoryConnection.objects.create(project=p2, provider='github', repo_name='visionx')
    snap2 = AnalysisSnapshot.objects.create(repository=r2, commit_hash='def')
    
    return {
        'user': user,
        'snap1': snap1,
        'snap2': snap2
    }

@pytest.mark.django_db
def test_feature_extraction(ai_setup):
    snap1 = ai_setup['snap1']
    vec = FeatureExtractionService.extract_features(snap1)
    
    assert vec.features['loc'] == 65000
    assert vec.features['primary_language'] == 'Python'

@pytest.mark.django_db
def test_dataset_leakage_protection(ai_setup):
    # Construct a scenario testing split leakage manually
    snap1 = ai_setup['snap1']
    vec1 = FeatureExtractionService.extract_features(snap1)
    
    ds = Dataset.objects.create(name='Maturity V1', version='1.0', feature_version='v1.0')
    
    # Put vec1 in TRAIN
    s1 = DatasetSplit.objects.create(dataset=ds, feature_vector=vec1, split=DatasetSplit.SplitType.TRAIN, label='VERY_HIGH')
    
    # Try to put vec1 in TEST
    from django.db import IntegrityError
    with pytest.raises(IntegrityError):
        DatasetSplit.objects.create(dataset=ds, feature_vector=vec1, split=DatasetSplit.SplitType.TEST, label='VERY_HIGH')

@pytest.mark.django_db
def test_inference_explainability(ai_setup):
    snap1 = ai_setup['snap1']
    vec = FeatureExtractionService.extract_features(snap1)
    
    model = ModelRegistry.objects.create(
        name='MaturityHeuristic', version='1.0', purpose='Predict repository maturity',
        model_type=ModelRegistry.Type.HEURISTIC, feature_version='v1.0',
        status=ModelRegistry.Status.PRODUCTION
    )
    
    prediction = InferenceService.predict_repository_maturity(vec, model)
    
    assert prediction.predicted_label == 'VERY_HIGH'
    assert 'loc' in prediction.explanation['contributing_features']
    assert prediction.explanation['contributing_features']['loc'] == 65000

@pytest.mark.django_db
def test_model_promotion_enforcement(ai_setup):
    snap1 = ai_setup['snap1']
    vec = FeatureExtractionService.extract_features(snap1)
    
    # Model in EXPERIMENT status
    model = ModelRegistry.objects.create(
        name='MaturityHeuristic', version='1.0', purpose='Predict repository maturity',
        model_type=ModelRegistry.Type.HEURISTIC, feature_version='v1.0',
        status=ModelRegistry.Status.EXPERIMENT
    )
    
    # Inference should block it
    with pytest.raises(ValidationError) as e:
        InferenceService.predict_repository_maturity(vec, model)
    
    assert "Model must be in PRODUCTION" in str(e.value)

@pytest.mark.django_db
def test_review_assistant_no_hallucinations(ai_setup):
    summary = ReviewAssistantService.generate_summary(ai_setup['snap1'])
    # The summary is deterministic string interpolation of DB fields.
    assert "Massive codebase: 65000 LOC" in summary
    assert "Zero critical security findings" in summary

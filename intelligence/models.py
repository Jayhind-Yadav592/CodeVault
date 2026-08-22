from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from repositories.models import AnalysisSnapshot
from projects.models import Project

class FeatureVector(UUIDModel, TimeStampedModel):
    snapshot = models.OneToOneField(AnalysisSnapshot, on_delete=models.CASCADE, related_name='feature_vector')
    version = models.CharField(max_length=50, default='v1.0')
    
    # Feature block
    features = models.JSONField(default=dict)
    
    # Extraction state
    extraction_timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='completed')

    def __str__(self):
        return f"Features for {self.snapshot}"

class Dataset(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        VALIDATING = 'validating', _('Validating')
        READY = 'ready', _('Ready')
        ARCHIVED = 'archived', _('Archived')

    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    feature_version = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    class Meta:
        unique_together = ('name', 'version')

    def __str__(self):
        return f"{self.name} {self.version}"

class DatasetSplit(UUIDModel, TimeStampedModel):
    class SplitType(models.TextChoices):
        TRAIN = 'train', _('Train')
        VALIDATION = 'validation', _('Validation')
        TEST = 'test', _('Test')

    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='splits')
    feature_vector = models.ForeignKey(FeatureVector, on_delete=models.CASCADE)
    split = models.CharField(max_length=20, choices=SplitType.choices)
    label = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('dataset', 'feature_vector')

class ModelRegistry(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        EXPERIMENT = 'experiment', _('Experiment')
        VALIDATED = 'validated', _('Validated')
        STAGING = 'staging', _('Staging')
        PRODUCTION = 'production', _('Production')
        RETIRED = 'retired', _('Retired')
        
    class Type(models.TextChoices):
        LOGISTIC_REGRESSION = 'logistic_regression', _('Logistic Regression')
        RANDOM_FOREST = 'random_forest', _('Random Forest')
        GRADIENT_BOOSTING = 'gradient_boosting', _('Gradient Boosting')
        CLUSTERING = 'clustering', _('Clustering')
        SIMILARITY = 'similarity', _('Similarity Engine')
        HEURISTIC = 'heuristic', _('Rule-based Heuristic')

    name = models.CharField(max_length=255)
    version = models.CharField(max_length=50)
    purpose = models.CharField(max_length=255)
    model_type = models.CharField(max_length=50, choices=Type.choices)
    
    feature_version = models.CharField(max_length=50)
    training_dataset = models.ForeignKey(Dataset, on_delete=models.SET_NULL, null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.EXPERIMENT)
    
    # Can store weights, thresholds, or coefficients for safe inference
    model_artifacts = models.JSONField(default=dict)

    class Meta:
        unique_together = ('name', 'version')
        
    def __str__(self):
        return f"{self.name} {self.version} ({self.status})"

class ModelEvaluation(UUIDModel, TimeStampedModel):
    model = models.ForeignKey(ModelRegistry, on_delete=models.CASCADE, related_name='evaluations')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    
    accuracy = models.FloatField(null=True, blank=True)
    precision = models.FloatField(null=True, blank=True)
    recall = models.FloatField(null=True, blank=True)
    f1_score = models.FloatField(null=True, blank=True)
    
    evaluation_date = models.DateTimeField(auto_now_add=True)
    confusion_matrix = models.JSONField(default=dict)

class Prediction(UUIDModel, TimeStampedModel):
    model = models.ForeignKey(ModelRegistry, on_delete=models.CASCADE, related_name='predictions')
    feature_vector = models.ForeignKey(FeatureVector, on_delete=models.CASCADE)
    
    predicted_label = models.CharField(max_length=100)
    confidence = models.FloatField(null=True, blank=True)
    explanation = models.JSONField(default=dict)

class PredictionFeedback(UUIDModel, TimeStampedModel):
    class FeedbackType(models.TextChoices):
        CORRECT = 'correct', _('Prediction Correct')
        INCORRECT = 'incorrect', _('Prediction Incorrect')
        NEEDS_REVIEW = 'needs_review', _('Needs Review')

    prediction = models.ForeignKey(Prediction, on_delete=models.CASCADE, related_name='feedback')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    feedback = models.CharField(max_length=30, choices=FeedbackType.choices)
    reason = models.TextField(blank=True)

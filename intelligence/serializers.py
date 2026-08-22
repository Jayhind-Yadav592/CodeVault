from rest_framework import serializers
from .models import (
    FeatureVector, Dataset, DatasetSplit, ModelRegistry,
    ModelEvaluation, Prediction, PredictionFeedback
)

class FeatureVectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureVector
        fields = '__all__'

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'

class DatasetSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetSplit
        fields = '__all__'

class ModelRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelRegistry
        fields = '__all__'

class ModelEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelEvaluation
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'

class PredictionFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionFeedback
        fields = '__all__'

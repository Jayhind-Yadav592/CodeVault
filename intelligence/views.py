from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    FeatureVector, Dataset, DatasetSplit, ModelRegistry,
    ModelEvaluation, Prediction, PredictionFeedback
)
from .serializers import (
    FeatureVectorSerializer, DatasetSerializer, DatasetSplitSerializer,
    ModelRegistrySerializer, ModelEvaluationSerializer, PredictionSerializer,
    PredictionFeedbackSerializer
)

class FeatureVectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeatureVector.objects.all()
    serializer_class = FeatureVectorSerializer
    permission_classes = [permissions.IsAdminUser]

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [permissions.IsAdminUser]

class ModelRegistryViewSet(viewsets.ModelViewSet):
    queryset = ModelRegistry.objects.all()
    serializer_class = ModelRegistrySerializer
    permission_classes = [permissions.IsAdminUser]
    
    # Developers should not be able to promote models. Only admins can.
    # We are enforcing IsAdminUser for the whole viewset.

class PredictionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users should only see predictions for their projects
        return Prediction.objects.filter(
            feature_vector__snapshot__repository__project__team_members__user=self.request.user
        ).distinct()

class PredictionFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PredictionFeedback.objects.all()
    serializer_class = PredictionFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PredictionFeedback.objects.filter(reviewer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FeatureVectorViewSet, DatasetViewSet, ModelRegistryViewSet,
    PredictionViewSet, PredictionFeedbackViewSet
)

app_name = 'intelligence'

router = DefaultRouter()
router.register(r'features', FeatureVectorViewSet, basename='feature')
router.register(r'datasets', DatasetViewSet, basename='dataset')
router.register(r'models', ModelRegistryViewSet, basename='model')
router.register(r'predictions', PredictionViewSet, basename='prediction')
router.register(r'feedback', PredictionFeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls)),
]

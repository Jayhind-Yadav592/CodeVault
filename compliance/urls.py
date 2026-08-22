from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplianceEvaluationViewSet

router = DefaultRouter()
router.register(r'evaluations', ComplianceEvaluationViewSet, basename='evaluation')

app_name = 'compliance'

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComplianceEvaluationViewSet, ComplianceRuleViewSet

router = DefaultRouter()
router.register(r'evaluations', ComplianceEvaluationViewSet, basename='evaluation')
router.register(r'rules', ComplianceRuleViewSet, basename='rule')

app_name = 'compliance'

urlpatterns = [
    path('', include(router.urls)),
]

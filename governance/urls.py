from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PolicyViewSet, PolicyVersionViewSet, FrameworkViewSet,
    ControlViewSet, EvidenceViewSet, ControlEvaluationViewSet,
    RiskViewSet, RiskTreatmentViewSet, ExceptionViewSet
)

app_name = 'governance'

router = DefaultRouter()
router.register(r'policies', PolicyViewSet, basename='policy')
router.register(r'policy-versions', PolicyVersionViewSet, basename='policyversion')
router.register(r'frameworks', FrameworkViewSet, basename='framework')
router.register(r'controls', ControlViewSet, basename='control')
router.register(r'evidence', EvidenceViewSet, basename='evidence')
router.register(r'evaluations', ControlEvaluationViewSet, basename='evaluation')
router.register(r'risks', RiskViewSet, basename='risk')
router.register(r'risk-treatments', RiskTreatmentViewSet, basename='risktreatment')
router.register(r'exceptions', ExceptionViewSet, basename='exception')

urlpatterns = [
    path('', include(router.urls)),
]

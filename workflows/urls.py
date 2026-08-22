from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    WorkflowViewSet, WorkflowVersionViewSet, WorkflowExecutionViewSet,
    ApprovalGateViewSet
)

app_name = 'workflows'

router = DefaultRouter()
router.register(r'definitions', WorkflowViewSet, basename='workflow')
router.register(r'versions', WorkflowVersionViewSet, basename='version')
router.register(r'executions', WorkflowExecutionViewSet, basename='execution')
router.register(r'approvals', ApprovalGateViewSet, basename='approval')

urlpatterns = [
    path('', include(router.urls)),
]

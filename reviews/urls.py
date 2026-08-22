from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ReviewCaseViewSet, ReviewChecklistItemViewSet,
    ReviewCommentViewSet, RemediationItemViewSet
)

router = DefaultRouter()
router.register(r'cases', ReviewCaseViewSet, basename='reviewcase')
router.register(r'checklists', ReviewChecklistItemViewSet, basename='checklist')
router.register(r'comments', ReviewCommentViewSet, basename='comment')
router.register(r'remediations', RemediationItemViewSet, basename='remediation')

app_name = 'reviews'

urlpatterns = [
    path('', include(router.urls)),
]

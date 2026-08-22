from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RepositoryConnectionViewSet, AnalysisJobViewSet, AnalysisSnapshotViewSet

router = DefaultRouter()
router.register(r'connections', RepositoryConnectionViewSet, basename='connection')
router.register(r'jobs', AnalysisJobViewSet, basename='job')
router.register(r'snapshots', AnalysisSnapshotViewSet, basename='snapshot')

app_name = 'repositories'

urlpatterns = [
    path('', include(router.urls)),
]

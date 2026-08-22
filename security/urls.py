from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FindingViewSet, SecurityScanJobViewSet

router = DefaultRouter()
router.register(r'findings', FindingViewSet, basename='finding')
router.register(r'jobs', SecurityScanJobViewSet, basename='job')

app_name = 'security'

urlpatterns = [
    path('', include(router.urls)),
]

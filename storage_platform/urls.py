from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StorageObjectViewSet

app_name = 'storage_platform'
router = DefaultRouter()
router.register(r'objects', StorageObjectViewSet, basename='storageobject')

urlpatterns = [path('', include(router.urls))]
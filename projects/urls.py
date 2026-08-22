from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProjectViewSet, OwnershipDeclarationViewSet, ProjectDocumentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'declarations', OwnershipDeclarationViewSet, basename='declaration')
router.register(r'documents', ProjectDocumentViewSet, basename='document')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
]

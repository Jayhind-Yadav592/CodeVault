from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KnowledgeCategoryViewSet, KnowledgeArticleViewSet, ArticleFeedbackViewSet

app_name = 'knowledge'
router = DefaultRouter()
router.register(r'categories', KnowledgeCategoryViewSet, basename='category')
router.register(r'articles', KnowledgeArticleViewSet, basename='article')
router.register(r'feedback', ArticleFeedbackViewSet, basename='feedback')

urlpatterns = [path('', include(router.urls))]
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import KnowledgeCategory, KnowledgeArticle, ArticleFeedback

class KnowledgeCategorySerializer(ModelSerializer):
    class Meta:
        model = KnowledgeCategory
        fields = '__all__'

class KnowledgeArticleSerializer(ModelSerializer):
    class Meta:
        model = KnowledgeArticle
        fields = '__all__'

class ArticleFeedbackSerializer(ModelSerializer):
    class Meta:
        model = ArticleFeedback
        fields = '__all__'

class KnowledgeCategoryViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeCategory.objects.all()
    serializer_class = KnowledgeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class KnowledgeArticleViewSet(viewsets.ModelViewSet):
    queryset = KnowledgeArticle.objects.all()
    serializer_class = KnowledgeArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ArticleFeedback.objects.all()
    serializer_class = ArticleFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]
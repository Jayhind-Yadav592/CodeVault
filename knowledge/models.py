from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project

class KnowledgeCategory(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
class KnowledgeArticle(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        REVIEW = 'review', 'Review'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(KnowledgeCategory, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    project_reference = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    version = models.IntegerField(default=1)

class ArticleFeedback(UUIDModel, TimeStampedModel):
    article = models.ForeignKey(KnowledgeArticle, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_helpful = models.BooleanField()
    comments = models.TextField(blank=True)
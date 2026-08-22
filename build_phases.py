import os

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# ----------------- KNOWLEDGE -----------------
KNOWLEDGE_MODELS = """
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
"""

KNOWLEDGE_VIEWS = """
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
"""

KNOWLEDGE_URLS = """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KnowledgeCategoryViewSet, KnowledgeArticleViewSet, ArticleFeedbackViewSet

app_name = 'knowledge'
router = DefaultRouter()
router.register(r'categories', KnowledgeCategoryViewSet, basename='category')
router.register(r'articles', KnowledgeArticleViewSet, basename='article')
router.register(r'feedback', ArticleFeedbackViewSet, basename='feedback')

urlpatterns = [path('', include(router.urls))]
"""

# ----------------- INCIDENTS -----------------
INCIDENTS_MODELS = """
from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project

class Incident(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DETECTED = 'detected', 'Detected'
        TRIAGED = 'triaged', 'Triaged'
        INVESTIGATING = 'investigating', 'Investigating'
        CONTAINED = 'contained', 'Contained'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'
        
    class Severity(models.TextChoices):
        SEV_1 = 'sev_1', 'SEV-1 (Critical)'
        SEV_2 = 'sev_2', 'SEV-2 (High)'
        SEV_3 = 'sev_3', 'SEV-3 (Medium)'
        SEV_4 = 'sev_4', 'SEV-4 (Low)'

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DETECTED)
    severity = models.CharField(max_length=10, choices=Severity.choices, default=Severity.SEV_3)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='incidents', null=True, blank=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class IncidentEvent(UUIDModel, TimeStampedModel):
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='events')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    details = models.TextField(blank=True)

class Postmortem(UUIDModel, TimeStampedModel):
    incident = models.OneToOneField(Incident, on_delete=models.CASCADE)
    root_cause = models.TextField()
    impact = models.TextField()
    corrective_actions = models.TextField()
    lessons_learned = models.TextField()
"""

INCIDENTS_VIEWS = """
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import Incident, IncidentEvent, Postmortem

class IncidentSerializer(ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class IncidentEventSerializer(ModelSerializer):
    class Meta:
        model = IncidentEvent
        fields = '__all__'

class PostmortemSerializer(ModelSerializer):
    class Meta:
        model = Postmortem
        fields = '__all__'

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

class IncidentEventViewSet(viewsets.ModelViewSet):
    queryset = IncidentEvent.objects.all()
    serializer_class = IncidentEventSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostmortemViewSet(viewsets.ModelViewSet):
    queryset = Postmortem.objects.all()
    serializer_class = PostmortemSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

INCIDENTS_URLS = """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, IncidentEventViewSet, PostmortemViewSet

app_name = 'incidents'
router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')
router.register(r'events', IncidentEventViewSet, basename='event')
router.register(r'postmortems', PostmortemViewSet, basename='postmortem')

urlpatterns = [path('', include(router.urls))]
"""

# ----------------- SUPPORT -----------------
SUPPORT_MODELS = """
from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from licensing.models import Organization

class Ticket(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        WAITING_USER = 'waiting_user', 'Waiting on User'
        WAITING_INTERNAL = 'waiting_internal', 'Waiting Internal'
        RESOLVED = 'resolved', 'Resolved'
        CLOSED = 'closed', 'Closed'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        NORMAL = 'normal', 'Normal'
        HIGH = 'high', 'High'
        URGENT = 'urgent', 'Urgent'

    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.NORMAL)
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submitted_tickets')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')

class TicketComment(UUIDModel, TimeStampedModel):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    is_internal = models.BooleanField(default=False)
"""

SUPPORT_VIEWS = """
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import Ticket, TicketComment

class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketCommentSerializer(ModelSerializer):
    class Meta:
        model = TicketComment
        fields = '__all__'

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

class TicketCommentViewSet(viewsets.ModelViewSet):
    queryset = TicketComment.objects.all()
    serializer_class = TicketCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

SUPPORT_URLS = """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, TicketCommentViewSet

app_name = 'support'
router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'comments', TicketCommentViewSet, basename='comment')

urlpatterns = [path('', include(router.urls))]
"""

# ----------------- BILLING -----------------
BILLING_MODELS = """
from django.db import models
from core.models import UUIDModel, TimeStampedModel
from licensing.models import Organization

class Plan(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_projects = models.IntegerField(default=1)

class Subscription(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        CANCELED = 'canceled', 'Canceled'
        PAST_DUE = 'past_due', 'Past Due'

    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.RESTRICT)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    current_period_end = models.DateTimeField()

class Invoice(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        ISSUED = 'issued', 'Issued'
        PAID = 'paid', 'Paid'
        VOID = 'void', 'Void'

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    due_date = models.DateField()
"""

BILLING_VIEWS = """
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import Plan, Subscription, Invoice

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

BILLING_URLS = """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanViewSet, SubscriptionViewSet, InvoiceViewSet

app_name = 'billing'
router = DefaultRouter()
router.register(r'plans', PlanViewSet, basename='plan')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'invoices', InvoiceViewSet, basename='invoice')

urlpatterns = [path('', include(router.urls))]
"""

# ----------------- STORAGE PLATFORM -----------------
STORAGE_MODELS = """
from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel

class StorageObject(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=100, default='local')
    path = models.CharField(max_length=1024)
    size_bytes = models.BigIntegerField(default=0)
    content_type = models.CharField(max_length=100, blank=True)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
"""

STORAGE_VIEWS = """
from rest_framework import viewsets, permissions
from rest_framework.serializers import ModelSerializer
from .models import StorageObject

class StorageObjectSerializer(ModelSerializer):
    class Meta:
        model = StorageObject
        fields = '__all__'

class StorageObjectViewSet(viewsets.ModelViewSet):
    queryset = StorageObject.objects.all()
    serializer_class = StorageObjectSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

STORAGE_URLS = """
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StorageObjectViewSet

app_name = 'storage_platform'
router = DefaultRouter()
router.register(r'objects', StorageObjectViewSet, basename='storageobject')

urlpatterns = [path('', include(router.urls))]
"""

# ----------------- EXECUTION -----------------
apps = {
    'knowledge': (KNOWLEDGE_MODELS, KNOWLEDGE_VIEWS, KNOWLEDGE_URLS),
    'incidents': (INCIDENTS_MODELS, INCIDENTS_VIEWS, INCIDENTS_URLS),
    'support': (SUPPORT_MODELS, SUPPORT_VIEWS, SUPPORT_URLS),
    'billing': (BILLING_MODELS, BILLING_VIEWS, BILLING_URLS),
    'storage_platform': (STORAGE_MODELS, STORAGE_VIEWS, STORAGE_URLS),
}

for app_name, (models_content, views_content, urls_content) in apps.items():
    base = os.path.join(r"c:\\Users\\admin\\Documents\\TrainPlex\\CodeVault", app_name)
    write_file(os.path.join(base, "models.py"), models_content.strip())
    write_file(os.path.join(base, "views.py"), views_content.strip())
    write_file(os.path.join(base, "urls.py"), urls_content.strip())
    
print("All final phase apps scaffolded successfully.")

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from core.models import UUIDModel, TimeStampedModel, SoftDeleteModel
from django.utils.translation import gettext_lazy as _
from developers.models import DeveloperProfile

class Category(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(UUIDModel, TimeStampedModel, SoftDeleteModel):
    class State(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        SUBMITTED = 'submitted', _('Submitted')
        UNDER_REVIEW = 'under_review', _('Under Review')
        TECHNICAL_REVIEW = 'technical_review', _('Technical Review')
        COMPLIANCE_REVIEW = 'compliance_review', _('Compliance Review')
        APPROVED = 'approved', _('Approved')
        REJECTED = 'rejected', _('Rejected')

    class ProjectType(models.TextChoices):
        LIBRARY = 'library', _('Library/Package')
        FRAMEWORK = 'framework', _('Framework')
        APPLICATION = 'application', _('Application')
        SERVICE = 'service', _('Service/API')
        TOOL = 'tool', _('Developer Tool')
        OTHER = 'other', _('Other')

    class DevStatus(models.TextChoices):
        PLANNING = 'planning', _('Planning')
        PRE_ALPHA = 'pre_alpha', _('Pre-Alpha')
        ALPHA = 'alpha', _('Alpha')
        BETA = 'beta', _('Beta')
        PRODUCTION = 'production', _('Production/Stable')
        MAINTENANCE = 'maintenance', _('Maintenance')

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    primary_language = models.CharField(max_length=50)
    additional_languages = models.JSONField(default=list, blank=True)
    project_type = models.CharField(max_length=20, choices=ProjectType.choices, default=ProjectType.APPLICATION)
    current_version = models.CharField(max_length=50, blank=True)
    development_status = models.CharField(max_length=20, choices=DevStatus.choices, default=DevStatus.PLANNING)
    
    repository_url = models.URLField(blank=True)
    documentation_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    
    license_info = models.CharField(max_length=100, blank=True)
    approximate_loc = models.PositiveIntegerField(default=0)
    project_start_date = models.DateField(null=True, blank=True)
    last_development_date = models.DateField(null=True, blank=True)
    team_size = models.PositiveIntegerField(default=1)
    
    state = models.CharField(max_length=20, choices=State.choices, default=State.DRAFT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_projects')

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['state']),
            models.Index(fields=['category']),
            models.Index(fields=['primary_language']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            # We add some uniqueness to the slug to prevent collisions
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}-{self.id}" if self.id else base_slug
        super().save(*args, **kwargs)
        # If it was saved without ID, the slug might be plain. Resave if needed.
        if '-' not in self.slug and self.id:
            self.slug = f"{slugify(self.name)}-{str(self.id)[:8]}"
            super().save(update_fields=['slug'])

    def __str__(self):
        return self.name

class ProjectStateHistory(UUIDModel, TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='state_history')
    from_state = models.CharField(max_length=20, choices=Project.State.choices)
    to_state = models.CharField(max_length=20, choices=Project.State.choices)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    reason = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.project.name}: {self.from_state} -> {self.to_state}"

class OwnershipDeclaration(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        SIGNED = 'signed', _('Signed')
        REVOKED = 'revoked', _('Revoked')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='declarations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    declaration_text = models.TextField(help_text=_("The exact text the user agreed to"))
    declaration_version = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    signed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Declaration for {self.project.name} by {self.user.email}"

class ProjectContributor(UUIDModel, TimeStampedModel):
    class Role(models.TextChoices):
        OWNER = 'owner', _('Owner')
        CO_OWNER = 'co_owner', _('Co-Owner')
        DEVELOPER = 'developer', _('Developer')
        MAINTAINER = 'maintainer', _('Maintainer')
        REVIEWER = 'reviewer', _('Reviewer')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributors')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_contributions')
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.DEVELOPER)
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    contribution_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.email} - {self.get_role_display()} on {self.project.name}"

class ProjectDocument(UUIDModel, TimeStampedModel):
    class DocType(models.TextChoices):
        README = 'readme', _('README')
        ARCHITECTURE = 'architecture', _('Architecture Document')
        TECHNICAL = 'technical', _('Technical Documentation')
        API = 'api', _('API Documentation')
        INSTALLATION = 'installation', _('Installation Guide')
        DEPLOYMENT = 'deployment', _('Deployment Guide')
        DEPENDENCY = 'dependency', _('Dependency Documentation')
        TESTING = 'testing', _('Testing Documentation')
        OWNERSHIP = 'ownership', _('Ownership Declaration File')
        OTHER = 'other', _('Other')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DocType.choices, default=DocType.OTHER)
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='project_docs/')
    version = models.CharField(max_length=50, blank=True, default='1.0')
    is_public = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.project.name} - {self.get_document_type_display()} ({self.title})"

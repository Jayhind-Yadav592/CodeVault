from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project
from reviews.models import ReviewCase
from django.utils.text import slugify

class Tag(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class MarketplaceListing(UUIDModel, TimeStampedModel):
    class Visibility(models.TextChoices):
        PRIVATE = 'private', _('Private')
        UNLISTED = 'unlisted', _('Unlisted')
        PUBLIC = 'public', _('Public')

    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PENDING_PUBLICATION = 'pending_publication', _('Pending Publication')
        PUBLISHED = 'published', _('Published')
        PAUSED = 'paused', _('Paused')
        UNPUBLISHED = 'unpublished', _('Unpublished')
        ARCHIVED = 'archived', _('Archived')

    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='marketplace_listing')
    review_case = models.ForeignKey(ReviewCase, on_delete=models.SET_NULL, null=True, blank=True)
    
    visibility = models.CharField(max_length=20, choices=Visibility.choices, default=Visibility.PRIVATE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    
    tags = models.ManyToManyField(Tag, blank=True, related_name='listings')
    
    # Pre-computed Analytics / Metadata for quick sorting
    popularity_score = models.DecimalField(max_digits=10, decimal_places=4, default=0.0)
    views_count = models.PositiveIntegerField(default=0)
    saves_count = models.PositiveIntegerField(default=0)
    
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Listing: {self.project.name} ({self.status})"

class SavedProject(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='saved_projects')
    listing = models.ForeignKey(MarketplaceListing, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    folder = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('user', 'listing')

class Watchlist(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='watchlist')
    listing = models.ForeignKey(MarketplaceListing, on_delete=models.CASCADE)
    
    notify_on_update = models.BooleanField(default=True)
    notify_on_license_change = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'listing')

class SearchQueryLog(UUIDModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    query_text = models.CharField(max_length=255)
    filters = models.JSONField(default=dict)
    result_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"Search: {self.query_text} ({self.result_count} results)"

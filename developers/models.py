from django.db import models
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from django.utils.translation import gettext_lazy as _

class DeveloperProfile(UUIDModel, TimeStampedModel):
    class DeveloperType(models.TextChoices):
        INDIVIDUAL = 'individual', _('Individual Developer')
        COMPANY = 'company', _('Company / Startup')
        STUDENT = 'student', _('Student')
        HOBBYIST = 'hobbyist', _('Hobbyist')
        OTHER = 'other', _('Other')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='developer_profile'
    )
    display_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True, max_length=1000)
    country = models.CharField(max_length=100, blank=True)
    developer_type = models.CharField(max_length=20, choices=DeveloperType.choices, default=DeveloperType.INDIVIDUAL)
    website = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    skills = models.JSONField(default=list, blank=True, help_text=_("List of technical skills"))
    languages = models.JSONField(default=list, blank=True, help_text=_("List of programming languages"))
    years_of_experience = models.PositiveIntegerField(default=0)
    company_name = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = _('developer profile')
        verbose_name_plural = _('developer profiles')

    def __str__(self):
        return f"{self.display_name or self.user.email}'s Profile"

    @property
    def completion_percentage(self):
        fields = [
            self.display_name,
            self.bio,
            self.country,
            self.website,
            self.github_url,
            self.linkedin_url,
            self.skills,
            self.languages,
            self.years_of_experience > 0,
            self.company_name
        ]
        completed = sum(1 for field in fields if field)
        return int((completed / len(fields)) * 100)

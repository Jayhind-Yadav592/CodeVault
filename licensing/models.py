from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from core.models import UUIDModel, TimeStampedModel
from projects.models import Project
from reviews.models import ReviewCase

class Organization(UUIDModel, TimeStampedModel):
    class OrgType(models.TextChoices):
        STARTUP = 'startup', _('Startup')
        ENTERPRISE = 'enterprise', _('Enterprise')
        RESEARCH_ORGANIZATION = 'research_org', _('Research Organization')
        UNIVERSITY = 'university', _('University')
        INDIVIDUAL = 'individual', _('Individual')
        OTHER = 'other', _('Other')

    class VerificationStatus(models.TextChoices):
        NOT_STARTED = 'not_started', _('Not Started')
        PENDING = 'pending', _('Pending')
        UNDER_REVIEW = 'under_review', _('Under Review')
        VERIFIED = 'verified', _('Verified')
        REJECTED = 'rejected', _('Rejected')
        EXPIRED = 'expired', _('Expired')

    name = models.CharField(max_length=255)
    org_type = models.CharField(max_length=20, choices=OrgType.choices, default=OrgType.OTHER)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=100)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)
    
    verification_status = models.CharField(max_length=20, choices=VerificationStatus.choices, default=VerificationStatus.NOT_STARTED)
    verification_notes = models.TextField(blank=True)
    verified_date = models.DateTimeField(null=True, blank=True)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organizations')
    
    def __str__(self):
        return f"{self.name} ({self.get_verification_status_display()})"

class LicenseType(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    is_commercial = models.BooleanField(default=False)
    default_duration_days = models.IntegerField(default=365)
    
    def __str__(self):
        return self.name

class LicenseProduct(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        AVAILABLE = 'available', _('Available')
        UNDER_NEGOTIATION = 'under_negotiation', _('Under Negotiation')
        LICENSED = 'licensed', _('Licensed')
        SUSPENDED = 'suspended', _('Suspended')
        EXPIRED = 'expired', _('Expired')
        RETIRED = 'retired', _('Retired')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='license_products')
    approved_review_case = models.ForeignKey(ReviewCase, on_delete=models.RESTRICT)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    available_types = models.ManyToManyField(LicenseType)
    
    def __str__(self):
        return f"{self.project.name} Product"

class LicenseRequest(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        SUBMITTED = 'submitted', _('Submitted')
        UNDER_REVIEW = 'under_review', _('Under Review')
        NEGOTIATION = 'negotiation', _('Negotiation')
        TERMS_AGREED = 'terms_agreed', _('Terms Agreed')
        AGREEMENT_PENDING = 'agreement_pending', _('Agreement Pending')
        SIGNED = 'signed', _('Signed')
        ACTIVE = 'active', _('Active')
        REJECTED = 'rejected', _('Rejected')
        CANCELLED = 'cancelled', _('Cancelled')
        EXPIRED = 'expired', _('Expired')
        TERMINATED = 'terminated', _('Terminated')

    product = models.ForeignKey(LicenseProduct, on_delete=models.CASCADE, related_name='requests')
    organization = models.ForeignKey(Organization, on_delete=models.RESTRICT)
    requested_type = models.ForeignKey(LicenseType, on_delete=models.RESTRICT)
    status = models.CharField(max_length=30, choices=Status.choices, default=Status.DRAFT)
    
    intended_usage = models.TextField()
    requested_duration_days = models.IntegerField(default=365)
    
    def __str__(self):
        return f"Req {self.id} for {self.product.project.name} by {self.organization.name}"

class LicenseTerms(UUIDModel, TimeStampedModel):
    class PricingType(models.TextChoices):
        FIXED = 'fixed', _('Fixed')
        PERIODIC = 'periodic', _('Periodic')
        USAGE_BASED = 'usage_based', _('Usage Based')
        NEGOTIATED = 'negotiated', _('Negotiated')
        CUSTOM = 'custom', _('Custom')

    request = models.ForeignKey(LicenseRequest, on_delete=models.CASCADE, related_name='terms_versions')
    version = models.IntegerField(default=1)
    
    pricing_type = models.CharField(max_length=20, choices=PricingType.choices, default=PricingType.FIXED)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default='USD')
    
    is_commercial = models.BooleanField(default=False)
    ai_training_permitted = models.BooleanField(default=False)
    redistribution_permitted = models.BooleanField(default=False)
    modification_permitted = models.BooleanField(default=False)
    
    duration_days = models.IntegerField(default=365)
    
    is_accepted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('request', 'version')

class NegotiationProposal(UUIDModel, TimeStampedModel):
    request = models.ForeignKey(LicenseRequest, on_delete=models.CASCADE, related_name='proposals')
    terms = models.ForeignKey(LicenseTerms, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    is_counter = models.BooleanField(default=False)

class Agreement(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        DRAFT = 'draft', _('Draft')
        PENDING_SIGNATURE = 'pending_signature', _('Pending Signature')
        PARTIALLY_SIGNED = 'partially_signed', _('Partially Signed')
        FULLY_SIGNED = 'fully_signed', _('Fully Signed')
        ACTIVE = 'active', _('Active')
        EXPIRED = 'expired', _('Expired')
        TERMINATED = 'terminated', _('Terminated')

    request = models.OneToOneField(LicenseRequest, on_delete=models.CASCADE, related_name='agreement')
    terms = models.ForeignKey(LicenseTerms, on_delete=models.RESTRICT)
    version = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    effective_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

class SignatureRequest(UUIDModel, TimeStampedModel):
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending')
        SIGNED = 'signed', _('Signed')
        DECLINED = 'declined', _('Declined')

    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='signatures')
    signer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    signed_at = models.DateTimeField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

class LicenseUsageEvent(UUIDModel, TimeStampedModel):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, related_name='usage_events')
    metric_name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    reported_at = models.DateTimeField(auto_now_add=True)

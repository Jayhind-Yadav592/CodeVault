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
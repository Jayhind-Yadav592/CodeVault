from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet, LicenseProductViewSet,
    LicenseRequestViewSet, AgreementViewSet
)

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet, basename='organization')
router.register(r'products', LicenseProductViewSet, basename='product')
router.register(r'requests', LicenseRequestViewSet, basename='request')
router.register(r'agreements', AgreementViewSet, basename='agreement')

app_name = 'licensing'

urlpatterns = [
    path('', include(router.urls)),
]

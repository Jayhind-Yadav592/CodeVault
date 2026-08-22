from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketplaceListingViewSet, SavedProjectViewSet, WatchlistViewSet, PublicProfileViewSet

app_name = 'marketplace'

router = DefaultRouter()
router.register(r'listings', MarketplaceListingViewSet, basename='listing')
router.register(r'saved', SavedProjectViewSet, basename='saved')
router.register(r'watchlist', WatchlistViewSet, basename='watchlist')
router.register(r'profiles', PublicProfileViewSet, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]

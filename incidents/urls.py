from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncidentViewSet, IncidentEventViewSet, PostmortemViewSet

app_name = 'incidents'
router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')
router.register(r'events', IncidentEventViewSet, basename='event')
router.register(r'postmortems', PostmortemViewSet, basename='postmortem')

urlpatterns = [path('', include(router.urls))]
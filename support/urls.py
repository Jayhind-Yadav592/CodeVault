from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet, TicketCommentViewSet

app_name = 'support'
router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'comments', TicketCommentViewSet, basename='comment')

urlpatterns = [path('', include(router.urls))]
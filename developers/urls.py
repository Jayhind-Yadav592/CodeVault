from django.urls import path
from .views import DeveloperProfileView, DashboardStatsView

app_name = 'developers'

urlpatterns = [
    path('profile/', DeveloperProfileView.as_view(), name='profile'),
    path('dashboard/stats/', DashboardStatsView.as_view(), name='dashboard_stats'),
]

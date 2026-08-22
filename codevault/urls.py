from django.contrib import admin
from django.urls import path, include
from core.views import home, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/v1/developers/', include('developers.urls', namespace='developers')),
    path('api/v1/projects/', include('projects.urls', namespace='projects')),
    path('api/v1/repositories/', include('repositories.urls', namespace='repositories')),
    path('api/v1/notifications/', include('notifications.urls', namespace='notifications')),
]

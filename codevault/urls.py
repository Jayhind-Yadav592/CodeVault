from django.contrib import admin
from django.urls import path, include
from core.views import home, dashboard, project_compliance, project_repository, project_security, project_reviews, reviewer_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('reviewer/', reviewer_dashboard, name='reviewer_dashboard'),
    path('project/<uuid:project_id>/compliance/', project_compliance, name='project_compliance'),
    path('project/<uuid:project_id>/repository/', project_repository, name='project_repository'),
    path('project/<uuid:project_id>/security/', project_security, name='project_security'),
    path('project/<uuid:project_id>/reviews/', project_reviews, name='project_reviews'),
    path('api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/v1/developers/', include('developers.urls', namespace='developers')),
    path('api/v1/projects/', include('projects.urls', namespace='projects')),
    path('api/v1/repositories/', include('repositories.urls', namespace='repositories')),
    path('api/v1/compliance/', include('compliance.urls', namespace='compliance')),
    path('api/v1/security/', include('security.urls', namespace='security')),
    path('api/v1/reviews/', include('reviews.urls', namespace='reviews')),
    path('api/v1/notifications/', include('notifications.urls', namespace='notifications')),
]

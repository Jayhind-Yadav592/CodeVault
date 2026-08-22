import pytest
from django.urls import reverse
from rest_framework import status
from .models import DeveloperProfile

@pytest.mark.django_db
class TestDeveloperAPI:
    def test_get_profile_creates_if_not_exists(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        assert DeveloperProfile.objects.count() == 0
        
        url = reverse('developers:profile')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert DeveloperProfile.objects.count() == 1

    def test_update_profile(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        url = reverse('developers:profile')
        data = {
            'display_name': 'Super Dev',
            'country': 'USA',
            'years_of_experience': 5
        }
        response = api_client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['display_name'] == 'Super Dev'
        assert response.data['completion_percentage'] > 0

    def test_dashboard_stats(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        url = reverse('developers:dashboard_stats')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'total_projects' in response.data
        assert 'profile_completion' in response.data

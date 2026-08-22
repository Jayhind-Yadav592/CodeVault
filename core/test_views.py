import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestWebViews:
    def test_home_page_unauthenticated(self, client):
        url = reverse('home')
        response = client.get(url)
        assert response.status_code == 200
        assert 'Welcome to CodeVault' in response.content.decode()

    def test_dashboard_redirects_if_unauthenticated(self, client):
        url = reverse('dashboard')
        response = client.get(url)
        assert response.status_code == 302 # Redirect to login

    def test_dashboard_authenticated(self, client, developer_user):
        client.force_login(developer_user)
        url = reverse('dashboard')
        response = client.get(url)
        assert response.status_code == 200
        assert 'Developer Dashboard' in response.content.decode()

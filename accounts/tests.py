import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

User = get_user_model()

@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(email='normal@user.com', password='foo')
        assert user.email == 'normal@user.com'
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        assert user.role == User.Role.DEVELOPER

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        assert admin_user.email == 'super@user.com'
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser
        assert admin_user.role == User.Role.ADMINISTRATOR

@pytest.mark.django_db
class TestAuthentication:
    def test_user_registration(self, api_client):
        url = reverse('accounts:register')
        data = {
            'email': 'newuser@example.com',
            'password': 'securepassword123',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(email='newuser@example.com').exists()

    def test_user_login(self, api_client, create_user):
        user = create_user(email='login@example.com', password='password123')
        url = reverse('accounts:login')
        data = {
            'email': 'login@example.com',
            'password': 'password123'
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_user_profile(self, api_client, create_user):
        user = create_user(email='profile@example.com', password='password123')
        # Login
        url = reverse('accounts:login')
        response = api_client.post(url, {'email': 'profile@example.com', 'password': 'password123'})
        access_token = response.data['access']
        
        # Get profile
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        profile_url = reverse('accounts:profile')
        response = api_client.get(profile_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['email'] == 'profile@example.com'

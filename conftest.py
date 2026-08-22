import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def make_user(**kwargs):
        kwargs.setdefault('password', 'testpass123')
        if 'email' not in kwargs:
            kwargs['email'] = 'test@example.com'
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def developer_user(create_user):
    return create_user(email='dev@example.com', role=User.Role.DEVELOPER)

@pytest.fixture
def reviewer_user(create_user):
    return create_user(email='reviewer@example.com', role=User.Role.REVIEWER)

@pytest.fixture
def admin_user(create_user):
    return create_user(email='admin@example.com', role=User.Role.ADMINISTRATOR, is_staff=True, is_superuser=True)

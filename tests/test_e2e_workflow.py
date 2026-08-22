import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from projects.models import Category, Project

User = get_user_model()

@pytest.fixture
def workflow_setup(db):
    dev = User.objects.create_user(email='dev@example.com', password='pw')
    admin = User.objects.create_superuser(email='admin@example.com', password='pw')
    cat = Category.objects.create(name='Security Tools', slug='sec-tools')
    return dev, admin, cat

@pytest.mark.django_db(transaction=True)
def test_full_project_lifecycle(workflow_setup):
    dev, admin, cat = workflow_setup
    
    dev_client = APIClient()
    dev_client.force_authenticate(user=dev)
    
    admin_client = APIClient()
    admin_client.force_authenticate(user=admin)
    
    # 1. Developer creates a project
    proj_url = reverse('projects:project-list')
    resp = dev_client.post(proj_url, {
        'name': 'Secure Vault App',
        'short_description': 'Test project',
        'category': cat.id,
        'primary_language': 'Python',
        'development_status': 'production',
        'project_type': 'library',
        'full_description': 'This is a long description.',
        'requires_attribution': True
    }, format='json')
    
    assert resp.status_code == status.HTTP_201_CREATED, resp.data
    project_id = resp.data['id']
    
    # 2. Add an ownership declaration
    decl_url = reverse('projects:declaration-list')
    resp = dev_client.post(decl_url, {
        'project': project_id,
        'declaration_text': 'I hereby declare I wrote this code.',
        'declaration_version': '1.0'
    }, format='json')
    assert resp.status_code == status.HTTP_201_CREATED
    
    # 3. Submit project
    submit_url = reverse('projects:project-submit', args=[project_id])
    resp = dev_client.post(submit_url, format='json')
    assert resp.status_code == status.HTTP_200_OK
    
    # Verify state updated
    resp = dev_client.get(f"{proj_url}{project_id}/")
    assert resp.data['state'] == 'submitted'
    
    # In a fully integrated flow, this would trigger review assignment,
    # compliance checks, repository scanning, and then approval.
    
    # Here we simulate the end state by admin actions or service calls.

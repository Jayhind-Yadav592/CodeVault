import pytest
from django.urls import reverse
from rest_framework import status
from .models import Category, Project, OwnershipDeclaration

@pytest.mark.django_db
class TestProjectModels:
    def test_category_slug_generation(self):
        category = Category.objects.create(name='Test Category')
        assert category.slug == 'test-category'

    def test_project_slug_generation(self, developer_user):
        category = Category.objects.create(name='Test')
        project = Project.objects.create(
            name='My Awesome Project',
            short_description='Test',
            full_description='Test',
            primary_language='Python',
            owner=developer_user,
            category=category
        )
        assert project.slug.startswith('my-awesome-project')

@pytest.mark.django_db
class TestProjectAPI:
    def test_create_project(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        category = Category.objects.create(name='Test')
        
        url = reverse('projects:project-list')
        data = {
            'name': 'API Project',
            'short_description': 'Test',
            'full_description': 'Test',
            'primary_language': 'Python',
            'category': category.id
        }
        
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Project.objects.count() == 1

    def test_submit_project_fails_without_declaration(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        project = Project.objects.create(
            name='Submit Me', short_description='Test', full_description='Test',
            primary_language='Python', owner=developer_user
        )
        
        url = reverse('projects:project-submit', args=[project.id])
        response = api_client.post(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'declaration is required' in response.data['error']

    def test_submit_project_succeeds_with_declaration(self, api_client, developer_user):
        api_client.force_authenticate(user=developer_user)
        project = Project.objects.create(
            name='Submit Me 2', short_description='Test', full_description='Test',
            primary_language='Python', owner=developer_user
        )
        
        # Add declaration
        OwnershipDeclaration.objects.create(
            project=project, user=developer_user,
            declaration_text='I own this', declaration_version='1.0',
            status=OwnershipDeclaration.Status.SIGNED
        )
        
        url = reverse('projects:project-submit', args=[project.id])
        response = api_client.post(url)
        assert response.status_code == status.HTTP_200_OK
        
        project.refresh_from_db()
        assert project.state == Project.State.SUBMITTED

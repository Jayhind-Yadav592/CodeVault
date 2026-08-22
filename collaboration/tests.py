import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from licensing.models import Organization
from projects.models import Project
from .models import (
    OrganizationMember, ProjectTeamMember, ProjectTask, 
    ProjectDiscussion, ActivityEvent
)

User = get_user_model()

@pytest.fixture
def collabo_setup(db):
    owner = User.objects.create_user(email='owner@test.com', password='pw')
    member = User.objects.create_user(email='member@test.com', password='pw')
    outsider = User.objects.create_user(email='outsider@test.com', password='pw')
    
    org = Organization.objects.create(name='Acme Corp', owner=owner)
    OrganizationMember.objects.create(organization=org, user=owner, role=OrganizationMember.Role.OWNER)
    OrganizationMember.objects.create(organization=org, user=member, role=OrganizationMember.Role.MEMBER)
    
    project = Project.objects.create(name='Titan', owner=owner)
    ProjectTeamMember.objects.create(project=project, user=owner, role=ProjectTeamMember.Role.OWNER)
    ProjectTeamMember.objects.create(project=project, user=member, role=ProjectTeamMember.Role.DEVELOPER)
    
    return {
        'owner': owner,
        'member': member,
        'outsider': outsider,
        'org': org,
        'project': project
    }

@pytest.mark.django_db
def test_organization_permissions(collabo_setup):
    client = APIClient()
    url = reverse('collaboration:org-members-list', kwargs={'org_pk': collabo_setup['org'].pk})
    
    # 1. Owner should be able to view members
    client.force_authenticate(user=collabo_setup['owner'])
    resp = client.get(url)
    assert resp.status_code == 200
    assert len(resp.data['results']) == 2
    
    # 2. Member should NOT be able to view (only Admin/Owner per IsOrganizationAdmin)
    client.force_authenticate(user=collabo_setup['member'])
    resp = client.get(url)
    assert resp.status_code == 403
    
    # 3. Outsider should NOT be able to view
    client.force_authenticate(user=collabo_setup['outsider'])
    resp = client.get(url)
    assert resp.status_code == 403

@pytest.mark.django_db
def test_project_task_creation_and_activity_logging(collabo_setup):
    client = APIClient()
    url = reverse('collaboration:project-task-list', kwargs={'project_pk': collabo_setup['project'].pk})
    
    client.force_authenticate(user=collabo_setup['member'])
    payload = {
        'title': 'Implement API',
        'description': 'Build the core endpoints'
    }
    resp = client.post(url, payload)
    
    assert resp.status_code == 201
    assert ProjectTask.objects.count() == 1
    
    # Verify ActivityEvent was logged
    event = ActivityEvent.objects.first()
    assert event.event_type == 'task_created'
    assert event.actor == collabo_setup['member']

@pytest.mark.django_db
def test_project_discussion_idor_protection(collabo_setup):
    client = APIClient()
    url = reverse('collaboration:project-discussion-list', kwargs={'project_pk': collabo_setup['project'].pk})
    
    client.force_authenticate(user=collabo_setup['owner'])
    client.post(url, {'title': 'Secret Architecture', 'body': 'Top secret plans'})
    
    # Outsider tries to read it
    client.force_authenticate(user=collabo_setup['outsider'])
    resp = client.get(url)
    
    # Should block completely since outsider isn't a ProjectTeamMember
    assert resp.status_code == 403

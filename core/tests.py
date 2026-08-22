import pytest
from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.permissions import IsDeveloper, IsReviewer, IsAdministrator

class MockDeveloperAPI(APIView):
    permission_classes = [IsDeveloper]
    def get(self, request):
        return Response({"message": "developer access"})

class MockReviewerAPI(APIView):
    permission_classes = [IsReviewer]
    def get(self, request):
        return Response({"message": "reviewer access"})

class MockAdminAPI(APIView):
    permission_classes = [IsAdministrator]
    def get(self, request):
        return Response({"message": "admin access"})

urlpatterns = [
    path('test-dev/', MockDeveloperAPI.as_view()),
    path('test-rev/', MockReviewerAPI.as_view()),
    path('test-adm/', MockAdminAPI.as_view()),
]

@pytest.mark.django_db
@pytest.mark.urls(__name__)
class TestPermissions:
    def test_developer_access(self, api_client, developer_user, reviewer_user):
        # Developer user accessing dev endpoint
        api_client.force_authenticate(user=developer_user)
        response = api_client.get('/test-dev/')
        assert response.status_code == status.HTTP_200_OK

        # Reviewer user accessing dev endpoint (should fail)
        api_client.force_authenticate(user=reviewer_user)
        response = api_client.get('/test-dev/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_reviewer_access(self, api_client, reviewer_user, developer_user):
        api_client.force_authenticate(user=reviewer_user)
        response = api_client.get('/test-rev/')
        assert response.status_code == status.HTTP_200_OK

        api_client.force_authenticate(user=developer_user)
        response = api_client.get('/test-rev/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_admin_access(self, api_client, admin_user, developer_user):
        api_client.force_authenticate(user=admin_user)
        response = api_client.get('/test-adm/')
        assert response.status_code == status.HTTP_200_OK

        api_client.force_authenticate(user=developer_user)
        response = api_client.get('/test-adm/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

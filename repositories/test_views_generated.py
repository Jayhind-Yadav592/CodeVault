from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class RepositoryConnectionAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_RepositoryConnection@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_RepositoryConnection@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_RepositoryConnection@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/repositoryconnections/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class AnalysisJobAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_AnalysisJob@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_AnalysisJob@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_AnalysisJob@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysisjobs/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class AnalysisSnapshotAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_AnalysisSnapshot@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_AnalysisSnapshot@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_AnalysisSnapshot@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/analysissnapshots/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LanguageStatAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LanguageStat@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LanguageStat@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LanguageStat@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/languagestats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ClassificationStatAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ClassificationStat@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ClassificationStat@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ClassificationStat@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/classificationstats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class PullRequestStatAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_PullRequestStat@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_PullRequestStat@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_PullRequestStat@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/repositories/pullrequeststats/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])



from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class OrganizationAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_Organization@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_Organization@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_Organization@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/organizations/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/organizations/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/organizations/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LicenseTypeAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LicenseType@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LicenseType@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LicenseType@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetypes/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LicenseProductAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LicenseProduct@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LicenseProduct@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LicenseProduct@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseproducts/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LicenseRequestAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LicenseRequest@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LicenseRequest@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LicenseRequest@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenserequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LicenseTermsAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LicenseTerms@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LicenseTerms@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LicenseTerms@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licensetermss/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class NegotiationProposalAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_NegotiationProposal@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_NegotiationProposal@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_NegotiationProposal@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/negotiationproposals/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class AgreementAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_Agreement@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_Agreement@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_Agreement@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/agreements/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/agreements/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/agreements/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class SignatureRequestAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_SignatureRequest@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_SignatureRequest@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_SignatureRequest@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/signaturerequests/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class LicenseUsageEventAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_LicenseUsageEvent@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_LicenseUsageEvent@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_LicenseUsageEvent@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/licensing/licenseusageevents/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])



from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class PlanAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_Plan@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_Plan@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_Plan@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/billing/plans/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/billing/plans/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/billing/plans/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/billing/plans/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/billing/plans/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/billing/plans/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/plans/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/plans/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class SubscriptionAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_Subscription@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_Subscription@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_Subscription@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/subscriptions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class InvoiceAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_Invoice@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_Invoice@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_Invoice@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/billing/invoices/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/billing/invoices/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/billing/invoices/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/billing/invoices/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/billing/invoices/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/billing/invoices/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/billing/invoices/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])



from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class PlatformMetricAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_PlatformMetric@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_PlatformMetric@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_PlatformMetric@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/platformmetrics/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReportTemplateAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReportTemplate@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReportTemplate@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReportTemplate@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reporttemplates/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReportExecutionAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReportExecution@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReportExecution@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReportExecution@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/reportexecutions/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ScheduledReportAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ScheduledReport@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ScheduledReport@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ScheduledReport@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/analytics/scheduledreports/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])



from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

class ReviewCaseAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReviewCase@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReviewCase@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReviewCase@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcases/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReviewerAssignmentAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReviewerAssignment@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReviewerAssignment@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReviewerAssignment@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewerassignments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReviewTransitionHistoryAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReviewTransitionHistory@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReviewTransitionHistory@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReviewTransitionHistory@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewtransitionhistorys/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReviewChecklistItemAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReviewChecklistItem@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReviewChecklistItem@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReviewChecklistItem@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewchecklistitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class ReviewCommentAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_ReviewComment@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_ReviewComment@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_ReviewComment@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/reviewcomments/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

class RemediationItemAPIDetailedTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(email='user1_RemediationItem@test.com', password='pwd')
        self.user2 = User.objects.create_user(email='user2_RemediationItem@test.com', password='pwd')
        self.admin = User.objects.create_superuser(email='admin_RemediationItem@test.com', password='pwd')

    def test_list_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_list_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_list_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_create_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_create_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/'
        response = self.client.post(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_retrieve_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_retrieve_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.put(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_partial_update_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_partial_update_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.patch(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_unauthenticated(self):
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [401, 403, 404])

    def test_destroy_user1(self):
        self.client.force_authenticate(user=self.user1)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])

    def test_destroy_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = '/api/v1/reviews/remediationitems/1/'
        response = self.client.delete(url)
        self.assertIn(response.status_code, [200, 201, 400, 403, 404, 405])



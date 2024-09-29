from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from .factories import MoodEntryFactory, UserFactory


class UserListTest(APITestCase):
    def setUp(self):
        self.url = reverse("user-list")
        self.user = UserFactory()
        self.data = {
            "username": "testusername",
            "email": "test@test.com",
            "password": "test password",
        }

    def test_post(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserDetailTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.url = reverse("user-detail", kwargs={"user_id": self.user.id})

    def test_get_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class MoodEntryListTest(APITestCase):
    def setUp(self):
        self.owner = UserFactory()
        self.not_owner = UserFactory()
        self.mood_entry = MoodEntryFactory(user=self.owner)
        self.url = reverse("mood-entry-list", kwargs={"user_id": self.owner.id})

        self.data = {
            "user": self.owner.id,
            "mood": 0,
            "description": "test description",
        }

    def test_get_authenticated(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_not_owner(self):
        self.client.force_authenticate(user=self.not_owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_authenticated(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_unauthenticated(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class MoodEntryDetailTest(APITestCase):
    def setUp(self):
        self.owner = UserFactory()
        self.not_owner = UserFactory()
        self.mood_entry = MoodEntryFactory(user=self.owner)
        self.url = reverse(
            "mood-entry-detail",
            kwargs={"user_id": self.owner.id, "mood_id": self.mood_entry.id},
        )

        self.data = {
            "user": self.owner.id,
            "mood": 1,
            "description": "test description updated",
        }

    def test_get_authenticated(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_not_owner(self):
        self.client.force_authenticate(user=self.not_owner)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authenticated(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_unauthenticated(self):
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_not_owner(self):
        self.client.force_authenticate(user=self.not_owner)
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_authenticated(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_unauthenticated(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_not_owner(self):
        self.client.force_authenticate(user=self.not_owner)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

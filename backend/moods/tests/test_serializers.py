from django.test import TestCase

from rest_framework.serializers import ValidationError
from .factories import MoodEntryFactory, UserFactory
from moods.serializers import (
    MoodEntrySerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)


class UserPrivateSerializerTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.serializer = UserPrivateSerializer(instance=self.user)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(set(self.data.keys()), {"id", "username", "email"})

    def test_id_field_content(self):
        self.assertEqual(self.data["id"], self.user.id)

    def test_username_field_content(self):
        self.assertEqual(self.data["username"], self.user.username)

    def test_email_field_content(self):
        self.assertEqual(self.data["email"], self.user.email)


class UserPublicSerializerTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.serializer = UserPublicSerializer(instance=self.user)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(set(self.data.keys()), {"id", "username"})

    def test_id_field_content(self):
        self.assertEqual(self.data["id"], self.user.id)

    def test_username_field_content(self):
        self.assertEqual(self.data["username"], self.user.username)


class MoodEntrySerializerTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.mood_entry = MoodEntryFactory(user=self.user)
        self.serializer = MoodEntrySerializer(instance=self.mood_entry)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            set(self.data.keys()),
            {"id", "user", "mood", "mood_display", "date", "description"},
        )

    def test_id_field_content(self):
        self.assertEqual(self.data["id"], self.mood_entry.id)

    def test_user_field_content(self):
        self.assertEqual(self.data["user"], self.mood_entry.user.id)

    def test_mood_field_content(self):
        self.assertEqual(self.data["mood"], self.mood_entry.mood)

    def test_mood_display_field_content(self):
        self.assertEqual(self.data["mood_display"], self.mood_entry.get_mood_display())

    def test_date_field_content(self):
        formatted_date = self.mood_entry.date.isoformat().replace("+00:00", "Z")
        self.assertEqual(self.data["date"], formatted_date)

    def test_description_field_content(self):
        self.assertEqual(self.data["description"], self.mood_entry.description)

    def test_validate(self):
        mood_entry = MoodEntryFactory()
        duplicate_data = {
            "mood": mood_entry.mood,
            "user": mood_entry.user.id,
            "date": mood_entry.date.isoformat(),
        }
        serializer = MoodEntrySerializer(data=duplicate_data)
        self.assertFalse(serializer.is_valid())

        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
            serializer.save()

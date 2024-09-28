from django.test import TestCase
from .factories import MoodEntryFactory


class MoodEntryModelTest(TestCase):
    def setUp(self):
        self.mood = MoodEntryFactory()

    def test_str(self):
        self.assertEqual(
            str(self.mood),
            f"{self.mood.user.username} on {self.mood.date}: {self.mood.get_mood_display()}",
        )

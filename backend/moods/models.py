from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class MoodChoices(models.IntegerChoices):
    AWFUL = -2, "Awful"
    bad = -1, "Bad"
    fine = 0, "Fine"
    good = 1, "Good"
    amazing = 2, "Amazing"


class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="days")
    mood = models.IntegerField(choices=MoodChoices.choices)
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} on {self.date}: {self.get_mood_display()}"

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now().date()
        super().save(*args, **kwargs)

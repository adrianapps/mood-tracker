from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory
from moods.models import MoodEntry, MoodChoices


class UserFactory(DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")

    class Meta:
        model = User


class MoodEntryFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    mood = factory.Iterator([choice[0] for choice in MoodChoices.choices])
    description = factory.Faker("text")
    date = factory.Faker("date_this_decade")

    class Meta:
        model = MoodEntry

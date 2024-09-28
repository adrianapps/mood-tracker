# Generated by Django 5.1.1 on 2024-09-22 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moods", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MoodEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mood",
                    models.IntegerField(
                        choices=[
                            (-2, "Awful"),
                            (-1, "Bad"),
                            (0, "Fine"),
                            (1, "Good"),
                            (2, "Amazing"),
                        ]
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("description", models.TextField(blank=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="days",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Day",
        ),
    ]

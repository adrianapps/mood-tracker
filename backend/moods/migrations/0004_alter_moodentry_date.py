# Generated by Django 5.1.1 on 2024-10-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moods', '0003_alter_moodentry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]

from django.contrib.auth.models import User
from rest_framework import serializers

from moods.models import MoodEntry


class UserPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class MoodEntrySerializer(serializers.ModelSerializer):
    mood_display = serializers.SerializerMethodField()

    class Meta:
        model = MoodEntry
        fields = ["id", "user", "mood", "mood_display", "date", "description"]

    def get_mood_display(self, obj):
        return obj.get_mood_display()

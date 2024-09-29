from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from moods.models import MoodEntry
from moods.permissions import IsMoodEntryOwner
from .serializers import (
    MoodEntrySerializer,
    UserPublicSerializer,
    UserPrivateSerializer,
)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserPrivateSerializer
        return UserPublicSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPublicSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = "user_id"


class MoodEntryList(generics.ListCreateAPIView):
    serializer_class = MoodEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsMoodEntryOwner]

    def get_queryset(self):
        queryset = MoodEntry.objects.select_related("user")
        user_id = self.kwargs.get("user_id")
        return queryset.filter(user__id=user_id)


class MoodEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoodEntrySerializer
    lookup_url_kwarg = "mood_id"
    permission_classes = [permissions.IsAuthenticated, IsMoodEntryOwner]

    def get_queryset(self):
        queryset = MoodEntry.objects.select_related("user")
        user_id = self.kwargs.get("user_id")
        return queryset.filter(user__id=user_id)

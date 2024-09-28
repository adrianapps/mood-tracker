from django.urls import path

from moods.views import MoodEntryDetail, MoodEntryList, UserCreate, UserDetail


urlpatterns = [
    path("users/", UserCreate.as_view(), name="register"),
    path("users/<int:user_id>/", UserDetail.as_view(), name="user-detail"),
    path("users/<int:user_id>/moods/", MoodEntryList.as_view(), name="mood-entry-list"),
    path(
        "users/<int:user_id>/moods/<int:mood_id>/",
        MoodEntryDetail.as_view(),
        name="mood-entry-detail",
    ),
]

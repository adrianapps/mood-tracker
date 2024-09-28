from rest_framework import permissions


class IsMoodEntryOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs.get("user_id")
        return request.user.id == int(user_id)

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

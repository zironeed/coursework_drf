from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

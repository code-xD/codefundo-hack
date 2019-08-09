from rest_framework import permissions
from django.contrib.auth.models import User


class IsAdminOrLoggedIn(permissions.BasePermission):

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            if request.user in User.objects.all():
                return True
                # Write permissions are only allowed to the owner of the snippet.
        return request.user.is_superuser

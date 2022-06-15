from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a resource to access an object.
    """

    def has_permission(self, request, view):
        """Check if user is authenticated."""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Check if user is the owner of the resource."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return (
            request.user.is_authenticated
            and obj == request.user
            or request.user.is_superuser
        )


class IsAdminToList(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated and (
                request.user.is_superuser or request.user.is_seller
            )
        return True


class IsAdminOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_seller
        )

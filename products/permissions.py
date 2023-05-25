from rest_framework import permissions
from .models import Product
from rest_framework.views import View


class IsAdminOrProductSeller(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or request.user == obj.seller


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj.user == request.user


class IsAdminOrSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_seller
        )


class IsAccountOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True

        return obj.user == request.user

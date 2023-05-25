from rest_framework import permissions

from users.models import User
from .models import Order, OrderedProducts
from rest_framework.views import View


class IsProductSeller(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return obj.seller == request.user


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method == "POST":
            return True
        if request.user.is_superuser or request.user.is_seller:
            return True

        return False

class IsAdminOrSellerOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Order) -> bool:
        if request.method == "PATCH":
            return True

        if (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.user.is_seller
        ):
            return True

        return request.user.is_authenticated and request.user.id == obj.client_id

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user

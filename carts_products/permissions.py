from rest_framework import permissions
from rest_framework.views import View


class IsCartOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj.cart.owner == request.user

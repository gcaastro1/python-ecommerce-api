from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema
from rest_framework.views import Response, status

from carts.serializers import CartSerializer
from carts.models import Cart
from users.permissions import IsAccountOwnerOrAdmin


class CartView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(owner_id=self.request.user.id)
 
    @extend_schema(
        operation_id="cart_get",
        description="Retrieve user cart",
        summary="Retrieve user cart - User owner or Admin only",
        tags=["Cart"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

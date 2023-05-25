from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart
from drf_spectacular.utils import extend_schema

from carts_products.permissions import IsCartOwnerOrAdmin

from .models import CartProduct
from .serializers import CartProductSerializer


class CartProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwnerOrAdmin]

    serializer_class = CartProductSerializer
    queryset = CartProduct.objects.all()

    def perform_create(self, serializer):
        cart = Cart.objects.get(owner=self.request.user)
        return serializer.save(cart=cart)

    @extend_schema(
        operation_id="cart_product_post",
        description="Add product in cart",
        summary="Add product in cart - User owner & Admin only",
        tags=["Cart Product"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="cart_product_get",
        description="List all products in cart",
        summary="List all products in cart - User owner & Admin only",
        tags=["Cart Product"],
    )
    def get(self, request, *args, **kwargs):       
        return super().get(request, *args, **kwargs)


class CartProductDetailView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwnerOrAdmin]

    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

    @extend_schema(
        operation_id="cart_product_detail_get",
        description="Retrieve product from cart by ID",
        summary="Retrieve product from cart by ID - User owner & Admin only",
        tags=["Cart Product Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="cart_product_detail_delete",
        description="Remove product from cart by ID",
        summary="Remove product from cart by ID - User owner & Admin only",
        tags=["Cart Product Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

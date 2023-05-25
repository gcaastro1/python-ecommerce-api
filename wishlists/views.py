from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from .models import WishList
from .serializers import WishListSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAccountOwner
from products.models import Product


class WishListView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = WishListSerializer

    def get_object(self):
        return WishList.objects.get(user=self.request.user)

    @extend_schema(
        operation_id="wishlist_get",
        description="Retrieve user wishlist",
        summary="Retrieve user wishlist - User owner",
        tags=["Wishlist"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class WishListAddView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = WishListSerializer

    @extend_schema(
        operation_id="wishlist_add_patch",
        description="Add product in wishlist",
        summary="Add product in wishlist - User owner",
        tags=["Wishlist"],
    )
    def patch(self, request, *arg, **kwargs):
        product_id = self.kwargs.get("product_id")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound(f"Product with ID {product_id} not found.")

        wishlist = WishList.objects.get(user=self.request.user)

        if product in wishlist.products.all():
            raise NotFound(detail="Product is already on the wishlist.")

        wishlist.products.add(product)

        serializer = self.serializer_class(wishlist)
        return Response(serializer.data)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class WishListRemoveView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = WishListSerializer

    @extend_schema(
        operation_id="wishlist_remove_patch",
        description="Remove product in wishlist",
        summary="Remove product in wishlist - User owner",
        tags=["Wishlist"],
    )
    def patch(self, request, *arg, **kwargs):
        product_id = self.kwargs.get("product_id")
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound(f"Product with ID {product_id} not found.")

        wishlist = WishList.objects.get(user=self.request.user)

        if product not in wishlist.products.all():
            raise NotFound(detail="Product is not on the wishlist.")

        wishlist.products.remove(product)

        serializer = self.serializer_class(wishlist)
        return Response(serializer.data)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

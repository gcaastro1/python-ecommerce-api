from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product, ProductComments
from .serializers import ProductSerializer, ProductCommentsSerializer
from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import (
    IsAdminOrProductSeller,
    IsAdminOrSellerOrReadOnly,
    IsAccountOwnerOrAdminOrReadOnly,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)

    @extend_schema(
        operation_id="product_post",
        description="Create new product",
        summary="Create new product - Seller and Admin only",
        tags=["Product"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_get",
        description="Retrieve all products",
        summary="Retrieve all products - All users",
        tags=["Product"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrProductSeller]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

    @extend_schema(
        operation_id="product_detail_get",
        description="Retrieve product by ID",
        summary="Retrieve product - All users",
        tags=["Product Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_detail_patch",
        description="Update product by ID",
        summary="Update product - User owner & Admin only",
        tags=["Product Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_detail_delete",
        description="Delete product by ID",
        summary="Delete product - User owner & Admin only",
        tags=["Product Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class ProductCommentsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = ProductComments.objects.all()
    serializer_class = ProductCommentsSerializer

    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user, product_id=self.kwargs["product_id"]
        )

    def get_queryset(self):
        return ProductComments.objects.filter(product_id=self.kwargs["product_id"])

    @extend_schema(
        operation_id="product_comment_post",
        description="Add new product comment",
        summary="Add new product comment - User & Admin only",
        tags=["Product Comments"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_comment_get",
        description="Retrieve all products comment",
        summary="Retrieve all products comment - All users",
        tags=["Product Comments"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCommentsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdminOrReadOnly]

    queryset = ProductComments.objects.all()
    serializer_class = ProductCommentsSerializer
    lookup_url_kwarg = "comment_id"

    @extend_schema(
        operation_id="product_comment_detail_get",
        description="Retrieve comment by ID",
        summary="Retrieve comment - All users",
        tags=["Product Comments Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_comment_detail_patch",
        description="Update product comment by ID",
        summary="Update product comment - User owner & Admin only",
        tags=["Product Comments Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="product_comment_detail_delete",
        description="Delete product comment by ID",
        summary="Delete product comment - User owner & Admin only",
        tags=["Product Comments Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

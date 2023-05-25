from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CouponSerializer
from .models import Coupon
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsAdminOrSellerOrReadOnly
from drf_spectacular.utils import extend_schema


class CouponView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    serializer_class = CouponSerializer

    @extend_schema(
        operation_id="coupon_post",
        description="Create new coupon",
        summary="Create new coupon - Seller and Admin only",
        tags=["Coupon"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="coupon_get",
        description="Retrieve all products",
        summary="Retrieve all coupons - All users",
        tags=["Coupon"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CouponDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()
    lookup_url_kwar = "coupon_id"

    @extend_schema(
        operation_id="coupon_detail_get",
        description="Retrieve coupon by ID",
        summary="Retrieve coupon - All users",
        tags=["Coupon Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="coupon_detail_patch",
        description="Update coupon by ID",
        summary="Update coupon - User owner & Admin only",
        tags=["Coupon Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="coupon_detail_delete",
        description="Delete coupon by ID",
        summary="Delete coupon - User owner & Admin only",
        tags=["Coupon Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

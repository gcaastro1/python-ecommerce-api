from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema

from addresses.models import Address
from addresses.serializers import AddressSerializer
from users.models import User


class AddressView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        get_object_or_404(User, pk=self.kwargs.get("user_id"))

        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return Address.objects.filter(user_id=self.kwargs.get("user_id"))

    @extend_schema(
        operation_id="address_post",
        description="Create new address",
        summary="Create new address - User or Admin only",
        tags=["Address"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_get",
        description="Retrieve all addresses",
        summary="Retrieve all addresses - All users",
        tags=["Address"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @extend_schema(
        operation_id="address_detail_get",
        description="Retrieve address by ID",
        summary="Retrieve address - User owner & Admin only",
        tags=["Address Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_detail_patch",
        description="Update address by ID",
        summary="Update address - User owner & Admin only",
        tags=["Address Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_detail_delete",
        description="Delete address by ID",
        summary="Delete address - User owner & Admin only",
        tags=["Address Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

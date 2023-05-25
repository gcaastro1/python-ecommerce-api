from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema

from users.models import User
from users.permissions import IsAccountOwnerOrAdmin
from users.serializers import UserSerializer


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        operation_id="user_post",
        description="Create new user",
        summary="Create new user - All users",
        tags=["User"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_get",
        description="Retrieve all users",
        summary="Retrieve all users - All users",
        tags=["User"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_detail_get",
        description="Retrieve user by ID",
        summary="Retrieve user - User owner & Admin only",
        tags=["User Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_detail_patch",
        description="Update user by ID",
        summary="Update user - User owner & Admin only",
        tags=["User Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_detail_delete",
        description="Soft Delete user by ID",
        summary="Soft Delete - User owner & Admin only",
        tags=["User Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema
from rest_framework.views import Response, status
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProductSeller, IsAdminOrSeller, IsAccountOwner

# Create your views here.


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated ,IsAccountOwner]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @extend_schema(
        operation_id="order_post",
        description="Create new order",
        summary="Create new order - User owner & Admin only",
        tags=["Order"],
    )
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.validated_data)
        return Response(data, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        operation_id="order_get",
        description="Retrieve all user orders",
        summary="Retrieve all user orders - User owner & Admin only",
        tags=["Order"],
    )
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    



class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsProductSeller, IsAdminOrSeller]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
    @extend_schema(
        operation_id="order_detail_get",
        description="Retrieve user order by ID",
        summary="Retrieve user order - User owner & Admin only",
        tags=["Order Detail"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_detail_patch",
        description="Update user order by ID",
        summary="Update user order - User owner & Admin only",
        tags=["Order Detail"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_detail_delete",
        description="Delete user order by ID",
        summary="Delete user order - User owner & Admin only",
        tags=["Order Detail"],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    


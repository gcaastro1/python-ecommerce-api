from rest_framework import serializers
from carts_products.models import CartProduct

from carts_products.serializers import CartProductDetailSerializer
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
    )
    product_list = CartProductDetailSerializer(
        read_only=True,
        many=True,
    )

    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = [
            "id",
            "owner",
            "product_list",
            "total",
        ]
    
    def get_total(self, cart):
        cart_products = CartProduct.objects.filter(cart=cart)
        
        total = 0
        
        for cart_product in cart_products:
            total += cart_product.quantity * cart_product.product.price
            
        return total
            

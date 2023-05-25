from rest_framework import serializers

from carts_products.models import CartProduct

from products.serializers import ProductSerializer


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct

        fields = [
            "id",
            "cart_id",
            "quantity",
            "product",
        ]

        read_only_fields = ["id"]
       

    def create(self, validated_data: dict) -> CartProduct:
        try:
            product = CartProduct.objects.get(
                cart=validated_data["cart"],
                product=validated_data["product"],
            )

            product.quantity = validated_data["quantity"]

            product.save()

            return product

        except CartProduct.DoesNotExist:           
            return CartProduct.objects.create(**validated_data)
        


class CartProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = CartProduct

        fields = [
            "id",
            "cart_id",
            "quantity",
            "product",
        ]

        read_only_fields = ["id"]
        depth = 1
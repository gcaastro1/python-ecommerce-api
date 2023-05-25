from rest_framework import serializers
from .models import Product, ProductComments


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "quantity", "description", "img", "seller_id"]
        extra_kwargs = {"seller_id": {"read_only": True}}

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class ProductCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComments
        fields = ["id", "comment", "product_rate", "user_id", "product_id"]
        extra_kwargs = {"user_id": {"read_only": True}}

    def create(self, validated_data: dict) -> Product:
        return ProductComments.objects.create(**validated_data)

    def update(self, instance: ProductComments, validated_data: dict) -> ProductComments:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

from itertools import groupby
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from carts_products.models import CartProduct
from carts_products.serializers import CartProductDetailSerializer
from products.models import Product
from products.serializers import ProductSerializer
from users.models import User
from users.serializers import UserSerializer
from .models import Order, OrderedProducts


class OrderedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProducts
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    ordered_products = OrderedProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "seller", "status", "ordered_at", "ordered_products"]
        read_only_fields = ["id", "ordered_at", "user", "seller"]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        cart_products = CartProduct.objects.filter(cart__owner=user)

        if not cart_products:
            return {"message": "The cart is empty"}

        serializer = CartProductDetailSerializer(data=cart_products, many=True)
        serializer.is_valid()

        print(serializer.data)

        sellers_list = {}
        for seller, group in groupby(
            serializer.data, key=lambda x: x["product"]["seller_id"]
        ):
            sellers_list[str(seller)] = [p for p in group]

        ordered_data = []
        out_of_stock = []

        for sellers, products in sellers_list.items():
            seller = get_object_or_404(User, pk=sellers)
            data = {"user": user, "seller": seller}

            has_stock = True

            for product in products:
                prod = Product.objects.get(id=product["product"]["id"]) 

                if prod.quantity < product["quantity"]:
                    has_stock = False
                    serializer = ProductSerializer(prod)
                    error = {
                        "product_id": serializer.data['id'],
                        "product": serializer.data['name'],
                        "error": "Product {} doesn't have enough stock".format(serializer.data['name'])
                    }
                    out_of_stock.append(error)

            if has_stock:
                order = Order.objects.create(**data)
                ordered_data.append(order)

                for product in products:
                    prod.quantity -= product["quantity"]
                    prod.save()
                    serializer = ProductSerializer(prod)

                    data = {
                        "product": prod,
                        "order": order,
                        "quantity": product["quantity"],
                    }
                    ordered_product = OrderedProducts.objects.create(**data)

        cart_products.delete()

        if out_of_stock:
            return {
                "orders": OrderSerializer(ordered_data, many=True).data,
                "error": out_of_stock
            }
        
        else:
            return OrderSerializer(ordered_data, many=True).data

    def update(self, instance, validated_data):
        ordered_products_data = validated_data.pop("ordered_products", [])
        instance.user = validated_data.get("user", instance.user)
        instance.seller = validated_data.get("seller", instance.seller)
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        products_mapping = {
            product.id: product for product in instance.ordered_products.all()
        }
        for product_data in ordered_products_data:
            product = products_mapping.get(product_data.get("id"), None)
            if product:
                product.user = product_data.get("user", product.user)
                product.product = product_data.get("product", product.product)
                product.save()
            else:
                OrderedProducts.objects.create(order=instance, **product_data)
        return instance

    def delete(self, instance):
        instance.delete()

from rest_framework import serializers
from .models import WishList


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ["id", "user_id", "products"]
        extra_kwargs = {"user_id": {"read_only": True}}
        depth = 1

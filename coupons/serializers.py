from rest_framework import serializers
from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Coupon
        fields = ["id", "coupon", "discount", "is_valid", "created_at"]
        read_only_fields = ["created_at"]

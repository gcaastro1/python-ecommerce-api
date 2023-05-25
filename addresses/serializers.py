from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = [
            "id",
            "street",
            "number",
            "neighborhood",
            "city",
            "state",
            "country",
            "zipcode",
            "is_default",
            "user_id"
        ]

        read_only_fields = ["id, user_id"]

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from carts.models import Cart
from wishlists.models import WishList
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_seller",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {"validators": [UniqueValidator(queryset=User.objects.all())]},
        }

    def create(self, validated_data: dict) -> User:
        superuser = User.objects.filter(is_superuser=True)

        if superuser:
            validated_data["is_superuser"] = False
            user = User.objects.create_user(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)

        Cart.objects.create(owner=user)
        WishList.objects.create(user=user)

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        instance.__dict__.update(**validated_data)
        instance.set_password(instance.password)
        instance.save()
        return instance

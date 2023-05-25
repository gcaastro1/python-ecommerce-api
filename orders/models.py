from django.db import models
from products.models import Product


class OrderStatus(models.TextChoices):
    Pending = "Pending"
    InTransit = "In Transit"
    Shipped = "Shipped"


class Order(models.Model):
    class Meta:
        ordering = ["id"]

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="orders"
    )
    seller = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="orders_as_seller",
    )
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.Pending
    )
    ordered_at = models.DateTimeField(auto_now_add=True)


class OrderedProducts(models.Model):
    class Meta:
        ordering = ["id"]

    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="ordered_products"
    )
    quantity = models.IntegerField(blank=True, default=0)
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="ordered_products"
    )
    ordered_at = models.DateTimeField(auto_now_add=True)

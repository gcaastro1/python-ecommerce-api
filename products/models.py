from django.db import models
from users.models import User


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    img = models.CharField(max_length=255)

    seller = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products"
    )


class ProductComments(models.Model):
    class Meta:
        ordering = ["id"]

    comment = models.TextField()
    product_rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")

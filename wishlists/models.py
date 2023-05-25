from django.db import models


class WishList(models.Model):
    class Meta:
        ordering = ["id"]

    products = models.ManyToManyField(
        "products.Product",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlist",
    )

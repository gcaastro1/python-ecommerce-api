from django.db import models


class Cart(models.Model):
    class Meta:
        ordering = ["id"]
        
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_cart",
    )
    products = models.ManyToManyField(
        "products.Product",
        through="carts_products.CartProduct",
        related_name="product_list",
    )

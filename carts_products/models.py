from django.db import models


class CartProduct(models.Model):
    class Meta:
        ordering = ["product__seller"]
        
    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name="product_list",
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="product_carts",
    )
    
    quantity = models.IntegerField(blank=True, default=1)

from django.db import models


class Coupon(models.Model):
    class Meta:
        ordering = ["id"]

    coupon = models.CharField(max_length=16)
    discount = models.IntegerField()
    is_valid = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models


class Address(models.Model):
    class Meta:
        ordering = ("id",)

    street = models.CharField(max_length=120)
    number = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=9)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                address = Address.objects.get(is_default=True)
                if self != address:
                    address.is_default = False
                    address.save()
            except Address.DoesNotExist:
                pass

        super(Address, self).save(*args, **kwargs)

from django.db import models


class Order(models.Model):
    number = models.CharField(max_length=100)
    products = models.ManyToManyField("Product")
    promo_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.number

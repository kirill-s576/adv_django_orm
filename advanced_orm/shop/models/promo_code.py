from django.db import models


class PromoCode(models.Model):
    name = models.CharField(max_length=100)


class PromoCodeValidity(models.Model):
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField(null=True, blank=True)

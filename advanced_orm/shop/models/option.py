from django.db import models


class Option(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    dimension = models.CharField(max_length=100)
    products = models.ManyToManyField("Product", through="ProductOption")

    def __str__(self):
        return self.name

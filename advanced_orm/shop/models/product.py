from django.db import models


class Product(models.Model):
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    categories = models.ManyToManyField("Category")
    options = models.ManyToManyField("Option", through="ProductOption")

    def __str__(self):
        return self.name

from django.db import models


class ProductOption(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="option_values")
    option = models.ForeignKey("Option", on_delete=models.CASCADE, related_name="product_values")
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"

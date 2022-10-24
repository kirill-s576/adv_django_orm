from cases.base import *
from shop.models import Product


products = Product.objects.all().prefetch_related("options", "option_values")
for product in products:
    print(product)
    print(product.options.all())
    print(product.option_values.all())

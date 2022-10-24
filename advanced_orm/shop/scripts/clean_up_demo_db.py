from shop.models import (
    Shop,
    Category,
    Product,
    Option,
    PromoCode,
    Order
)
from django.db.transaction import atomic


@atomic()
def clean_up_db():
    Product.objects.all().delete()
    Category.objects.all().delete()
    Shop.objects.all().delete()
    Option.objects.all().delete()
    PromoCode.objects.all().delete()
    Order.objects.all().delete()

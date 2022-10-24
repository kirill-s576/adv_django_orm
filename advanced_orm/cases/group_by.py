from cases.base import *
from shop.models import Product
from django.db.models import Max, Min, Count, Sum, F


#
qs = Product.objects.annotate(
    max_price=Max("price"),
    min_price=Min("price"),
    cnt=Count("id"),
    avg=Sum("price")/F("cnt")
).values("shop_id")
print(list(qs))


qs = Product.objects.annotate(
    max_price=Max("price"),
    min_price=Min("price"),
    cnt=Count("id"),
    avg=Sum("price")/F("cnt")
).values("shop_id", "max_price", "min_price", "avg")
print(list(qs))

# В этом примере нам мешает order_by("price"). Сортировка по несгруппированному значению.
# ORM автоматически добавляет GROUP BY price.
qs = Product.objects.values("shop_id").annotate(
    max_price=Max("price"),
    min_price=Min("price"),
    cnt=Count("id"),
    avg=Sum("price")/F("cnt")
).order_by("price")
print(list(qs))

# Правильный.
# + Демонстрация работы HAVING.
# + Демонстрация того, что Django не переиспользует переменную avg.
qs = Product.objects.values("shop_id").annotate(
    max_price=Max("price"),
    min_price=Min("price"),
    cnt=Count("id"),
    avg=Sum("price")/F("cnt")
).filter(avg__gt=20)
print(list(qs))
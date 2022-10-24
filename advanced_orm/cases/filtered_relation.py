from cases.base import *
from shop.models import Shop
from django.db.models import FilteredRelation, Q


# Способ отсечения присоединяемых через JOIN данных
# Сильно оптимизирует запрос при больших датасетах.
#
qs = (
    Shop.objects
    .annotate(
        expensive_products=FilteredRelation(
            'product',
            condition=Q(product__price__gt=20)
        )
    )
    .filter(expensive_products__price__gt=42)
)

print(qs.query)

from cases.base import *
from shop.models import Order, PromoCode
from django.db.models import OuterRef, Subquery, F


# С какого времени действует последний промо-код?
# GПример демонстрирует работу OuterRef.
# Если кратко - дает доступ Subquery на поля "внешние" поля.
# Хорошо видно на примере чистого SQL как селект на таблицу с промо-кодом обращается к полю promo_code заказа.
pm_q = (
    PromoCode.objects
    .filter(
        name=OuterRef('promo_code'),
    )
    .annotate(
        valid_from=F("promocodevalidity__valid_from")
    )
    .values("valid_from")[:1]
)

q = Order.objects.annotate(valid_from=Subquery(pm_q))
print(q[0].valid_from)

"""
SELECT 
"shop_order"."id", 
"shop_order"."number", 
"shop_order"."promo_code", 
(
    SELECT 
    U1."valid_from" AS "valid_from" 
    FROM "shop_promocode" U0 
    LEFT OUTER JOIN "shop_promocodevalidity" U1 ON (U0."id" = U1."promo_code_id") 
    WHERE U0."name" = ("shop_order"."promo_code") 
    LIMIT 1
) AS "valid_from" 
FROM "shop_order" LIMIT 1
"""

from cases.base import *
from shop.models import Order, PromoCode
from django.db.models import OuterRef, Subquery, Q, F, IntegerField, Case, When, Value
from django.db.models.functions import Cast
from django.utils import timezone
from django.db.models import Func


class TimeDiff(Func):
    function = 'EXTRACT(EPOCH FROM '
    template = "%(function)s%(expressions)s)"


# Данный запрос существует для того, чтобы у каждого заказа появилось поле promo_code_expiration_seconds
# Которое дает информацию о том, сколько секунд до истечения срока действия данного промо-кода.
# 0 - если промо-код не активен в данное время или такого нет. 999999999 - если промо-код не ограничен по времени.
pm_q = (
    PromoCode.objects
    .filter(
        Q(promocodevalidity__valid_to__gt=timezone.now()) | Q(promocodevalidity__valid_to__isnull=True),
        promocodevalidity__valid_from__lt=timezone.now(),
        name=OuterRef('promo_code'),
    )
    .annotate(
        expiration_seconds=Case(
            When(
                promocodevalidity__valid_to__isnull=False,
                then=Cast(
                    TimeDiff(F('promocodevalidity__valid_to') - F('promocodevalidity__valid_from')),
                    output_field=IntegerField()
                ),
            ),
            When(
                Q(promocodevalidity__valid_to__isnull=True, promocodevalidity__valid_from__lt=timezone.now()),
                then=Value(999999999),
            ),
            default=Value(0),
            output_field=IntegerField(),
        )
    )
    .values("expiration_seconds")[:1]
)

q = Order.objects.annotate(promo_code_expiration_seconds=Subquery(pm_q))
print(q[0].promo_code_expiration_seconds)

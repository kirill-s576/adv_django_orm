from cases.base import *
from shop.models import Product


# Наглядно демонстрирует механику работы select(prefetch) related.
# В данном случае мы отправляем 3! запроса в БД
# Вывод в том, что Django собирает несколько датасетов из разных таблиц и маппит их обработкой в Python
# Следствие - мы сами можем отправить 3 запроса и объединить данные как нам надо без потерь производительности
# Может даже быстрее...
products = Product.objects.all().prefetch_related("options", "option_values")
for product in products:
    print(product)
    for option in product.options.all():
        print(option)
    for option_value in product.option_values.all():
        print(option_value)

from shop.factories import (
    ShopFactory,
    ProductFactory,
    CategoryFactory,
    OrderFactory
)
from shop.models import (
    Shop,
    Product,
    Category,
    Option,
    PromoCode,
    PromoCodeValidity
)
from django.db.transaction import atomic
from django.utils import timezone
from datetime import timedelta


@atomic()
def init_db():
    shop_1, shop_2 = (ShopFactory() for _ in range(2))
    product_1 = ProductFactory(shop=shop_1)
    product_2, product_3, product_4 = (ProductFactory(shop=shop_2) for _ in range(3))

    print("Shop count created:", Shop.objects.count())
    print("Product count created:", Product.objects.count())

    # Categories
    category_1, category_2 = (CategoryFactory() for _ in range(2))
    print("Category count created:", Category.objects.count())

    product_1.categories.set([category_1])
    product_2.categories.set([category_2])
    product_3.categories.set([category_1, category_2])
    product_4.categories.set([category_1, category_2])
    print("Categories were created added to products")

    # Options
    with_option = Option.objects.create(
        name="Width",
        dimension="mm",
        type="int"
    )
    height_option = Option.objects.create(
        name="Height",
        dimension="mm",
        type="int"
    )
    weight_option = Option.objects.create(
        name="Weight",
        dimension="kg",
        type="float"
    )
    display_type_option = Option.objects.create(
        name="Display type",
        dimension="-",
        type="str"
    )
    for product in [
        product_1, product_2, product_3, product_4
    ]:
        product.options.add(with_option, through_defaults={"value": "100"})
        product.options.add(height_option, through_defaults={"value": "200"})

    product_3.options.add(weight_option, through_defaults={"value": "2.3"})
    product_4.options.add(display_type_option, through_defaults={"value": "IPS"})

    print("Options were created and added to the products")

    # Promo codes
    promo_code_1 = PromoCode.objects.create(name="ABC")
    promo_code_2 = PromoCode.objects.create(name="QWERTY")
    PromoCodeValidity.objects.create(
        promo_code=promo_code_1,
        valid_from=timezone.now() - timedelta(days=1),
        valid_to=None
    )
    PromoCodeValidity.objects.create(
        promo_code=promo_code_2,
        valid_from=timezone.now() - timedelta(days=3),
        valid_to=timezone.now() - timedelta(days=2)
    )
    PromoCodeValidity.objects.create(
        promo_code=promo_code_2,
        valid_from=timezone.now() + timedelta(days=2),
        valid_to=timezone.now() + timedelta(days=3)
    )
    print("Promocodes 'ABC' and 'QWERTY' were created")

    # Orders
    order_1 = OrderFactory(promo_code="ABC")
    order_1.products.set([product_1, product_3])
    order_2 = OrderFactory(promo_code="QWERTY")
    order_2.products.set([product_2, product_4])
    order_3 = OrderFactory()
    order_3.products.set([product_1])
    print("Orders were created")



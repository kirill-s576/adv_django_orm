from factory.django import DjangoModelFactory
from factory import SubFactory, Sequence
from factory.fuzzy import FuzzyFloat
from shop.models import Product
from .shop import ShopFactory


class ProductFactory(DjangoModelFactory):
    name = Sequence(lambda n: f"Product_{n}")
    price = FuzzyFloat(low=10, high=50, precision=2)
    shop = SubFactory(ShopFactory)
    description = "-"

    class Meta:
        model = Product

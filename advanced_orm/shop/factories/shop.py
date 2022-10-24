from factory.django import DjangoModelFactory
from factory import Sequence
from shop.models import Shop


class ShopFactory(DjangoModelFactory):
    name = Sequence(lambda n: f"Shop_{n}")
    description = "-"

    class Meta:
        model = Shop

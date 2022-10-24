from shop.models import Order
from factory.django import DjangoModelFactory
from factory import Sequence


class OrderFactory(DjangoModelFactory):
    number = Sequence(lambda n: f"order_{n}")

    class Meta:
        model = Order


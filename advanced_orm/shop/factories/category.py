from factory.django import DjangoModelFactory
from factory import Sequence
from shop.models import Category


class CategoryFactory(DjangoModelFactory):
    name = Sequence(lambda n: f"Category_{n}")
    description = "-"

    class Meta:
        model = Category

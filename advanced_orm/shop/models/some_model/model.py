from django.db import models
from .manager import SomeModelManager


class SomeModel(models.Model):
    x = models.CharField(max_length=100)

    def __str__(self):
        return self.x

    objects = SomeModelManager()

from django.db import models


class SomeModelManager(models.Manager):

    def filter_by_x(self, x: str):
        return self.filter(x=x)

from django.db import models
from django.utils.timezone import now


class Stock(models.Model):
    Date = models.DateTimeField(default=now)
    Product = models.ForeignKey('Products.Product', models.CASCADE)
    Quantity = models.PositiveIntegerField()

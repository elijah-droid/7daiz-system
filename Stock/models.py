from django.db import models
from django.utils.timezone import now


class Stock(models.Model):
    Date = models.DateTimeField(default=now)
    Branch = models.ForeignKey('Branches.Branch', models.SET_NULL, null=True)
    Product = models.ForeignKey('Products.Product', models.CASCADE)
    Quantity = models.PositiveIntegerField()
    Items_Sold = models.PositiveIntegerField(null=True)
    Price = models.PositiveIntegerField(null=True)
    Alert_Level = models.PositiveIntegerField(default=0)

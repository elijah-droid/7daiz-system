from django.db import models

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Stock = models.ManyToManyField('Stock.Stock')
    Sales = models.ManyToManyField('Sales.Sale')
    Price = models.PositiveIntegerField()

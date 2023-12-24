from django.db import models

types = (
    ('Merchandise', 'Merchandise'),
    ('Paper', 'Paper')
)

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=100, choices=types, null=True)
    Stock = models.ManyToManyField('Stock.Stock')
    Sales = models.ManyToManyField('Sales.Sale')
    Price = models.PositiveIntegerField()

    def __str__(self):
        return self.Name

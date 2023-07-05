from django.db import models

class Paper(models.Model):
    product = models.ForeignKey('Products.Product', models.CASCADE)
    Price = models.PositiveIntegerField()
    Prints = models.ManyToManyField('Printing.Printing')

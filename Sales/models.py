from django.db import models
from django.utils.timezone import now

class Sale(models.Model):
    Product = models.ForeignKey('Products.Product', models.CASCADE)
    Date = models.DateTimeField(default=now)
    Quantity = models.PositiveIntegerField()
    Money_Collected = models.PositiveIntegerField()
    Money_Expected = models.PositiveIntegerField(null=True)
    Employee = models.ForeignKey('Employees.Employee', models.CASCADE)
    Refunded = models.BooleanField(default=False)
    Staff = models.ForeignKey('Employees.Employee', models.CASCADE, null=True, blank=True, related_name='employee_sale')

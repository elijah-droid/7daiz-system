from django.db import models

class Branch(models.Model):
    Cashier = models.ForeignKey('Employees.Employee', models.SET_NULL, null=True, blank=True, related_name='branch_cashier')
    Name = models.CharField(max_length=100, blank=True, null=True)
    Reports = models.ManyToManyField('Reports.Report', blank=True)
    Sales = models.ManyToManyField('Sales.Sale', blank=True)
    Printing = models.ManyToManyField('Printing.Printing', blank=True)
    Stock = models.ManyToManyField('Stock.Stock', blank=True)
    Expenses = models.ManyToManyField('Expenses.Expense', blank=True)
    Employees = models.ManyToManyField('Employees.Employee', blank=True)

    def __str__(self):
        return self.Name
from django.db import models

class Branch(models.Model):
    Cashier = models.ForeignKey('Employees.Employee', models.CASCADE, related_name='branch_cashier')
    Reports = models.ManyToManyField('Reports.Report')
    Sales = models.ManyToManyField('Sales.Sale')
    Printing = models.ManyToManyField('Printing.Printing')
    Stock = models.ManyToManyField('Stock.Stock')
    Expenses = models.ManyToManyField('Expenses.Expense')
    Employees = models.ManyToManyField('Employees.Employee')

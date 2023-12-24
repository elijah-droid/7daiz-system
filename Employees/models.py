from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils.timezone import now

class Employee(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    Branch = models.ForeignKey('Branches.Branch', models.CASCADE)
    printing = models.ManyToManyField('Printing.Printing', blank=True)
    large_format_attribute = models.ManyToManyField('Largeformat.LargeformatPrinting', related_name="employee_largeprints", blank=True)
    printing_attribute = models.ManyToManyField('Printing.Printing', related_name="employee_prints", blank=True)
    sales_attribute = models.ManyToManyField('Sales.Sale', blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    def day_contribution(self):
        printing_sum = self.printing_attribute.filter(Date__date=now()).aggregate(printing=Sum('Amount_Paid'))
        large_format_sum = self.large_format_attribute.filter(Date__date=now()).aggregate(large_format=Sum('Amount_Paid'))
        sales_sum = self.sales_attribute.filter(Date__date=now()).aggregate(sales=Sum('Money_Collected'))
        figures = [printing_sum['printing'], large_format_sum['large_format'], sales_sum['sales']]
        cash = [cash for cash in figures if cash != None]
        return sum(cash)

    def month_contribution(self):
        printing_sum = self.printing_attribute.filter(Date__date__month=now().month).aggregate(printing=Sum('Amount_Paid'))
        large_format_sum = self.large_format_attribute.filter(Date__date__month=now().month).aggregate(large_format=Sum('Amount_Paid'))
        sales_sum = self.sales_attribute.filter(Date__date__month=now().month).aggregate(sales=Sum('Money_Collected'))
        figures = [printing_sum['printing'], large_format_sum['large_format'], sales_sum['sales']]
        cash = [cash for cash in figures if cash != None]
        return sum(cash)

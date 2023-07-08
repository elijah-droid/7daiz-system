from django.urls import reverse
from django import template
from django.utils.timezone import now
from django.db.models import Sum

register = template.Library()


@register.filter
def grandtotal(branch):
    salestotal = branch.Sales.filter(Date__date=now().date()).aggregate(total=Sum('Money_Collected'))['total']
    if not salestotal:
        salestotal = 0
    printingtotal = branch.Printing.filter(Date__date=now().date()).aggregate(total=Sum('Amount_Paid'))['total']
    if not printingtotal:
        printingtotal = 0
    return printingtotal + salestotal
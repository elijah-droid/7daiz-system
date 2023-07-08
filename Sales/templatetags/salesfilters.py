from django.urls import reverse
from django import template
from Stock.models import Stock
from django.utils.timezone import now
from django.db.models import Sum

register = template.Library()


@register.filter
def salestotal(branch):
    total = branch.Sales.filter(Date__date=now().date(), Refunded=False).aggregate(total=Sum('Money_Collected'))['total']
    if total:
        return total 
    else:
        return 0
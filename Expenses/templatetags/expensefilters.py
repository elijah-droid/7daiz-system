from django.urls import reverse
from django import template
from django.utils.timezone import now
from django.db.models import Sum

register = template.Library()


@register.filter
def expensetotal(branch):
    total = branch.Expenses.filter(Date__date=now().date()).aggregate(total=Sum('Amount'))['total']
    if total:
        return total 
    else:
        return 0
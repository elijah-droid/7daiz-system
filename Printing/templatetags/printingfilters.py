from django.urls import reverse
from django import template
from Printing.models import Printing
from django.utils.timezone import now
from django.db.models import Sum

register = template.Library()


@register.filter
def printingtotal(branch):
    total = branch.Printing.filter(Date__date=now().date()).aggregate(total=Sum('Amount_Paid'))['total']
    if total:
        return total
    else:
        return 0
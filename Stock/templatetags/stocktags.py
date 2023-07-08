from django.urls import reverse
from django import template
from Stock.models import Stock

register = template.Library()


@register.filter
def stock(product, branch):
    try:
        stock = Stock.objects.get(Product=product, Branch=branch)
        return stock
    except:
        pass
from django.shortcuts import render, redirect
from .forms import SalesForm
from django.utils.timezone import now
from Stock.models import Stock
from Products.models import Product
import pandas as pd
from .models import Sale
from django.db import models

def sales(request):
    sales = request.user.employee.Branch.Sales.filter(Date__date=now().date())
    context = {
        'sales': sales
    }
    return render(request, 'sales.html', context)

def register(request):
    form = SalesForm()
    stocked_products = Stock.objects.filter(Branch=request.user.employee.Branch, Quantity__gt=0).values('Product__id')
    form.fields['Product'].queryset = Product.objects.filter(id__in=stocked_products)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sale = form.save(commit=False)
            sale.Employee = request.user.employee
            sale.save()
            sale.Money_Expected = sale.Quantity * sale.Product.Price
            sale.save()
            request.user.employee.Branch.Sales.add(sale)
            stock = Stock.objects.get(Product=sale.Product, Branch=request.user.employee.Branch)
            stock.Quantity -= sale.Quantity
            stock.Items_Sold += sale.Quantity
            stock.save()
            sale.Staff.sales_attribute.add(sale)
            return redirect('sales')
    else:
        return render(request, 'register_sale.html', context)


def export_sales(request):
    queryset = Sale.objects.all()
    queryset = queryset.annotate(
        Date_Time=models.functions.Cast(models.F('Date'), models.CharField()
    ))
    data = pd.DataFrame(list(queryset.values('Date_Time' ,'Product__Name', 'Quantity', 'Money_Collected', 'Money_Expected', 'Staff__user__first_name', )))

    excel_file_path = 'data_export_pandas.xlsx'

    data.to_excel(excel_file_path, index=False)
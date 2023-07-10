from django.shortcuts import render, redirect
from .forms import SalesForm
from django.utils.timezone import now
from Stock.models import Stock
from Products.models import Product

def sales(request):
    sales = request.user.employee.Branch.Sales.filter(Date__date=now().date())
    context = {
        'sales': sales
    }
    return render(request, 'sales.html', context)

def register(request):
    form = SalesForm()
    stocked_products = Stock.objects.filter(Branch=request.user.employee.Branch).values('Product__id')
    print(stocked_products)
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
            request.user.employee.Branch.Sales.add(sale)
            stock = Stock.objects.get(Product=sale.Product, Branch=request.user.employee.Branch)
            stock.Quantity -= sale.Quantity
            stock.Items_Sold += sale.Quantity
            stock.save()
            return redirect('sales')
    else:
        return render(request, 'register_sale.html', context)


from django.shortcuts import render, redirect
from .forms import SalesForm
from Stock.models import Stock

def sales(request):
    return render(request, 'sales.html')

def register(request):
    form = SalesForm()
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
            stock.save()
            return redirect('sales')
    else:
        return render(request, 'register_sale.html', context)


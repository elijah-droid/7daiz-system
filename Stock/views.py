from django.shortcuts import render, redirect
from .forms import StockForm
from Products.models import Product
from django.contrib import messages
from .models import Stock

def stock(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'stock.html', context)

def add_stock(request, product):
    product = Product.objects.get(id=product)
    form = StockForm(initial={'Product': product, 'Quantity': 0, 'Price': product.Price})
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = StockForm(request.POST)
        stock = form.save(commit=False)
        stock.Branch = request.user.employee.Branch
        stock.save()
        messages.success(request, 'Stock added successfully.')
        return redirect('stock')
    else:
        return render(request, 'add_stock.html', context)


def edit_stock(request, stock):
    stock = Stock.objects.get(id=stock)
    form = StockForm(instance=stock)
    context = {
        'form': form,
        'stock': stock    
    }
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save()
            return redirect('stock')
    else:
        return render(request, 'edit_stock.html', context)

def delete_stock(request):
    pass
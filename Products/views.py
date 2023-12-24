from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def add_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
        return redirect('add-stock', product=product.id)
    else:
        return render(request, 'add_product.html', context)


def edit_product(request, product):
    product = Product.objects.get(id=product)
    form = ProductForm(instance=product)
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('stock')
    else:
        return render(request, 'edit_product.html', context)
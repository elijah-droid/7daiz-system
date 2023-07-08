from django.shortcuts import render, redirect
from .forms import ProductForm

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
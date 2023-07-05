from django.shortcuts import render
from .forms import ProductForm

def add_product(request):
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)
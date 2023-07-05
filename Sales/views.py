from django.shortcuts import render
from .forms import SalesForm

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
            pass
    else:
        return render(request, 'register_sale.html', context)


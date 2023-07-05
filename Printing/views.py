from django.shortcuts import render
from .forms import PrintingForm

def printing(request):
    return render(request, 'printing.html')

def register(request):
    form = PrintingForm()
    context = {
        'form': form
    }
    return render(request, 'register_print.html', context)
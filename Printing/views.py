from django.shortcuts import render, redirect
from .forms import PrintingForm
from Stock.models import Stock

def printing(request):
    return render(request, 'printing.html')

def register(request):
    form = PrintingForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PrintingForm(request.POST)
        if form.is_valid():
            printing = form.save(commit=False)
            printing.Branch = request.user.employee.Branch
            printing.save()
            stock = Stock.objects.get(Branch=request.user.employee.Branch, Product=printing.Paper.product)
            stock.Quantity -= printing.No_of_Papers
            stock.save()
            request.user.employee.Branch.Printing.add(printing)
            return redirect('printing')
    else:
        return render(request, 'register_print.html', context)
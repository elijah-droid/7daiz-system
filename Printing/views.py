from django.shortcuts import render, redirect
from .forms import PrintingForm
from Stock.models import Stock
from django.utils.timezone import now
from django.contrib import messages
from Papers.models import Paper

def printing(request):
    printing = request.user.employee.Branch.Printing.filter(Date__date=now().date())
    context = {
        'printing': printing
    }
    return render(request, 'printing.html', context)

def register(request):
    form = PrintingForm() 
    stocked_products = Stock.objects.filter(Product__Type='Paper', Quantity__gt=0).values('Product')
    papers = Paper.objects.filter(product__id__in=stocked_products)
    form.fields['Paper'].queryset = papers
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PrintingForm(request.POST)
        if form.is_valid():
            stock = Stock.objects.get(Branch=request.user.employee.Branch, Product=form.cleaned_data['Paper'].product)
            if stock.Quantity >= form.cleaned_data['No_of_Papers']:
                printing = form.save(commit=False)
                printing.Branch = request.user.employee.Branch
                printing.save()
                stock.Quantity -= printing.No_of_Papers
                stock.save()
                request.user.employee.Branch.Printing.add(printing)
                printing.Staff.printing_attribute.add(printing)
                return redirect('printing')
            else:
                messages.success(request, 'Number of papers greater than the stock available.')
                return redirect('.')
        else:
            print(form.errors)
            pass
    else:
        return render(request, 'register_print.html', context)


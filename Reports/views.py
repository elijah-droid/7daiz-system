from django.shortcuts import render, redirect
from .forms import ReportForm
from Sales.templatetags.salesfilters import salestotal
from Printing.templatetags.printingfilters import printingtotal
from django.contrib import messages

def reports(request):
    
    return render(request, 'reports.html')

def add_report(request):
    data = {
        'Sales': salestotal(request.user.employee.Branch),
        'Printing': printingtotal(request.user.employee.Branch),
        'Grand_Total': salestotal(request.user.employee.Branch) + printingtotal(request.user.employee.Branch),
        'Balance': salestotal(request.user.employee.Branch) + printingtotal(request.user.employee.Branch)
    }
    form = ReportForm(initial=data)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['Grand_Total'] < data['Cash_Taken']:
                messages.success(request, 'The cash taken should be <= the balance')
                return redirect('.')
            else:
                report = form.save(commit=False)
                report.Branch = request.user.employee.Branch
                report.save()
                request.user.employee.Branch.Reports.add(report)
                report.Balance = data['Balance'] - data['Cash_Taken']
                return redirect('reports')
    else:
        context = {
            'form': form
        }
        return render(request, 'add_report.html', context)

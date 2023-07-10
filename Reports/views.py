from django.shortcuts import render
from .forms import ReportForm

def reports(request):
    
    return render(request, 'reports.html')

def add_report(request):
    data = {
        'Sales': 0,
        'Printing': 0,
        'Grand_Total': 0,
    }
    form = ReportForm(initial=data)
    context = {
        'form': form
    }
    return render(request, 'add_report.html', context)

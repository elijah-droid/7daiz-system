from django.shortcuts import render
from .forms import ReportForm

def reports(request):
    
    return render(request, 'reports.html')

def add_report(request):
    form = ReportForm()
    context = {
        'form': form
    }
    return render(request, 'add_report.html', context)

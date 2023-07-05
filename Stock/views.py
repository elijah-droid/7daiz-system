from django.shortcuts import render

def stock(request):
    return render(request, 'stock.html')
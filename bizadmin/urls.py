from django.contrib import admin
from django.urls import path, include
from .views import index

admin.site.title = '7daiz'

urlpatterns = [
    path('', index, name='home'),
    path('auth/', include('Auth.urls')),
    path('employees/', include('Employees.urls')),
    path('sales/', include('Sales.urls')),
    path('printing/', include('Printing.urls')),
    path('stock/', include('Stock.urls')),
    path('products/', include('Products.urls')),
    path('reports/', include('Reports.urls')),
    path('papers/', include('Papers.urls')),
    path('expenses/', include('Expenses.urls')),
    path('branches/', include('Branches.urls')),
    path('largeformat/', include('Largeformat.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from .views import index

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
    path('admin/', admin.site.urls),
]

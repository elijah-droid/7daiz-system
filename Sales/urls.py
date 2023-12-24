from django.urls import path 
from .views import sales, register, export_sales


urlpatterns = [
    path('today/', sales, name='sales'), 
    path('register/', register, name='register-sale'),
    path('export/', export_sales, name='export-sales')
]
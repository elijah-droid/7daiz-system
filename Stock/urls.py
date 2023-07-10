from django.urls import path
from .views import stock, add_stock, edit_stock


urlpatterns = [
    path('', stock, name='stock'),
    path('add/<int:product>/', add_stock, name='add-stock'),
    path('edit/<int:stock>/', edit_stock, name='edit-stock')
]
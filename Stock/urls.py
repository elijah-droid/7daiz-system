from django.urls import path
from .views import stock, add_stock


urlpatterns = [
    path('', stock, name='stock'),
    path('add/<int:product>/', add_stock, name='add-stock')
]
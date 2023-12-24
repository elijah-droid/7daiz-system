from django.urls import path
from .views import add_product, edit_product

urlpatterns = [
    path('add/', add_product, name='add-product'),
    path('edit/<int:product>/', edit_product, name='edit-product')
]
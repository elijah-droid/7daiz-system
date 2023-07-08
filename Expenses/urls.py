from django.urls import path
from .views import expenses, add_expense


urlpatterns = [
    path('', expenses, name='expenses'),
    path('new/', add_expense, name='new-expense')
]
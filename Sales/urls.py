from django.urls import path 
from .views import sales, register


urlpatterns = [
    path('today/', sales, name='sales'), 
    path('register/', register, name='register-sale')
]
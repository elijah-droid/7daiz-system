from django.urls import path
from .views import printing, register


urlpatterns = [
    path('today/', printing, name='printing'),
    path('register/', register, name='register-print')
]
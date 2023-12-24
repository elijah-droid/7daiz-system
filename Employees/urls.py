from django.urls import path
from .views import dashboard, staff


urlpatterns = [
    path('dashboard/', dashboard, name='employee-dashboard'),
    path('', staff, name='staff')
]
from django.urls import path
from .views import reports, add_report


urlpatterns = [
    path('', reports, name='reports'),
    path('add/', add_report, name='add-report')
]
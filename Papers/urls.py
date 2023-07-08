from django.urls import path
from .views import papers, add_paper


urlpatterns = [
    path('', papers, name='papers'),
    path('add/', add_paper, name='add-paper')
]
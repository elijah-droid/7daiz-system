from django.urls import path
from .views import papers, add_paper, delete_paper, edit_paper


urlpatterns = [
    path('', papers, name='papers'),
    path('add/', add_paper, name='add-paper'),
    path('edit/<int:paper>/', edit_paper, name='edit-paper'),
    path('delete/<int:paper>/', delete_paper, name="delete-paper")
]
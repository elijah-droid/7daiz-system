from django.urls import path
from .views import switch_branch

urlpatterns = [
    path('switch-branch/<int:branch>/', switch_branch, name='switch-branch'),
]
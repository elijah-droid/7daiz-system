from django.urls import path
from .views import largeformat, calculator, register_largeformat, rolls, add_roll, edit__roll

urlpatterns = [
    path('', largeformat, name="largeformat"),
    path('calculator/', calculator, name="calculator"),
    path('register/', register_largeformat, name='register-largeformat'),
    path('rolls/', rolls, name='rolls'),
    path('add-roll/', add_roll, name='add-roll'),
    path('edit-roll/<int:roll>/', edit__roll, name='edit-roll')
]
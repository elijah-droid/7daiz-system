from django.urls import path 
from .views import login, confirm_email, signup, forgot_password


urlpatterns = [
    path('login/', login, name='login'),
    path('confirm-email/', confirm_email, name='confirm-email'),
    path('signup/<int:confirmation>/', signup, name="signup"),
    path('forgot-password/', forgot_password, name='forgot-password')
]
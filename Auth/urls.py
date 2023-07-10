from django.urls import path 
from .views import login_user, confirm_email, signup, forgot_password, logout


urlpatterns = [
    path('login/', login_user, name='login'),
    path('confirm-email/', confirm_email, name='confirm-email'),
    path('signup/<int:confirmation>/', signup, name="signup"),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('logout/', logout, name='logout')
]
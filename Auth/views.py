from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import send_mail
import random
from .models import EmailConfirmation
from django.contrib.auth.models import User

def generate_otp():
    code = random.randint(111111, 999999)
    return code

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee-dashboard')
        else:
            messages.success(request, 'Invalid Login Credentials')
            return redirect('.')
    else:
        return render(request, 'login.html')


def confirm_email(request):
    if request.method == 'POST':
        code =  generate_otp()
        message = f'''
            Your O-T-P code is {code}
        '''
        send_mail(
            'Email Confirmation',
            message,
            '7daiz <info@edu-metrics.com>',
            [request.POST['email'],]
        )
        try:
            confirmation = EmailConfirmation.objects.get(email=request.POST['email'])
            confirmation.code = code
            confirmation.save()
        except EmailConfirmation.DoesNotExist:
            confirmation = EmailConfirmation.objects.create(
                email = request.POST['email'],
                code=code
            )
        return redirect('signup', confirmation=confirmation.id)
    else:
        return render(request, 'confirm_email.html')

def signup(request, confirmation):
    confirmation = EmailConfirmation.objects.get(id=confirmation)
    if request.method == 'POST':
        if int(request.POST['code']) == confirmation.code:
            data = request.POST
            if data['password'] == data['confirmpassword']:
                user = User.objects.create(
                    username=confirmation.email,
                    first_name=data['firstname'],
                    last_name=data['lastname'],
                    email=confirmation.email,
                    password=make_password(request.POST['password'])
                )
                messages.success(request, 'Account created successfully.')
                return redirect('login')
            else:
                messages.success(request, 'Passwords do not match.')
                return redirect('.')
        else:
            messages.success(request, 'Invalid Code')
            return redirect('.')
    else:
        return render(request, 'signup.html')

def forgot_password(request):
    if request.method == 'POST':
        return redirect('reset-password', reset=1)
    else:
        return render(request, 'forgot_password.html')


def reset_password(request, reset):
    if request.method == 'POST':
        
        return redirect('login')
    else:
        return render(request, 'reset_password.html')
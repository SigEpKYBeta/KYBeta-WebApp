from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .models import User
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']

            user = User.objects.create_user(email, first_name, last_name, password)
            return render(request, 'accounts/success.html')
    else:
        reg_form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': reg_form})


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(username=email, password=password)
            if user is not None and user.is_active:
                auth_login(request, user)
                return redirect('/index')
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'form': login_form})


def logout(request):
    auth_logout(request)
    return redirect('/index')

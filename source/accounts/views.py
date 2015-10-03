from django.shortcuts import render, redirect

from accounts.models import User, UserManager
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user = User.objects.create_user(request.POST['email'], request.POST['first_name'],
                    request.POST['last_name'], request.POST['password'])
            return render(request, 'accounts/success.html') 

    else:
        reg_form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': reg_form})

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if reg_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
    else:
        login_form = LoginForm()
    return render(request, 'accounts/login.html', {'form': login_form})


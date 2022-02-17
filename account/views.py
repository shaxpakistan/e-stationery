from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.db import IntegrityError
from .forms import RegisterForm

#creating registration view to handle inputs for new user
User = get_user_model()
def UserRegister(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # throw message when user successfuk created
            messages.success(request, 'Account was sucessful created for '+user)
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('port')

        else:
            messages.info(request, "Incorrect username or password")

    context = {}
    return render(request, 'user/login.html', context)


# legal.com/logout/
# this terminate user authentication
def logout(request):
	logout(request)
	messages.success(request, 'Logged out successfully')
	return redirect('homepage')

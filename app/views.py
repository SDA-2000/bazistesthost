from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Register, Login, Change
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse

def red(request):
    return redirect(reverse('login'))
    
def profile(request, username = ''):
    if request.method == 'GET':
        user_prof = User.objects.get(username=username)
        users = User.objects.all()
        data = {"user_prof" : user_prof, "users" : users}
        return render(request, 'apply.html', data)

def login(request):
    if request.method == "POST":
        log_form = Login(request.POST)
        if log_form.is_valid():
            username = log_form.cleaned_data.get('username')
            password = log_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return redirect(f'../profile/{username}')
            else:
                log_form.add_error(None, 'Invalid username or password')
    else:
        log_form = Login()
        data = {"log_form" : log_form}
        return render(request, 'login.html', data)


def registration(request):
    if request.method == "POST":
        reg_form = Register(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            data = {"new_user" : new_user}

            new_user.save()
            return redirect(reverse('login'))
        else:
            data = {"reg_form" : reg_form}
            return render(request, 'register.html', data)
    else:
        reg_form = Register()
        data = {"reg_form" : reg_form}
        return render(request, 'register.html', data)

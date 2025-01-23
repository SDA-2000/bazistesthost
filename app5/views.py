from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, Register, Login, Change
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse

def get_endp(request):

    if request.method == 'GET':
        form = NameForm()

        data = {"form" : form} 
    
        return render(request, 'form.html', data)

    if request.method == 'POST':

        form = NameForm(request.POST)

        your_name = request.POST['your_name']

        data = {"your_name" : your_name}
        
        if form.is_valid():
            return render(request, "apply.html", data)
    
def get2_endp_crud_read(request, username = ''):
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

def change_user_data(request, username: str, change_user: str):
    user = User.objects.get(username=change_user)
    change_us = User.objects.get(username=change_user)

    if request.method == 'GET':
        change_form = Change(instance=change_us)
        data = {"change_form" : change_form, "username" : change_us}
        return render(request, 'changing.html', data)

    if request.method == 'POST':
        change_form = Change(request.POST, instance=change_us)
        if change_form.is_valid():
            change_form.save()
            return redirect(reverse('profile', kwargs={'username' : User.objects.get(username=username)}))
        else:
            change_form = Change(instance=change_us)
            data = {"change_form" : change_form, "username" : change_us}
            return render(request, 'changing.html', data)


def delete_user(request, username: str, del_user : str):
    user = User.objects.get(username=del_user)
    user.delete()
    return redirect(reverse('profile', kwargs={'username' : User.objects.get(username=username)}))
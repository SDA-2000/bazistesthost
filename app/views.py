from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Register, Change
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.urls import reverse

def red(request):
    return redirect(reverse('profile', kwargs={'username' : User.objects.get(username='sda')}))
    
def profile(request, username = ''):
    if request.method == 'GET':
        user_prof = User.objects.get(username=username)
        users = User.objects.all()
        data = {"user_prof" : user_prof, "users" : users}
        return render(request, 'apply.html', data)

def add_user(request, username: str):
    if request.method == "POST":
        reg_form = Register(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password'])
            data = {"new_user" : new_user}

            new_user.save()
            return redirect(reverse('profile', kwargs={'username' : User.objects.get(username=username)}))
        else:
            data = {"reg_form" : reg_form}
            return render(request, 'add_user.html', data)
    else:
        reg_form = Register()
        data = {"reg_form" : reg_form}
        return render(request, 'add_user.html', data)

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
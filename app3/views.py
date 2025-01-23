from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def red(request):
    return redirect(reverse('endp'))

def endp(request):
    if request.method == "GET":
        data = {"met" : "rly get"}
        return render(request, 'endp.html', data)
    if request.method == "POST":
        return redirect(reverse('post'))
    
def post(request):
    return HttpResponse("<h1>POST RESPONSE</h1>")
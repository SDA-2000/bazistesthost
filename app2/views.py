from django.shortcuts import render

def get1(request):
    if request.method == 'GET':
        return render(request, 'get1.html')

def get2(request):
    if request.method == 'GET':
        return render(request, 'get2.html')

def post1(request):
    if request.method == 'POST':
        return render(request, 'post1.html')
from django.http import HttpResponse

def get_endp(request):
    return HttpResponse("Hello World!")
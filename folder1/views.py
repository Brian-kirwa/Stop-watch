from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Brian! Welcome to Django my name .")


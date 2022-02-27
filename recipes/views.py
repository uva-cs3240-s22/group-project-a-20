from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, home page! Go to /login to log in")

#temp pre-login
def pre(request):
    return HttpResponse("Hello, you are not logged in yet")

#temp post-login
def post(request):
    return HttpResponse("Hello, you are logged in!")

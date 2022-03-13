from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    return render(request, 'recipes/home.html', context)

#temp pre-login
def login(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    return render(request, 'recipes/login.html', context)

#temp post-login
#I don't fully know how the api works so imma include this as well
def loggedIn(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    return render(request, 'recipes/loggedin.html', context)

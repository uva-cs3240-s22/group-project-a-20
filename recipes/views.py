from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    template = loader.get_template('recipes/home.html')
    return HttpResponse(template.render(context, request))

#temp pre-login
def pre(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    template = loader.get_template('recipes/login.html')
    return HttpResponse(template.render(context, request))

#temp post-login
def post(request):
    name = "you are not logged in"
    context = {
        "name" : name,
        }
    template = loader.get_template('recipes/loggedin.html')
    return HttpResponse(template.render(context, request))

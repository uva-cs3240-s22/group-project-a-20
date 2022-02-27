from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.pre, name = 'pre'),
    path('loggedIn', views.post, name = 'post'),
]
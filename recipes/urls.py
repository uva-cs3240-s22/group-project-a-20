from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('loggedIn', views.loggedIn, name = 'loggedIn'),
    # for account authentication
    path('accounts/', include('allauth.urls')),
]
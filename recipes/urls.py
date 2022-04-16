from django.urls import path, include

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.login, name = 'login'),
    # path('loggedIn', views.loggedIn, name = 'loggedIn'),
    # path('recipes/profile/', views.get_profile, name = 'profile'),
    path('recipes/form/', views.get_recipe, name = 'recipeform'),
    path('recipes/list/', views.RecipeListView.as_view(), name = 'recipelist'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name = 'recipe'),
    path('recipes/fork/<int:pk>/', views.fork_recipe, name = "forkrecipe"),
    # for account authentication
    path('accounts/', include('allauth.urls')),
    # for comments
    path('recipes/<int:pk>/comments/', include('django_comments_xtd.urls')),
]
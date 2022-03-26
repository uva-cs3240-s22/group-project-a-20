from django.urls import path, include

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('loggedIn', views.loggedIn, name = 'loggedIn'),
    path('recipe/form/', views.get_recipe, name = 'recipeform'),
    path('recipe/list/', views.RecipeListView.as_view(), name = 'recipelist'),
    path('recipe/<int:pk>/', views.RecipeView.as_view(), name = 'recipe'),
    # for account authentication
    path('accounts/', include('allauth.urls')),
]
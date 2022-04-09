from django.urls import path, include

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name = 'login'),
    path('loggedIn', views.loggedIn, name = 'loggedIn'),
    path('recipes/form/', views.get_recipe, name = 'recipeform'),
    path('recipes/list/', views.RecipeListView.as_view(), name = 'recipelist'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name = 'recipe'),
    path('recipes/editedrecipe', view.views.EditedRecipesList.as_view(), name = 'editedrecipeslist')
    # path('recipes/editedlist', ) - not sure if want to use the original recipe view for the edited recipes as well
    # for account authentication
    path('accounts/', include('allauth.urls')),
]
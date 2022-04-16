from django.urls import path, include

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.login, name = 'login'),
    # path('loggedIn', views.loggedIn, name = 'loggedIn'),
    path('profile/<int:pk>', views.profile_detail.as_view(), name = 'profile'),
    path('profile/<int:pk>/edit/', views.profile_edit.as_view(), name = "editprofile"),
    path('profile/<int:pk>/update/', views.updateProfile, name = "updateProfile"),
    path('recipes/form/', views.get_recipe, name = 'recipeform'),
    path('recipes/list/', views.RecipeListView.as_view(), name = 'recipelist'),
    path('recipes/<int:pk>/', views.RecipeView.as_view(), name = 'recipe'),
    path('recipes/fork/<int:pk>/', views.fork_recipe, name = "forkrecipe"),
    # for account authentication
    path('accounts/', include('allauth.urls')),
]
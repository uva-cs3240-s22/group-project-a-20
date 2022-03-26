from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .forms import RecipeForm
from .models import Recipe

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

# Handles recipe submission. By default it takes you to the form to submit a recipe. 
# When you submit a recipe, it can handle the data and redirect to the new recipe page
def get_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe.id,)))
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipeform.html', {'form': form})

# Brings you to the list of recipes, ordered by date submitted
class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/recipelist.html'
    context_object_name = 'recipes_list'

    def get_queryset(self):
        return Recipe.objects.order_by('pub_date')

class RecipeView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe.html'
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import RecipeForm
from .models import Recipe

def home(request):
    # recipe_list = Recipe.objects.values_list('recipe_title', 'img', 'pk')[:3]

    recipe_list = Recipe.objects.exclude(img__exact='')[:3]
    return render(request, 'recipes/home.html', {'recipe_list': recipe_list})

#temp pre-login
# def login(request):
#     name = "you are not logged in"
#     context = {
#         "name" : name,
#         }
#     return render(request, 'recipes/login.html', context)
#
# #temp post-login
# #I don't fully know how the api works so imma include this as well
# def loggedIn(request):
#     name = "you are not logged in"
#     context = {
#         "name" : name,
#         }
#     return render(request, 'recipes/loggedin.html', context)

# Handles recipe submission. By default it takes you to the form to submit a recipe. 
# When you submit a recipe, it can handle the data and redirect to the new recipe page
def get_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            '''recipe.author = request.user
            recipe.save(update_fields=['author'])'''
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe.id,)))
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipeform.html', {'form': form})

def fork_recipe(request, pk):
    parent = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.parent = parent
            recipe.save()
            '''if (recipe.img == None):
                recipe.img = parent.img
                recipe.save(update_fields=['img'])'''
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe.id,)))
    else:
        form = RecipeForm(
            {'recipe_title': parent.recipe_title, 
            'recipe_ingredients': parent.recipe_ingredients, 
            'recipe_instructions': parent.recipe_instructions, 
            'img': parent.img},
            initial={'img': parent.img}
            )
    return render(request, 'recipes/recipeform.html', {'form': form, 'recipe': parent})

'''class RecipeForkCreateView(generic.edit.CreateView):
    model = Recipe
    form_class=RecipeForm

    def get_initial(self, *args, **kwargs):
        initial = super(RecipeForkCreateView, self).get_initial(**kwargs)
        initial['recipe_title'] = self.request.recipe_title
        initial['recipe_ingredients'] = self.request.recipe_ingredients
        initial['recipe_instructions'] = self.request.recipe_instructions
        return initial
'''

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
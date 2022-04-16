from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from .forms import RecipeForm
from .models import Recipe, Profile

def home(request):
    recipe_list = Recipe.objects.exclude(img__exact='')[:3]
    return render(request, 'recipes/home.html', {'recipe_list': recipe_list})

#for personal profile, so editable
class profile_detail(generic.DetailView):
    model = Profile
    template_name = 'recipes/profile.html'

@method_decorator(login_required, name='dispatch')
class profile_edit(generic.DetailView):
    model = Profile
    template_name = 'recipes/editprofile.html'

def updateProfile(request, pk):
    profile = get_object_or_404(Profile, pk = pk)
    if request.POST['gender']:
        profile.gender = request.POST['gender']
    if request.POST['bday']:
        profile.birthday = request.POST['bday']
    if request.POST['bio']:
        profile.bio = request.POST['bio']

    
    
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    profile.save()
    return HttpResponseRedirect(reverse('recipes:profile', args=(profile.id,)))

# Handles recipe submission. By default it takes you to the form to submit a recipe. 
# When you submit a recipe, it can handle the data and redirect to the new recipe page
def get_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe.id,)))
    else:
        form = RecipeForm()

    return render(request, 'recipes/recipeform.html', {'form': form})

def fork_recipe(request, pk):
    parent = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.parent = parent
            recipe.author = request.user
            recipe.save()
            if (recipe.img == None):
                recipe.img = parent.img
                recipe.save(update_fields=['img'])
            return HttpResponseRedirect(reverse('recipes:recipe', args=(recipe.id,)))
    else:
        form = RecipeForm(
            {'recipe_title': parent.recipe_title, 
            'recipe_ingredients': parent.recipe_ingredients, 
            'recipe_instructions': parent.recipe_instructions, },
            initial={'img': parent.img}
        )
    return render(request, 'recipes/recipeform.html', {'form': form, 'recipe': parent})

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
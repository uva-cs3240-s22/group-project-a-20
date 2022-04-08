from django.shortcuts import render, get_object_or_404
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
    # name = "you are not logged in"
    # context = {
    #     "name" : name,
    #     }
    # return render(request, 'recipes/home.html', context)
    return render(request, 'recipes/index.html')

#for personal profile, so editable
class profile_detail(generic.DetailView):
    model = Profile
    template_name = 'recipes/profile.html'

#def get_profile(request, key):
    #user = get_object_or_404(Profile, pk = key)
    #return render(request, 'recipes/profile.html')

@method_decorator(login_required, name='dispatch')
class profile_edit(generic.DetailView):
    model = Profile
    template_name = 'recipes/editprofile.html'

#def edit_profile(request):
    #user = get_object_or_404(Profile)
    #if(request.POST['gender']):
    #    user.gender = request.POST['gender']

    #return render(request, 'recipes/editprofile.html')

# class ProfileView(View):
#     profile = None
#
#     def




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
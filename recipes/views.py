from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models import Count

from .forms import RecipeForm
from .models import Recipe, Profile

def home(request):
    # recipe_list = Recipe.objects.exclude(img__exact='')[:3]
    topfavs = Recipe.objects.annotate(num_favs=Count('favorite')).order_by('-num_favs').exclude(img__exact='')[:3]
    # topfavs[0].num_favs
    return render(request, 'recipes/home.html', {'recipe_list': topfavs})

def profile(request, pk): 
    user = get_object_or_404(User, pk = pk)
    try: 
        profile = user.profile
    except (Profile.DoesNotExist):
        profile = Profile()
        profile.user = user
        profile.save()
        return HttpResponseRedirect(reverse('recipes:editprofile', args=(profile.id,)))
    favorites = user.favorites.all()
    authored = user.recipe_set.all()
    return render(request, 'recipes/profile.html', {'profile': profile, 'favorites': favorites, 'authored': authored})

@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(generic.UpdateView):
    model = Profile
    fields = ['gender', 'birthday', 'bio']
    template_name = 'recipes/editprofile.html'
    def get_success_url(self):
        return reverse('recipes:profile', kwargs={'pk': self.object.user.id})

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_set'] = self.get_object().favorite.all()
        return context

def favorite(request, recipe_id, user_id):
    recipe = Recipe.objects.get(pk = recipe_id)
    user = User.objects.get(pk = user_id)
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        try:
            user.favorites.get(pk = recipe_id)
        except (Recipe.DoesNotExist):
            user.favorites.add(recipe)
        else:
            user.favorites.remove(recipe)
    return HttpResponseRedirect(next)
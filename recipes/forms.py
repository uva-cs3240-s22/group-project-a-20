from django import forms
from recipes.models import EditRecipe, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_title', 'recipe_instructions']

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = EditRecipe
        fields = ['recipe_title','recipe_instructions']

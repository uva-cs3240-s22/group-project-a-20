from django import forms
from recipes.models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_title', 'recipe_ingredients', 'recipe_instructions']

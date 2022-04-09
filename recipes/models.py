from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_instructions = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)

class EditRecipe(models.Model):
    originalRecipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=100)
    recipe_instructions = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_ingredients = ArrayField(base_field=models.CharField(max_length=100), null=True)
    recipe_instructions = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)

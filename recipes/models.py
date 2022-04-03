from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_instructions = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.recipe_title

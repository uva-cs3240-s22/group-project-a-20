from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_ingredients = ArrayField(base_field=models.CharField(max_length=100), null=True)
    recipe_instructions = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.recipe_title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # implement this when we have an image database
    # avatar = models.ImageField(default = 'default.jpg', upload_to = 'profile_images')
    gender = models.CharField(max_length=15, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField()
    
    # implement this when our recipe database is updated
    # saved_recipes =
    # created_recipes =

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

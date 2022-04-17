from django.test import TestCase
from recipes.models import Recipe, Profile
from django.contrib.auth.models import User
from django.urls import reverse

# from django.core.exceptions import ObjectDoesNotExist
# import pytest

def createRecipe(title):
    # Create some recipes
    return Recipe.objects.create(recipe_title=title)

class DummyTests(TestCase):
    def test_1(self):
        self.assertIs(True, True)

class ModelsTests(TestCase):
    def setUp(self):
        # Create some users
        self.user_1 = User.objects.create_user('Fippy Darkpaw', 'fippy@freeport.com', 'Grrrbarkbarkgrrrr')

    #Recipe
    def test_recipe_name_to_string(self):
        porkchop = createRecipe("pork chops")
        self.assertEqual(str(porkchop), "pork chops")

    def test_recipe_name_length_limit(self):
        createRecipe("This really long name for a Scandinavian recipe my grandmother from Blokumannaland gave me.")
        #shouldn't insert this; it's > 100 chars
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(recipe_title="This really long name for a Scandinavian recipe my grandmother from Blokumannaland gave me that her grandmother gave her.")


    #Profile
    def test_profile_name_to_string(self):
        self.assertEqual(str(self.user_1), "Fippy Darkpaw")

class ViewsTests(TestCase):
    def test_recipe_list_empty_view(self):
        response = self.client.get(reverse('recipes:recipelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Waiting for recipes.')

    def test_multiple_recipe_list_view(self):
        porkchop = createRecipe("pork chops")
        muffins = createRecipe("muffins")
        response = self.client.get(reverse('recipes:recipelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, porkchop.recipe_title)
        self.assertContains(response, muffins)

    def test_recipe_view(self):
        cookies = createRecipe("cookies")
        response = self.client.get(reverse('recipes:recipe/1'))



#class RecipePageDisplayed(TestCase):
#    def build_and_show_recipe():

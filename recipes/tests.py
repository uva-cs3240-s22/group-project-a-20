from django.test import TestCase
# import pytest
from recipes.models import Recipe, Profile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

#We'll need to import the models once we make them
#from recipes.models import _________

class DummyTests(TestCase):
    def test_1(self):
        self.assertIs(True, True)

class ModelsTests(TestCase):
    def setUp(self):
        # Create some recipes
        Recipe.objects.create(recipe_title="pork chops")
        Recipe.objects.create(recipe_title="This really long name for a Scandinavian recipe my grandmother from Blokumannaland gave me.")

        # Create some users
        self.user_1 = User.objects.create_user('Fippy Darkpaw', 'fippy@freeport.com', 'Grrrbarkbarkgrrrr')

    #Recipe
    def test_recipe_name_to_string(self):
        porkchop = Recipe.objects.get(recipe_title="pork chops")
        self.assertEqual(str(porkchop), "pork chops")

    def test_recipe_name_length_limit(self):
        #shouldn't insert this
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(recipe_title="This really long name for a Scandinavian recipe my grandmother from Blokumannaland gave me that her grandmother gave her.")


    #Profile
    def test_profile_name_to_string(self):
        self.assertEqual(str(self.user_1), "Fippy Darkpaw")


#class RecipePageDisplayed(TestCase):
#    def build_and_show_recipe():

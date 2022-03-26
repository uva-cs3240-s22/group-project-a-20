from django.test import TestCase
import pytest
from recipes.models import Recipe

#We'll need to import the models once we make them
#from recipes.models import _________

class DummyTests(TestCase):
    def test_1(self):
        self.assertIs(True, True)

#class RecipePageDisplayed(TestCase):
#    def build_and_show_recipe():

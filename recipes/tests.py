from django.test import TestCase
#We'll need to import the models once we make them
#from recipes.models import _________

class DummyTests(TestCase):
    def test_1(self):
        self.assertIs(True, True)


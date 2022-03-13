from django.test import TestCase

class DummyTests(TestCase):
    def test_1(self):
        self.assertIs(True, True)


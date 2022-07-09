from django.test import TestCase

class ExemploTestCase(TestCase):
    def test_exemplo(self):
        a=2
        b=2
        self.assertTrue(a+b==4)
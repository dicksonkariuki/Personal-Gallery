from django.test import TestCase
import datetime as dt
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    """
    Creating an instance of Image
    """
    def setUp(self):
        self.depic = Image(name ='Movie',description='Watching movies is the best way to spend free time')
    """
    Test instance of image
    """
    def test_instance(self)
        self.assertTrue(isinstance(self.depic,Image))

# Create your tests here.

from django.test import TestCase
import datetime as dt
from .models import Image,Category,Location

class ImageTestClass(TestCase):
    """
    Creating an instance of Image
    """
    def setUp(self):
        self.pic = Image(name ='Movie',description='Watching movies is the best way to spend free time')

# Create your tests here.

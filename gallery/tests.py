from django.test import TestCase
import datetime as dt
from .models import Image,Categorys,Location

class ImageTestClass(TestCase):
    """
    Creating an instance of Image
    """
    def setUp(self):
        self.depic = Image(name ='Movie',description='Watching movies is the best way to spend free time')
    """
    Test instance of image
    """
    def test_instance(self):
        self.assertTrue(isinstance(self.depic,Image))
    """
    Test to delete image
    """
    def test_delete_image(self):
        self.depic.save_image()
        self.depic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
    def test_save_image(self):
        self.depic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_get_image_today(self):
        today_images = Image.todays_images()
        self.assertTrue(len(today_images)>0)
class LocationTestClass(TestCase):
    """
    Setup for location class test
    """
    def Setup(self):
        self.New=Location(name ='New')
    """
    Test for location instance
    """
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Location))
    '''
    test to assertain save Location
    '''
    def test_save_location(self):
        self.New.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0)
    

# Create your tests here.

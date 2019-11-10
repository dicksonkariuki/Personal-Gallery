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
    '''
    test to confirm delete is working
    '''
    def test_delete_location(self):
        self.New.save_location()
        self.New.delete_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)== 0)
    '''
    test to ensure Location update
    '''
    def test_update_location(self):
        self.New.save_location()
        new = Location.objects.filter(name='New').update(name='outdated')
        loc = Location.objects.get(name='outdated')
        self.assertEqual(loc.name,'outdated') 
class CategorysTestClass(TestCase):
        '''
    test setup of Categorys
    '''
    def setUp(self):
        self.New = Categorys(name='New')
     '''
    test instance of category
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.New,Categorys))
    '''
    test to assertain save category
    '''
    def test_save_category(self):
        self.New.save_category()
        cat = Categorys.objects.all()
        self.assertTrue(len(cat)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_category(self):
        self.New.save_category()
        self.New.delete_category()
        cat = Categorys.objects.all()
        self.assertTrue(len(cat)== 0)
    '''
    test to assert that categorys update
    '''
    def test_update_category(self):
        self.New.save_category()
        new = Categorys.objects.filter(name='New').update(name='outdated')
        cat = Categorys.objects.get(name='outdated')
        self.assertEqual(cat.name,'outdated') 



# Create your tests here.

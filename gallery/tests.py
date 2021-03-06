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
    def SetUp(self):
        self.Nairobi=Location(name ='Nairobi')
    """
    Test for location instance
    """
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))
    
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
        catego = Categorys.objects.all()
        self.assertTrue(len(catego)>0)
    '''
    test to assert that delete is working
    '''
    def test_delete_category(self):
        self.New.save_category()
        self.New.delete_category()
        catego = Categorys.objects.all()
        self.assertTrue(len(catego)== 0)
    '''
    test to assert that categorys update
    '''
    def test_update_category(self):
        self.New.save_category()
        New = Categorys.objects.filter(name='New').update(name='outdated')
        catego = Categorys.objects.get(name='outdated')
        self.assertEqual(catego.name,'outdated') 



# Create your tests here.

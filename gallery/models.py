from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=20)

# class Image(models.Model):
#     name = models.CharField(max_length = 30)
#     Description = models.TextField()
#     location = models.ForeignKey(Location)
#     category = models.ManyToManyField(Categorys, default = True)
#     pub_date = models.DateTimeField(auto_now_add=True, null=True)
#     Image_image = models.ImageField(upload_to = 'images/')

from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']

    def save_location(self):
        self.save()

    def delete_location(self):
        sel.delete()

# class Image(models.Model):
#     name = models.CharField(max_length = 30)
#     Description = models.TextField()
#     location = models.ForeignKey(Location)
#     category = models.ManyToManyField(Categorys, default = True)
#     pub_date = models.DateTimeField(auto_now_add=True, null=True)
#     Image_image = models.ImageField(upload_to = 'images/')

"""
Definition of models.
"""

from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('thumbnails', str(instance.id), filename)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    introduction = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title
		

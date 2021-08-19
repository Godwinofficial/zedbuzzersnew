from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from cloudinary.models import CloudinaryField



# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(null=True, unique=True)
  
  def __str__(self):
    return self.title



class Post(models.Model):
  image       = CloudinaryField('images', use_filename=True, unique_filename=False, blank=True)
  file        = CloudinaryField('files',use_filename=True, unique_filename=False, resource_type='raw', blank=True)
  link        = models.URLField(null=True, blank=True)
  name        = models.CharField(blank=True, max_length=100)
  title       = models.CharField(blank=True, max_length=100)
  category    = models.ForeignKey(Category, on_delete=CASCADE)
  time_stamp  = models.DateTimeField(auto_created=True)
  posted_by   = models.CharField(max_length=30, default='Godwin')
  description = models.TextField(max_length=90000, blank=True)
  post_views  = models.IntegerField(default=0)
  slug        = models.SlugField(null=True, unique=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self, *args, **kwargs):
    return reverse('post-details', kwargs={'slug': self.slug})




class Ads(models.Model):
  name        = models.CharField(max_length=500, null=True)
  ad_file     = CloudinaryField('images', null=True, resource_type='raw')

  def __str__(self):
    return self.name

 


  
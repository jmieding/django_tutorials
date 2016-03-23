from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Category(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, unique=False, default='')

  def __unicode__(self):
    return self.title

class Post(models.Model):
  title = models.CharField(max_length=400)
  text = HTMLField()
  published_date = models.DateTimeField()
  slug = models.SlugField(max_length=400, unique=False, default='')
  categories = models.ManyToManyField(Category)
  published = models.BooleanField(default=False)

  def publish(self):
    if not self.id:
      self.slug = slugify(self.title)
      self.published_date = timezone.now()
    self.save()

  def __unicode__(self):
    return self.title

class Comment(models.Model):
  author = models.CharField(max_length=100)
  text = models.CharField(max_length=1000)
  date = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post)

  def __unicode__(self):
    return self.text[0:50]+'...'

# Create your models here.
# sample model syntax:

#class ModelName(models.Model):
#   email = models.EmailField()
#   full_name = models.CharField(max_length=120, blank = True, null=True)
#   timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
#   updated = models.DateTimeField(auto_now_add = False, auto_now = True)

#   def __unicode__(self): # in Python 3.3, this is __str__
#     return self.email
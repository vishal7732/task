from django.db import models
from django.utils.text import slugify
import string 
import random
from django.db.models.signals import pre_save

# Create your models here.


class Category(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False)
    image = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=50,blank=True)
    new_price = models.IntegerField(default=0)
    description = models.TextField(max_length=500)
    Width = models.CharField(max_length=50)
    Height = models.CharField(max_length=50)
    Depth = models.CharField(max_length=50)
    Weight = models.CharField(max_length=50)
    metatitle = models.CharField(max_length=100, blank=True, null=True)
    metadesc = models.CharField(max_length=250, blank=True, null=True)

    

    def __str__(self):
        return self.Name

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.Name) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
  
pre_save.connect(pre_save_receiver, sender = Product)
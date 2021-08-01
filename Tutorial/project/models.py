from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    technology=models.CharField(max_length=100,default='',null=False)
    title=models.CharField(max_length=100,default='',null=False)
    description=models.TextField(default='',null=False)
    slug=models.SlugField(null=False,unique=True,default='')
    img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_details',kwargs={'slug':self.slug})
    
    
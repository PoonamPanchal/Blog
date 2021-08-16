from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Category(models.Model):
    name = models.CharField(max_length=100, default='', null=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    technology = models.CharField(max_length=100, default='', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)
    title = models.CharField(max_length=100, default='', null=False)
    description = models.TextField(default='', null=False)
    slug = models.SlugField(null=False, unique=True, default='')
    status = models.IntegerField(choices=STATUS, default=0)
    img = models.ImageField(upload_to='images/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

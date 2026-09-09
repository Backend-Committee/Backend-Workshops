from xml.parsers.expat import model

from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_data = models.DateField(auto_now_add=True)

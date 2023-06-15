# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=20) 
    description = models.TextField()
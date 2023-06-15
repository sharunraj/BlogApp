from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    course = models.CharField(max_length=20)

class Course(models.Model):
    courseName = models.CharField(max_length=20)
    courseDate = models.DateField()
    duration = models.DecimalField(decimal_places=3,max_digits=200)
from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    course=models.CharField(max_length=10)
    marks=models.IntegerField()

    def __str__(self):
      return self.name
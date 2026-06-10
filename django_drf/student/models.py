from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.EmailField(max_length=10)
    email=models.CharField(max_length=10)
    age=models.IntegerField()
    course=models.CharField(max_length=10)


def __str__(self):
    return self.name
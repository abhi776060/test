from django.db import models


# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    email=models.EmailField()
    password1=models.CharField(max_length=20)
    

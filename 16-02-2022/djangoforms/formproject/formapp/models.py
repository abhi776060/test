
from django.db import models



# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    second_name=models.CharField(max_length=20)
    email=models.EmailField()
    password1=models.CharField(max_length=20)
class Item(models.Model):
    item_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    price=models.IntegerField(null=True)
    img=models.URLField() 
    discription=models.CharField(max_length=100000,null=True)
    

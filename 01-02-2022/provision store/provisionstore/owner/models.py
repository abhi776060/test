from django.db import models

# Create your models here.
class Credential(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.CharField(max_length=10,unique=True)
    password=models.IntegerField()
class Items(models.Model):
    name=models.CharField(max_length=10)
    price=models.FloatField()
    quantity=models.FloatField()



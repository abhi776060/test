from django.db import models

# Create your models here.
class Vote(models.Model):
    question=models.CharField(max_length=50)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    v1=models.IntegerField()
    v2=models.IntegerField(default=0)
    v3=models.IntegerField(default=0)
    v4=models.IntegerField(default=0)

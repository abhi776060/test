from django.db import models

# Create your models here.
class Credential(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.CharField(max_length=10,unique=True)
    password=models.IntegerField()
    
    def authenticate(self,username,password):
        self.username=username
        return username
    
    def login(self,username):
        self.username=username
        return self.username

    def logout(self):
        return ''
    


class Items(models.Model):
    name=models.CharField(max_length=10)
    price=models.FloatField()
    quantity=models.FloatField()

class Authentication:
    def login(self,a):
        return self.a
    def logout(self):
        return ''


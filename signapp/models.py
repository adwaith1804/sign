from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class StudentsMod(models.Model):
    admissionno = models.CharField(max_length=12)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    guardianName = models.CharField(max_length=30)
    guradPhone = models.CharField(max_length=10)
    userName = models.CharField(max_length=6)
    gender = models.CharField(max_length=7)
    email = models.CharField(max_length=30,unique=True)
    
    
    
    
    
      
# Create your models here.

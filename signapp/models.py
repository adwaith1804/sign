from django.db import models

class MyModel(models.Model):
    Teachername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    
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

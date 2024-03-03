from django.db import models

# class MyModel(models.Model):
#     Teachername = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     age = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30,unique=True)
    
#     def __str__(self):
#         return self.name
class StudentsMod(models.Model):
    admissionno = models.CharField(primary_key=True,max_length=12)
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    guardianName = models.CharField(max_length=30)
    guradPhone = models.CharField(max_length=10)
    userName = models.CharField(max_length=6)
    gender = models.CharField(max_length=7)
    email = models.CharField(max_length=30,unique=True)
class ModelForTeacher(models.Model):
    teachid = models.AutoField(primary_key=True)
    teachername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True) 
class TableOfNotifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=70)
    current_date = models.DateField(null=True)
class TableForDoubt(models.Model):
    doubtid = models.AutoField(primary_key=True)
    doubt = models.CharField(max_length=1000)
    teacherloginid = models.CharField(max_length=10)
    studentloginid= models.CharField(max_length=50)
    currentdate= models.DateField(null=True)
    reply=models.CharField(max_length=50)
    

    
      
# Create your models here.

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
    classstud = models.CharField(max_length=5)
    contact = models.CharField(max_length=10)
    guardianName = models.CharField(max_length=30)
    guradPhone = models.CharField(max_length=10)
    userName = models.CharField(max_length=6)
    gender = models.CharField(max_length=7)
    email = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=32, default=None, blank=True, null=True)
    usertype = models.CharField(max_length=100,default='Student')
    
    
class ModelForTeacher(models.Model):
    teachid = models.AutoField(primary_key=True)
    teachername = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True) 
    password = models.CharField(max_length=32, default=None, blank=True, null=True)
    usertype=models.CharField(max_length=100,default='Teacher')
    
    
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

class LoginModel(models.Model):
    email=models.EmailField(max_length=254)
    password = models.CharField(max_length=34)
    
class AttendanceMod(models.Model):
    attendanceid = models.AutoField(primary_key=True)
    studentsaddmissionno = models.CharField(max_length=100)
    teacherid=models.CharField(max_length=100)
    currentdate= models.DateField(null=True)
    attendancestatus=models.CharField(max_length=11)

        
class ExamModel(models.Model):
    exam_key = models.AutoField(primary_key=True)
    class_student = models.CharField( max_length=5)
    question = models.CharField( max_length=100)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=5)
    current_date = models.DateField(auto_now=True)
    exam_date = models.DateField(null=True)

class AnswerModel(models.Model):
    primary_key = models.AutoField(primary_key=True)
    question_id = models.CharField(max_length=50)
    answer = models.CharField( max_length=50)
    login_id = models.CharField( max_length=50)
    current_date = models.DateField( auto_now=True)
    #teacher_id = models.CharField(max_length=50)
    

# Create your models here.

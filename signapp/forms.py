from django import forms
from .models import StudentsMod,ModelForTeacher,TableOfNotifications,TableForDoubt,LoginModel,AttendanceMod,ExamModel,AnswerModel
from datetime import date

class ModelForStud(forms.ModelForm):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())

    class Meta:
        model = StudentsMod
        fields = ['admissionno', 'name', 'classstud' , 'contact', 'guardianName', 'guradPhone', 'userName', 'gender', 'email']

        widgets = {
            'admissionno': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'guardianName': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'guradPhone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'userName': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
        }

        
class TeacherForm(forms.ModelForm):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect(attrs={'class': 'form-radio'}))
    
    class Meta:
        model = ModelForTeacher
        fields = ['teachername', 'gender', 'age', 'email']
        widgets = {
            'teachername': forms.TextInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name'}),
            'age': forms.NumberInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'appearance-none checked:bg-gray-900 checked:border-transparent ...;'}),
            'email': forms.EmailInput(attrs={'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="grid-first-name'}),

        }
class NotificationForm(forms.ModelForm):
    current_date = forms.DateField(widget=forms.HiddenInput(),initial=date.today)
    class Meta:
        model = TableOfNotifications
        fields = ['notification' ]
    widgets={
            'notification':forms.Textarea(attrs={'class': 'form-control'})
    }
class FormForDoubt(forms.ModelForm):
    currentdate = forms.DateField(widget=forms.HiddenInput(),initial=date.today)
    class Meta:
        model = TableForDoubt
        fields = ['doubt']
        widgets={
            'Doubt':forms.TextInput(attrs={'class': 'form-control'}),
        }
class FormForReply(forms.ModelForm):
    
    class Meta:
        model = TableForDoubt
        fields = ['reply']
        widgets={
            'reply':forms.TextInput(attrs={'class': 'form-control'}),
        }
 
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = ['email','password']
    
    widgets = {
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),

    }  
    
class AttendanceForm(forms.ModelForm):
    currentdate = forms.DateField(widget=forms.HiddenInput(),initial=date.today)
    Attendance = (
        ('present', 'present'),
        ('absent', 'absent'),
        
    )
    attendancestatus = forms.ChoiceField(choices=Attendance, widget=forms.RadioSelect())
    class Meta:
        model = AttendanceMod
        fields = ['attendancestatus']
    
    widgets = {
        
        'attendancestatus': forms.Select(attrs={'class': 'form-control'}),
        

    }  

class FormForExams(forms.ModelForm):
    

    class Meta:
        model = ExamModel
        fields = ['class_student', 'question', 'option1' , 'option2', 'option3', 'exam_date']

        widgets = {
            'class_student': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option1': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option2': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option3': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'exam_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'type': 'date'}),
        }    
        
class AnswerForm(forms.Form):
    question_id = forms.CharField(widget=forms.HiddenInput)
    answer = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
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
            'admissionno': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'admission'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px; ', 'name': 'name'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'class'}),
            'guardianName': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'contact'}),
            'guradPhone': forms.NumberInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'guardian'}),
            'userName': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'usernme'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'gender'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'name': 'email'}),
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
            'teachername': forms.TextInput(attrs={'class': 'custom-control-input" id="grid-first-name'}),
            'age': forms.NumberInput(attrs={'class': 'custom-control-input" id="grid-first-name'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'appearance-none checked:bg-gray-900 checked:border-transparent ...;'}),
            'email': forms.EmailInput(attrs={'class': 'custom-control-input" id="grid-first-name'}),

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
        'email': forms.EmailInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),
        'password': forms.PasswordInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'}),

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
        fields = ['class_student', 'question', 'option1' , 'option2', 'option3', 'exam_date','answer']

        widgets = {
            'class_student': forms.TextInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option1': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option2': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'option3': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;'}),
            'exam_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'border: 1px solid #ccc; padding: 10px; border-radius: 5px;', 'type': 'date'}),
        }    
        
class AnswerForm(forms.Form):
    question_id = forms.CharField(widget=forms.HiddenInput)
    answer = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
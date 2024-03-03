from django import forms
from .models import StudentsMod,ModelForTeacher,TableOfNotifications,TableForDoubt
from datetime import date

class ModelForStud(forms.ModelForm):
    GENDER=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect())
    
    class Meta:
        model = StudentsMod
        fields = ['admissionno' ,'name', 'contact', 'guardianName','guradPhone','userName','gender','email']

        widgets={
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
    GENDER=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    class Meta:
        model = ModelForTeacher
        fields = ['teachername' ,'gender', 'age', 'email']
    gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect())
    widgets={
            'teachername':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
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
    

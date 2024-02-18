from django import forms
from .models import StudentsMod,ModelForTeach

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
            'admissionno':forms.NumberInput(),
            'name':forms.TextInput(),
            'contact' : forms.NumberInput(),
            'guardianName':forms.TextInput(),
            'guradPhone':forms.NumberInput(),
            'userName':forms.TextInput(),
            'gender':forms.Select(),
            'email':forms.EmailInput(),
        }
class TeacherForm(forms.ModelForm):
    GENDER=(
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    class Meta:
        model = ModelForTeach
        fields = ['teachername' ,'gender', 'age', 'email']
    gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect())
    widgets={
            'teachername':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
        }
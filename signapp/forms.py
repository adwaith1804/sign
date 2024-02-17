from django import forms
from .models import MyModel,StudentsMod
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name' ,'contact', 'email', 'password']
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
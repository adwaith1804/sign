from django.shortcuts import render, redirect
from .forms import ModelForStud,TeacherForm
from .models import StudentsMod,ModelForTeach
#run on /sign
# def insert_data(request):
#     if request.method == 'POST':
#         form = MyModelForm(request.POST)
#         if form.is_valid():
#             form.save()
           
#             return redirect('insert_data')
            
#     else:
#         form = MyModelForm()
#     return render(request,'registeration.html', {'form': form}) 

def students_reg(request):
    if request.method =='POST':
        form = ModelForStud(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_reg')
    else:
        form = ModelForStud()  
    return render(request,'studentsreg.html', {'form': form})
def insert_data(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('insert_data')
            
    else:
        form = TeacherForm()
    return render(request,'registeration.html', {'form': form}) 
def view_teacher(request):
    my_models = ModelForTeach.objects.all()
    return render(request, 'teachtable.html', {'my_models': my_models})
def view_students(request):
    my_students = StudentsMod.objects.all()
    return render(request, 'studentstable.html', {'my_students': my_students})
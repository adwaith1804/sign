from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModelForStud, TeacherForm, NotificationForm,FormForDoubt,FormForReply
from .models import StudentsMod,ModelForTeacher,TableOfNotifications,TableForDoubt
from datetime import date
from django.db.models import Q
import random
import string
import uuid

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
    if request.method == 'POST':
        form = ModelForStud(request.POST)
        if form.is_valid():
            # Generate a unique password using uuid and take a substring
            password = str(uuid.uuid4())[:8]  # Change 8 to your desired length
            form.instance.password = password

            form.save()
            return redirect('students_reg')
    else:
        form = ModelForStud()

    return render(request, 'studentsreg.html', {'form': form})


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
    my_models = ModelForTeacher.objects.all()
    return render(request, 'teachtable.html', {'my_models': my_models})

def view_students(request):
    my_students = StudentsMod.objects.all()
    return render(request, 'studentstable.html', {'my_students': my_students})

def edit_student(request, admissionno):
    student = get_object_or_404(StudentsMod, admissionno=admissionno)
    if request.method == 'POST':
        form = ModelForStud(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')  # Redirect to a success page or appropriate URL
    else:
        form = ModelForStud(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, admissionno):
    student = get_object_or_404(StudentsMod, admissionno=admissionno)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')  # Redirect to a success page or appropriate URL
    # Handle GET request (optional)
    return render(request, 'confirm_delete_student.html', {'student': student})

def edit_teacher(request, teachid):
    teacher = get_object_or_404(ModelForTeacher, teachid = teachid)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('view_teacher')  # Redirect to a success page or appropriate URL
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})

def delete_teacher(request, teachid):
    teacher = get_object_or_404(ModelForTeacher, teachid=teachid)
    if request.method == 'POST':
        teacher.delete()
        return redirect('view_teacher')  # Redirect to a success page or appropriate URL
    # Handle GET request (optional)
    return render(request, 'delete_teacher.html', {'teacher': teacher})

def add_notification(request):
    if request.method =='POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            notifi = form.save(commit=False)
            notifi.current_date = date.today()
            notifi.save()
            return redirect('add_notification')
    else:
        form = NotificationForm()  
    return render(request,'add_notification.html', {'form': form})

def view_notification(request):
    my_models = TableOfNotifications.objects.all()
    return render(request, 'view_notification.html', {'my_models': my_models})
from django.db.models import Q

def search_students(request):
    query = request.GET.get('query')
    results = None
    
    if query:
        results = StudentsMod.objects.filter(
            Q(name__icontains=query) | Q(admissionno__icontains=query)
        )
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

def table_doubt(request):
    if request.method =='POST':
        form = FormForDoubt(request.POST)
        if form.is_valid():
            notifi = form.save(commit=False)
            notifi.currentdate = date.today()
            notifi.save()
            return redirect('table_doubt')
    else:
        form = FormForDoubt()  
    return render(request,'doubtview.html', {'form': form})

def index(request):
    return render(request , 'index.html' )


def indexstudent(request):
    return render(request , 'indexstudent.html')

def view_doubts(request):
    my_models = TableForDoubt.objects.all()
    return render(request, 'view_doubts.html', {'my_models': my_models})

def edit_doubt(request, doubtid):
    doubt = get_object_or_404(TableForDoubt, doubtid = doubtid)
    if request.method == 'POST':
        form = FormForDoubt(request.POST, instance=doubt)
        if form.is_valid():
            form.save()
            return redirect('view_doubts')  # Redirect to a success page or appropriate URL
    else:
        form = FormForDoubt(instance=doubt)
    return render(request, 'edit_doubt.html', {'form': form})

def delete_doubts(request, doubtid):
    doubt = get_object_or_404(TableForDoubt, doubtid=doubtid)
    if request.method == 'POST':
        doubt.delete()
        return redirect('view_doubts')  # Redirect to a success page or appropriate URL
    # Handle GET request (optional)
    return render(request, 'delete_dbt_confirm.html', {'doubt': doubt})

def view_teach_doubts(request):
    my_models = TableForDoubt.objects.all()
    return render(request, 'teacher_view_doubt.html', {'my_models': my_models})

def insert_reply(request,doubtid):
    doubt = get_object_or_404(TableForDoubt, doubtid = doubtid)
    if request.method == 'POST':
        form = FormForReply(request.POST, instance=doubt)
        if form.is_valid():
            form.save()
            return redirect('view_doubts')  # Redirect to a success page or appropriate URL
    else:
        form = FormForReply(instance=doubt)
    return render(request, 'edit_doubt.html', {'form': form})

def edit_reply(request,doubtid):
    doubt = get_object_or_404(TableForDoubt, doubtid = doubtid)
    if request.method == 'POST':
        form = FormForReply(request.POST, instance=doubt)
        if form.is_valid():
            form.save()
            return redirect('view_teach_doubts')  # Redirect to a success page or appropriate URL
    else:
        form = FormForReply(instance=doubt)
    return render(request, 'edit_reply.html', {'form': form})
            

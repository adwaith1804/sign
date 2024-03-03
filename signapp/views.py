from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModelForStud, TeacherForm, NotificationForm,FormForDoubt
from .models import StudentsMod,ModelForTeacher,TableOfNotifications,TableForDoubt
from datetime import date
from django.db.models import Q

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
            form.save()
            return redirect('add_notification')
    else:
        form = FormForDoubt()  
    return render(request,'doubtview.html', {'form': form})



def index(request):
    return render(request , 'index.html' )

def indexstudent(request):
    return render(request , 'indexstudent.html')
    
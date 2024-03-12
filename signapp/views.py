from django.shortcuts import render, redirect, get_object_or_404
from .forms import ModelForStud, TeacherForm, NotificationForm,FormForDoubt,FormForReply,LoginForm,AttendanceForm,FormForExams,AnswerForm
from .models import StudentsMod,ModelForTeacher,TableOfNotifications,TableForDoubt,AttendanceMod,ExamModel,AnswerModel
from datetime import date,datetime
from django.db.models import Q
import random
import string
import uuid
from django.utils import timezone
from datetime import datetime

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
            password = str(uuid.uuid4())[:8]  # Change 8 to your desired length
            form.instance.password = password
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

def indexteacher(request):
    return render(request , 'indexteacher.html')


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

def login_func(request, usertype):
    if usertype == "Student":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    student = StudentsMod.objects.get(email=email, password=password)
                    request.session['admissionno'] = student.admissionno
                    return redirect('student_home')
                except StudentsMod.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif usertype == "Teacher":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    teacher = ModelForTeacher.objects.get(email=email, password=password)
                    request.session['teachid'] = teacher.teachid
                    return redirect('teacher_home')
                except ModelForTeacher.DoesNotExist:
                    form.add_error(None, 'Invalid Username or Password')
        else:
            form = LoginForm()  # Assigning form variable here
        return render(request, 'login.html', {'form': form})
    
    
def edit_student_individual(request):

    admissionno = request.session.get('admissionno')
    student = StudentsMod.objects.get(admissionno=admissionno)
    if request.method == 'POST':
        form = ModelForStud(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_home')  # Redirect to homepage after editing
    else:
        form = ModelForStud(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def edit_teacher_individual(request):

    teachid = request.session.get('teachid')
    teacher = ModelForTeacher.objects.get(teachid=teachid)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_home')  # Redirect to homepage after editing
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})
 
def logout(request):
    request.session.clear()
    return redirect('index')

def insert_attendance(request,admissionno):
    teacherid = request.session.get('teachid')
    
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            notifi = form.save(commit=False)
            notifi.currentdate = date.today()
            notifi.studentsaddmissionno = admissionno
            notifi.teacherid = teacherid  # Assign the teacherid retrieved from the session
            notifi.save()
            return redirect('teacher_home')
    else:
        form = AttendanceForm()
    return render(request, 'attendance_update.html', {'form': form})

def attendance_status(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'error.html', {'error_message': 'Invalid date format'})
        attendance_records = AttendanceMod.objects.filter(currentdate=date)
        student_attendance = {}
        for record in attendance_records:
            if record.studentsaddmissionno not in student_attendance:
                student_attendance[record.studentsaddmissionno] = {'name': '', 'status': ''}
            student = StudentsMod.objects.get(admissionno=record.studentsaddmissionno)
            student_name = student.name
            student_attendance[record.studentsaddmissionno]['name'] = student_name
            student_attendance[record.studentsaddmissionno]['status'] = record.attendancestatus
        return render(request, 'attendance_status.html', {'student_attendance': student_attendance, 'date': date})
    else:
        return render(request, 'search_date.html')

def add_examination(request):
    teacherid = request.session.get('teachid')
    if teacherid is None:
        return redirect('')
    if request.method =='POST':
        form = FormForExams(request.POST)
        if form.is_valid():
            exam_instance = form.save(commit=False)
            exam_instance.teacher_id = teacherid  # Assign teacher_id to the instance
            exam_instance.save()
            form.save()
            return redirect('add_examination')
    else:
        form = FormForExams()  
    return render(request,'add_examinations.html', {'form': form})


def view_examinations(request):
    teacher_id = request.session.get('teachid')
    if teacher_id is None:
        return redirect('login')  # Redirect to login page or wherever appropriate if teacher_id is not found in session
    
    # Retrieve all exam instances for the current teacher
    exams = ExamModel.objects.filter(teacher_id=teacher_id)
    
    return render(request, 'view_examinations_teacher.html', {'exams': exams})
        
def edit_examination(request, exam_key):
    teacher_id = request.session.get('teachid')
    if teacher_id is None:
        return redirect('login')  # Redirect to login page or wherever appropriate if teacher_id is not found in session
    
    # Retrieve the exam instance to edit
    exam_instance = get_object_or_404(ExamModel, pk=exam_key, teacher_id=teacher_id)
    
    if request.method == 'POST':
        form = FormForExams(request.POST, instance=exam_instance)
        if form.is_valid():
            form.save()
            return redirect('view_examinations')
    else:
        form = FormForExams(instance=exam_instance)
        
    return render(request, 'edit_examinations.html', {'form': form})

def delete_examination(request, exam_key):
    # Retrieve the exam instance to delete
    exam_instance = get_object_or_404(ExamModel, pk=exam_key)
    exam_instance.delete()
    return redirect('teacher_home') 




def exam_view(request):
    if 'admissionno' in request.session:
        student_admissionno = request.session['admissionno']
        student = StudentsMod.objects.filter(admissionno=student_admissionno).first()
        if student:
            student_class = student.classstud
            current_date = date.today()
            exams = ExamModel.objects.filter(exam_date=current_date, class_student=student_class)
            if exams:
                questions = []
                for exam in exams:
                    question = {
                        'question': exam.question,
                        'options': [exam.option1, exam.option2, exam.option3],
                        'question_id': exam.exam_key
                    }
                    questions.append(question)
                form = AnswerForm()
                return render(request, 'view_exams.html', {'questions': questions, 'form': form})
            else:
                questions = [] 
                return render(request, 'no_exam.html', {'questions': questions})
        else:
            return render(request, 'no_student.html') 
    else:
        return render(request, 'no_session.html')
def save_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question_id = form.cleaned_data['question_id']
            answer = form.cleaned_data['answer']
            login_id = request.session.get('admissionno')  # Assuming you set this in the login process
            AnswerModel.objects.create(question_id=question_id, answer=answer, login_id=login_id)
            return redirect('exam_view')
    return redirect('exam_view')
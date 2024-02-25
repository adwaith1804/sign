from django.urls import path
# from.http import views
from .import views

urlpatterns = [
    path('insert_data/', views.insert_data, name='insert_data'),
    #path('view_table/', view_table, name='table'),
    path('students_reg/', views.students_reg , name='students_reg'),
    path('view_teacher/', views.view_teacher, name='view_teacher'),
    path('view_students/', views.view_students, name='view_students'),
    path('edit_student/<str:admissionno>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:admissionno>/', views.delete_student, name='delete_student'),
    path('edit_teacher/<str:teachid>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<str:teachid>/', views.delete_teacher, name='delete_teacher'),
    path('add_notification/', views.add_notification, name='add_notification'),
    path('view_notification/', views.view_notification, name='view_notification'),
    path('search_students/', views.search_students, name='search_students'),

]

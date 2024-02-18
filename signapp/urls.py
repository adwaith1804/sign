from django.urls import path
# from.http import views
from .import views

urlpatterns = [
    path('insert_data/', views.insert_data, name='insert_data'),
    #path('view_table/', view_table, name='table'),
    path('students_reg/', views.students_reg , name='students_reg'),
    path('view_teacher/', views.view_teacher, name='table'),
]

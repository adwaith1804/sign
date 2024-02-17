from django.urls import path
# from.http import views
from .views import insert_data,students_reg

urlpatterns = [
    # path('insert_data/', insert_data, name='insert_data'),
    #path('view_table/', view_table, name='table'),
    path('students_reg/', students_reg , name='students_reg'),
]

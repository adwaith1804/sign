from django.urls import path
# from.http import views
from.views import insert_data

urlpatterns = [
    path('insert_data/', insert_data, name='insert_data'),
    path('edit_data/', insert_data, name='adwaith'),
    #path('view_table/', view_table, name='table'),
]

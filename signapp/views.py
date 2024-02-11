from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel
#run on /sign
def insert_data(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('insert_data')
            
    else:
        form = MyModelForm()
    return render(request,'registeration.html', {'form': form}) 
    
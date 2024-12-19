from django.shortcuts import render, redirect
from .forms import *

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_profesor')
    else:
        form = ProfesorForm()
    return render(request, 'crear_profesor.html', {'form2': form})

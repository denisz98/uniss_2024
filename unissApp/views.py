from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
from .forms import *
def clase(request):
    # buscamos todass las clases en la base de datos
    clases = Clase.objects.all()

    return render(request, 'Clase/Clase.html', {"clase": clases})

def insertar_clase(request):
    # creamos una instancia del formulario de la clase
    miformulario = ClaseForm()
    # claseFormularios = Clase.objects.all()

    if request.method == "POST":
        miformulario = ClaseForm(data=request.POST)
        if miformulario.is_valid():
            miformulario.save()

            return redirect("/clase/")

    return render(request, 'Clase/form.html', { "miformulario": miformulario})

def editar_clase(request, id_clase):
    # cargamos los datos de la clase a traves del id obtenido en caso de q no exista el id devuelve un error 404
    clase = get_object_or_404(Clase, idClase=id_clase)

    if request.method == "POST":
        miformulario = ClaseForm(request.POST, instance=clase)
        if miformulario.is_valid():
            miformulario.save()
            return redirect("/clase/")
    else:
        miformulario = ClaseForm(instance=clase)
    return render(request, 'Clase/form.html', {"miformulario": miformulario})

def eliminar_clase(request, id_clase):
    clase = Clase.objects.get(pk=id_clase)

    clase.delete()

    return redirect("/clase/")

# ==========================================================Profesor====================================================


def profesor(request):
    profesores = Profesor.objects.all()

    return render(request, 'Profesor/Profesor.html', {"profesor": profesores})


def insertar_profesor(request):
    miformulario = ProfesorForm()

    if request.method == "POST":
        miformulario = ProfesorForm(data=request.POST)
        if miformulario.is_valid():
            miformulario.save()

            return redirect("/insertar_profesor/")

    return render(request, 'Profesor/form.html',
                  {"miformulario": miformulario})


def editar_profesor(request, id_profesor):
    # obtiene el profesor o muestra un error 404 si no existe
    profesor = get_object_or_404(Profesor, idProfesor=id_profesor)

    if request.method == "POST":
        # Rellena el formulario con los datos enviados y la instancia existente
        miformulario = ProfesorForm(request.POST, instance=profesor)
        if miformulario.is_valid():
            # Guarda  cambios
            miformulario.save()
            return redirect("/profesor/")
    else:
        # Si es una solicitud GET, inicializa el formulario con la instancia existente
        miformulario = ProfesorForm(instance=profesor)

    return render(request, 'Profesor/form.html', {"miformulario": miformulario})


def eliminar_profesor(request, id_profesor):
    profesor = Profesor.objects.get(pk=id_profesor)

    profesor.delete()

    return redirect("/profesor/")

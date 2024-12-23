from django.urls import path
from .views import *

urlpatterns = [
    path('clase/', clase, name="Clase"),
    path('insertar_clase/', insertar_clase,name="insertar_clase"),
    path('editar_clase/<int:id_clase>', editar_clase,name="editar_clase"),
    path('eliminar_clase/<int:id_clase>', eliminar_clase,name="eliminar_clase"),


    path('profesor/', profesor, name="Profesor"),
    path('insertar_profesor/', insertar_profesor,name="insertar_profesor"),
    path('editar_profesor/<int:id_profesor>', editar_profesor,name="editar_profesor"),
    path('eliminar_profesor/<int:id_profesor>', eliminar_profesor,name="eliminar_profesor"),

    path('estudiante/', estudiante, name="Estudiante"),
    path('insertar_estudiante/', insertar_estudiante,name="insertar_estudiante"),
    path('editar_estudiante/<int:id_estudiante>', editar_estudiante,name="editar_estudiante"),
    path('eliminar_estudiante/<int:id_estudiante>', eliminar_estudiante,name="eliminar_estudiante"),

]
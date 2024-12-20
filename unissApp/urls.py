from django.urls import path
from .views import *

urlpatterns = [
    path('clase/', clase, name="Clase"),
    path('insertar_clase/', insertar_clase,name="insertar_clase"),
    path('editar_clase/<int:id_clase>', editar_clase,name="editar_clase"),
    path('eliminar_clase/<int:id_clase>', eliminar_clase,name="eliminar_clase"),

]
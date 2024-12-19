from django.urls import path
from .views import crear_profesor

urlpatterns = [
    path('profesor_crear/', crear_profesor, name='crear_profesor'),
]
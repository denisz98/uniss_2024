from rest_framework import serializers
from .models import Disciplina, Profesor, Clase, Estudiante

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'
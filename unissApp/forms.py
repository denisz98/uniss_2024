from django import forms
from .models import Profesor, Disciplina, Clase, Estudiante

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'ci': forms.TextInput(attrs={'placeholder': 'Carnet de identidad'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

from django.db import models

# Create your models here.


dict_agno = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

dict_grado_cientifico = [
    ('ninguno', 'ninguno'),
    ('master', 'master'),
    ('doctor', 'doctor'),
]

dict_categoria = [
    ('Instructor', 'Instructor'),
    ('asistente', 'asistente'),
    ('auxiliar', 'auxiliar'),
    ('titular', 'titular'),
]


class Disciplina(models.Model):
    idDisciplina = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    idProfesor = models.BigAutoField(primary_key=True)
    fecha = models.DateField(null=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    ci = models.CharField(max_length=11, unique=True, verbose_name='Carnet identidad')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')

    grado_cientifico = models.CharField(max_length=255, verbose_name='Grado científico', choices=dict_grado_cientifico)
    categoria_docente = models.CharField(max_length=20, choices=dict_categoria)

    class Admin:
        list_display = ('categoria')
        list_filter = ('grado_cientifico')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    idClase = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    agno = models.CharField(max_length=1, choices=dict_agno)

    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    idEstudiante = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    ci = models.CharField(max_length=11, unique=True, verbose_name='Carnet identidad')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    direccion = models.CharField(max_length=255, verbose_name='Dirección')
    agno_academico = models.CharField(max_length=1, choices=dict_agno)

    clase = models.ManyToManyField(Clase, verbose_name='Clases')

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.nombre

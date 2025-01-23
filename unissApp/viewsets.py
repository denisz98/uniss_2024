from rest_framework import viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Disciplina, Profesor, Clase, Estudiante
from .serializer import DisciplinaSerializer, ProfesorSerializer, ClaseSerializer, EstudianteSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    permission_classes = [IsAuthenticated]

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Obtiene el número total de clases en la base de datos.",
        responses={200: '{"total_clases": 10}'}
    )
    @action(detail=False, methods=['get'])
    def total_clases(self, request):
        total = Clase.objects.count()
        return Response({'total_clases': total})

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAuthenticated]


class CantidadEstudiantesView(APIView):
    def get(self, request):
        cantidad = Estudiante.objects.count()
        return Response({'cantidad_estudiantes': cantidad}, status=status.HTTP_200_OK)
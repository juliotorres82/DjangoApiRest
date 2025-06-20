from .models import Proyecto
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny] #estos son permisos, se pueden cambiar despues 
    serializer_class = ProjectSerializer


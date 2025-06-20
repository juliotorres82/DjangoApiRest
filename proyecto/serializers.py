from rest_framework import serializers
from .models import Proyecto

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'creado_en')
        read_only_fields = ("creado_en",)
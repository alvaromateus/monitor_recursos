from rest_framework import viewsets
from recursos.api import serializers
from recursos import models

class RegistroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecursosSerializers
    queryset = models.Registro.objects.all()
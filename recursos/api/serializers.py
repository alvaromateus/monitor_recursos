from rest_framework import serializers
from recursos import models


class RecursosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Registro
        fields = '__all__'
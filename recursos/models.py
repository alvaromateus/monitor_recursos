from django.db import models

# Create your models here.

class Registro(models.Model):
    nome_equipamento = models.CharField(max_length=255)
    data_hora = models.CharField(max_length=255)
    memoria = models.FloatField()
    cpu = models.FloatField()
    # nome_equipamento_X = 'asas'

    def __str__(self):
        return self.nome_equipamento
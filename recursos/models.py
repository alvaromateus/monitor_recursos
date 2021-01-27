from django.db import models
from django.urls import reverse

# Create your models here.

class Registro(models.Model):
    nome_equipamento = models.CharField(max_length=255)
    data_hora = models.CharField(max_length=255)
    memoria = models.FloatField()
    cpu = models.FloatField()
    
    memoria_total = models.CharField(max_length=50, null=True)
    clock_processador = models.CharField(max_length=255, null=True)
    numero_nucleos = models.CharField(max_length=2, null=True)
    # nome_equipamento_X = 'asas'

    def __str__(self):
        return self.nome_equipamento

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))

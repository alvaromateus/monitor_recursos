from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ['nome_equipamento','cpu','memoria','data_hora']
    search_fields = ['nome_equipamento']
    list_filter =['nome_equipamento']

# Register your models here.

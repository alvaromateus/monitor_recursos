from django.contrib import admin
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ['nome_equipamento','cpu','memoria']

# Register your models here.

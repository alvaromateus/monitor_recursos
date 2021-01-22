from django.shortcuts import render
from django.http import HttpResponse
import json

from recursos.models import Registro

# Create your views here.

def home(request):
    return render(request, 'home.html')

def comportamento(equipamento):
    media_memoria = 0
    media_cpu = 0    
    registros = Registro.objects.filter(nome_equipamento=equipamento)

    for i in registros:
        media_memoria = media_memoria+i.memoria
        media_cpu = media_cpu+i.cpu

    media_memoria = media_memoria/registros.count()
    media_cpu = media_cpu/registros.count()

    return (media_memoria+media_memoria)/2

def lista_equipamentos(request):    
    equipamentos = Registro.objects.filter().distinct("nome_equipamento").values_list("nome_equipamento", flat=True)

    dicionario_equipamentos = list(equipamentos.values())

    # cria dicionario para comportamento e chama método que calcula a média
    for i in dicionario_equipamentos:
        media_comportamento = comportamento(i['nome_equipamento']) 
        i['comportamento'] = media_comportamento
   
    # Faz a ordenação por média comportamental
    dicionario_equipamentos = sorted(dicionario_equipamentos, key=lambda k: k['comportamento'])
    context_object_name = {
        'equipamentos': dicionario_equipamentos        
    }
    return render(request, 'list.html', context_object_name)

def graph(request, equipamento):    
    queryset = Registro.objects.filter(nome_equipamento=equipamento)    
    primeiro = queryset.count()-100
    ultimo = queryset.count()
    if ultimo >= 100:
        queryset = Registro.objects.filter(nome_equipamento=equipamento)[primeiro:ultimo]
    names = [obj.nome_equipamento for obj in queryset]
    dates = [obj.data_hora for obj in queryset]
    mems = [obj.memoria for obj in queryset]
    cpus = [obj.cpu for obj in queryset]

    context = {
        'equipamento': json.dumps(equipamento),
        'names': json.dumps(names),
        'dates': json.dumps(dates),
        'mems': json.dumps(mems),
        'cpus': json.dumps(cpus),
    }
    return render(request, 'graph.html', context)
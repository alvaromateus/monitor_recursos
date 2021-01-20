from django.shortcuts import render
from django.http import HttpResponse
import json

from recursos.models import Registro

# Create your views here.

def home(request):
    return render(request, 'home.html')

def list(request):
    equipamentos = Registro.objects.filter().distinct("nome_equipamento").values_list("nome_equipamento", flat=True)
    context_object_name = {
        'equipamentos': equipamentos
    }
    return render(request, 'list.html', context_object_name)

def graph(request, equipamento):    
    queryset = Registro.objects.filter(nome_equipamento=equipamento)

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

def updateGraph(request):
    queryset = Registro.objects.all()
    names = [obj.nome_equipamento for obj in queryset]
    dates = [obj.data_hora for obj in queryset]
    mems = [obj.memoria for obj in queryset]
    cpus = [obj.cpu for obj in queryset]

    context = {
        'names': names,
        'dates': dates,
        'mems': mems,
        'cpus': cpus,
    }
    return JsonResponse(context)
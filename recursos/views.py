from django.shortcuts import render
from django.http import HttpResponse
import json
from sklearn import preprocessing

from recursos.models import Registro

def home(request):
    return render(request, 'home.html')

def comportamento(equipamento):
    # memória_disponível = memória_total-((percentual_memoria_ocupada/100) * memoria_total)
    # clock_processador = numero_nucleos * clock_processador
    # clock_disponível = clock_processador - ((percentual_cpu_ocupada/100) * clock_processador)
    # comportamento = normalizar(memoria_disponível + clock_disponível)

    # cálcula média de consumo de cpu e memória
    media_memoria = 0
    media_cpu = 0    
    registros = Registro.objects.filter(nome_equipamento=equipamento).order_by('id')

    for i in registros:
        media_memoria = media_memoria+i.memoria
        media_cpu = media_cpu+i.cpu

    media_memoria = media_memoria/registros.count()
    media_cpu = media_cpu/registros.count()

    setup_equipamento = registros[0] # retorna primeiro registro enviado onde há informações do setup (memória total, quantidade nucleos e clock)
    
    memoria_disponivel = float(setup_equipamento.memoria_total) -((media_memoria/100) * float(setup_equipamento.memoria_total))
    clock_total = float(setup_equipamento.numero_nucleos) * float(setup_equipamento.clock_processador)
    clock_disponível = clock_total -((media_cpu/100) * float(setup_equipamento.clock_processador))    

    return ((memoria_disponivel + clock_disponível) /2)/10000000

def lista_equipamentos(request):    
    equipamentos = Registro.objects.filter().distinct("nome_equipamento").values_list("nome_equipamento", flat=True)

    dicionario_equipamentos = list(equipamentos.values()) # transforma em dicionário

    # cria dicionario para comportamento e chama método que calcula o comportamento normalizado
    for i in dicionario_equipamentos:
        media_comportamento = comportamento(i['nome_equipamento'])
        i['comportamento'] = media_comportamento
   
    # Faz a ordenação por média comportamental
    dicionario_equipamentos = sorted(dicionario_equipamentos, key=lambda k: k['comportamento'], reverse=True)
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
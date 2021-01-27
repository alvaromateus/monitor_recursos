import pandas as pd
from datetime import datetime
import time
import requests
import json
import socket
from threading import Thread

def search(dictionary_list, name_equipment):
    res = None
    for i in dictionary_list:
        if i['nome_equipamento'] == name_equipment:            
            res = i
            break            
    return res

while(True): 
    #dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y %H:%M:%S.%f')
    dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y %H:%M:%S')

    # abre aquivo csv para fazer parse da data
    data = pd.read_csv('log.csv', parse_dates=['data'], index_col='data', date_parser=dateparse)

    media_cpu = data['cpu'].rolling(6).mean()
    media_memoria = data['memoria'].rolling(42).mean()

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%m/%d/%Y %H:%M:%S')


    response = requests.get(url="http://192.168.1.31:8000/api/registros/")
    data = json.loads(response.content)
    print(search(data, "socket.gethostname())"))
    # Verificar se o computador já foi cadastrado
    if (search(data, socket.gethostname()) != None): # encontrou 
        # somente inclui dados gerais
        registro = {
            'nome_equipamento': socket.gethostname(),
            'data_hora': data_e_hora_em_texto,
            'memoria': media_memoria.tail(1)[0],
            'cpu': media_cpu.tail(1)[0]            
        }
        print("incluindo computador já existente")
        response = requests.post(url="http://192.168.1.31:8000/api/registros/", json=registro)
    else: # Se for um computador novo
        registro = {
            'nome_equipamento': socket.gethostname(),
            'data_hora': data_e_hora_em_texto,
            'memoria': media_memoria.tail(1)[0],
            'cpu': media_cpu.tail(1)[0],
            'memoria_total': '8GB',
            'clock_processador': 'quad core 3.2ghz'            
        }
        print("incluindo computador novo computador")
        response = requests.post(url="http://192.168.1.31:8000/api/registros/", json=registro)

    if response.status_code >= 200 and response.status_code <= 299:
        print('Status Code', response.status_code)
        print('Reason', response.reason)
        print('Texto', response.text)
        print('JSON', response.json)
    else:
        print('Status Code', response.status_code)
        print('Reason', response.reason)
        print('Texto', response.text)
    time.sleep(1170)
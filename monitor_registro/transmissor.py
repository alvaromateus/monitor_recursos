import pandas as pd
from datetime import datetime
import time
import requests
import json
import socket

while(True): 
    #dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y %H:%M:%S.%f')
    dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y %H:%M:%S')

    # abre aquivo csv para fazer parse da data
    data = pd.read_csv('log.csv', parse_dates=['data'], index_col='data', date_parser=dateparse)

    media_cpu = data['cpu'].rolling(39).mean()
    media_memoria = data['memoria'].rolling(39).mean()

    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%m/%d/%Y %H:%M:%S')

    registro = {
        'nome_equipamento': socket.gethostname(),
        'data_hora': data_e_hora_em_texto,
        'memoria': media_memoria.tail(1)[0],
        'cpu': media_cpu.tail(1)[0]
    }
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
    time.sleep(390)
# -*- coding: utf:8 -*-

import psutil
import time
from datetime import datetime
import requests
import json
import socket
#import registro

try:
    while True:
        arquivo = open('log.csv', 'a') # abre arquivo no modo a -> para inclusão ao final

        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%m/%d/%Y %H:%M:%S')
        arquivo.write('"'+str(data_e_hora_em_texto)+'.743",')

        memory_usage = dict(psutil.virtual_memory()._asdict())
        arquivo.write('"'+str(memory_usage['percent'])+'",')

        CPU_usage = psutil.cpu_percent()
        arquivo.write('"'+str(CPU_usage)+'"\n')
        print(str(data_e_hora_em_texto) + " - Memória: " + str(memory_usage['percent']) + " - CPU: " + (str(CPU_usage)))
        registro = {
            'nome_equipamento': socket.gethostname(),
            'data_hora': data_e_hora_em_texto,
            'memoria': memory_usage['percent'],
            'cpu': CPU_usage
        }
        response = requests.post(url="http://localhost:8000/registros/", json=registro)

        if response.status_code >= 200 and response.status_code <= 299:
            print('Status Code', response.status_code)
            print('Reason', response.reason)
            print('Texto', response.text)
            print('JSON', response.json)
        else:
            print('Status Code', response.status_code)
            print('Reason', response.reason)
            print('Texto', response.text)
                
        arquivo.close

        time.sleep(30)
except KeyboardInterrupt:
    print("Programa encerrado")
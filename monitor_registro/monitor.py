# -*- coding: utf:8 -*-

import psutil
import time
from datetime import datetime

#import registro
time.sleep(30)
try:
    while True:
        arquivo = open('log.csv', 'a') # abre arquivo no modo a -> para inclusão ao final

        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%m/%d/%Y %H:%M:%S')
        arquivo.write('"'+str(data_e_hora_em_texto)+'",')

        CPU_usage = psutil.cpu_percent()
        memory_usage = dict(psutil.virtual_memory()._asdict())
        arquivo.write('"'+str(memory_usage['percent'])+'",')        
        
        arquivo.write('"'+str(CPU_usage)+'"\n')
        print(str(data_e_hora_em_texto) + " - Memória: " + str(memory_usage['percent']) + " - CPU: " + (str(CPU_usage)))               
        arquivo.close

        time.sleep(30)
except KeyboardInterrupt:
    print("Programa encerrado")
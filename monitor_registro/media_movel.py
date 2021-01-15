import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import datetime
from matplotlib.pylab import rcParams
import matplotlib.pyplot
import pandas as pd
import matplotlib.animation as animation

# 03/13/2020 14:58:08.719
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y %H:%M:%S.%f')

# abre aquivo csv para fazer parse da data
data = pd.read_csv('log.csv', parse_dates=['data'], index_col='data', date_parser=dateparse)

fig = plt.figure(figsize=(10,3))
ax = fig.add_subplot(1, 1, 1)

media_cpu = data['cpu'].rolling(39).mean()
#media_cpu = data['cpu'].ewm(span=39).mean()
media_memoria = data['memoria'].rolling(39).mean()
#media_memoria = data['memoria'].ewm(span=39).mean()

def animate(i):
    global media_memoria
    global media_cpu
    ax.clear()
    plt.plot(media_memoria, color='red', label='Média móvel do consumo de memória')
    plt.plot(media_cpu, color='blue', label='Média móvel do consumo de CPU')
    plt.title("Média móvel  - Percentual de Consumo de Memoria e CPU")
    plt.legend()
    data_ = pd.read_csv('log.csv', parse_dates=['data'], index_col='data', date_parser=dateparse)
    media_cpu = data_['cpu'].rolling(3900).mean()
    media_memoria = data_['memoria'].rolling(3900).mean()
    #media_cpu = data['cpu'].ewm(span=39).mean()
    #media_memoria = data['memoria'].ewm(span=39).mean()

ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()
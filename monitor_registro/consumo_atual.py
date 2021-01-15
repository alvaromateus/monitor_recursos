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

ts_cpu = data['cpu'].tail(20)
ts_memoria = data['memoria'].tail(20)

def animate(i):
    global ts_memoria
    global ts_cpu
    ax.clear()
    plt.plot(ts_memoria, color='red', label='Percentual de consumo de memória')
    plt.plot(ts_cpu, color='blue', label='Percentual de consumo de CPU')
    plt.title("Percentual de Consumo de Memoria e CPU")
    plt.legend()
    data_ = pd.read_csv('log.csv', parse_dates=['data'], index_col='data', date_parser=dateparse)
    ts_memoria = data_['memoria'].tail(20)
    ts_cpu = data_['cpu'].tail(20)

ani = animation.FuncAnimation(fig, animate, interval=200)
plt.show()
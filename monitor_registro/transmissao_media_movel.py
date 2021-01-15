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

quantidade_períodos = 39
#quantidade_registros_período = 960

media_movel = data.tail(2000).rolling(quantidade_períodos).mean()

compression_opts = dict(method='zip', archive_name='log_media_movel.csv')
media_movel.to_csv('log_media_movel.zip', compression=compression_opts) # gera arquivo compactado para tranmissão da série temporal da média

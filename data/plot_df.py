#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

#font = {'family' : 'normal',
#        'weight' : 'bold',
#        'size'   : 22}

#plt.rc('font', **font)

filename = 'df.csv'
xlabel = r'$\rm Density\ (mol/L)$'
ylabel = r'$\rm d\mathit{f_{n}}$'

#Read values
df = pd.read_csv('%s' %filename,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())

#plot
fig, ax = plt.subplots(1,1)
x0 = np.array(out[0]).astype(np.float)/1e3
y0 = np.array(out[1]).astype(np.float)
y1 = np.array(out[2]).astype(np.float)
y2 = np.array(out[3]).astype(np.float)
y3 = np.array(out[4]).astype(np.float)
y4 = np.array(out[5]).astype(np.float)

ax.tick_params(direction='in',size=6,labelsize=18)
plt.plot(x0, y0, color='midnightblue', linewidth=1.0, linestyle='-',  label='n = 1')
plt.plot(x0, y1, color='b',  linewidth=1.0, linestyle='--', label='n = 2')
plt.plot(x0, y2, color='dodgerblue',   linewidth=1.0, linestyle='-.',  label='n = 3')
plt.plot(x0, y3, color='deepskyblue', linewidth=1.0, linestyle=':',  label='n = 4')
plt.plot(x0, y4, color='cyan', linewidth=1.0, linestyle='-',  label='n = 5')
#plt.plot(x0, y5, color='darkgray', linewidth=1.0, linestyle='--',  label='i = 6')
#plt.plot(x0, y6, color='darkgrey', linewidth=1.0, linestyle='-.',  label='i = 7')
#plt.plot(x0, y6, color='silver', linewidth=1.0, linestyle='-',  label='i = 8')

plt.legend(loc='best')
ax.set_xlabel(xlabel, fontsize=26)
ax.set_ylabel(ylabel, fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

#ax.set_xlim([xmin,xmax])
ax.set_ylim([-5.5e-4,1.0e-5])


plt.ylabel(ylabel)
plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
fig.savefig(('df_csv.png'))

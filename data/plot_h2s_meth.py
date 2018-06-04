#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'h2s_meth_298.csv'
file2 = 'h2s_meth_298_cpa_cparg.csv'
file3 = 'h2s_meth_448.csv'
file4 = 'h2s_meth_448_cpa.csv'
file5 = 'h2s_meth_448_cparg.csv'
xlabel = r'$\rm x_{H_{2}S}$'
ylabel = r'$\rm Pressure (MPa)$'

#298.15K exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P298 = np.array(out[0]).astype(np.float)
x298 = np.array(out[1]).astype(np.float)

#298.15K CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
x298c = np.array(out[0]).astype(np.float)
y298c = np.array(out[1]).astype(np.float)
P298c = np.array(out[2]).astype(np.float)/1000

#298.15K CPARG
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
x298cr = np.array(out[3]).astype(np.float)
y298cr = np.array(out[4]).astype(np.float)
P298cr = np.array(out[5]).astype(np.float)/1000

#448.15K exp
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P448 = np.array(out[0]).astype(np.float)
x448 = np.array(out[1]).astype(np.float)

#448.15K CPA
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
x448c = np.array(out[0]).astype(np.float)
y448c = np.array(out[1]).astype(np.float)
P448c = np.array(out[2]).astype(np.float)

#448.15K CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
x448cr = np.array(out[0]).astype(np.float)
y448cr = np.array(out[1]).astype(np.float)
P448cr = np.array(out[2]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in',size=6,labelsize=18)
ax.plot(x298, P298, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x448, P448, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x298c, P298c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y298c, P298c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x448c, P448c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y448c, P448c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x298cr, P298cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y298cr, P298cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(x448cr, P448cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y448cr, P448cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.set_xlabel(xlabel,fontsize=26)
ax.set_ylabel(ylabel,fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,1])
ax.set_ylim([0,14])
ax.text(0.2, 12, '$k_{ij}=0$', color='red', fontsize=18)

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'bin_h2s_meth'
fig.savefig(('%s.png' %filename))

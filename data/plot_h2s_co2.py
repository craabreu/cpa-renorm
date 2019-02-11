#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'h2s_co2_303.csv'
file2 = 'h2s_co2_303_cpa.csv'
file3 = 'h2s_co2_303_cparg.csv'
file4 = 'h2s_co2_328.csv'
file5 = 'h2s_co2_328_cpa.csv'
file6 = 'h2s_co2_328_cparg.csv'
xlabel = r'$\rm \mathit{x}_{H_{2}S}$'
ylabel = r'$\rm Pressure\ (MPa)$'

#303.15K exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P303 = np.array(out[0]).astype(np.float)/1000
x303 = np.array(out[1]).astype(np.float)

#303.15K CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x303c = np.array(out[0]).astype(np.float)
y303c = np.array(out[1]).astype(np.float)
P303c = np.array(out[3]).astype(np.float)/1000

#303.15K CPARG
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x303cr = np.array(out[0]).astype(np.float)
y303cr = np.array(out[1]).astype(np.float)
P303cr = np.array(out[3]).astype(np.float)/1000

#328.15K exp
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P328 = np.array(out[0]).astype(np.float)/1000
x328 = np.array(out[1]).astype(np.float)

#328.15K CPA
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x328c = np.array(out[0]).astype(np.float)
y328c = np.array(out[1]).astype(np.float)
P328c = np.array(out[3]).astype(np.float)/1000

#328.15K CPARG
df = pd.read_csv('%s' %file6,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x328cr = np.array(out[0]).astype(np.float)
y328cr = np.array(out[1]).astype(np.float)
P328cr = np.array(out[3]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in',size=6,labelsize=18)
ax.plot(x303, P303, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x328, P328, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x303c, P303c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y303c, P303c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x328c, P328c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y328c, P328c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x303cr, P303cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y303cr, P303cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(x328cr, P328cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y328cr, P328cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.set_xlabel(xlabel,fontsize=26)
ax.set_ylabel(ylabel,fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,1])
ax.set_ylim([2,10])
ax.text(0.2, 9, '$k_{ij}=0$', color='red', fontsize=18)

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'bin_h2s_co2'
fig.savefig(('%s.png' %filename))

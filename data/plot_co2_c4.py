#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'co2_c4_260.csv'
file2 = 'co2_c4_260_cpa_cparg.csv'
file3 = 'co2_c4_344.csv'
file4 = 'co2_c4_344_cpa.csv'
file5 = 'co2_c4_344_cparg.csv'
xlabel = r'$\rm x_{CO_{2}}$'
ylabel = r'$\rm Pressure (MPa)$'

#260.15K exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P260 = np.array(out[0]).astype(np.float)
x260 = np.array(out[1]).astype(np.float)

#260.15K CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
x260c = np.array(out[0]).astype(np.float)
y260c = np.array(out[1]).astype(np.float)
P260c = np.array(out[2]).astype(np.float)

#260.15K CPARG
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
x260cr = np.array(out[3]).astype(np.float)
y260cr = np.array(out[4]).astype(np.float)
P260cr = np.array(out[5]).astype(np.float)

#344.15K exp
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P344 = np.array(out[0]).astype(np.float)
x344 = np.array(out[1]).astype(np.float)

#344.15K CPA
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x344c = np.array(out[0]).astype(np.float)
y344c = np.array(out[1]).astype(np.float)
P344c = np.array(out[3]).astype(np.float)

#344.15K CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
x344cr = np.array(out[0]).astype(np.float)
y344cr = np.array(out[1]).astype(np.float)
P344cr = np.array(out[3]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in')
ax.plot(x260, P260, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x344, P344, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
ax.plot(x260c, P260c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y260c, P260c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x344c, P344c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(y344c, P344c, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(x260cr, P260cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y260cr, P260cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(x344cr, P344cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.plot(y344cr, P344cr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax.set_xlabel(xlabel, fontsize=26)
ax.set_ylabel(ylabel, fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,1])
ax.set_ylim([0,10])
ax.text(0.2, 8, '$k_{ij}=0$', color='red', fontsize=18)
ax.tick_params(size=6,labelsize=18)

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'bin_co2_c4'
fig.savefig(('%s.png' %filename))

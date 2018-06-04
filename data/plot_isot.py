#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'isot_exp.csv'
file2 = 'isot_cpa_cparg.csv'
xlabel = r'$\rm Density (mol/m^{3})$'
ylabel = r'$\rm Pressure (MPa)$'

#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
P0 = np.array(out[0]).astype(np.float)
rho0 = np.array(out[1]).astype(np.float)
P1 = np.array(out[2]).astype(np.float)
rho1 = np.array(out[3]).astype(np.float)

#Read values - calc values
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
out.append(df[:][6].values.tolist())
out.append(df[:][7].values.tolist())
CPA_P0 = np.array(out[0]).astype(np.float)
CPA_rho0 = np.array(out[1]).astype(np.float)
CPARG_P0 = np.array(out[2]).astype(np.float)
CPARG_rho0 = np.array(out[3]).astype(np.float)
CPA_P1 = np.array(out[4]).astype(np.float)
CPA_rho1 = np.array(out[5]).astype(np.float)
CPARG_P1 = np.array(out[6]).astype(np.float)
CPARG_rho1 = np.array(out[7]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in',size=6,labelsize=18)

plt.plot(rho0, P0, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='512.60 K')
plt.plot(rho1, P1, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='563.86 K')
plt.plot(CPA_rho0, CPA_P0, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(CPARG_rho0, CPARG_P0, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
plt.plot(CPA_rho1, CPA_P1, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
plt.plot(CPARG_rho1, CPARG_P1, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')

#plt.legend()
ax.set_xlabel(xlabel,fontsize=26)
ax.set_ylabel(ylabel,fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

ax.set_xlim([0,20000])
ax.set_ylim([0,35])

plt.ylabel(ylabel)
plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'isotherm'
fig.savefig(('%s.png' %filename))

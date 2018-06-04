#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file_exp = 'methanol_pv.csv'
file0 = 'PV_Methanol_n0.csv'
file1 = 'PV_Methanol_n1.csv'
file2 = 'PV_Methanol_n2.csv'
file3 = 'PV_Methanol_n3.csv'
file4 = 'PV_Methanol_n4.csv'
file5 = 'PV_Methanol_n5.csv'
xlabel = r'$\rm Density\ (mol/L)$'
ylabel = r'$\rm Temperature\ (K)$'

#methanol exp
df = pd.read_csv('%s' %file_exp,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T_exp = np.array(out[0]).astype(np.float)
rhol_exp = np.array(out[1]).astype(np.float)/1e3
rhov_exp = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file0,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T0 = np.array(out[0]).astype(np.float)
rhol0 = np.array(out[1]).astype(np.float)/1e3
rhov0 = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T1 = np.array(out[0]).astype(np.float)
rhol1 = np.array(out[1]).astype(np.float)/1e3
rhov1 = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T2 = np.array(out[0]).astype(np.float)
rhol2 = np.array(out[1]).astype(np.float)/1e3
rhov2 = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T3 = np.array(out[0]).astype(np.float)
rhol3 = np.array(out[1]).astype(np.float)/1e3
rhov3 = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T4 = np.array(out[0]).astype(np.float)
rhol4 = np.array(out[1]).astype(np.float)/1e3
rhov4 = np.array(out[2]).astype(np.float)/1e3

#methanol exp
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
T5 = np.array(out[0]).astype(np.float)
rhol5 = np.array(out[1]).astype(np.float)/1e3
rhov5 = np.array(out[2]).astype(np.float)/1e3

#plot
fig, ax = plt.subplots(1,1)

#Methanol subplot
ax.tick_params(direction='in',size=6,labelsize=18)
plt.plot(rhol_exp, T_exp, 's', markerfacecolor='none', markeredgecolor='black', markersize=6)
plt.plot(rhov_exp, T_exp, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Exp.')
plt.plot(rhol0, T0, color='midnightblue', linewidth=1.0, linestyle='-')
plt.plot(rhov0, T0, color='midnightblue', linewidth=1.0, linestyle='-',  label='n = 0')
plt.plot(rhol1, T1, color='midnightblue', linewidth=1.0, linestyle='--')
plt.plot(rhov1, T1, color='midnightblue', linewidth=1.0, linestyle='--',  label='n = 1')
plt.plot(rhol2, T2, color='b', linewidth=1.0, linestyle='-.')
plt.plot(rhov2, T2, color='b', linewidth=1.0, linestyle='-.',  label='n = 2')
plt.plot(rhol3, T3, color='dodgerblue', linewidth=1.0, linestyle=':')
plt.plot(rhov3, T3, color='dodgerblue', linewidth=1.0, linestyle=':',  label='n = 3')
plt.plot(rhol4, T4, color='deepskyblue', linewidth=1.0, linestyle='-')
plt.plot(rhov4, T4, color='deepskyblue', linewidth=1.0, linestyle='-',  label='n = 4')
plt.plot(rhol5, T5, color='cyan', linewidth=1.0, linestyle='--')
plt.plot(rhov5, T5, color='cyan', linewidth=1.0, linestyle='--',  label='n = 5')
#print len(rhol_exp),len(T0),len(T1)
#ax.fill_between(rhol_exp, T0, T1)
ax.set_xlabel(xlabel,fontsize=26)
ax.set_ylabel(ylabel,fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([1.5,16])
ax.set_ylim([490,540])

plt.legend(loc='best')
plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'PV_evol'
fig.savefig(('%s.png' %filename))

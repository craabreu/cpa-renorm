#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'cv_crit_exp.csv'
file2 = 'cv_10_cpa.csv'
file3 = 'cv_10_cparg.csv'
x0label = r'$\rm Pressure (MPa)$'
y0label = r'$\rm C_{v}^{res}/R$'
x1label = r'$\rm Pressure (MPa)$'
y1label = r'$\rm C_{p}^{res}/R$'

#BEGIN Cv--------------------------------------------------------------
#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P = np.array(out[0]).astype(np.float)
cv = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P = np.array(out[0]).astype(np.float)
CPA_Cv = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P = np.array(out[0]).astype(np.float)
CPARG_Cv = np.array(out[1]).astype(np.float)
#END Cv===============================================================

#BEGIN Cp--------------------------------------------------------------
file1 = 'cp_10_11_12_exp.csv'
file2 = 'cp_10_cpa.csv'
file3 = 'cp_10_cparg.csv'

#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Pp = np.array(out[0]).astype(np.float)
cp = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.0 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp = np.array(out[0]).astype(np.float)
CPA_Cp = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.0 - CPARG
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp = np.array(out[0]).astype(np.float)
CPARG_Cp = np.array(out[1]).astype(np.float)
#END Cp===============================================================

#plot 1 - Cv
fig, ax = plt.subplots(1,2)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in',size=6,labelsize=16)
ax[0].plot(P, cv, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 1.0')
ax[0].plot(CPA_P, CPA_Cv, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P, CPARG_Cv, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].set_xlabel(x0label,fontsize=16)
ax[0].set_ylabel(y0label,fontsize=16)
ax[0].yaxis.set_ticks_position('both')
ax[0].xaxis.set_ticks_position('both')
ax[0].set_xlim([0,20])
ax[0].set_ylim([0.0,10.0])
x0,x1 = ax[0].get_xlim()
y0,y1 = ax[0].get_ylim()
ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[1].tick_params(direction='in',size=6,labelsize=16)
ax[1].plot(Pp, cp, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 1.0')
ax[1].plot(CPA_Pp, CPA_Cp, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1].plot(CPARG_Pp, CPARG_Cp, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[1].set_xlabel(x1label,fontsize=16)
ax[1].set_ylabel(y1label,fontsize=16)
ax[1].yaxis.set_ticks_position('both')
ax[1].xaxis.set_ticks_position('both')
ax[1].set_xlim([0,25])
ax[1].set_ylim([0.0,50.0])
x0,x1 = ax[1].get_xlim()
y0,y1 = ax[1].get_ylim()
ax[1].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_cp_critical'
fig.savefig(('%s.png' %filename))


#ONLY Cv PLOT=======================================================================================
#plot 1 - Cv
fig, ax = plt.subplots(1,1)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P, cv, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P, CPA_Cv, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P, CPARG_Cv, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.set_xlabel(x0label,fontsize=22)
ax.set_ylabel(y0label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,20])
ax.set_ylim([0.0,10.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_critical'
fig.savefig(('%s.png' %filename))

#ONLY CP PLOT==========================================================================================
fig, ax = plt.subplots(1,1)

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(Pp, cp, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_Pp, CPA_Cp, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_Pp, CPARG_Cp, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,25])
ax.set_ylim([0.0,50.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cp_critical'
fig.savefig(('%s.png' %filename))

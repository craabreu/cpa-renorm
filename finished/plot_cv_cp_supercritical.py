#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'cv_supercrit_exp.csv'
file2 = 'cv_11_cpa.csv'
file3 = 'cv_12_cpa.csv'
file4 = 'cv_11_cparg.csv'
file5 = 'cv_12_cparg.csv'
x0label = '$Pressure (MPa)$'
y0label = '$C_{v}^{res}/R$'
x1label = '$Pressure (MPa)$'
y1label = '$C_{p}^{res}/R$'

#BEGIN Cv--------------------------------------------------------------
#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
P = np.array(out[0]).astype(np.float)
cv11 = np.array(out[1]).astype(np.float)
cv12 = np.array(out[2]).astype(np.float)

#Read values - Cv calc values - Tr 1.1 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P11 = np.array(out[0]).astype(np.float)
CPA_Cv11 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.2 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P12 = np.array(out[0]).astype(np.float)
CPA_Cv12 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPARG
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P11 = np.array(out[0]).astype(np.float)
CPARG_Cv11 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P12 = np.array(out[0]).astype(np.float)
CPARG_Cv12 = np.array(out[1]).astype(np.float)
#END Cv===============================================================

#BEGIN Cp--------------------------------------------------------------
file1 = 'cp_10_11_12_exp.csv'
file2 = 'cp_11_cpa.csv'
file3 = 'cp_12_cpa.csv'
file4 = 'cp_11_cparg.csv'
file5 = 'cp_12_cparg.csv'

#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
Pp = np.array(out[0]).astype(np.float)
cp11 = np.array(out[3]).astype(np.float)
cp12 = np.array(out[5]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp11 = np.array(out[0]).astype(np.float)
CPA_Cp11 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp12 = np.array(out[0]).astype(np.float)
CPA_Cp12 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPARG
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp11 = np.array(out[0]).astype(np.float)
CPARG_Cp11 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp12 = np.array(out[0]).astype(np.float)
CPARG_Cp12 = np.array(out[1]).astype(np.float)
#END Cp===============================================================

#plot 1 - Cv
fig, ax = plt.subplots(1,2)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in')
ax[0].plot(P, cv11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.8')
ax[0].plot(P, cv12, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.9')
ax[0].plot(CPA_P11, CPA_Cv11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P11, CPARG_Cv11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].plot(CPA_P12, CPA_Cv12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P12, CPARG_Cv12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].set_xlabel(x0label)
ax[0].set_ylabel(y0label)
ax[0].yaxis.set_ticks_position('both')
ax[0].xaxis.set_ticks_position('both')
ax[0].set_xlim([0,40])
ax[0].set_ylim([0.0,7.5])
x0,x1 = ax[0].get_xlim()
y0,y1 = ax[0].get_ylim()
ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[1].tick_params(direction='in')
ax[1].plot(Pp, cp11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.8')
ax[1].plot(Pp, cp12, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.9')
ax[1].plot(CPA_Pp11, CPA_Cp11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1].plot(CPARG_Pp11, CPARG_Cp11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[1].plot(CPA_Pp12, CPA_Cp12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[1].plot(CPARG_Pp12, CPARG_Cp12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax[1].set_xlabel(x1label)
ax[1].set_ylabel(y1label)
ax[1].yaxis.set_ticks_position('both')
ax[1].xaxis.set_ticks_position('both')
ax[1].set_xlim([0,40])
ax[1].set_ylim([0.0,40.0])
x0,x1 = ax[1].get_xlim()
y0,y1 = ax[1].get_ylim()
ax[1].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_cp_supercrit'
fig.savefig(('%s.png' %filename))


#ONLY Cv PLOT=======================================================================================
#plot 1 - Cv
fig, ax = plt.subplots(1,1)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in')
ax.plot(P, cv11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.8')
ax.plot(P, cv12, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.9')
ax.plot(CPA_P11, CPA_Cv11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P11, CPARG_Cv11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P12, CPA_Cv12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P12, CPARG_Cv12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x0label)
ax.set_ylabel(y0label)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,40])
ax.set_ylim([0.0,7.5])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_supercrit'
fig.savefig(('%s.png' %filename))

#ONLY CP PLOT==========================================================================================
fig, ax = plt.subplots(1,1)

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in')
ax.plot(Pp, cp11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.8')
ax.plot(Pp, cp12, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Tr = 0.9')
ax.plot(CPA_Pp11, CPA_Cp11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_Pp11, CPARG_Cp11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_Pp12, CPA_Cp12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_Pp12, CPARG_Cp12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x1label)
ax.set_ylabel(y1label)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,40])
ax.set_ylim([0.0,40.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cp_supercrit'
fig.savefig(('%s.png' %filename))

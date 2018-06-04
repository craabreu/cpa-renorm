#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory
from matplotlib.ticker import FormatStrFormatter

file1 = 'cv_compressed_exp.csv'
file2 = 'cv_08_cpa.csv'
file3 = 'cv_09_cpa.csv'
file4 = 'cv_08_cparg.csv'
file5 = 'cv_09_cparg.csv'
x0label = r'$\rm Pressure\ (MPa)$'
y0label = r'$\rm C_{v}^{res}/R$'
x1label = r'$\rm Pressure\ (MPa)$'
y1label = r'$\rm C_{p}^{res}/R$'

#BEGIN Cv--------------------------------------------------------------
#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
P = np.array(out[0]).astype(np.float)
cv8 = np.array(out[1]).astype(np.float)
cv9 = np.array(out[2]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P8 = np.array(out[0]).astype(np.float)
CPA_Cv8 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P9 = np.array(out[0]).astype(np.float)
CPA_Cv9 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPARG
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P8 = np.array(out[0]).astype(np.float)
CPARG_Cv8 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P9 = np.array(out[0]).astype(np.float)
CPARG_Cv9 = np.array(out[1]).astype(np.float)
#END Cv===============================================================

#BEGIN Cp--------------------------------------------------------------
file1 = 'cp_exp.csv'
file2 = 'cp_08_cpa.csv'
file3 = 'cp_09_cpa.csv'
file4 = 'cp_08_cparg.csv'
file5 = 'cp_09_cparg.csv'

#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Pp = np.array(out[0]).astype(np.float)
cp8 = np.array(out[1]).astype(np.float)
cp9 = np.array(out[2]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp8 = np.array(out[0]).astype(np.float)
CPA_Cp8 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp9 = np.array(out[0]).astype(np.float)
CPA_Cp9 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.8 - CPARG
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp8 = np.array(out[0]).astype(np.float)
CPARG_Cp8 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 0.9 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp9 = np.array(out[0]).astype(np.float)
CPARG_Cp9 = np.array(out[1]).astype(np.float)
#END Cp===============================================================

#plot 1 - Cv
fig, ax = plt.subplots(1,2)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in',size=6,labelsize=12)
ax[0].plot(P, cv8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax[0].plot(P, cv9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[0].plot(CPA_P8, CPA_Cv8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P8, CPARG_Cv8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].plot(CPA_P9, CPA_Cv9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P9, CPARG_Cv9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].set_xlabel(x0label, fontsize=16)
ax[0].set_ylabel(y0label, fontsize=16)
ax[0].yaxis.set_ticks_position('both')
ax[0].xaxis.set_ticks_position('both')
ax[0].set_xlim([0,100])
ax[0].set_ylim([4.5,6.0])
ax[0].set_xticks(np.arange(0,100,20)) 
ax[0].set_yticks(np.arange(4.5,6.0,0.25))
ax[0].yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
x0,x1 = ax[0].get_xlim()
y0,y1 = ax[0].get_ylim()
ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[1].tick_params(direction='in',size=6,labelsize=12)
ax[1].plot(Pp, cp8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax[1].plot(Pp, cp9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[1].plot(CPA_Pp8, CPA_Cp8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1].plot(CPARG_Pp8, CPARG_Cp8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[1].plot(CPA_Pp9, CPA_Cp9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[1].plot(CPARG_Pp9, CPARG_Cp9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax[1].set_xlabel(x1label,fontsize=16)
ax[1].set_ylabel(y1label,fontsize=16)
ax[1].yaxis.set_ticks_position('both')
ax[1].xaxis.set_ticks_position('both')
ax[1].set_xlim([0,100])
ax[1].set_ylim([5.0,11.0])
ax[1].set_xticks(np.arange(0,100,20)) 
ax[1].set_yticks(np.arange(5.0,11.0,1.0))
ax[1].yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
x0,x1 = ax[1].get_xlim()
y0,y1 = ax[1].get_ylim()
ax[1].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_cp_compressed'
fig.savefig(('%s.png' %filename))


#ONLY Cv PLOT=======================================================================================
#plot 1 - Cv
fig, ax = plt.subplots(1,1)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P, cv8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(P, cv9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P8, CPA_Cv8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P8, CPARG_Cv8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P9, CPA_Cv9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P9, CPARG_Cv9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x0label,fontsize=22)
ax.set_ylabel(y0label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,100])
ax.set_ylim([4.5,6.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cv_compressed'
fig.savefig(('%s.png' %filename))

#ONLY CP PLOT==========================================================================================
fig, ax = plt.subplots(1,1)

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(Pp, cp8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(Pp, cp9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_Pp8, CPA_Cp8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_Pp8, CPARG_Cp8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_Pp9, CPA_Cp9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_Pp9, CPARG_Cp9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,100])
ax.set_ylim([5.0,11.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cp_compressed'
fig.savefig(('%s.png' %filename))

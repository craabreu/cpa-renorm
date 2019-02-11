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
file2 = 'cv_101_cpa.csv'
file3 = 'cv_105_cpa.csv'
file4 = 'cv_110_cpa.csv'
file5 = 'cv_101_cparg.csv'
file6 = 'cv_105_cparg.csv'
file7 = 'cv_110_cparg.csv'
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
out.append(df[:][3].values.tolist())
P = np.array(out[0]).astype(np.float)
cv101 = np.array(out[1]).astype(np.float)
cv105 = np.array(out[2]).astype(np.float)
cv110 = np.array(out[3]).astype(np.float)

#Read values - Cv calc values - Tr 1.01 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P101 = np.array(out[0]).astype(np.float)
CPA_Cv101 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.05 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P105 = np.array(out[0]).astype(np.float)
CPA_Cv105 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.10 - CPA
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P110 = np.array(out[0]).astype(np.float)
CPA_Cv110 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.01 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P101 = np.array(out[0]).astype(np.float)
CPARG_Cv101 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.05 - CPARG
df = pd.read_csv('%s' %file6,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P105 = np.array(out[0]).astype(np.float)
CPARG_Cv105 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.10 - CPARG
df = pd.read_csv('%s' %file7,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P110 = np.array(out[0]).astype(np.float)
CPARG_Cv110 = np.array(out[1]).astype(np.float)
#END Cv===============================================================

#BEGIN Cp--------------------------------------------------------------
file1 = 'cp_10_101_105_110_exp.csv'
file1exp2 = 'cp_101_exp.csv'
file1exp1 = 'cp_105_exp.csv'
file2 = 'cp_101_cpa.csv'
file3 = 'cp_105_cpa.csv'
file4 = 'cp_11_cpa.csv'
file5 = 'cp_101_cparg.csv'
file6 = 'cp_105_cparg.csv'
file7 = 'cp_11_cparg.csv'

#Read values - exp values
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
out.append(df[:][6].values.tolist())
out.append(df[:][7].values.tolist())
Pp = np.array(out[0]).astype(np.float)
Pp101 = np.array(out[2]).astype(np.float)
Pp105 = np.array(out[4]).astype(np.float)
Pp110 = np.array(out[6]).astype(np.float)
cp10 = np.array(out[1]).astype(np.float)
cp101 = np.array(out[3]).astype(np.float)
cp105 = np.array(out[5]).astype(np.float)
cp110 = np.array(out[7]).astype(np.float)

#Read values - exp 101 values
df = pd.read_csv('%s' %file1exp1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Pp101 = np.array(out[0]).astype(np.float)
cp101 = np.array(out[1]).astype(np.float)

#Read values - exp 105 values
df = pd.read_csv('%s' %file1exp2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Pp105 = np.array(out[0]).astype(np.float)
cp105 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.01 - CPA
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp101 = np.array(out[0]).astype(np.float)
CPA_Cp101 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.05 - CPA
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp105 = np.array(out[0]).astype(np.float)
CPA_Cp105 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.10 - CPA
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_Pp110 = np.array(out[0]).astype(np.float)
CPA_Cp110 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.01 - CPARG
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp101 = np.array(out[0]).astype(np.float)
CPARG_Cp101 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.05 - CPARG
df = pd.read_csv('%s' %file6,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp105 = np.array(out[0]).astype(np.float)
CPARG_Cp105 = np.array(out[1]).astype(np.float)

#Read values - Cv calc values - Tr 1.10 - CPARG
df = pd.read_csv('%s' %file7,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_Pp110 = np.array(out[0]).astype(np.float)
CPARG_Cp110 = np.array(out[1]).astype(np.float)
#END Cp===============================================================

#plot 1 - Cv
fig, ax = plt.subplots(1,2)

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in',size=6,labelsize=12)
ax[0].plot(P, cv101, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax[0].plot(P, cv105, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax[0].plot(P, cv110, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax[0].plot(CPA_P101, CPA_Cv101, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P101, CPARG_Cv101, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].plot(CPA_P105, CPA_Cv105, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P105, CPARG_Cv105, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].plot(CPA_P110, CPA_Cv110, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P110, CPARG_Cv110, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].set_xlabel(x0label,fontsize=16)
ax[0].set_ylabel(y0label,fontsize=16)
ax[0].yaxis.set_ticks_position('both')
ax[0].xaxis.set_ticks_position('both')
ax[0].set_xticks(np.arange(0,50,10))
ax[0].set_xlim([0,30])
ax[0].set_ylim([0.0,10.0])
x0,x1 = ax[0].get_xlim()
y0,y1 = ax[0].get_ylim()
ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 2 - Cp
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[1].tick_params(direction='in',size=6,labelsize=12)
ax[1].plot(Pp101, cp101, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax[1].plot(Pp105, cp105, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax[1].plot(Pp110, cp110, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[1].plot(CPA_Pp101, CPA_Cp101, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1].plot(CPARG_Pp101, CPARG_Cp101, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[1].plot(CPA_Pp105, CPA_Cp105, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax[1].plot(CPARG_Pp105, CPARG_Cp105, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax[1].plot(CPA_Pp110, CPA_Cp110, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax[1].plot(CPARG_Pp110, CPARG_Cp110, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax[1].set_xlabel(x1label,fontsize=16)
ax[1].set_ylabel(y1label,fontsize=16)
ax[1].yaxis.set_ticks_position('both')
ax[1].xaxis.set_ticks_position('both')
ax[1].set_xticks(np.arange(0,100.0,10))
ax[1].set_yticks(np.arange(0,180.0,20))
ax[1].set_xlim([0,30])
ax[1].set_ylim([0.0,160.0])
#ax[1].set_xticklabels(np.arange(0,50,10))
#ax[1].set_yticklabels(np.arange(0,50,10))
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
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P, cv11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(P, cv12, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P11, CPA_Cv11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P11, CPARG_Cv11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P12, CPA_Cv12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P12, CPARG_Cv12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x0label,fontsize=22)
ax.set_ylabel(y0label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,40])
ax.set_ylim([0.0,10.0])
ax.set_xticks(np.arange(0,50,10))
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
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(Pp, cp11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(Pp, cp12, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_Pp11, CPA_Cp11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_Pp11, CPARG_Cp11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_Pp12, CPA_Cp12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_Pp12, CPARG_Cp12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,40])
ax.set_ylim([0.0,40.0])
ax.set_xticks(np.arange(0,50,10))
ax.set_yticks(np.arange(0,50,10))
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'cp_supercrit'
fig.savefig(('%s.png' %filename))

#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'u_09_exp.csv'
file2 = 'u_095_exp.csv'
file3 = 'u_099_exp.csv'
file4 = 'u_09_cpa.csv'
file5 = 'u_095_cpa.csv'
file6 = 'u_099_cpa.csv'
file7 = 'u_09_cparg.csv'
file8 = 'u_095_cparg.csv'
file9 = 'u_099_cparg.csv'
file10 = 'u_10_101_105_110_exp.csv'
file11 = 'u_10_cpa.csv'
file12 = 'u_101_105_110_cpa.csv'
file122 = 'u_101_cpa.csv'
file13 = 'u_10_101_105_110_cparg.csv'
x0label = r'$\rm Pressure\ (MPa)$'
y0label = r'$\rm u\ (m/s)$'
x1label = r'$\rm Pressure\ (MPa)$'
y1label = r'$\rm u\ (m/s)$'
x2label = r'$\rm Pressure\ (MPa)$'
y2label = r'$\rm u\ (m/s)$'

#BEGIN u--------------------------------------------------------------
#u exp tr 0.9 
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P9 = np.array(out[0]).astype(np.float)
u9 = np.array(out[1]).astype(np.float)

#BEGIN u--------------------------------------------------------------
#u exp tr 0.95 
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P95 = np.array(out[0]).astype(np.float)
u95 = np.array(out[1]).astype(np.float)

#BEGIN u--------------------------------------------------------------
#u exp tr 0.99 
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
P99 = np.array(out[0]).astype(np.float)
u99 = np.array(out[1]).astype(np.float)

#u cpa tr 0.9
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P9 = np.array(out[0]).astype(np.float)
CPA_u9 = np.array(out[1]).astype(np.float)

#u cpa tr 0.95
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P95 = np.array(out[0]).astype(np.float)
CPA_u95 = np.array(out[1]).astype(np.float)

#u cpa tr 0.99
df = pd.read_csv('%s' %file6,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P99 = np.array(out[0]).astype(np.float)
CPA_u99 = np.array(out[1]).astype(np.float)

#u cparg tr 0.9
df = pd.read_csv('%s' %file7,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P9 = np.array(out[0]).astype(np.float)
CPARG_u9 = np.array(out[1]).astype(np.float)

#u cparg tr 0.95
df = pd.read_csv('%s' %file8,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P95 = np.array(out[0]).astype(np.float)
CPARG_u95 = np.array(out[1]).astype(np.float)

#u cparg tr 0.99
df = pd.read_csv('%s' %file9,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P99 = np.array(out[0]).astype(np.float)
CPARG_u99 = np.array(out[1]).astype(np.float)

#u exp tr 1 1.01 1.05 1.10
df = pd.read_csv('%s' %file10,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
out.append(df[:][6].values.tolist())
out.append(df[:][7].values.tolist())
P10 = np.array(out[0]).astype(np.float)
u10 = np.array(out[1]).astype(np.float)
P101 = np.array(out[2]).astype(np.float)
u101 = np.array(out[3]).astype(np.float)
P105 = np.array(out[4]).astype(np.float)
u105 = np.array(out[5]).astype(np.float)
P110 = np.array(out[6]).astype(np.float)
u110 = np.array(out[7]).astype(np.float)

#u cpa tr 1
df = pd.read_csv('%s' %file11,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P10 = np.array(out[0]).astype(np.float)
CPA_u10 = np.array(out[1]).astype(np.float)

#u cpa tr 1.01 1.05 1.10
df = pd.read_csv('%s' %file12,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
CPA_P101 = np.array(out[0]).astype(np.float)
CPA_u101 = np.array(out[1]).astype(np.float)
CPA_P105 = np.array(out[2]).astype(np.float)
CPA_u105 = np.array(out[3]).astype(np.float)
CPA_P110 = np.array(out[4]).astype(np.float)
CPA_u110 = np.array(out[5]).astype(np.float)

#u cpa tr 1.01 1.05 1.10
df = pd.read_csv('%s' %file122,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P101 = np.array(out[0]).astype(np.float)
CPA_u101 = np.array(out[1]).astype(np.float)

#u cparg tr 1 1.01 1.05 1.10
df = pd.read_csv('%s' %file13,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
out.append(df[:][6].values.tolist())
out.append(df[:][7].values.tolist())
CPARG_P10 = np.array(out[0]).astype(np.float)
CPARG_u10 = np.array(out[1]).astype(np.float)
CPARG_P101 = np.array(out[2]).astype(np.float)
CPARG_u101 = np.array(out[3]).astype(np.float)
CPARG_P105 = np.array(out[4]).astype(np.float)
CPARG_u105 = np.array(out[5]).astype(np.float)
CPARG_P110 = np.array(out[6]).astype(np.float)
CPARG_u110 = np.array(out[7]).astype(np.float)
#END u===============================================================

#ALL PLOTS
fig, ax = plt.subplots(nrows=3,ncols=1)
#plot 1 - u compressed
#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in',size=6,labelsize=16)
ax[0].plot(P9, u9, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax[0].plot(P95, u95, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax[0].plot(P99, u99, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[0].plot(CPA_P9, CPA_u9, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P9, CPARG_u9, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].plot(CPA_P95, CPA_u95, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P95, CPARG_u95, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].plot(CPA_P99, CPA_u99, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P99, CPARG_u99, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax[0].set_xlabel(x0label,fontsize=22)
ax[0].set_ylabel(y0label,fontsize=22)
ax[0].yaxis.set_ticks_position('both')
ax[0].xaxis.set_ticks_position('both')
ax[0].set_xlim([0,100])
ax[0].set_ylim([400.0,1400.0])
x0,x1 = ax[0].get_xlim()
y0,y1 = ax[0].get_ylim()
#ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 2 - u critical
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[1].tick_params(direction='in',size=6,labelsize=16)
ax[1].plot(P10, u10, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[1].plot(CPA_P10, CPA_u10, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1].plot(CPARG_P10, CPARG_u10, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[1].set_xlabel(x1label,fontsize=22)
ax[1].set_ylabel(y1label,fontsize=22)
ax[1].yaxis.set_ticks_position('both')
ax[1].xaxis.set_ticks_position('both')
ax[1].set_xlim([0,22])
ax[1].set_ylim([200.0,600.0])
x0,x1 = ax[1].get_xlim()
y0,y1 = ax[1].get_ylim()
#ax[1].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

#plot 3 - u supercritical
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax[2].tick_params(direction='in',size=6,labelsize=16)
ax[2].plot(P101, u101, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax[2].plot(P105, u105, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax[2].plot(P110, u110, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[2].plot(CPA_P101, CPA_u101, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[2].plot(CPARG_P101, CPARG_u101, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[2].plot(CPA_P105, CPA_u105, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax[2].plot(CPARG_P105, CPARG_u105, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax[2].plot(CPA_P110, CPA_u110, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax[2].plot(CPARG_P110, CPARG_u110, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax[2].set_xlabel(x1label,fontsize=22)
ax[2].set_ylabel(y1label,fontsize=22)
ax[2].yaxis.set_ticks_position('both')
ax[2].xaxis.set_ticks_position('both')
ax[2].set_xlim([0,50])
ax[2].set_ylim([200.0,700.0])
x0,x1 = ax[2].get_xlim()
y0,y1 = ax[2].get_ylim()
#ax[2].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'u_all'
fig.savefig(('%s.png' %filename))


#ONLY COMPRESSED PLOT=======================================================================================
#plot 1 - Cv
fig, ax = plt.subplots(1,1)

#plot 1 - u compressed
#ax[0].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P9, u9, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax.plot(P95, u95, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax.plot(P99, u99, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P9, CPA_u9, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P9, CPARG_u9, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P95, CPA_u95, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P95, CPARG_u95, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax.plot(CPA_P99, CPA_u99, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P99, CPARG_u99, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x0label,fontsize=22)
ax.set_ylabel(y0label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,100])
ax.set_ylim([200.0,1200.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
#ax[0].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'u_compressed'
fig.savefig(('%s.png' %filename))

#ONLY CRITICAL PLOT==========================================================================================
fig, ax = plt.subplots(1,1)

#plot 2 - u critical
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P10, u10, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P10, CPA_u10, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P10, CPARG_u10, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,22])
ax.set_ylim([150.0,600.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'u_critical'
fig.savefig(('%s.png' %filename))

#ONLY SUPERCRITICAL PLOT==========================================================================================
fig, ax = plt.subplots(1,1)

#plot 3 - u supercritical
#ax[1].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P101, u101, 'o', markerfacecolor='none', markeredgecolor='blue', markersize=6, label='Tr = 0.8')
ax.plot(P105, u105, 's', markerfacecolor='none', markeredgecolor='green', markersize=6, label='Tr = 0.9')
ax.plot(P110, u110, 'd', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P101, CPA_u101, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P101, CPARG_u101, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P105, CPA_u105, color='green', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P105, CPARG_u105, color='green', linewidth=1.0, linestyle='-',  label='i = 6')
ax.plot(CPA_P110, CPA_u110, color='black', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P110, CPARG_u110, color='black', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,50])
ax.set_ylim([150.0,650.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
#ax[2].set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'u_supercritical'
fig.savefig(('%s.png' %filename))

#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'u_08_09_exp.csv'
file2 = 'u_08_cpa.csv'
file3 = 'u_09_cpa.csv'
file4 = 'u_08_cparg.csv'
file5 = 'u_09_cparg.csv'
file6 = 'u_10_11_12_exp.csv'
file7 = 'u_10_cpa.csv'
file8 = 'u_11_12_cpa.csv'
file9 = 'u_10_11_12_cparg.csv'
x0label = r'$\rm Pressure (MPa)$'
y0label = r'$\rm u (m/s)$'
x1label = r'$\rm Pressure (MPa)$'
y1label = r'$\rm u (m/s)$'
x2label = r'$\rm Pressure (MPa)$'
y2label = r'$\rm u (m/s)$'

#BEGIN u--------------------------------------------------------------
#u exp tr 0.8 0.9 
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
P = np.array(out[0]).astype(np.float)
u8 = np.array(out[1]).astype(np.float)
u9 = np.array(out[2]).astype(np.float)

#u cpa tr 0.8
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P8 = np.array(out[0]).astype(np.float)
CPA_u8 = np.array(out[1]).astype(np.float)

#u cpa tr 0.9
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P9 = np.array(out[0]).astype(np.float)
CPA_u9 = np.array(out[1]).astype(np.float)

#u cparg tr 0.8
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P8 = np.array(out[0]).astype(np.float)
CPARG_u8 = np.array(out[1]).astype(np.float)

#u cparg tr 0.9
df = pd.read_csv('%s' %file5,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPARG_P9 = np.array(out[0]).astype(np.float)
CPARG_u9 = np.array(out[1]).astype(np.float)

#u exp tr 1 1.1 1.2
df = pd.read_csv('%s' %file6,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
P10 = np.array(out[0]).astype(np.float)
u10 = np.array(out[1]).astype(np.float)
u11 = np.array(out[3]).astype(np.float)
u12 = np.array(out[5]).astype(np.float)

#u cpa tr 1
df = pd.read_csv('%s' %file7,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
CPA_P10 = np.array(out[0]).astype(np.float)
CPA_u10 = np.array(out[1]).astype(np.float)

#u cpa tr 1.1 1.2
df = pd.read_csv('%s' %file8,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
CPA_P11 = np.array(out[0]).astype(np.float)
CPA_u11 = np.array(out[1]).astype(np.float)
CPA_P12 = np.array(out[2]).astype(np.float)
CPA_u12 = np.array(out[3]).astype(np.float)

#u cparg tr 1 1.1 1.2
df = pd.read_csv('%s' %file9,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
out.append(df[:][4].values.tolist())
out.append(df[:][5].values.tolist())
CPARG_P10 = np.array(out[0]).astype(np.float)
CPARG_u10 = np.array(out[1]).astype(np.float)
CPARG_P11 = np.array(out[2]).astype(np.float)
CPARG_u11 = np.array(out[3]).astype(np.float)
CPARG_P12 = np.array(out[4]).astype(np.float)
CPARG_u12 = np.array(out[5]).astype(np.float)
#END u===============================================================

#ALL PLOTS
fig, ax = plt.subplots(nrows=3,ncols=1)
#plot 1 - u compressed
#ax[0].set_aspect(aspect='auto', adjustable='box')
ax[0].tick_params(direction='in',size=6,labelsize=16)
ax[0].plot(P, u8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax[0].plot(P, u9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[0].plot(CPA_P8, CPA_u8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0].plot(CPARG_P8, CPARG_u8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[0].plot(CPA_P9, CPA_u9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[0].plot(CPARG_P9, CPARG_u9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
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
ax[2].plot(P10, u11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax[2].plot(P10, u12, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax[2].plot(CPA_P11, CPA_u11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[2].plot(CPARG_P11, CPARG_u11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax[2].plot(CPA_P12, CPA_u12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax[2].plot(CPARG_P12, CPARG_u12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
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

#ax[0].set_aspect(aspect='auto', adjustable='box')
ax.tick_params(direction='in',size=6,labelsize=16)
ax.plot(P, u8, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(P, u9, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P8, CPA_u8, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P8, CPARG_u8, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P9, CPA_u9, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P9, CPARG_u9, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x0label,fontsize=22)
ax.set_ylabel(y0label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,100])
ax.set_ylim([400.0,1400.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
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
ax.set_ylim([200.0,600.0])
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
ax.plot(P10, u11, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.8')
ax.plot(P10, u12, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Tr = 0.9')
ax.plot(CPA_P11, CPA_u11, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax.plot(CPARG_P11, CPARG_u11, color='blue', linewidth=1.0, linestyle='-',  label='i = 4')
ax.plot(CPA_P12, CPA_u12, color='blue', linewidth=1.0, linestyle='--',  label='i = 5')
ax.plot(CPARG_P12, CPARG_u12, color='blue', linewidth=1.0, linestyle='-',  label='i = 6')
ax.set_xlabel(x1label,fontsize=22)
ax.set_ylabel(y1label,fontsize=22)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.set_xlim([0,50])
ax.set_ylim([200.0,700.0])
x0,x1 = ax.get_xlim()
y0,y1 = ax.get_ylim()
ax.set_aspect((x1-x0)/(y1-y0))
#ax[0].legend()

plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'u_supercritical'
fig.savefig(('%s.png' %filename))

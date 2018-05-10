#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'methanol_pv.csv'
file2 = 'co2_pv.csv'
file3 = 'h2s_pv.csv'
file4 = 'c4_pv.csv'
file1c = 'methanol_cpa.csv'
file2c = 'co2_cpa.csv'
file3c = 'h2s_cpa.csv'
file4c = 'c4_cpa.csv'
file1cr = 'methanol_cparg.csv'
file2cr = 'co2_cparg.csv'
file3cr = 'h2s_cparg.csv'
file4cr = 'c4_cparg.csv'
xlabel = '$Density (mol/m^{3})$'
ylabel = '$Temperature (K)$'

#methanol exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tm = np.array(out[0]).astype(np.float)
rholm = np.array(out[1]).astype(np.float)
rhovm = np.array(out[2]).astype(np.float)

#co2 exp
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tc = np.array(out[0]).astype(np.float)
rholc = np.array(out[1]).astype(np.float)
rhovc = np.array(out[2]).astype(np.float)

#h2s exp
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Th = np.array(out[0]).astype(np.float)
rholh = np.array(out[1]).astype(np.float)
rhovh = np.array(out[2]).astype(np.float)

#butane exp
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tb = np.array(out[0]).astype(np.float)
rholb = np.array(out[1]).astype(np.float)
rhovb = np.array(out[2]).astype(np.float)

#methanol cpa
df = pd.read_csv('%s' %file1c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tmc = np.array(out[0]).astype(np.float)
rholmc = np.array(out[1]).astype(np.float)
rhovmc = np.array(out[2]).astype(np.float)

#co2 cpa
df = pd.read_csv('%s' %file2c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tcc = np.array(out[0]).astype(np.float)
rholcc = np.array(out[1]).astype(np.float)
rhovcc = np.array(out[2]).astype(np.float)

#h2s cpa
df = pd.read_csv('%s' %file3c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Thc = np.array(out[0]).astype(np.float)
rholhc = np.array(out[1]).astype(np.float)
rhovhc = np.array(out[2]).astype(np.float)

#butane cpa
df = pd.read_csv('%s' %file4c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tbc = np.array(out[0]).astype(np.float)
rholbc = np.array(out[1]).astype(np.float)
rhovbc = np.array(out[2]).astype(np.float)

#methanol cparg
df = pd.read_csv('%s' %file1cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tmcr = np.array(out[0]).astype(np.float)
rholmcr = np.array(out[1]).astype(np.float)
rhovmcr = np.array(out[2]).astype(np.float)

#co2 cparg
df = pd.read_csv('%s' %file2cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tccr = np.array(out[0]).astype(np.float)
rholccr = np.array(out[1]).astype(np.float)
rhovccr = np.array(out[2]).astype(np.float)

#h2s cparg
df = pd.read_csv('%s' %file3cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Thcr = np.array(out[0]).astype(np.float)
rholhcr = np.array(out[1]).astype(np.float)
rhovhcr = np.array(out[2]).astype(np.float)

#butane cparg
df = pd.read_csv('%s' %file4cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
Tbcr = np.array(out[0]).astype(np.float)
rholbcr = np.array(out[1]).astype(np.float)
rhovbcr = np.array(out[2]).astype(np.float)

#plot
fig, ax = plt.subplots(2,2)

#Methanol subplot
ax[0,0].tick_params(direction='in')
ax[0,0].plot(rholm, Tm, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[0,0].plot(rhovm, Tm, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[0,0].plot(rholmc, Tmc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0,0].plot(rhovmc, Tmc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0,0].plot(rholmcr, Tmcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[0,0].plot(rhovmcr, Tmcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[0,0].set_xlabel(xlabel)
ax[0,0].set_ylabel(ylabel)
ax[0,0].yaxis.set_ticks_position('both')
ax[0,0].xaxis.set_ticks_position('both')
ax[0,0].set_xlim([-500,25000])
ax[0,0].set_ylim([300,550])
ax[0,0].text(18500, 515, '$Methanol$')
ax[0,0].tick_params(labelsize=8)

#CO2 subplot
ax[1,0].tick_params(direction='in')
ax[1,0].plot(rholc, Tc, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[1,0].plot(rhovc, Tc, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[1,0].plot(rholcc, Tcc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1,0].plot(rhovcc, Tcc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1,0].plot(rholccr, Tccr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[1,0].plot(rhovccr, Tccr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[1,0].set_xlabel(xlabel)
ax[1,0].set_ylabel(ylabel)
ax[1,0].yaxis.set_ticks_position('both')
ax[1,0].xaxis.set_ticks_position('both')
ax[1,0].set_xlim([-500,27500])
ax[1,0].set_ylim([220,320])
ax[1,0].text(23000, 305, '$CO_{2}$')
ax[1,0].tick_params(labelsize=8)

#H2S subplot
ax[0,1].tick_params(direction='in')
ax[0,1].plot(rholh, Th, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[0,1].plot(rhovh, Th, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[0,1].plot(rholhc, Thc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0,1].plot(rhovhc, Thc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[0,1].plot(rholhcr, Thcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[0,1].plot(rhovhcr, Thcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[0,1].set_xlabel(xlabel)
ax[0,1].set_ylabel(ylabel)
ax[0,1].yaxis.set_ticks_position('both')
ax[0,1].xaxis.set_ticks_position('both')
ax[0,1].set_xlim([-500,30000])
ax[0,1].set_ylim([200,400])
ax[0,1].text(25500, 375, '$H_{2}S$')
ax[0,1].tick_params(labelsize=8)

#Butane subplot
ax[1,1].tick_params(direction='in')
ax[1,1].plot(rholb, Tb, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[1,1].plot(rhovb, Tb, 's', markerfacecolor='none', markeredgecolor='black', markersize=5, label='Methanol')
ax[1,1].plot(rholbc, Tbc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1,1].plot(rhovbc, Tbc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
ax[1,1].plot(rholbcr, Tbcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[1,1].plot(rhovbcr, Tbcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
ax[1,1].set_xlabel(xlabel)
ax[1,1].set_ylabel(ylabel)
ax[1,1].yaxis.set_ticks_position('both')
ax[1,1].xaxis.set_ticks_position('both')
ax[1,1].set_xlim([-500,15000])
ax[1,1].set_ylim([150,450])
ax[1,1].text(10500, 415, '$n-Butane$')
ax[1,1].tick_params(labelsize=8)


plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'PV_pure_4'
fig.savefig(('%s.png' %filename))

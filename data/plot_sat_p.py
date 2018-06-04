#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'methanol_pt.csv'
file2 = 'co2_pt.csv'
file3 = 'h2s_pt.csv'
file4 = 'c4_pt.csv'
file1c = 'methanol_cpa.csv'
file2c = 'co2_cpa.csv'
file3c = 'h2s_cpa.csv'
file4c = 'c4_cpa.csv'
file1cr = 'methanol_cparg.csv'
file2cr = 'co2_cparg.csv'
file3cr = 'h2s_cparg.csv'
file4cr = 'c4_cparg.csv'
fileexp = 'critexp_pt.csv'
xlabel = r'$\rm Temperature (K)$'
ylabel = r'$\rm Pressure (MPa)$'

#methanol exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Tm = np.array(out[0]).astype(np.float)
Pm = np.array(out[1]).astype(np.float)

#critical points exp
df = pd.read_csv('%s' %fileexp,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Tcrit = np.array(out[0]).astype(np.float)
Pcrit = np.array(out[1]).astype(np.float)
Tcritb = Tcrit[0]
Tcritc = Tcrit[1]
Tcrith = Tcrit[2]
Tcritm = Tcrit[3]
Pcritb = Pcrit[0]
Pcritc = Pcrit[1]
Pcrith = Pcrit[2]
Pcritm = Pcrit[3]

#co2 exp
df = pd.read_csv('%s' %file2,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Tc = np.array(out[0]).astype(np.float)
Pc = np.array(out[1]).astype(np.float)

#h2s exp
df = pd.read_csv('%s' %file3,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Th = np.array(out[0]).astype(np.float)
Ph = np.array(out[1]).astype(np.float)

#butane exp
df = pd.read_csv('%s' %file4,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
Tb = np.array(out[0]).astype(np.float)
Pb = np.array(out[1]).astype(np.float)

#methanol cpa
df = pd.read_csv('%s' %file1c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tmc = np.array(out[0]).astype(np.float)
Pmc = np.array(out[3]).astype(np.float)

#co2 cpa
df = pd.read_csv('%s' %file2c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tcc = np.array(out[0]).astype(np.float)
Pcc = np.array(out[3]).astype(np.float)

#h2s cpa
df = pd.read_csv('%s' %file3c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Thc = np.array(out[0]).astype(np.float)
Phc = np.array(out[3]).astype(np.float)

#butane cpa
df = pd.read_csv('%s' %file4c,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tbc = np.array(out[0]).astype(np.float)
Pbc = np.array(out[3]).astype(np.float)

#methanol cparg
df = pd.read_csv('%s' %file1cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tmcr = np.array(out[0]).astype(np.float)
Pmcr = np.array(out[3]).astype(np.float)

#co2 cparg
df = pd.read_csv('%s' %file2cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tccr = np.array(out[0]).astype(np.float)
Pccr = np.array(out[3]).astype(np.float)

#h2s cparg
df = pd.read_csv('%s' %file3cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Thcr = np.array(out[0]).astype(np.float)
Phcr = np.array(out[3]).astype(np.float)

#butane cparg
df = pd.read_csv('%s' %file4cr,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
Tbcr = np.array(out[0]).astype(np.float)
Pbcr = np.array(out[3]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in',size=6,labelsize=18)

plt.plot(Tm, Pm, 'o', markerfacecolor='none', markeredgecolor='black', markersize=7, label='Methanol')
plt.plot(Tc, Pc, 's', markerfacecolor='none', markeredgecolor='black', markersize=7, label='CO2')
plt.plot(Th, Ph, '^', markerfacecolor='none', markeredgecolor='black', markersize=7, label='H2S')
plt.plot(Tb, Pb, 'D', markerfacecolor='none', markeredgecolor='black', markersize=7, label='n-Butane')
plt.plot(Tcritm, Pcritm, 'o', markerfacecolor='black', markeredgecolor='black', markersize=7, label='Methanol')
plt.plot(Tcritc, Pcritc, 's', markerfacecolor='black', markeredgecolor='black', markersize=7, label='CO2')
plt.plot(Tcrith, Pcrith, '^', markerfacecolor='black', markeredgecolor='black', markersize=7, label='H2S')
plt.plot(Tcritb, Pcritb, 'D', markerfacecolor='black', markeredgecolor='black', markersize=7, label='n-Butane')
plt.plot(Tmc, Pmc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(Tcc, Pcc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(Thc, Phc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(Tbc, Pbc, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(Tmcr, Pmcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
plt.plot(Tccr, Pccr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
plt.plot(Thcr, Phcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')
plt.plot(Tbcr, Pbcr, color='blue',   linewidth=1.0, linestyle='-',  label='i = 3')

#plt.legend()
ax.set_xlabel(xlabel,fontsize=26)
ax.set_ylabel(ylabel,fontsize=26)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

plt.text(300, 8.5, r'$\rm CO_{2}$',fontsize=20)
plt.text(375, 10.7, r'$\rm H_{2}S$',fontsize=20)
plt.text(400, 4.5, r'$\rm n-Butane$',fontsize=20)
plt.text(480, 11.0, r'$\rm Methanol$',fontsize=20)

ax.set_xlim([200,550])
ax.set_ylim([0,12])

plt.ylabel(ylabel,fontsize=22)
plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'sat_p'
fig.savefig(('%s.png' %filename))

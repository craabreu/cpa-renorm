#Python script to plot
import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
from matplotlib.transforms import blended_transform_factory

file1 = 'beta.csv'
xlabel = r'$\rm ln|T_{r}-1|$'
ylabel = r'$\rm ln|\frac{(\rho_{l}-\rho_{v})}{\rho_{c}}|$'

#methanol exp
df = pd.read_csv('%s' %file1,sep=';',header=None)
out = []
out.append(df[:][0].values.tolist())
out.append(df[:][1].values.tolist())
out.append(df[:][2].values.tolist())
out.append(df[:][3].values.tolist())
cparg = np.array(out[0]).astype(np.float)
cparg1 = np.array(out[1]).astype(np.float)
cpa = np.array(out[2]).astype(np.float)
cpa1 = np.array(out[3]).astype(np.float)

#plot
fig, ax = plt.subplots(1,1)
ax.tick_params(direction='in',size=6,labelsize=16)

plt.plot(cparg, cparg1, 'o', markerfacecolor='none', markeredgecolor='black', markersize=6, label='Methanol')
plt.plot(cpa, cpa1, 's', markerfacecolor='none', markeredgecolor='black', markersize=6, label='CO2')
plt.plot(cparg, cparg1, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')
plt.plot(cpa, cpa1, color='blue',   linewidth=1.0, linestyle='--',  label='i = 3')

#plt.legend()
ax.set_xlabel(xlabel, fontsize=16)
ax.set_ylabel(ylabel, fontsize=16)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

plt.text(-5.9, -0.2, '$CPA+RG$', fontsize=20)
plt.text(-5.9, -1.3, '$CPA$', fontsize=20)
plt.text(-5.9, -0.3, r'$\beta=0.330$', fontsize=20)
plt.text(-5.9, -1.4, r'$\beta=0.496$', fontsize=20)
#plt.text(300, 8.5, '$CO_{2}$')
#plt.text(375, 10.7, '$H_{2}S$')

ax.set_xlim([-7.5,-4.5])
ax.set_ylim([-1.7,0.0])

plt.ylabel(ylabel, fontsize=22)
plt.tight_layout()
plt.rcParams["axes.labelweight"] = "bold"
filename = 'beta'
fig.savefig(('%s.png' %filename))

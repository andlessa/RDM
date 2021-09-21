#!/usr/bin/env python3

"""Plot validation results."""

# %% Imports
import os,glob
import pyslha
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from getContour import getContour
import seaborn as sns
pd.options.mode.chained_assignment = None #Disable copy warnings
#Define plotting style:
sns.set() #Set style
sns.set_style('ticks',{'font.family':'serif', 'font.serif':'Times New Roman'})
sns.set_context('paper', font_scale=2.5)
cm = plt.cm.get_cmap('RdYlBu')

# %% Load data
offCurve = np.genfromtxt('../orig/fig_aux01a_exclusion.csv',
                        delimiter=',', names=['msb','mlsp'],skip_header=1)


# %% Get data from SModelS results
with open('T2bb_2EqMassAx_EqMassBy.py','r') as f:
    exec(f.read())
valData = validationData[:]
recastData = []

for pt in valData:
    if not 'UL' in pt or not pt['UL']:
        continue
    robs = pt['signal']/pt['UL']
    recastData.append([pt['axes']['x'],pt['axes']['y'],robs])

recastData = np.array(recastData)

##  %% --------------------Best SR:
## Get exclusion contours for combined results (signal +- 20%)
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
# ax = plt.scatter(recastData[:,0],recastData[:,1],
    # c=recastData[:,5],cmap=cm,vmin=0.0,vmax=2.0,s=70)
# cb = plt.colorbar(ax)
for level,curves in contours.items():
    npts = [len(c) for c in curves]
    for curve in curves:
        if len(curve) != max(npts): continue
        if level == 1.0:
            ls = '-'
            label = r'Recast'
        elif level == 0.8:
            ls = '--'
            label = r'Recast $\pm$ 20%'
        elif level == 1.2:
            ls = '--'
            label = None

        #Add low m point to exclusion curve:
        curve = np.insert(curve,len(curve), [[min(recastData[:,0]),max(recastData[recastData[:,0] == min(recastData[:,0])][:,1])]],axis=0)
        contours[level] = [curve]

        plt.plot(curve[:,0],curve[:,1],c='r',label= label,linestyle=ls,linewidth=4)

plt.fill_between(contours[1.0][0][:,0], contours[1.0][0][:,1], color='r', alpha=0.2)
plt.plot(offCurve['msb'],offCurve['mlsp'],linewidth=4,
            color='black',label='ATLAS-SUSY-2018-34')
plt.xlabel(r'$\mathregular{m_{\tilde{b}}}$ (GeV)',fontsize=30)
plt.ylabel(r'$\mathregular{m_{\tilde{\chi}_1^0}}$ (GeV)',fontsize=30)
plt.legend(loc='upper left',framealpha=1.0)
plt.title(r'ATLAS $bb$ plus MET: $pp \to \tilde{b} \tilde{b}, \tilde{b} \to b + \tilde{\chi}_1^0$')
plt.tight_layout()
plt.ylim(100,1000)
plt.xlim(400,1400)
plt.savefig("atlas_susy_2018_34_T2bb.png")
plt.show()

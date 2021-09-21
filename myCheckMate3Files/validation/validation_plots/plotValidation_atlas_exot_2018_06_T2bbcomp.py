#!/usr/bin/env python3

"""Plot validation results."""

# %% Imports
import os,glob
import pyslha
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from getContour import getContour

pd.options.mode.chained_assignment = None #Disable copy warnings
#Define plotting style:
sns.set() #Set style
sns.set_style('ticks',{'font.family':'serif', 'font.serif':'Times New Roman'})
sns.set_context('paper', font_scale=1.8)
cm = plt.cm.get_cmap('RdYlBu')

# %% Load data
offCurve = np.genfromtxt('./ATLAS_data/ATLAS-EXOT-2018-06_fig_08a.csv',
                        delimiter=',', names=['msb','mlsp'])

# %% Get data from CheckMate results
resultFolder = '../validation_results/atlas_exot_2018_06'
slhaFolder = '../validation_slha/'
recastData = []
srRecast = []
for slhaFile in glob.glob(slhaFolder+'T2bbcomp*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    msb = slhaData.blocks['MASS'][1000005]
    mlsp = slhaData.blocks['MASS'][1000022]
    resDir = os.path.splitext(os.path.basename(slhaFile))[0]
    resFile = os.path.join(resultFolder,resDir,'evaluation',
                'total_results.txt')
    if not os.path.isfile(resFile):
        continue
    data = np.genfromtxt(resFile,names=True,
            usecols=(1,2,3,4,5,6,7,8,9,10,11,12),
            dtype=None,encoding=None)
    ibest = np.argmax(data['rexp'])
    bestSR = data['sr'][ibest]
    robs = data['robs'][ibest]
    robscons = data['robscons'][ibest]
    recastData.append([msb,mlsp,robs,robscons])

recastData = np.array(recastData)

## %% Get exclusion contours for combined results (signal +- 20%)
contours = getContour(recastData[:,0],recastData[:,0]-recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,0]-recastData[:,1],
    c=recastData[:,2],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contours.items():
    # if level != 1.0: continue
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

        plt.plot(curve[:,0],curve[:,1],c='r',label= label,linestyle=ls,linewidth=4)

plt.fill_betweenx(contours[1.0][0][:,1], contours[1.0][0][:,0], color='r', alpha=0.2)
plt.plot(offCurve['msb'],offCurve['msb']-offCurve['mlsp'],linewidth=4,
            color='black',label='ATLAS-EXOT-2018-06')
plt.xlabel(r'$m_{\tilde{t}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{t}}-m_{\tilde{\chi}_1^0}$ (GeV)')
# for pt in recastData:
    # if pt[2] < 1.0:
        # plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    # fontsize=10)
# cb.set_label("r")
plt.legend(loc='upper left')
plt.xlim(200.,600)
plt.ylim(0.,30)

plt.title(r'$\tilde{b} \tilde{b}, \tilde{b} \to b + \tilde{\chi}_1^0$ (Best SR Exclusion)')
plt.savefig("atlas_exot_2018_06_T2bb.png")
plt.show()

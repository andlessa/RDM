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
offCurve = np.genfromtxt('./CMS_data/CMS-SUS-16-032_Figure_005.csv',
                        delimiter=',', names=['msb','mlsp'])

# %% Get data from CheckMate results
resultFolder = './validation_results'
slhaFolder = './validation_slha/'
recastData = []
srRecast = []
for slhaFile in glob.glob(slhaFolder+'/sbottom*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    msb = slhaData.blocks['MASS'][1000005]
    mlsp = slhaData.blocks['MASS'][1000022]
    resDir = os.path.splitext(os.path.basename(slhaFile))[0]
    resFile = os.path.join(resultFolder,resDir,'evaluation',
                'total_results.txt')
    if not os.path.isfile(resFile):
        continue
    data = np.genfromtxt(resFile,names=True,usecols=(1,2,3,4,5,6,7,8,9,10,11),
            dtype=None,encoding=None)
    ibest = np.argmax(data['rexp'])
    robs = data['robs'][ibest]
    s = data['s'][ibest]
    ds = data['ds'][ibest]
    # ds = 0.2*s
    s95obs = data['s95obs'][ibest]
    rcons = (s-1.64*ds)/s95obs
    recastData.append([msb,mlsp,robs])
    srRecast.append([msb,mlsp,data['sr'][ibest]])

recastData = np.array(recastData)

## %% Get exclusion contours for signal +- 20%
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,2],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contours.items():
    for curve in curves:
        plt.plot(curve[:,0],curve[:,1],label=level,linestyle='--',linewidth=4)
plt.plot(offCurve['msb'],offCurve['mlsp'],linewidth=4,color='black')
plt.xlabel(r'$m_{\tilde{b}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
for pt in recastData:
    if pt[2] < 1.0:
        plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    fontsize=10)
cb.set_label("r")
plt.show()



# %% plot signal regions
fig = plt.figure(figsize=(15,8))
for curve in contours[1.0]:
    plt.plot(curve[:,0],curve[:,1],label=level,linestyle='--',linewidth=4)
plt.plot(offCurve['msb'],offCurve['mlsp'],linewidth=4,color='black')
plt.xlabel(r'$m_{\tilde{b}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
for pt in srRecast[0::4]:
    plt.annotate(str(pt[2]),(pt[0],pt[1]),
                fontsize=10)
plt.show()

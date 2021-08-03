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
import itertools

pd.options.mode.chained_assignment = None #Disable copy warnings
#Define plotting style:
sns.set() #Set style
sns.set_style('ticks',{'font.family':'serif', 'font.serif':'Times New Roman'})
sns.set_context('paper', font_scale=1.8)
cm = plt.cm.get_cmap('RdYlBu')

# %% Load data
offCurve = np.genfromtxt('./ATLAS_data/HEPData-ins1827025-v2-Obs.Contour_1.csv',
                        delimiter=',', names=['msq','mlsp'])


# %% Get data from CheckMate results
resultFolder = '../validation_results/atlas_conf_2019_040'
slhaFolder = '../validation_slha/'
recastData = []
srRecast = []
for slhaFile in glob.glob(slhaFolder+'/T2_*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    #Get k-factor:
    pids = [1000001,2000001,1000002,2000002,1000003,2000003,1000004,2000004]
    pids += [-p for p in pids[:]]
    xsecNLO = 0.0
    xsecLO = 0.0
    for pA,pB in itertools.product(pids,pids):
        if pA > pB: continue
        key = (2212,2212,pA,pB)
        if not key in slhaData.xsections:
            continue
        xsecs = slhaData.xsections[key]
        xNLO = xsecs.get_xsecs(sqrts=13000., qcd_order=2)
        if xNLO:
            xsecNLO += xNLO[0].value
        xLO = xsecs.get_xsecs(sqrts=13000., qcd_order=0)
        if xLO:
            xsecLO += xLO[0].value

    kfactor = xsecNLO/xsecLO
    msq = slhaData.blocks['MASS'][1000001]
    mlsp = slhaData.blocks['MASS'][1000022]
    resDir = os.path.splitext(os.path.basename(slhaFile))[0]
    resFile = os.path.join(resultFolder,resDir,'evaluation',
                'total_results.txt')
    if not os.path.isfile(resFile):
        continue
    data = np.genfromtxt(resFile,names=True,
            usecols=(1,2,3,4,5,6,7,8,9,10,11,12),
            dtype=None,encoding=None)
    #Get r values from best SR
    ibest = np.argmax(data['rexp'])
    bestSR = data['sr'][ibest]
    robs = kfactor*data['robs'][ibest]
    robscons = kfactor*data['robscons'][ibest]

    recastData.append([msq,mlsp,robs,robscons])
    srRecast.append([msq,mlsp,bestSR])

recastData = np.array(recastData)


##  %% --------------------Best SR:
## Get exclusion contours (signal +- 20%)
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,3],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contours.items():
    if level != 1.0: continue
    for i,curve in enumerate(curves):
        if i == 0:
            p = plt.plot(curve[:,0],curve[:,1],label='Recast (r = %s)' %str(level),
                linestyle='--',linewidth=4)
            color = p[0].get_color()
        else:
            # continue
            plt.plot(curve[:,0],curve[:,1],
                linestyle='--',linewidth=4,color=color)
plt.plot(offCurve['msq'],offCurve['mlsp'],linewidth=4,
            color='black',label='ATLAS-CONF-2019-040')
plt.xlabel(r'$m_{\tilde{q}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
cb.set_label("r")
plt.legend()
plt.title(r'$\tilde{q} \tilde{q}, \tilde{q} \to q + \tilde{\chi}_1^0$ (Best SR Exclusion, $r_{cons}$)')
plt.savefig("atlas_conf_2019_040_T2.png")
plt.show()


## %% Get exclusion contours for compressed region
contoursComp = getContour(recastData[:,0],recastData[:,0]-recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,0]-recastData[:,1],
    c=recastData[:,3],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contoursComp.items():
    if level != 1.0: continue
    for i,curve in enumerate(curves):
        if i == 0:
            p = plt.plot(curve[:,0],curve[:,1],label='Recast (r = %s)' %str(level),
                linestyle='--',linewidth=4)
            color = p[0].get_color()
        else:
            # continue
            plt.plot(curve[:,0],curve[:,1],
                linestyle='--',linewidth=4,color=color)
plt.plot(offCurve['msq'],offCurve['msq']-offCurve['mlsp'],linewidth=4,
            color='black',label='ATLAS-CONF-2019-040')
plt.xlabel(r'$m_{\tilde{q}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{q}}-m_{\tilde{\chi}_1^0}$ (GeV)')
plt.ylim(0,50)
plt.xlim(300,1000)
cb.set_label("r")
plt.legend()
plt.title(r'$\tilde{q} \tilde{q}, \tilde{q} \to q + \tilde{\chi}_1^0$ (Best SR Exclusion, $r_{cons}$)')
plt.savefig("atlas_conf_2019_040_T2_delta.png")
plt.show()

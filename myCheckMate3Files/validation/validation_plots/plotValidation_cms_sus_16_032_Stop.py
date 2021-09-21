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
from scipy.interpolate import interp1d

pd.options.mode.chained_assignment = None #Disable copy warnings
#Define plotting style:
sns.set() #Set style
sns.set_style('ticks',{'font.family':'serif', 'font.serif':'Times New Roman'})
sns.set_context('paper', font_scale=1.8)
cm = plt.cm.get_cmap('RdYlBu')

# %% Load data
offCurve = np.genfromtxt('./CMS_data/CMS-SUS-16-032_Figure_006.csv',
                        delimiter=',', names=['mstop','mlsp'])

# %% Get data from CheckMate results
resultFolder = '../validation_results/cms_sus_16_032'
slhaFolder = '../validation_slha/'
recastData = []
srRecast = []
for slhaFile in glob.glob(slhaFolder+'/T2cc*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    mst = slhaData.blocks['MASS'][1000006]
    mlsp = slhaData.blocks['MASS'][1000022]
    resDir = os.path.splitext(os.path.basename(slhaFile))[0]
    resFile = os.path.join(resultFolder,resDir,'evaluation',
                'total_results.txt')
    if not os.path.isfile(resFile):
        continue
    data = np.genfromtxt(resFile,names=True,
            usecols=(1,2,3,4,5,6,7,8,9,10,11,12),
            dtype=None,encoding=None)
    #Split into single SRs and combined one:
    single_rows = []
    comb_rows = []
    for i,pt in enumerate(data):
        if not 'combined' in pt['sr'].lower():
            single_rows.append(i)
        else:
            comb_rows.append(i)
    dataComb = np.delete(data,single_rows,axis=0)
    data = np.delete(data,comb_rows,axis=0)

    #Get r values from best SR
    ibest = np.argmax(data['rexp'])
    bestSR = data['sr'][ibest]
    robs = data['robs'][ibest]
    robscons = data['robscons'][ibest]

    #Get r values from best combined SR
    ibestComb = np.argmax(dataComb['rexp'])
    bestComb = dataComb['sr'][ibestComb]
    robsComb = dataComb['robs'][ibestComb]
    robsconsComb = dataComb['robscons'][ibestComb]

    recastData.append([mst,mlsp,robs,robscons,robsComb,robsconsComb])
    srRecast.append([mst,mlsp,bestSR,bestComb])

recastData = np.array(recastData)

## %% --------------------Best SR:
## Get exclusion contours for signal +- 20%
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,3],levels=[0.8,1.0,1.2])

# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,3],cmap=cm,vmin=0.0,vmax=2.0,s=70)
for level,curves in contours.items():
    if level != 1.0: continue
    npts = [len(c) for c in curves]
    for curve in curves:
        if len(curve) != max(npts): continue
        plt.plot(curve[:,0],curve[:,1],label='Recast (r = %s)' %str(level),linestyle='--',linewidth=4)
plt.plot(offCurve['mstop'],offCurve['mlsp'],linewidth=4,
        color='black',label='CMS-SUS-16-032')
plt.xlabel(r'$m_{\tilde{\t}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
cb = plt.colorbar(ax)
# for pt in recastData:
    # if pt[2] < 1.2:
        # plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    # fontsize=10)
cb.set_label("r")
plt.title(r'$\tilde{t} \tilde{t}, \tilde{t} \to c + \tilde{\chi}_1^0$ (Best Exclusion, $r_{cons}$)')
plt.savefig("cms_sus_16_032_T2cc_best.png")
plt.show()


##  %% --------------------Combined SR:
## Get exclusion contours for signal +- 20%
contours = getContour(recastData[:,0],recastData[:,0]-recastData[:,1],recastData[:,5],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
# ax = plt.scatter(recastData[:,0],recastData[:,0]-recastData[:,1],
    # c=recastData[:,5],cmap=cm,vmin=0.0,vmax=2.0,s=70)
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

plt.plot(offCurve['mstop'],offCurve['mstop']-offCurve['mlsp'],linewidth=4,
        color='black',label='CMS-SUS-16-032')
plt.xlabel(r'$m_{\tilde{t}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{t}}-m_{\tilde{\chi}_1^0}$ (GeV)')
plt.ylim(0,70)
plt.xlim(200,600)
# cb = plt.colorbar(ax)
# for pt in recastData:
    # if pt[2] < 1.2:
        # plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    # fontsize=10)
# cb.set_label("r")
plt.legend(loc='upper left')
plt.title(r'$\tilde{t} \tilde{t}, \tilde{t} \to c + \tilde{\chi}_1^0$ (Compressed SRs)')
plt.savefig("cms_sus_16_032_T2cc.png")
plt.show()

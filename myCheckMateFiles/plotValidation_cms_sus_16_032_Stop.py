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
from getCombinedLimit import  getCombinedR, CovarianceHandler

pd.options.mode.chained_assignment = None #Disable copy warnings
#Define plotting style:
sns.set() #Set style
sns.set_style('ticks',{'font.family':'serif', 'font.serif':'Times New Roman'})
sns.set_context('paper', font_scale=1.8)
cm = plt.cm.get_cmap('RdYlBu')

# %% Load data
offCurve = np.genfromtxt('./CMS_data/CMS-SUS-16-032_Figure_006.csv',
                        delimiter=',', names=['mstop','mlsp'])

# %% Get covariance matrix for compressed signal regions:
covC = CovarianceHandler(filename = './CMS_data/CMS-SUS-16-032_Figure-aux_004.root',
                        histoname = 'Canvas_1/Cov', max_datasets=None,
                        aggregate = None , triangular=True)

SRsC = ['1b_ETmiss_250', '2b_ETmiss_500', '2b_ETmiss_500_HT_100', '1c_ETmiss_250',
 '1c_ETmiss_300', '1c_ETmiss_500', '1c_ETmiss_750', '1c_ETmiss_1000', '2c_ETmiss_250',
 '2c_ETmiss_250_HT_100', '2c_ETmiss_300', '1b_ETmiss_300', '2c_ETmiss_300_HT_100',
 '2c_ETmiss_500', '2c_ETmiss_500_HT_100', '2c_ETmiss_750', '2c_ETmiss_750_HT_100',
 'NSV_ETmiss_250', 'NSV_ETmiss_300', 'NSV_ETmiss_500', 'NSV_ETmiss_750', 'NSV_ETmiss_1000',
 '1b_ETmiss_500', '0b_ETmiss_300', '0b_ETmiss_500', '0b_ETmiss_750', '0b_ETmiss_1000',
 '0b_ETmiss_1250', '1b_ETmiss_750', '1b_ETmiss_1000', '2b_ETmiss_250',
 '2b_ETmiss_250_HT_100', '2b_ETmiss_300', '2b_ETmiss_300_HT_100']



# %% Get data from CheckMate results
resultFolder = './validation_results/cms_sus_16_032'
slhaFolder = './validation_slha/'
recastData = []
for slhaFile in glob.glob(slhaFolder+'/stop*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    mstop = slhaData.blocks['MASS'][1000006]
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
    rComb = getCombinedR(data,covC,SRsC,deltas_rel=0.2)
    s = data['s'][ibest]
    recastData.append([mstop,mlsp,rComb,robs])

recastData = np.array(recastData)

## %% Get exclusion contours for signal +- 20%
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])

# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,2],cmap=cm,vmin=0.0,vmax=2.0,s=70)
for level,curves in contours.items():
    npts = [len(c) for c in curves]
    for curve in curves:
        if len(curve) != max(npts): continue
        plt.plot(curve[:,0],curve[:,1],label=level,linestyle='--',linewidth=4)
plt.plot(offCurve['mstop'],offCurve['mlsp'],linewidth=4,
        color='black',label='CMS-SUS-16-032')
plt.xlabel(r'$m_{\tilde{\t}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
cb = plt.colorbar(ax)
for pt in recastData:
    if pt[2] < 1.2:
        plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    fontsize=10)
cb.set_label("r")
plt.savefig("cms_sus_16_032_Stop.png")
plt.show()

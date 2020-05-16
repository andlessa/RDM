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
offCurve = np.genfromtxt('./CMS_data/CMS-SUS-16-032_Figure_005.csv',
                        delimiter=',', names=['msb','mlsp'])

# %% Get covariance matrix for non-compressed signal regions:
covNC = CovarianceHandler(filename = './CMS_data/CMS-SUS-16-032_Figure-aux_003.root',
                        histoname = 'Canvas_1/Cov', max_datasets=None,
                        aggregate = None , triangular=True)
# %% Get covariance matrix for compressed signal regions:
covC = CovarianceHandler(filename = './CMS_data/CMS-SUS-16-032_Figure-aux_004.root',
                        histoname = 'Canvas_1/Cov', max_datasets=None,
                        aggregate = None , triangular=True)

# %%
# for pt in covNC.covariance:
#     if min(pt) < 0:
#         print("Negative values in non-compressed covariance:",pt)
#
# for pt in covC.covariance:
#     if min(pt) < 0:
#         print("Negative values in compressed covariance:",pt)



# %% Specify the ordering of the signal regions as used in the covariance matrix:
SRsNC = ['HT_200_MCT_150', 'HT_1000_MCT_150', 'HT_1000_MCT_250', 'HT_1000_MCT_350',
 'HT_1000_MCT_450', 'HT_1000_MCT_600', 'HT_1000_MCT_800', 'HT_200_MCT_250',
 'HT_200_MCT_350', 'HT_200_MCT_450', 'HT_500_MCT_150', 'HT_500_MCT_250', 'HT_500_MCT_350',
 'HT_500_MCT_450', 'HT_500_MCT_600']

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
srRecast = []
for slhaFile in glob.glob(slhaFolder+'/T2bb*.slha'):
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
    if bestSR in SRsNC:
        cov = covNC
        SRs = SRsNC
    elif bestSR in SRsC:
        cov = covC
        SRs = SRsC
    else:
        print('SR not found')
        continue
    robs = data['robs'][ibest]
    rComb = getCombinedR(data,cov,SRs,deltas_rel=0.2)
    recastData.append([msb,mlsp,rComb,robs])
    srRecast.append([msb,mlsp,bestSR])

recastData = np.array(recastData)

## %% Get exclusion contours for combined results (signal +- 20%)
contours = getContour(recastData[:,0],recastData[:,1],recastData[:,2],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,2],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contours.items():
    for i,curve in enumerate(curves):
        if i == 0:
            plt.plot(curve[:,0],curve[:,1],label='r = '+str(level),
                linestyle='--',linewidth=4)
        else:
            plt.plot(curve[:,0],curve[:,1],
                linestyle='--',linewidth=4)
plt.plot(offCurve['msb'],offCurve['mlsp'],linewidth=4,
            color='black',label='CMS-SUS-16-032')
plt.xlabel(r'$m_{\tilde{b}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
# for pt in recastData:
    # if pt[2] < 1.0:
        # plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    # fontsize=10)
cb.set_label("r")
plt.legend()
plt.title("Combined Exclusion")
plt.savefig("cms_sus_16_032_T2bb.png")
plt.show()


# %%
## %% Get exclusion contours for best signal region results (signal +- 20%)
contoursBest = getContour(recastData[:,0],recastData[:,1],recastData[:,3],levels=[0.8,1.0,1.2])


# %% plot result
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(recastData[:,0],recastData[:,1],
    c=recastData[:,3],cmap=cm,vmin=0.0,vmax=2.0,s=70)
cb = plt.colorbar(ax)
for level,curves in contoursBest.items():
    for curve in curves:
        plt.plot(curve[:,0],curve[:,1],label='r = '+str(level),
        linestyle='--',linewidth=4)
plt.plot(offCurve['msb'],offCurve['mlsp'],linewidth=4,
            color='black',label='CMS-SUS-16-032')
plt.xlabel(r'$m_{\tilde{b}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
for pt in recastData:
    if pt[2] < 1.0:
        plt.annotate('%1.1f'%pt[2],(pt[0],pt[1]),
                    fontsize=10)
cb.set_label("r")
plt.legend()
plt.title("Best SR Exclusion")
plt.show()

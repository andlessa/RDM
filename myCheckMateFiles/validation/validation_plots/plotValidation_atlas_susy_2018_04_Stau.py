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
effOfficialHigh = pd.read_csv('./ATLAS_data/HEPData-ins1765529-v1-Eff_Acc_table_SRhigh.csv',
                                comment='#', delimiter=',', names=['mstau','mlsp','effATLAS'],
                                skiprows=10)

effOfficialLow = pd.read_csv('./ATLAS_data/HEPData-ins1765529-v1-Eff_Acc_table_SRlow.csv',
                                comment='#', delimiter=',', names=['mstau','mlsp','effATLAS'],
                                skiprows=10)

effs = pd.concat([effOfficialLow,effOfficialHigh],
                        keys=['SR-lowMass','SR-highMass'])
effs['effATLAS'] = effs['effATLAS']/100.
effs['effATLAS'] = effs['effATLAS'].replace({0.0 : np.nan})
effs["effRecast"] = np.nan
effs["r-value"] = np.nan

# %% Get data from CheckMate results
resultFolder = '../validation_results/atlas_susy_2018_04'
slhaFolder = '../validation_slha/'
for slhaFile in glob.glob(slhaFolder+'/*.slha'):
    slhaData = pyslha.readSLHAFile(slhaFile)
    mstau = slhaData.blocks['MASS'][1000013]
    mlsp = slhaData.blocks['MASS'][1000022]
    resDir = os.path.splitext(os.path.basename(slhaFile))[0]
    resFile = os.path.join(resultFolder,resDir,'analysis',
                'StauStau_atlas_susy_2018_04_signal.dat')
    if not os.path.isfile(resFile):
        continue
    with open(resFile,'r') as f:
        acc = dict([[l.split()[0],eval(l.split()[3])] for l in f.readlines()[-2:]])
    for sr,eff in acc.items():
        effs.loc[(effs.index.isin([sr],level=0)) &
                 (effs['mstau'] == mstau) &
                (effs['mlsp'] == mlsp),'effRecast'] = eff
    resFile = os.path.join(resultFolder,resDir,
                'result.txt')
    with open(resFile,'r') as f:
        r = eval(f.read().split('Result for r:')[1].split('\n')[0])
        effs.loc[(effs['mstau'] == mstau) &
                (effs['mlsp'] == mlsp),'r-value'] = r

# %% Compute relative difference
effs['relDiff'] = (effs.effRecast - effs.effATLAS)/effs.effATLAS

# %% plot result High mass
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18,8))
ax = axes[0].scatter(effs.loc['SR-highMass']['mstau'],effs.loc['SR-highMass']['mlsp'],
    c=effs.loc['SR-highMass']['relDiff'],cmap=cm,vmin=-1.0,vmax=1.0,s=120)
for index,row in effs.loc['SR-highMass'].iterrows():
    if abs(row['relDiff']) > 0.3 and not np.isnan([row['relDiff']]):
        axes[0].annotate('%1.1f'%row['relDiff'],(row['mstau'],row['mlsp']+3.),
                    fontsize=11)
axes[0].set_xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
axes[0].set_ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
axes[0].set_title(r'$\tilde{\tau} \tilde{\tau}, \tilde{\tau} \to \tau + \tilde{\chi}_1^0$ (SR-HighMass Efficiencies)')

ax = axes[1].scatter(effs.loc['SR-lowMass']['mstau'],effs.loc['SR-lowMass']['mlsp'],
    c=effs.loc['SR-lowMass']['relDiff'],cmap=cm,vmin=-1.0,vmax=1.0,s=120)
for index,row in effs.loc['SR-lowMass'].iterrows():
    if abs(row['relDiff']) > 0.3 and not np.isnan([row['relDiff']]):
        axes[1].annotate('%1.1f'%row['relDiff'],(row['mstau'],row['mlsp']+3.),
                    fontsize=11)
axes[1].set_xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
# axes[1].set_ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
axes[1].set_title(r'$\tilde{\tau} \tilde{\tau}, \tilde{\tau} \to \tau + \tilde{\chi}_1^0$ (SR-lowMass Efficiencies)')

cb = fig.colorbar(ax, ax=axes.ravel().tolist())
cb.set_label(r'$\Delta\epsilon/\epsilon_{ATLAS}$')
plt.savefig("atlas_susy_2018_04_StauEffs.png")


## %% Get exclusion contours for signal +- 20%
contours = getContour(effs.loc['SR-lowMass']['mstau'],effs.loc['SR-lowMass']['mlsp'],effs.loc['SR-lowMass']['r-value'],levels=[1.0])

# %% Load data
offCurveComb = np.genfromtxt('./ATLAS_data/HEPData-ins1765529-v1-Exclusion_contour_1_Obs.csv',
                        delimiter=',', names=True, skip_header=10)
offCurveLow = np.genfromtxt('./ATLAS_data/HEPData-ins1765529-v1-Exclusion_contour_aux_1_Obs.csv',
                        delimiter=',', names=True, skip_header=10)
offCurveHigh = np.genfromtxt('./ATLAS_data/HEPData-ins1765529-v1-Exclusion_contour_aux_2_Obs.csv',
                        delimiter=',', names=True, skip_header=10)

# %% Plot exclusion curve
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(effs.loc['SR-lowMass']['mstau'],effs.loc['SR-lowMass']['mlsp'],
    c=effs.loc['SR-lowMass']['r-value'],cmap=cm,vmin=0.0,vmax=2.0,s=70)
for level,curves in contours.items():
    if level != 1.0: continue
    npts = [len(c) for c in curves]
    for curve in curves:
        if len(curve) != max(npts): continue
        plt.plot(curve[:,0],curve[:,1],label='Recast (r = %s)' %str(level),linestyle='--',linewidth=4)

plt.plot(offCurveComb['MSTAU_GeV'],offCurveComb['MNEUTRALINO1_GeV'],linewidth=4,
        color='black',label='ATLAS-SUSY-2018-04 (Combined)')
plt.plot(offCurveLow['MSTAU_GeV'],offCurveLow['MNEUTRALINO1_GeV'],linewidth=4,
        color='black',label='ATLAS-SUSY-2018-04 (Low Mass)', linestyle='-.')
plt.plot(offCurveHigh['MSTAU_GeV'],offCurveHigh['MNEUTRALINO1_GeV'],linewidth=4,
        color='black',label='ATLAS-SUSY-2018-04 (High Mass)', linestyle='--')


plt.xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
cb = plt.colorbar(ax)
cb.set_label(r'$r$')
plt.legend()
plt.title(r'$\tilde{\tau} \tilde{\tau}, \tilde{\tau} \to \tau + \tilde{\chi}_1^0$ (Best SR)')
plt.savefig("atlas_susy_2018_04_Stau.png")
plt.show()

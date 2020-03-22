#!/usr/bin/env python3

"""Plot validation results."""

# %% Imports
import os,glob
import pyslha
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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
resultFolder = './validation_results'
slhaFolder = './validation_slha/'
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
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(effs.loc['SR-highMass']['mstau'],effs.loc['SR-highMass']['mlsp'],
    c=effs.loc['SR-highMass']['relDiff'],cmap=cm,vmin=-1.0,vmax=1.0,s=70)
plt.xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
plt.title('SR-HighMass')
cb = plt.colorbar(ax)
for index,row in effs.loc['SR-highMass'].iterrows():
    if abs(row['relDiff']) > 0.15 and not np.isnan([row['relDiff']]):
        plt.annotate('%1.1f'%row['relDiff'],(row['mstau'],row['mlsp']),
                    fontsize=10)
cb.set_label(r'$\Delta\epsilon/\epsilon_{ATLAS}$')
plt.show()

# %% plot result Low mass
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(effs.loc['SR-lowMass']['mstau'],effs.loc['SR-lowMass']['mlsp'],
    c=effs.loc['SR-lowMass']['relDiff'],cmap=cm,vmin=-1.0,vmax=1.0,s=70)
plt.xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
plt.title('SR-LowMass')
cb = plt.colorbar(ax)
cb.set_label(r'$\Delta\epsilon/\epsilon_{ATLAS}$')
for index,row in effs.loc['SR-lowMass'].iterrows():
    if abs(row['relDiff']) > 0.15 and not np.isnan([row['relDiff']]):
        plt.annotate('%1.1f'%row['relDiff'],(row['mstau'],row['mlsp']),
                    fontsize=10)
plt.show()

# %% Plot exclusion curve
fig = plt.figure(figsize=(12,8))
ax = plt.scatter(effs.loc['SR-lowMass']['mstau'],effs.loc['SR-lowMass']['mlsp'],
    c=effs.loc['SR-lowMass']['r-value'],cmap=cm,vmin=0.0,vmax=2.0,s=70)
plt.xlabel(r'$m_{\tilde{\tau}}$ (GeV)')
plt.ylabel(r'$m_{\tilde{\chi}_1^0}$ (GeV)')
cb = plt.colorbar(ax)
cb.set_label(r'$r$')
plt.show()

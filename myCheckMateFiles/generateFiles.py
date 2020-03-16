#!/usr/bin/env python3

"""Generate SLHA files from a template."""

import os
import numpy as np

template = 'param_card_DS_120_1.slha'

effOfficialHigh = np.genfromtxt('./HEPData-ins1765529-v1-Eff_Acc_table_SRhigh.csv',
                        comments='#', delimiter=',', names=True, skip_header=9)
effOfficialLow = np.genfromtxt('./HEPData-ins1765529-v1-Eff_Acc_table_SRlow.csv',
                        comments='#', delimiter=',', names=True, skip_header=9)

massPairs = list(zip(effOfficialHigh['MSTAU_GeV'],
                      effOfficialHigh['MNEUT_GeV']))
massPairs += list(zip(effOfficialLow['MSTAU_GeV'],
                      effOfficialLow['MNEUT_GeV']))

massPairs = list(set(massPairs))

ftemplate = open(template, 'r')
data = ftemplate.readlines()
ftemplate.close()
slhaFolder = './validation_slha/'
for mstau,mlsp in massPairs:
    newfile = os.path.join(slhaFolder,'param_card_DS_%i_%i.slha' %(int(mstau),int(mlsp)))
    with open(newfile,'w') as fnew:
        data[58] = '   1000011    %s  # \n' %mstau
        data[60] = '   1000013    %s  # \n' %mstau
        data[61] = '   1000015    %s  # \n' %mstau
        data[64] = '   1000022    %s  # \n' %mlsp
        data[74] = '   2000011    %s  # \n' %mstau
        data[75] = '   2000013    %s  # \n' %mstau
        data[76] = '   2000015    %s  # \n' %mstau
        for l in data:
            fnew.write(l)

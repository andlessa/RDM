#!/usr/bin/env python3

"""Generate SLHA files from a template."""

import os
import numpy as np


T2bbf = open('/home/lessa/smodels-database/13TeV/CMS/CMS-SUS-16-032/data/T2bb.txt','r')
T2bb = eval(T2bbf.read().split("upperLimits:")[-1],{'GeV':1.0,'fb':1.0,'pb' : 1e3})
T2bbf.close()
masses = np.array([pt[0][0] for pt in T2bb])

template = 'sbottom_900.slha'
ftemplate = open(template, 'r')
data = ftemplate.readlines()
ftemplate.close()
slhaFolder = './validation_slha/'
for msb,mlsp in masses:
    newfile = os.path.join(slhaFolder,'sbottom_%i_%i.slha' %(int(msb),int(mlsp)))
    with open(newfile,'w') as fnew:
        data[53] = '      1000005 %1.6e # ~b_1\n' %msb
        data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
        for l in data:
            fnew.write(l)


T2ccf = open('/home/lessa/smodels-database/13TeV/CMS/CMS-SUS-16-032/data/T2cc.txt','r')
T2cc = eval(T2ccf.read().split("upperLimits:")[-1],{'GeV':1.0,'fb':1.0,'pb' : 1e3})
T2ccf.close()
masses = np.array([pt[0][0] for pt in T2cc])

template = 'stop_400.slha'
ftemplate = open(template, 'r')
data = ftemplate.readlines()
ftemplate.close()
slhaFolder = './validation_slha/'
for mst,mlsp in masses:
    newfile = os.path.join(slhaFolder,'stop_%i_%i.slha' %(int(mst),int(mlsp)))
    with open(newfile,'w') as fnew:
        data[55] = '      1000006 %1.6e # ~t_1\n' %mst
        data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
        for l in data:
            fnew.write(l)



# template = 'param_card_DS_120_1.slha'
#
# effOfficialHigh = np.genfromtxt('./HEPData-ins1765529-v1-Eff_Acc_table_SRhigh.csv',
#                         comments='#', delimiter=',', names=True, skip_header=9)
# effOfficialLow = np.genfromtxt('./HEPData-ins1765529-v1-Eff_Acc_table_SRlow.csv',
#                         comments='#', delimiter=',', names=True, skip_header=9)
#
# massPairs = list(zip(effOfficialHigh['MSTAU_GeV'],
#                       effOfficialHigh['MNEUT_GeV']))
# massPairs += list(zip(effOfficialLow['MSTAU_GeV'],
#                       effOfficialLow['MNEUT_GeV']))
#
# massPairs = list(set(massPairs))
#
# ftemplate = open(template, 'r')
# data = ftemplate.readlines()
# ftemplate.close()
# slhaFolder = './validation_slha/'
# for mstau,mlsp in massPairs:
#     newfile = os.path.join(slhaFolder,'param_card_DS_%i_%i.slha' %(int(mstau),int(mlsp)))
#     with open(newfile,'w') as fnew:
#         data[58] = '   1000011    %s  # \n' %mstau
#         data[60] = '   1000013    %s  # \n' %mstau
#         data[61] = '   1000015    %s  # \n' %mstau
#         data[64] = '   1000022    %s  # \n' %mlsp
#         data[74] = '   2000011    %s  # \n' %mstau
#         data[75] = '   2000013    %s  # \n' %mstau
#         data[76] = '   2000015    %s  # \n' %mstau
#         for l in data:
#             fnew.write(l)

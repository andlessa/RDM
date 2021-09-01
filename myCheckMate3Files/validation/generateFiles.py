#!/usr/bin/env python3

"""Generate SLHA files from a template."""

import os
import numpy as np
import tarfile
import itertools


txname = "T6bbWWoff"

if txname == "T2bb_comp":
    sb_masses = np.linspace(300.,600.,31)
    deltam = np.linspace(5.,40.0,8)
    template = 'T2bb_900.slha'
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for msb in sb_masses:
        for dm in deltam:
            mlsp = max(10,msb - dm)
            newfile = os.path.join(slhaFolder,'T2bbcomp_%i_%i.slha' %(int(msb),int(mlsp)))
            with open(newfile,'w') as fnew:
                data[53] = '      1000005 %1.6e # ~b_1\n' %msb
                data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
                for l in data:
                    fnew.write(l)


if "T2bb" in txname:
    T2bbf = open('/home/lessa/smodels-database/13TeV/CMS/CMS-SUS-16-032/data/T2bb.txt','r')
    T2bb = eval(T2bbf.read().split("upperLimits:")[-1],{'GeV':1.0,'fb':1.0,'pb' : 1e3})
    T2bbf.close()
    masses = np.array([pt[0][0] for pt in T2bb])

    template = 'T2bb_900.slha'
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for msb,mlsp in masses:
        newfile = os.path.join(slhaFolder,'T2bb_%i_%i.slha' %(int(msb),int(mlsp)))
        with open(newfile,'w') as fnew:
            data[53] = '      1000005 %1.6e # ~b_1\n' %msb
            data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
            for l in data:
                fnew.write(l)

if txname == "T2cc":
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
        newfile = os.path.join(slhaFolder,'T2cc_%i_%i.slha' %(int(mst),int(mlsp)))
        with open(newfile,'w') as fnew:
            data[55] = '      1000006 %1.6e # ~t_1\n' %mst
            data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
            for l in data:
                fnew.write(l)

if txname == "T2tt":
    tf = tarfile.open('/home/lessa/smodels-utils/slha/T2tt.tar.gz','r:gz')
    fname = tf.next()
    masses = []
    while (fname):
        mstop,mlsp = fname.name.split('_')[1:3]
        masses.append([eval(mstop),eval(mlsp)])
        fname = tf.next()

    masses = np.array(masses)

    template = 'T2tt.slha'
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for mst,mlsp in masses:
        newfile = os.path.join(slhaFolder,'T2tt_%i_%i.slha' %(int(mst),int(mlsp)))
        with open(newfile,'w') as fnew:
            data[55] = '      1000006 %1.6e # ~t_1\n' %mst
            data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
            for l in data:
                fnew.write(l)


if txname == "TStauStau":
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

if txname == "T1":
    template = 'T1.slha'
    mlspV = np.linspace(0,1500,31)
    mgluinoV = np.linspace(800,2400,33)
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for mg,mlsp in itertools.product(mgluinoV,mlspV):
        if mlsp > mg: continue
        if mlsp == 0.0: mlsp = 10.0
        newfile = os.path.join(slhaFolder,'T1_%i_%i.slha' %(int(mg),int(mlsp)))
        with open(newfile,'w') as fnew:
            data[66] = '      1000021 %1.6e # ~g\n' %mg
            data[67] = '      1000022 %1.6e # ~chi_10\n' %mlsp
            for l in data:
                fnew.write(l)

if txname == "T2":
    template = 'T2.slha'
    mlspV = np.linspace(0,1000,31)
    msqV = np.linspace(400,2000,33)
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for msq,mlsp in itertools.product(msqV,mlspV):
        if mlsp > msq: continue
        if mlsp == 0.0: mlsp = 10.0
        newfile = os.path.join(slhaFolder,'T2_%i_%i.slha' %(int(msq),int(mlsp)))
        newdata = data[:]
        with open(newfile,'w') as fnew:
            for i in range(68,76):
                newdata[i] = newdata[i].replace('MSQUARK','%1.6e' %msq)
            newdata[90] = newdata[90].replace('MLSP','%1.6e' %mlsp)
            for l in newdata:
                fnew.write(l)


if txname == "T6bbWWoff":
    template = 'T6bbWWoff.template'
    deltaMV = np.linspace(10,100,20)
    mstV = np.linspace(300,500,10)
    ftemplate = open(template, 'r')
    data = ftemplate.readlines()
    ftemplate.close()
    slhaFolder = './validation_slha/'
    for mst,deltaM in itertools.product(mstV,deltaMV):
        mlsp = mst-deltaM
        mc1 = (mst+mlsp)/2.0
        if mlsp == 0.0: mlsp = 10.0
        if mlsp > mst: continue
        if mc1 > mst: continue
        if mc1 < mlsp: continue
        newfile = os.path.join(slhaFolder,'T6bbWWoff_%i_%i.slha' %(int(mst),int(mlsp)))
        newdata = data[:]
        with open(newfile,'w') as fnew:
            newdata[29] = newdata[29].replace('M0','%1.6e' %mst)
            newdata[41] = newdata[41].replace('M2','%1.6e' %mlsp)
            newdata[45] = newdata[45].replace('M1','%1.6e' %mc1)
            for l in newdata:
                fnew.write(l)

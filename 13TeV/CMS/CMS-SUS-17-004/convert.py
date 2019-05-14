#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description =  
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '-utilsPath', 
help = 'path to the package smodels_utils',\
type = types.StringType)
argparser.add_argument ('-smodelsPath', '-smodelsPath', 
help = 'path to the package smodels_utils',\
type = types.StringType)
args = argparser.parse_args()

if args.utilsPath:
    utilsPath = args.utilsPath
else:
    databaseRoot = '../../../'
    sys.path.append(os.path.abspath(databaseRoot))
    from utilsPath import utilsPath
    utilsPath = databaseRoot + utilsPath
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-17-004')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-004/index.html'
info.sqrts = 13
info.lumi = 35.9
info.prettyName = 'Chargino-neutralino production with WZ topology'
info.private = False
info.arxiv = 'https://arxiv.org/abs/1801.03957'
info.contact = 'cms-phys-conveners-sus@cern.ch'
info.publication = 'JHEP 1803 (2018) 160, http://dx.doi:10.1007/JHEP03(2018)160'
info.comment = 'Fig. 7 with chi02 -> chi10Z on one branch and chi+/-1 -> chi01 Wpm on the other branch, chargino mass are fixed equal to second lightest neutralino mass.'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++txName block +++++++++++++++++

T2tt=dataset.addTxName('TchiWZ')
T2tt.checked=''
T2tt.constraint="[[['W']],[['Z']]]"
T2tt.condition=None
T2tt.conditionDescription = None
#T2tt.massConstraint=[['dm > 169.']]*2  #Use only on-shell region to avoid interpolating in the excluded band
T2tt.source="CMS"



#++++++next mass plane block+++++++++

T2tt_1 = T2tt.addMassPlane(2*[[x,y]])
T2tt_1.figure='Fig. 7'
T2tt_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-004/CMS-SUS-17-004_Figure_007.png'
T2tt_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-049/CMS-SUS-17-004_Figure_007.root'
T2tt_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-049/CMS-SUS-17-004_Figure_007.root'
T2tt_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-049/CMS-SUS-17-004_Figure_007.root'
T2tt_1.setSources(dataLabels=['upperLimits'],
                    dataFiles=['orig/CMS-SUS-17-004_Figure_007.root'],
                    dataFormats=['root'],objectNames=['TChiWZ;1'],units=[None,'pb'])

#+++++txName block +++++++++++++++++
 

databaseCreator.create()




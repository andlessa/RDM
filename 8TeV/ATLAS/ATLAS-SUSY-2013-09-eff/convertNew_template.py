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
argparser.add_argument ('-utilsPath', '--utilsPath', 
help = 'path to the package smodels_utils',\
type = types.StringType)
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
info = MetaInfoInput('ATLAS-SUSY-2013-09')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/'
info.sqrts = 8
info.lumi = '20.3'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1404.2500'
info.contact = "ATLAS collaboration"
info.publication = 'http://link.springer.com/article/10.1007/JHEP06(2014)035'
info.supersedes = 'ATLAS-CONF-2013-007; ATLAS-CONF-2012-151'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription = "None"
T1tttt.condition = "None"
T1tttt.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane([[x,y]]*2)
T1tttt_1.figure ="No Figure"
T1tttt_1.figureUrl ="No Figure"
T1tttt_1.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt_1.addSource('efficiencyMap', "orig/EffMap_T1tttt_$datasetStr$.txt", "txt")
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
END_BLOCK_TO_FILL

databaseCreator.create()

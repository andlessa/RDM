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
info = MetaInfoInput('ATLAS-SUSY-2013-21')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-21/'
info.sqrts = 8
info.lumi = 20.3
info.prettyName = 'stop  to charm'
info.private = False
info.arxiv = 'http://arxiv.org/pdf/1407.0608v2.pdf'
info.publication = 'http://journals.aps.org/prd/abstract/10.1103/PhysRevD.90.052008'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2bbWW =  dataset.addTxName('T2bbWW')
T2bbWW.constraint = "[[['b','W']],[['b','W']]]"
T2bbWW.conditionDescription = None
T2bbWW.condition = None
T2bbWW.massConstraint = None
T2bbWW.source = 'ATLAS'
#+++++++ next txName block ++++++++++++++
T2bbWWoff = dataset.addTxName('T2bbWWoff')
T2bbWWoff.constraint = "[[['b','L','nu']],[['b','L','nu']]]+[[['b','jet','jet']],[['b','jet','jet']]]+[[['b','jet','jet']],[['b','L','nu']]]"
T2bbWWoff.conditionDescription = None
T2bbWWoff.condition = None 
T2bbWWoff.massConstraint = [['dm <= 76.']]*2
T2bbWWoff.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T2bbWW_1 = T2bbWW.addMassPlane([[x,y]]*2)
T2bbWW_1.addSource('obsExclusion','orig/T2bbWWoff_Obs.txt','txt')
T2bbWW_1.addSource('obsExclusionM1','orig/T2bbWWoff_ObsMinus.txt', 'txt')
T2bbWW_1.addSource('obsExclusionP1','orig/T2bbWWoff_ObsPlus.txt',  'txt')
T2bbWW_1.addSource('efficiencyMap','orig/T2bbWWoff_$datasetStr$.dat', 'txt')
T2bbWW_1.dataUrl = None
T2bbWWoff.addMassPlane(T2bbWW_1)
#+++++++ next txName block ++++++++++++++
T2cc = dataset.addTxName('T2cc')
T2cc.constraint = "[[['c']],[['c']]]"
T2cc.conditionDescription = None
T2cc.condition = None
T2cc.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T2cc_1 = T2cc.addMassPlane([[x,y]]*2)
T2cc_1.addSource('obsExclusion','orig/T2cc_Obs.txt', 'txt')
T2cc_1.addSource('obsExclusionM1','orig/T2cc_ObsMinus.txt', 'txt')
T2cc_1.addSource('obsExclusionP1','orig/T2cc_ObsPlus.txt',  'txt')
T2cc_1.addSource('efficiencyMap','orig/T2cc_$datasetStr$.dat', 'txt')
T2cc_1.dataUrl = None
#+++++++ next txName block ++++++++++++++
T2bb = dataset.addTxName('T2bb')
T2bb.constraint ="[[['b']],[['b']]]"
T2bb.conditionDescription = None
T2bb.condition = None
T2bb.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane([[x,y]]*2)
T2bb_1.addSource('obsExclusion','orig/T2bb_Obs.txt', 'txt')
T2bb_1.addSource('obsExclusionM1','orig/T2bb_ObsMinus.txt', 'txt')
T2bb_1.addSource('obsExclusionP1','orig/T2bb_ObsPlus.txt', 'txt')
T2bb_1.addSource('efficiencyMap','orig/T2bb_$datasetStr$.dat', 'txt')
T2bb_1.dataUrl = None

END_BLOCK_TO_FILL

databaseCreator.create()

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
info = MetaInfoInput('CMS-SUS-14-021')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
info.sqrts = 8
info.lumi = 19.7
info.prettyName = 'stop 4body decay'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1512.08002'
info.comment ='stop 4 body decay'


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2bbWW =  dataset.addTxName('T2bbWW')
T2bbWW.constraint = "[[['b','W']],[['b','W']]]"
T2bbWW.conditionDescription = None
T2bbWW.condition =None
T2bbWW.massConstraint = None
T2bbWW.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T2bbWWoff = dataset.addTxName('T2bbWWoff')
T2bbWWoff.constraint = "6.94*[[['b','mu','nu']],[['b','jet','jet']]]"
T2bbWWoff.conditionDescription =None
T2bbWWoff.condition =None
T2bbWWoff.massConstraint = [['dm <= 76.']]*2
T2bbWWoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T2bbWW_1 = T2bbWW.addMassPlane([[x,y]]*2)
#---- new efficiency map -----
#----figure----
T2bbWW_1.figure = $$
T2bbWW_1.figureUrl = $$
T2bbWW_1.addSource('obsExclusion','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObserved')
T2bbWW_1.addSource('obsExclusionM1','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObservedDown')
T2bbWW_1.addSource('obsExclusionP1','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObservedUp')
T2bbWW_1.addSource('expExclusion','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpected')
T2bbWW_1.addSource('expExclusionM1','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpectedDown')
T2bbWW_1.addSource('expExclusionP1','orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpectedUp')
T2bbWW_1.addSource('efficiencyMap','orig/efficienciesSRSL.root', 'root', objectName = 'eff$datasetStr$',scale = 0.01)
T2bbWW_1.efficiencyMap.dataUrl = $$
T2bbWWoff.addMassPlane(T2bbWW_1)

END_BLOCK_TO_FILL

databaseCreator.create()

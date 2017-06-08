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
info = MetaInfoInput('CMS-SUS-13-013')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13013'
info.sqrts = 8
info.lumi = 19.5
info.private = False
info.arxiv = 'http://arxiv.org/pdf/1311.6736v2.pdf'
info.publication ='http://link.springer.com/article/10.1007%2FJHEP01%282014%29163'
info.supersedes ='CMS-SUS-12-017'


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.massConstraint = None
T1tttt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.constraint = "[[['b','b','W','W']],[['b','b','W','W']]]"
T1ttttoff.conditionDescription ="None"
T1ttttoff.condition = "None"
T1ttttoff.massConstraint = [['dm <= 338.']]*2
T1ttttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane([[x,y]]*2)
T1tttt_1.figure ='Figure 5'
T1tttt_1.figureUrl = $$
T1tttt_1.addSource('obsExclusion','orig/ModelA1.root', 'root', objectName = 'graph_smoothed_Obs')
T1tttt_1.addSource('obsExclusionM1','orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ObsM')
T1tttt_1.addSource('obsExclusionP1','orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ObsP')
T1tttt_1.addSource('expExclusion', 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_Exp')
T1tttt_1.addSource('expExclusionM1', 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ExpM')
T1tttt_1.addSource('expExclusionP1', 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ExpP')
#----limit source----
T1tttt_1.addSource('efficiencyMap', 'orig/$datasetStr$.txt', 'txt')
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelA1.root'
T1ttttoff.addMassPlane(T1tttt_1)

END_BLOCK_TO_FILL

databaseCreator.create()

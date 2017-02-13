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
info = MetaInfoInput('ATLAS-SUSY-2013-16')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-16/'
info.sqrts = '8'
info.lumi = '20.1'
info.prettyName = ''
info.private = False
info.arxiv = 'http://arxiv.org/abs/1406.1122'
info.contact = ''
info.publication = 'http://link.springer.com/article/10.1007%2FJHEP09%282014%29015'
info.comment ='EM given for All SRs for one topo, only for 3 for the other. Only these 3 are implemented.'
info.supersedes ='ATLAS-CONF-2013-024'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2tt = dataset.addTxName('T2tt')
T2tt.constraint = "[[['t']],[['t']]]"
T2tt.conditionDescription ="None"
T2tt.condition ="None"
T2tt.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane([[x,y]]*2)
T2tt_1.addSource('obsExclusion', "./orig/T2tt_Exclusion.txt", "txt")
T2tt_1.addSource('efficiencyMap','orig/EffMap_T2tt_$datasetStr$.txt', 'txt')
T2tt_1.dataUrl = $$
#+++++++ next txName block ++++++++++++++
T6bbWW = dataset.addTxName('T6bbWW')
T6bbWW.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.conditionDescription ="None"
T6bbWW.condition ="None"
T6bbWW.massConstraint = None
T6bbWW.source = 'ATLAS'
#+++++++ next txName block ++++++++++++++
T6bbWWoff = dataset.addTxName('T6bbWWoff')
T6bbWWoff.condition ="None"
T6bbWWoff.constraint ="[[['b'],['jet','jet']],[['b'],['jet','jet']]]"
T6bbWWoff.conditionDescription ="None"
T6bbWWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T6bbWWoff.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T6bbWW_1 = T6bbWW.addMassPlane([[x,2*y,y]]*2)
T6bbWW_1.addSource('obsExclusion', "./orig/T6bbWW_Exclusion.txt" ,"txt")
T6bbWW_1.addSource('efficiencyMap', "./orig/EffMap_T6bbWW_$datasetStr$.txt", "txt")
T6bbWW_1.dataUrl = $$
T6bbWWoff.addMassPlane(T6bbWW_1)


END_BLOCK_TO_FILL

databaseCreator.create()

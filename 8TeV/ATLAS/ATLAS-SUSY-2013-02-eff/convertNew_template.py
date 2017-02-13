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
info = MetaInfoInput('ATLAS-SUSY-2013-02')
info.comment = 'T5WWLSP060 and T6WWLSP060 originally have xvalue on y-axes, changed by us to M2'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP09%282014%29176'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/'
info.arxiv = 'http://arxiv.org/abs/1405.7875'
info.prettyName =  "jets and met"
info.supersedes = 'ATLAS-CONF-2013-047'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2 = dataset.addTxName('T2')
T2.constraint ="[[['jet']],[['jet']]]"
T2.conditionDescription ="None"
T2.condition ="None"
T2.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T2 = T2.addMassPlane([[x,y]]*2)
T2.figure = $$
T2.addSource('efficiencyMap',"orig/T2_$datasetStr$.dat","txt")
T2.addSource('obsExclusion',"orig/exclusion_T2.txt", "txt")
T2.figureUrl = $$
T2.dataUrl = $$
#+++++++ next txName block ++++++++++++++
T1 = dataset.addTxName('T1')
T1.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.conditionDescription ="None"
T1.condition ="None"
T1.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T1 = T1.addMassPlane([[x,y]]*2)
T1.figure = $$
T1.addSource('efficiencyMap',"orig/T1_$datasetStr$.dat","txt")
T1.addSource('obsExclusion',"orig/exclusion_T1.txt", "txt")
T1.figureUrl = $$
T1.dataUrl = $$
END_BLOCK_TO_FILL

databaseCreator.create()

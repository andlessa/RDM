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
info = MetaInfoInput('ATLAS-SUSY-2014-03')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2014-03/'
info.sqrts = 8
info.lumi = 20.3 
info.arxiv = 'http://arxiv.org/abs/1501.01325'
info.publication = 'http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.161801'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
TScharm = dataset.addTxName('TScharm')
TScharm.checked = 'NO'
TScharm.constraint ="[[['c']],[['c']]]"
TScharm.conditionDescription = "None"
TScharm.condition ='None'
TScharm.source ='ATLAS'
#+++++++ next mass plane block ++++++++++++++
TScharm_1 = TScharm.addMassPlane([[x,y]]*2)
TScharm_1.figure = $$
TScharm_1.figureUrl = $$
TScharm_1.addSource('obsExclusion', 'orig/TScharm_Exclusion.txt', 'txt')
TScharm_1.addSource('efficiencyMap', 'orig/$datasetStr$.dat', 'txt')
TScharm_1.dataUrl = $$


END_BLOCK_TO_FILL

databaseCreator.create()

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
info = MetaInfoInput('ATLAS-SUSY-2013-18')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/'
info.sqrts = '8.0*TeV'
info.lumi = 20.1
info.prettyName ='Three b'
info.private =False
info.arxiv = 'http://arxiv.org/abs/1407.0600'
info.contact ='ATLAS'
info.publication ='http://link.springer.com/article/10.1007/JHEP10(2014)024'
info.comment ='Using combined Exclusion line. Superseeded CONF-2013-061(from FastLim) has more topologies'
info.supersedes ='ATLAS-CONF-2013-061'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
T1bbbb = dataset.addTxName('T1bbbb')
T1bbbb.constraint = "[[['b','b']],[['b','b']]]"
T1bbbb.conditionDescription ="None"
T1bbbb.condition ="None"
T1bbbb.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane([[x,y]]*2)
T1bbbb_1.figure = $$
T1bbbb_1.figureUrl = $$
T1bbbb_1.addSource('obsExclusion', 'orig/T1bbbb_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt')
T1bbbb_1.addSource('efficiencyMap','orig/EffMap_T1bbbb_$datasetStr$.txt', 'txt')
T1bbbb_1.dataUrl = $$
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane([[x,y]]*2)
T1tttt_1.figure = $$
T1tttt_1.figureUrl = $$
T1tttt_1.addSource('obsExclusion', 'orig/T1tttt_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt')
T1tttt_1.addSource('efficiencyMap','orig/EffMap_T1tttt_$datasetStr$.txt', 'txt')
T1tttt_1.dataUrl = $$


END_BLOCK_TO_FILL

databaseCreator.create()

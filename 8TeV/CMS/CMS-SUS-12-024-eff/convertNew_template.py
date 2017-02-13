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
info = MetaInfoInput('CMS-SUS-12-024')
info.sqrts = '8.0'
info.private = False
info.lumi = '19.4'
info.publication = 'http://www.sciencedirect.com/science/article/pii/S0370269313005339'
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12024'
info.arxiv = 'http://arxiv.org/abs/1305.2390'
info.contact = 'Keith Ulmer <keith.ulmer@cern.ch>, Josh Thompson <joshua.thompson@cern.ch>, Alessandro Gaz <alessandro.gaz@cern.ch>'
info.prettyName = '\slash{E}_{T}+b'


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T1bbbb = dataset.addTxName('T1bbbb')
T1bbbb.checked ="AL"
T1bbbb.constraint ="[[['b','b']],[['b','b']]]"
T1bbbb.conditionDescription ="None"
T1bbbb.condition ="None"
T1bbbb.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1bbbb = T1bbbb.addMassPlane([[x,y]]*2)
T1bbbb.addSource('efficiencyMap', "orig/efficiency_T1bbbb_multi.root", "root", objectName = "heff_$datasetStr$")
T1bbbb.addSource('obsExclusion',"orig/graph_smoothed_Obs_T1bbbb.root", "root", objectName = "graph_smoothed_Obs_T1bbbb")
T1bbbb.figure = "Fig 7 (left)"
T1bbbb.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1bbbb_exclusions_corrected.pdf"
T1bbbb.efficiencyMap.dataUrl = $$
# +++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="AL"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.massConstraint = None
T1tttt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.checked ="AL"
T1ttttoff.constraint ="[[['b','b','W','W']],[['b','b','W','W']]]"
T1ttttoff.condition ="None"
T1ttttoff.conditionDescription ="None"
T1ttttoff.massConstraint = [['dm <= 338.']]*2
T1ttttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"orig/efficiency_T1tttt_multi.root", "root", objectName = "heff_$datasetStr$")
T1tttt.addSource('obsExclusionM1',"orig/graph_smoothed_Obs_T1tttt.root", "root", objectName = "graph_smoothed_Obs_T1tttt")
T1tttt.figure = "Fig 7 (right)"
T1tttt.figureUrl =  "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1tttt_exclusions_corrected.pdf"
T1tttt.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024"
T1ttttoff.addMassPlane(T1tttt)
END_BLOCK_TO_FILL

databaseCreator.create()

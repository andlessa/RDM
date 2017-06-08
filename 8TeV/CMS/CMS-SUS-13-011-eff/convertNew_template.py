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
info = MetaInfoInput('CMS-SUS-13-011')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
info.sqrts = 8
info.lumi = 19.5
info.private = False
info.arxiv = 'arXiv:1308.1586v2'
info.publication = 'Eur. Phys. J. C 73 (2013) 2677'


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2tt = dataset.addTxName('T2tt')
T2tt.constraint =  "[[['t']],[['t']]]"
T2tt.conditionDescription ="None"
T2tt.condition = None
T2tt.massConstraint = None
T2tt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T2ttoff = dataset.addTxName('T2ttoff')
T2ttoff.constraint = "[[['W','b']],[['W','b']]]"
T2ttoff.conditionDescription ="None"
T2ttoff.condition = None
T2ttoff.massConstraint = [['dm <= 169.0']]*2
T2ttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane([[x,y]]*2)
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl =  'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
T2tt_1.addSource('obsExclusion', 'orig/SUS13011_T2tt_exclusion.txt', 'txt')
T2tt_1.addSource('efficiencyMap','orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_$datasetStr$')
T2tt_1.dataUrl =  'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
T2ttoff.addMassPlane(T2tt_1)

END_BLOCK_TO_FILL

databaseCreator.create()

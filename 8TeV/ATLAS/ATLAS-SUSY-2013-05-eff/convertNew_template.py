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
info = MetaInfoInput('ATLAS-SUSY-2013-05')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-05/'
info.sqrts = '8.0*TeV'
info.lumi = 20.1
info.prettyName = 'ATLAS 2b'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1308.2631'
info.publication = 'http://link.springer.com/article/10.1007/JHEP10%282013%29189'
info.comment = 'T2bb efficiency maps created by the SModelS collaboration using CheckMATE'
info.supersedes = 'ATLAS_CONF_2013_001;ATLAS_CONF_2013_053'
info.implementedBy = 'Federico A'
info.contact = 'SModelS'

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2bb = dataset.addTxName('T2bb')
T2bb.checked =''
T2bb.constraint = "[[['b']],[['b']]]"
T2bb.conditionDescription = None
T2bb.condition =None
T2bb.source ='SModelS'
#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane([[x,y]]*2)
#----exclusion source----
T2bb_1.addSource('obsExclusion','orig/T2bb_exc.dat','txt')
T2bb_1.addSource('obsExclusionM1','orig/EXPECTED.txt','txt')
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_$datasetStr$.dat', 'txt')
T2bb_1.dataUrl = None
END_BLOCK_TO_FILL

databaseCreator.create()

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



#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRA-mCT300")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRA-mCT300", observedN = 7, expectedBG = 5.9 , bgError = 1.1)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRA-mCT300.dat', 'txt')
T2bb_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRB")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRB", observedN = 65, expectedBG = 64 , bgError = 10)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRB.dat', 'txt')
T2bb_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRA-mCT350")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRA-mCT350", observedN = 3, expectedBG = 2.5 , bgError = 0.6)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRA-mCT350.dat', 'txt')
T2bb_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRA-mCT150")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRA-mCT150", observedN = 102, expectedBG = 94 , bgError = 13)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRA-mCT150.dat', 'txt')
T2bb_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRA-mCT250")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRA-mCT250", observedN = 14, expectedBG = 15.8 , bgError = 2.8)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRA-mCT250.dat', 'txt')
T2bb_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("SRA-mCT200")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "SRA-mCT200", observedN = 48, expectedBG = 39 , bgError = 6)
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
T2bb_1.addSource('efficiencyMap', 'orig/CM_EM_SRA-mCT200.dat', 'txt')
T2bb_1.dataUrl = None

databaseCreator.create()

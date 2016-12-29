#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', 
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

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

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
info.comment = 'upper limits for T6bbWWC150 are not public'
info.contact = 'SModelS'
#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =''
T2bb.off.checked =''
T2bb.on.constraint = "[[['b']],[['b']]]"
#T2bb.off.constraint = ''
T2bb.on.conditionDescription = None
#T2bb.off.conditionDescription =''
T2bb.on.condition =None
#T2bb.off.condition =''
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----exclusion source----
T2bb_1.obsExclusion.setSource('orig/T2bb_exc.dat','txt')
T2bb_1.obsExclusionM1.setSource( 'orig/EXPECTED.txt', 'txt', objectName = None, index = None )
#T2bb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRA-mCT150.dat', 'txt', objectName = None, index = None, dataset="SRA-mCT150" )
T2bb_1.efficiencyMap.setStatistics( observedN= 102, expectedBG=94, bgError=13 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRA-mCT200.dat', 'txt', objectName = None, index = None, dataset="SRA-mCT200" )
T2bb_1.efficiencyMap.setStatistics( observedN=48, expectedBG=39 , bgError=6 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)


#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRA-mCT250.dat', 'txt', objectName = None, index = None, dataset="SRA-mCT250" )
T2bb_1.efficiencyMap.setStatistics( observedN=14, expectedBG=15.8, bgError=2.8 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)



#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRA-mCT300.dat', 'txt', objectName = None, index = None, dataset="SRA-mCT300" )
T2bb_1.efficiencyMap.setStatistics( observedN=7, expectedBG=5.9, bgError=1.1 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRA-mCT350.dat', 'txt', objectName = None, index = None, dataset="SRA-mCT350" )
T2bb_1.efficiencyMap.setStatistics( observedN=3, expectedBG=2.5, bgError=0.6 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/CM_EM_SRB.dat', 'txt', objectName = None, index = None, dataset="SRB" )
T2bb_1.efficiencyMap.setStatistics( observedN=65, expectedBG=64, bgError=10 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)



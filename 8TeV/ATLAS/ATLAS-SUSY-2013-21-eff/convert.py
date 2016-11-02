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

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2013-21')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-21/'
info.sqrts = 8
info.lumi = 20.3
info.prettyName = 'stop  to charm'
info.private = False
info.arxiv = 'http://arxiv.org/pdf/1407.0608v2.pdf'
#info.contact =
info.publication = 'http://journals.aps.org/prd/abstract/10.1103/PhysRevD.90.052008'
#info.comment =
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2bbWW = TxNameInput('T2bbWW')
T2bbWW.on.checked = ''
T2bbWW.off.checked =''
T2bbWW.on.constraint = "[[['b','W']],[['b','W']]]"
T2bbWW.off.constraint = "[[['b','L','nu']],[['b','L','nu']]]+[[['b','jet','jet']],[['b','jet','jet']]]+[[['b','jet','jet']],[['b','L','nu']]]"
T2bbWW.on.conditionDescription = None
T2bbWW.off.conditionDescription = None
T2bbWW.on.condition = None
T2bbWW.off.condition = None 
#T2bbWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bbWW_1 = T2bbWW.addMassPlane(motherMass = x , lspMass = y )
#---- new efficiency map -----
#----figure----
T2bbWW_1.figure =''
T2bbWW_1.figureUrl =''
#----exclusion source----
T2bbWW_1.obsExclusion.setSource(   'orig/T2bbWWoff_Obs.txt',      'txt', objectName = None, index = None )
T2bbWW_1.obsExclusionM1.setSource( 'orig/T2bbWWoff_ObsMinus.txt', 'txt', objectName = None, index = None )
T2bbWW_1.obsExclusionP1.setSource( 'orig/T2bbWWoff_ObsPlus.txt',  'txt', objectName = None, index = None )
#T2bbWW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2bbWW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bbWW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/T2bbWWoff_M1.dat', 'txt', objectName = None, index = None, dataset="M1" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=33054, expectedBG=33450, bgError=960 )
#----global url settings ----
T2bbWW_1.dataUrl =''
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl =''
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2bbWW_1.figure =''
T2bbWW_1.figureUrl =''
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/T2bbWWoff_M2.dat', 'txt', objectName = None, index = None, dataset="M2" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=8606, expectedBG=8620, bgError=270 )
#----global url settings ----
T2bbWW_1.dataUrl =''
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bbWW_1.figure =''
T2bbWW_1.figureUrl =''
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/T2bbWWoff_M3.dat', 'txt', objectName = None, index = None, dataset="M3" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=1776, expectedBG=1770, bgError=81 )
#----global url settings ----
T2bbWW_1.dataUrl =''
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)


#+++++++ next txName block ++++++++++++++
T2cc = TxNameInput('T2cc')
T2cc.on.checked =''
T2cc.off.checked =''
T2cc.on.constraint = "[[['c']],[['c']]]"
#T2cc.off.constraint =
T2cc.on.conditionDescription = None
#T2cc.off.conditionDescription =
T2cc.on.condition = None
#T2cc.off.condition =
#T2cc.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2cc_1 = T2cc.addMassPlane(motherMass =x , lspMass =y )
#---- new efficiency map -----
#----figure----
T2cc_1.figure =''
T2cc_1.figureUrl =''
#----exclusion source----
T2cc_1.obsExclusion.setSource(   'orig/T2cc_Obs.txt',      'txt', objectName = None, index = None )
T2cc_1.obsExclusionM1.setSource( 'orig/T2cc_ObsMinus.txt', 'txt',objectName = None, index = None )
T2cc_1.obsExclusionP1.setSource( 'orig/T2cc_ObsPlus.txt',  'txt', objectName = None, index = None )
#T2cc_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2cc_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2cc_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2cc_1.efficiencyMap.setSource( 'orig/T2cc_C1.dat', 'txt', objectName = None, index = None, dataset="C1" )
T2cc_1.efficiencyMap.setStatistics( observedN=208, expectedBG=210, bgError=21 )
#----global url settings ----
T2cc_1.dataUrl =''
#----efficiency map url settings ----
T2cc_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2cc_1.figure =''
T2cc_1.figureUrl =''
#----limit source----
T2cc_1.efficiencyMap.setSource( 'orig/T2cc_C2.dat', 'txt', objectName = None, index = None, dataset="C2" )
T2cc_1.efficiencyMap.setStatistics( observedN=71, expectedBG=75, bgError=11 )
#----global url settings ----
T2cc_1.dataUrl =''
#----efficiency map url settings ----
T2cc_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)


#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =''
T2bb.off.checked =''
T2bb.on.constraint ="[[['b']],[['b']]]"
#T2bb.off.constraint =
T2bb.on.conditionDescription = None
#T2bb.off.conditionDescription =
T2bb.on.condition = None
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass =x , lspMass =y )
#---- new efficiency map -----
#----figure----
T2bb_1.figure =''
T2bb_1.figureUrl =''
#----exclusion source----
T2bb_1.obsExclusion.setSource(   'orig/T2bb_Obs.txt',      'txt', objectName = None, index = None )
T2bb_1.obsExclusionM1.setSource( 'orig/T2bb_ObsMinus.txt',      'txt', objectName = None, index = None )
T2bb_1.obsExclusionP1.setSource( 'orig/T2bb_ObsPlus.txt',      'txt', objectName = None, index = None )
#T2bb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/T2bb_M1.dat', 'txt', objectName = None, index = None, dataset="M1" )
T2bb_1.efficiencyMap.setStatistics( observedN=33054, expectedBG=33450, bgError=960 )
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
T2bb_1.efficiencyMap.setSource( 'orig/T2bb_M2.dat', 'txt', objectName = None, index = None, dataset="M2" )
T2bb_1.efficiencyMap.setStatistics( observedN=8606, expectedBG=8620, bgError=270 )
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
T2bb_1.efficiencyMap.setSource( 'orig/T2bb_M3.dat','txt', objectName = None, index = None, dataset="M3" )
T2bb_1.efficiencyMap.setStatistics( observedN=1776, expectedBG=1770, bgError=81 )
#----global url settings ----
T2bb_1.dataUrl =''
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)



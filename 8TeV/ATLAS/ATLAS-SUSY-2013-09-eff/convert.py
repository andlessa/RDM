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
info = MetaInfoInput('ATLAS-SUSY-2013-09')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/'
info.sqrts = 8
info.lumi = '20.3'
#info.prettyName =
info.private = False
info.arxiv = 'http://arxiv.org/abs/1404.2500'
info.contact = "ATLAS collaboration"
info.publication = 'http://link.springer.com/article/10.1007/JHEP06(2014)035'
#info.comment =
info.supersedes = 'ATLAS-CONF-2013-007; ATLAS-CONF-2012-151'
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
#T1tttt.on.checked =
#T1tttt.off.checked =
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription = "None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition = "None"
#T1tttt.off.condition =
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y)
#---- new efficiency map -----
#----figure----
T1tttt_1.figure ="No Figure"
T1tttt_1.figureUrl ="No Figure"
#----exclusion source----
T1tttt_1.obsExclusion.setSource( "orig/exclusion_T1tttt.txt", "txt", objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( "orig/GluinoStop_observedDown.C", "cMacro", objectName = "GluinoStop_observedDown", index = None )
#T1tttt_1.obsExclusionP1.setSource( "orig/GluinoStop_observedUp.C", "cMacro", objectName = "GluinoStop_observedUp", index = None )
#T1tttt_1.expExclusion.setSource( "orig/GluinoStop_expected.C", "cMacro", objectName = "GluinoStop_expected", index = None )
#T1tttt_1.expExclusionM1.setSource( "orig/GluinoStop_expectedDown.C", "cMacro", objectName = "GluinoStop_expectedDown", index = None )
#T1tttt_1.expExclusionP1.setSource( "orig/GluinoStop_expectedUp.C", "cMacro", objectName = "GluinoStop_expectedUp", index = None )
#----limit source----
T1tttt_1.efficiencyMap.setSource( "orig/EffMap_T1tttt_SR3b.txt", "txt", objectName = None, index = None, dataset="SR3b" )
T1tttt_1.efficiencyMap.setStatistics( observedN=1, expectedBG=2.2, bgError=0.8 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = "No Figure"
T1tttt_1.figureUrl ="No Figure"
#----limit source----
T1tttt_1.efficiencyMap.setSource(  "orig/EffMap_T1tttt_SR0b.txt", "txt", index = None, dataset="SR0b" )
T1tttt_1.efficiencyMap.setStatistics( observedN=14, expectedBG=6.5, bgError= 2.3)
#----global url settings ----
T1tttt_1.dataUrl =  'http://hepdata.cedar.ac.uk/view/ins1289225'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl =  'http://hepdata.cedar.ac.uk/view/ins1289225'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ="No Figure"
T1tttt_1.figureUrl ="No Figure"
#----limit source----
T1tttt_1.efficiencyMap.setSource( "orig/EffMap_T1tttt_SR1b.txt", "txt", objectName = None, index = None, dataset="SR1b" )
T1tttt_1.efficiencyMap.setStatistics( observedN=10, expectedBG=4.7, bgError=2.1 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ="No Figure"
T1tttt_1.figureUrl ="No Figure"
#----limit source----
T1tttt_1.efficiencyMap.setSource( "orig/EffMap_T1tttt_SR3Llow.txt", "txt", objectName = None, index = None, dataset="SR3Llow" )
T1tttt_1.efficiencyMap.setStatistics( observedN=6, expectedBG=4.3, bgError=2.1 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ="No Figure"
T1tttt_1.figureUrl ="No Figure"
#----limit source----
T1tttt_1.efficiencyMap.setSource( "orig/EffMap_T1tttt_SR3LHigh.txt", "txt", objectName = None, index = None, dataset="SR3Lhigh" )
T1tttt_1.efficiencyMap.setStatistics( observedN=2, expectedBG=2.5, bgError=0.9 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225'
databaseCreator.create(True)



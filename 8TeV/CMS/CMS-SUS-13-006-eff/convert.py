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
info = MetaInfoInput('CMS-SUS-13-006')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
info.sqrts = 8
info.lumi = 19.5
info.prettyName ='CMS electroweakinos'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1405.7570'
info.contact = ''
info.publication = 'http://link.springer.com/article/10.1140%2Fepjc%2Fs10052-014-3036-7'
info.comment ='Using single lepton analysis EM'
info.supersedes ='CMS-PAS-SUS-12-022'
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
TChiWH.on.checked =''
TChiWH.off.checked =''
TChiWH.on.constraint = "[[['W']],[['higgs']]]"
#TChiWH.off.constraint = ''
TChiWH.on.conditionDescription =None
#TChiWH.off.conditionDescription =None
TChiWH.on.condition =None
#TChiWH.off.condition = "" 
#TChiWZ.branchingRatio =

TChiWH_1 = TChiWH.addMassPlane(motherMass = x , lspMass = y)
#---- new efficiency map -----
#----figure----
TChiWH_1.figure = 'Fig. 16(right)'
TChiWH_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig16_exclusion_TChiWH.png'
#----exclusion source----
TChiWH_1.obsExclusion.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 9 )
TChiWH_1.obsExclusionM1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 7 )
TChiWH_1.obsExclusionP1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 6 )
TChiWH_1.expExclusion.setSource("orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 8 )
TChiWH_1.expExclusionM1.setSource("orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 4 )
TChiWH_1.expExclusionP1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 5 )
#----limit source----
TChiWH_1.efficiencyMap.setSource( 'orig/singlelep_results.root', 'root', objectName = 'h_eff_met100', index = None, dataset="MET_100" )
TChiWH_1.efficiencyMap.setStatistics( observedN=7, expectedBG=7.7, bgError=1.9 )
#----global url settings ----
TChiWH_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiWH_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
databaseCreator.create() 


#---- new efficiency map -----
#----figure----
#TChiWH_1.figure =
#TChiWH_1.figureUrl =
#----limit source----
TChiWH_1.efficiencyMap.setSource( 'orig/singlelep_results.root', 'root',  objectName = 'h_eff_met125', index = None, dataset="MET_125" )
TChiWH_1.efficiencyMap.setStatistics( observedN=6, expectedBG=5.4, bgError=1.3 )
#----global url settings ----
TChiWH_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
#----efficiency map url settings ----
TChiWH_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#TChiWH_1.figure =
#TChiWH_1.figureUrl =
#----limit source----
TChiWH_1.efficiencyMap.setSource( 'orig/singlelep_results.root', 'root',  objectName = 'h_eff_met150', index = None, dataset="MET_150" )
TChiWH_1.efficiencyMap.setStatistics( observedN=3, expectedBG=3.8, bgError=1.0 )
#----global url settings ----
TChiWH_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
#----efficiency map url settings ----
TChiWH_1.efficiencyMap.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#TChiWH_1.figure =
#TChiWH_1.figureUrl =
#----limit source----
TChiWH_1.efficiencyMap.setSource( 'orig/singlelep_results.root', 'root',  objectName = 'h_eff_met175', index = None, dataset="MET_175" )
TChiWH_1.efficiencyMap.setStatistics( observedN=3, expectedBG=2.3, bgError=0.6 )
#----global url settings ----
TChiWH_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
#----efficiency map url settings ----
TChiWH_1.efficiencyMap.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/ss_eff_map.root'
databaseCreator.create(True)



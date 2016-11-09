#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.dat and the <txname>.dat files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description =
'create info.dat, txname.dat, twiki.dat and sms.py')
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
info = MetaInfoInput('CMS-SUS-13-012')
#info.comment =
info.sqrts = '8.0'
info.private = False
info.lumi = '19.5'
info.publication = 'JHEP06(2014)055'
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13012'
#info.superseded_by =
info.arxiv = 'http://arxiv.org/abs/1402.4770'
info.contact = 'cms-pag-conveners-sus@NOSPAMcernSPAMNOT.ch'
info.prettyName = ''
info.implementedBy = 'Federico A.'
# info.supersedes =


#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
T2.on.checked =''
T2.on.constraint ="[[['jet']],[['jet']]]"
T2.on.conditionDescription ="None"
T2.on.condition ="None"
#+++++++ next mass plane block ++++++++++++++
T2 = T2.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T2.figure = "Fig_7a"
T2.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7a.pdf"
#----exclusion source----
T2.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T2.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T2.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T2.expExclusion.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T2.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T2.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )
#----limit source----
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_200MHT300", index = None, dataset="3NJet6_500HT800_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
#----efficiency map url settings ----
databaseCreator.create()

T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_300MHT450", index = None, dataset="3NJet6_500HT800_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)

T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_450MHT600", index = None, dataset="3NJet6_500HT800_450MHT600" )
T2.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_600MHTinf", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_200MHT300", index = None, dataset="3NJet6_800HT1000_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_300MHT450", index = None, dataset="3NJet6_800HT1000_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_450MHT600", index = None, dataset="3NJet6_800HT1000_450MHT600" )
T2.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_600MHTinf", index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_200MHT300", index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_300MHT450", index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_450MHT600", index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T2.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_600MHTinf", index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_200MHT300", index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_300MHT450", index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_450MHTinf", index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_200MHT300", index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_300MHTinf", index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_200MHT300", index = None, dataset="6NJet8_500HT800_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_300MHT450", index = None, dataset="6NJet8_500HT800_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_450MHTinf", index = None, dataset="6NJet8_500HT800_450MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3 ) ### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_200MHT300", index = None, dataset="6NJet8_800HT1000_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_300MHT450", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_450MHTinf", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_200MHT300", index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_300MHT450", index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_450MHTinf", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_200MHT300", index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_300MHT450", index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T2.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_450MHTinf", index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6  ) #check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_200MHT300", index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T2.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_300MHTinf", index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_8NJetinf_500HT800_200MHTinf", index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource("orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_8NJetinf_800HT1000_200MHTinf", index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_8NJetinf_1000HT1250_200MHTinf", index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_8NJetinf_1250HT1500_200MHTinf", index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8 )#### check error
databaseCreator.create(True)
T2.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "h_EffAcc_8NJetinf_1500HTinf_200MHTinf", index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T2.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)




#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription ="None"
T1tttt.off.conditionDescription ="None"
T1tttt.off.condition = "None"
T1tttt.on.condition ="None"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T1tttt.figure = "Fig_7c"
T1tttt.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7c.pdf"
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T1tttt.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T1tttt.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T1tttt.expExclusion.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T1tttt.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T1tttt.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )
#----limit source----
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_200MHT300", index = None, dataset="3NJet6_500HT800_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_300MHT450", index = None, dataset="3NJet6_500HT800_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_450MHT600", index = None, dataset="3NJet6_500HT800_450MHT600" )
T1tttt.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_600MHTinf", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_200MHT300", index = None, dataset="3NJet6_800HT1000_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_300MHT450", index = None, dataset="3NJet6_800HT1000_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_450MHT600", index = None, dataset="3NJet6_800HT1000_450MHT600" )
T1tttt.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_450MHT600", index = None, dataset="3NJet6_800HT1000_450MHT600" )
T1tttt.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_200MHT300", index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_300MHT450", index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_450MHT600", index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T1tttt.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_600MHTinf", index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_200MHT300", index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_300MHT450", index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_450MHTinf", index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_200MHT300", index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_300MHTinf", index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_200MHT300", index = None, dataset="6NJet8_500HT800_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_300MHT450", index = None, dataset="6NJet8_500HT800_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_450MHTinf", index = None, dataset="6NJet8_500HT800_450MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3 ) ### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_200MHT300", index = None, dataset="6NJet8_800HT1000_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_300MHT450", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_450MHTinf", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_200MHT300", index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_300MHT450", index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_450MHTinf", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 )  ### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_200MHT300", index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_300MHT450", index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T1tttt.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_450MHTinf", index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6  ) #check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_200MHT300", index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T1tttt.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_300MHTinf", index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_8NJetinf_500HT800_200MHTinf", index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_8NJetinf_800HT1000_200MHTinf", index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_8NJetinf_1000HT1250_200MHTinf", index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_8NJetinf_1250HT1500_200MHTinf", index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8 )#### check error
databaseCreator.create(True)
T1tttt.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "h_EffAcc_8NJetinf_1500HTinf_200MHTinf", index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T1tttt.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)


#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
#T1.on.checked =" "
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.on.conditionDescription ="None"
T1.on.condition ="None"
#T1bbbb.off.fuzzycondition =
#+++++++ next mass plane block ++++++++++++++
T1 = T1.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T1.figure = "Fig_7b"
T1.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7b.pdf"
#----exclusion source----
T1.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T1.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T1.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T1.expExclusion.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T1.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T1.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )
#----limit source----
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_200MHT300", index = None, dataset="3NJet6_500HT800_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
#----global url settings ----
T1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13012'
#----efficiency map url settings ----
T1.efficiencyMap.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/c_AccEffMap_T1qqqq.tar"
databaseCreator.create(True)

T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_300MHT450", index = None, dataset="3NJet6_500HT800_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_450MHT600", index = None, dataset="3NJet6_500HT800_450MHT600" )
T1.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_500HT800_600MHTinf", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_200MHT300", index = None, dataset="3NJet6_800HT1000_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_300MHT450", index = None, dataset="3NJet6_800HT1000_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_450MHT600", index = None, dataset="3NJet6_800HT1000_450MHT600" )
T1.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_800HT1000_600MHTinf", index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_200MHT300", index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_300MHT450", index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_450MHT600", index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T1.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1000HT1250_600MHTinf", index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_200MHT300", index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_300MHT450", index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1250HT1500_450MHTinf", index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_200MHT300", index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_3NJet6_1500HTinf_300MHTinf", index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_200MHT300", index = None, dataset="6NJet8_500HT800_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_300MHT450", index = None, dataset="6NJet8_500HT800_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_500HT800_450MHTinf", index = None, dataset="6NJet8_500HT800_450MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3 ) ### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_200MHT300", index = None, dataset="6NJet8_800HT1000_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_300MHT450", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T1.efficiencyMap.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_800HT1000_450MHTinf", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_200MHT300", index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_300MHT450", index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1000HT1250_450MHTinf", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_200MHT300", index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_300MHT450", index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T1.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1250HT1500_450MHTinf", index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_200MHT300", index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T1.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_6NJet8_1500HTinf_300MHTinf", index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_8NJetinf_500HT800_200MHTinf", index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_8NJetinf_800HT1000_200MHTinf", index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_8NJetinf_1000HT1250_200MHTinf", index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_8NJetinf_1250HT1500_200MHTinf", index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8 )#### check error
databaseCreator.create(True)
T1.efficiencyMap.setSource(  "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "h_EffAcc_8NJetinf_1500HTinf_200MHTinf", index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T1.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)





#+++++++ next txName block ++++++++++++++
T5ZZ = TxNameInput('T5ZZ')
T5ZZ.on.checked =" "
T5ZZ.off.checked =''
T5ZZ.on.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.off.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZ.on.conditionDescription ="None"
T5ZZ.off.conditionDescription ="None"
T5ZZ.off.condition =None
T5ZZ.on.condition ="None"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5ZZ_1 .obsExclusion.setSource( "orig/CMS_T5VV_x05.dat", "txt", objectName = None, index = None )
#----limit source----
T5ZZ_1 .efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5ZZ_1.efficiencyMap.setSource( "orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5ZZ_1.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)


#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5ZZ_2 .obsExclusion.setSource( "orig/Null_Line.txt", "txt", objectName = None, index = None )
#----limit source----
T5ZZ_2 .efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5ZZ_2.efficiencyMap.setSource( "orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5ZZ_2.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)



#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5ZZ_3 .obsExclusion.setSource( "orig/Null_Line.txt", "txt", objectName = None, index = None )
#----limit source----
T5ZZ_3 .efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5ZZ_3.efficiencyMap.setSource( "orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5ZZ_3.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)




#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked =" "
T5WW.off.checked =''
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WW.on.conditionDescription ="None"
T5WW.off.conditionDescription ="None"
T5WW.off.condition =None
T5WW.on.condition ="None"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5WW_1 .obsExclusion.setSource( "orig/CMS_T5VV_x05.dat", "txt", objectName = None, index = None )
#----limit source----
T5WW_1 .efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5WW_1.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5WW_1.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5WW_1.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5WW_1.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5WW_1.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5WW_1.efficiencyMap.setSource( "orig/T5WW_x05/MA5_EM_T5WW_x05_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5WW_1.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)


#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5WW_2 .obsExclusion.setSource( "orig/Null_Line.txt", "txt", objectName = None, index = None )
#----limit source----
T5WW_2 .efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5WW_2.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5WW_2.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5WW_2.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5WW_2.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5WW_2.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5WW_2.efficiencyMap.setSource( "orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5WW_2.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)



#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y)
#---- new efficiency map -----
#----figure----
#----exclusion source----
T5WW_3.obsExclusion.setSource( "orig/Null_Line.txt", "txt", objectName = None, index = None )
#----limit source----
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=6159, expectedBG=6088, bgError=665 )
databaseCreator.create(True)

T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=2305, expectedBG=2278, bgError=266 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_500HT800_450MHT600.dat", "txt", objectName = None, index = None, dataset="3NJet6_500HT800_450MHT600" )
T5WW_3.efficiencyMap.setStatistics ( observedN=454, expectedBG=418, bgError=66 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_500HT800_600MHTinf.dat", "txt", objectName = "None", index = None, dataset="3NJet6_500HT800_600MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=62, expectedBG=57.4, bgError=11.2 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=808, expectedBG=777, bgError=107 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=305, expectedBG=330, bgError=40 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_450MHT600.dat", "txt", objectName = None , index = None, dataset="3NJet6_800HT1000_450MHT600" )
T5WW_3.efficiencyMap.setStatistics ( observedN=124, expectedBG=108, bgError=15 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_800HT1000_600MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=52, expectedBG=54.8, bgError=9.7 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=335, expectedBG=305, bgError=41 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=129, expectedBG=137, bgError=20 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1000HT1250_450MHT600.dat", "txt", objectName =None, index = None, dataset="3NJet6_1000HT1250_450MHT600" )
T5WW_3.efficiencyMap.setStatistics ( observedN=34, expectedBG=32.3, bgError=6.1 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1000HT1250_600MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1000HT1250_600MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=32, expectedBG=22.8, bgError=5.2 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=98, expectedBG=109, bgError=18 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=38, expectedBG=42.8, bgError=9.5 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1250HT1500_450MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=23, expectedBG=17.6, bgError=4.1 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=94, expectedBG=86, bgError=17 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="3NJet6_1500HTinf_300MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=39, expectedBG=29.7, bgError=5.8 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_500HT800_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=266, expectedBG=290, bgError=65 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_500HT800_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=62, expectedBG=52, bgError=12 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_500HT800_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_500HT800_450MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=9, expectedBG=0.8, bgError=3.3  ) ### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_800HT1000_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_800HT1000_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=111, expectedBG=124, bgError=29 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_800HT1000_300MHT450.dat", "txt", objectName = "", index = None, dataset="6NJet8_800HT1000_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=35, expectedBG=28.6, bgError=6.9 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_800HT1000_450MHTinf.dat", "txt", objectName = "None", index = None, dataset="6NJet8_800HT1000_450MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=4, expectedBG=6.0, bgError=2.8 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1000HT1250_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=67, expectedBG=70, bgError=16 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1000HT1250_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1000HT1250_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=20, expectedBG=21.6, bgError=5.8 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1000HT1250_450MHTinf.dat", "txt", objectName = "", index = None, dataset="6NJet8_1000HT1250_450MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=4, expectedBG=2.2, bgError=3.8 ) ### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1250HT1500_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=24, expectedBG=28.0, bgError=8.2 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1250HT1500_300MHT450.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_300MHT450" )
T5WW_3.efficiencyMap.setStatistics ( observedN=5, expectedBG=9.4, bgError=3.6 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1250HT1500_450MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1250HT1500_450MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=2, expectedBG=0.5, bgError=2.6 ) #check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1500HTinf_200MHT300.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_200MHT300" )
T5WW_3.efficiencyMap.setStatistics ( observedN=18, expectedBG=21.1, bgError=8.1 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_6NJet8_1500HTinf_300MHTinf.dat", "txt", objectName = None, index = None, dataset="6NJet8_1500HTinf_300MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=3, expectedBG=7.9, bgError=3.6 )
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8NJetinf_500HT800_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_500HT800_200MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=8, expectedBG=4.8, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8NJetinf_800HT1000_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_800HT1000_200MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=9, expectedBG=8.3, bgError=3.4 )#### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8NJetinf_1000HT1250_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1000HT1250_200MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=8, expectedBG=5.6, bgError=2.3 )#### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8NJetinf_1250HT1500_200MHTinf.dat", "txt", objectName = None , index = None, dataset="8NJetinf_1250HT1500_200MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.1, bgError=3.8  )#### check error
databaseCreator.create(True)
T5WW_3.efficiencyMap.setSource( "orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8NJetinf_1500HTinf_200MHTinf.dat", "txt", objectName = None, index = None, dataset="8NJetinf_1500HTinf_200MHTinf" )
T5WW_3.efficiencyMap.setStatistics ( observedN=2, expectedBG=3.3, bgError=4.7 )#### check error
databaseCreator.create(True)


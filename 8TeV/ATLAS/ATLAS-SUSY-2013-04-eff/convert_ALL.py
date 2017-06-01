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
info = MetaInfoInput('ATLAS-SUSY-2013-04')
info.comment = 'Erratum: JHEP01(2014)109. T1tttt official efficiency maps from ATLAS collaboration; T5WW and T5ZZ efficiency maps created by the SModelS collaboration using MadAnalysis5'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP10%282013%29130'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/'
# info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1308.1841'
info.contact = "ATLAS collaboration for T1tttt models;SModelS for T5WW and T5ZZ models"
info.prettyName = 'ATLAS \ge 7 jets'
info.supersedes = 'ATLAS-CONF-2012-103'


#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked ="None"
#T1tttt.off.checked =
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription ="None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition ="None"
#T1tttt.off.condition =

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
T1tttt.obsExclusion.setSource( "orig/exclusion_T1tttt.txt", "txt", objectName = None, index = None )
#----figure----
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'

#+++++++ next txName block ++++++++++++++                                                                         
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint =  "[[['t']],[['t']]]"
T2tt.off.constraint = "[[['W','b']],[['W','b']]]"
T2tt.on.conditionDescription ="None"
T2tt.off.conditionDescription ="None"
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =                                                                                            
#+++++++ next mass plane block ++++++++++++++                                                                     
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#T2tt_1.obsExclusion.setSource( 'orig/Null.txt', 'txt', objectName = None, index = None )


#+++++++ next txName block ++++++++++++++                                                                                                                                                                    
T5 = TxNameInput('T5')
T5.on.checked =" "
T5.off.checked =''
T5.on.constraint ="[[['jet'],['jet']],[['jet'],['jet']]]"
T5.on.conditionDescription ="None"
T5.on.condition ="None"
#+++++++ next mass plane block ++++++++++++++                                                                                                                                                                
T5_x05 = T5.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y)
T5_x005 = T5.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y)
T5_x095 = T5.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y)


#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked =''
T5WW.off.checked =''
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WW.on.conditionDescription =None
T5WW.off.conditionDescription =None
T5WW.on.condition =None
T5WW.off.condition =None
#T5WW.branchingRatio =
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y )
#---- new efficiency map -----
#----figure----
T5WW_1.figure =''
T5WW_1.figureUrl =''
#----exclusion source----
T5WW_1.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5WW_1.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5WW_1.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y )
T5WW_3 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y )

#+++++++ next txName block ++++++++++++++
T5ZZ = TxNameInput('T5ZZ')
T5ZZ.on.checked =''
T5ZZ.off.checked =''
T5ZZ.on.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.off.constraint ="2.1*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZ.on.conditionDescription =None
T5ZZ.off.conditionDescription =None
T5ZZ.on.condition =None
T5ZZ.off.condition =None
#T5ZZ.branchingRatio =
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y )
T5ZZ_2 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y )
T5ZZ_3 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y )

#+++++++ next txName block ++++++++++++++                                                                             
T1btbt = TxNameInput('T1btbt')
T1btbt.on.checked =''
T1btbt.off.checked =''
T1btbt.on.constraint =  "[[['b','t']],[['b','t']]]"
#T2tt.off.constraint = "[[['W','b']],[['W','b']]]"                                                                    
T1btbt.on.conditionDescription ="None"
#T2tt.off.conditionDescription ="None"                                                                                
T1btbt.on.condition = None
#T2tt.off.condition = None                                                                                            
#T2tt.branchingRatio =                                                                                                
#+++++++ next mass plane block ++++++++++++++                                                                         
T1btbt_1 = T1btbt.addMassPlane(motherMass = x, lspMass = y)
#T1btbt_1.obsExclusion.setSource( 'orig/Null.txt', 'txt', objectName = None , index = None )

#+++++++ next txName block ++++++++++++++                                                                             
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked =''
T1bbbb.off.checked =''
T1bbbb.on.constraint =  "[[['b','b']],[['b','b']]]"
T1bbbb.on.conditionDescription ="None"
T1bbbb.on.condition = None
#T2tt.branchingRatio =                                                                                                
#+++++++ next mass plane block ++++++++++++++                                                                         
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#T1bbbb_1.obsExclusion.setSource( 'orig/Null.txt', 'txt', objectName = None , index = None )

#+++++++ next txName block ++++++++++++++                                                                                                                                                                    
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked =" "
T6bbWW.off.checked =''
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="2.23*[[['b'],['jet','jet']],[['b'],['jet','jet']]]"
T6bbWW.on.conditionDescription ="None"
T6bbWW.off.conditionDescription ="None"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="None"
#+++++++ next mass plane block ++++++++++++++                                                                                                                                                                
T6bbWW_x05 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y)
T6bbWW_x01 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 0.1*x + 0.9*y, lspMass = y)
T6bbWW_x09 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 0.9*x + 0.1*y, lspMass = y)



###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_10ij50_bjetblind.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T1tttt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5WW_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5WW_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5WW_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T2tt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T1btbt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T1bbbb_1.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_10ij50_bjetblind.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_10ij50_bjetblind")
T5_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_7ej80_0bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5_x005.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5_x05.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_7ej80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_0bjet")
T5_x095.efficiencyMap.setStatistics(observedN=12, expectedBG=11, bgError=2.2)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_7ej80_1bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5_x005.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5_x05.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_7ej80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_1bjet")
T5_x095.efficiencyMap.setStatistics(observedN=17, expectedBG=17, bgError=6)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_7ej80_2ibjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T2tt_1.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5_x005.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5_x05.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_7ej80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_7ej80_2ibjet")
T5_x095.efficiencyMap.setStatistics(observedN=13, expectedBG=25, bgError=10)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ej50_0bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5_x005.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5_x05.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_0bjet")
T5_x095.efficiencyMap.setStatistics(observedN=40, expectedBG=35, bgError=4)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ej50_1bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_1bjet")
T5_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=40, bgError=10)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ej50_2ibjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T2tt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5_x005.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5_x05.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ej50_2ibjet")
T5_x095.efficiencyMap.setStatistics(observedN=44, expectedBG=50, bgError=10)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ij80_0bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5_x005.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5_x05.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ij80_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_0bjet")
T5_x095.efficiencyMap.setStatistics(observedN=2, expectedBG=0.9, bgError=0.6)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ij80_1bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5_x005.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5_x05.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ij80_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_1bjet")
T5_x095.efficiencyMap.setStatistics(observedN=1, expectedBG=1.5, bgError=0.9)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_8ij80_2ibjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T2tt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5_x005.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5_x05.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_8ij80_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_8ij80_2ibjet")
T5_x095.efficiencyMap.setStatistics(observedN=3, expectedBG=3.3, bgError=2.2)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_9ej50_0bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5_x005.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5_x05.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_9ej50_0bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_0bjet")
T5_x095.efficiencyMap.setStatistics(observedN=5, expectedBG=3.3, bgError=0.7)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_9ej50_1bjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T2tt_1.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5_x005.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5_x05.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_9ej50_1bjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_1bjet")
T5_x095.efficiencyMap.setStatistics(observedN=8, expectedBG=6.1, bgError=1.7)
databaseCreator.create()
###
T1tttt_1.efficiencyMap.setSource("orig/T1tttt_1_Official/GtGrid_SR_9ej50_2ibjet.txt", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T1tttt_1.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5WW_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x005_EM_MAPS/MA5_EM_T5WW_x005_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5WW_x005.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5WW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x05_EM_MAPS/MA5_EM_T5WW_x05_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5WW_x05.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5WW_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5WW_x095_EM_MAPS/MA5_EM_T5WW_x095_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5WW_x095.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5ZZ_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x005_EM_MAPS/MA5_EM_T5ZZ_x005_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5ZZ_x005.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5ZZ_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x05_EM_MAPS/MA5_EM_T5ZZ_x05_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5ZZ_x05.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5ZZ_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5ZZ_x095_EM_MAPS/MA5_EM_T5ZZ_x095_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5ZZ_x095.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T2tt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T2tt_1.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T1btbt_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T1btbt_1.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T1bbbb_1.efficiencyMap.setSource("orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T1bbbb_1.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T6bbWW_x01.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T6bbWW_x01.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T6bbWW_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T6bbWW_x05.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T6bbWW_x09.efficiencyMap.setSource("orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T6bbWW_x09.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5_x005.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5_x005.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5_x05.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5_x05.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
T5_x095.efficiencyMap.setSource("orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_GtGrid_SR_9ej50_2ibjet.dat", "txt", objectName ="None", index = None, dataset="GtGrid_SR_9ej50_2ibjet")
T5_x095.efficiencyMap.setStatistics(observedN=7, expectedBG=8.0,   bgError=2.7)
databaseCreator.create()















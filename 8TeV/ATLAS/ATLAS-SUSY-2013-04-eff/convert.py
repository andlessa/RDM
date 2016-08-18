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
info.comment = 'Erratum: JHEP01(2014)109'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP10%282013%29130'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/'
# info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1308.1841'
info.contact = "ATLAS collaboration"
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

#----figure----
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#----limit url settings ----

## EFFICIENCIES

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_10ij50_bjetblind.txt", "txt" , objectName =  "GtGrid_SR_10ij50_bjetblind.txt", index = None , dataset = "GtGrid_SR_10ij50_bjetblind" )
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_10ij50_bjetblind.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 3 ,  expectedBG= 1.37   , bgError=  0.35 )
databaseCreator.create()


T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_7ej80_0bjet.txt", "txt" , objectName =  "GtGrid_SR_7ej80_0bjet.txt", index = None , dataset = "GtGrid_SR_7ej80_0bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_0bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN=  12 ,  expectedBG= 11.0  , bgError= 2.2  )
databaseCreator.create(True)


T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_7ej80_1bjet.txt", "txt" , objectName =  "GtGrid_SR_7ej80_1bjet.txt", index = None , dataset = "GtGrid_SR_7ej80_1bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_1bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN=  17,  expectedBG= 17  , bgError=  6 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_7ej80_2ibjet.txt", "txt" , objectName =  "GtGrid_SR_7ej80_2ibjet.txt", index = None , dataset = "GtGrid_SR_7ej80_2ibjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_2ibjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 13 ,  expectedBG=  25 , bgError=  10 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ej50_0bjet.txt", "txt" , objectName =  "GtGrid_SR_8ej50_0bjet.txt", index = None , dataset = "GtGrid_SR_8ej50_0bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_0bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 40 ,  expectedBG= 35  , bgError= 4  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ej50_1bjet.txt", "txt" , objectName =  "GtGrid_SR_8ej50_1bjet.txt", index = None , dataset = "GtGrid_SR_8ej50_1bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_1bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 44 ,  expectedBG=  40 , bgError= 10  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ej50_2ibjet.txt", "txt" , objectName =  "GtGrid_SR_8ej50_2ibjet.txt", index = None , dataset = "GtGrid_SR_8ej50_2ibjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_2ibjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 44 ,  expectedBG= 50  , bgError= 10  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ij80_0bjet.txt", "txt" , objectName =  "GtGrid_SR_8ij80_0bjet.txt", index = None , dataset = "GtGrid_SR_8ij80_0bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_0bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 2 ,  expectedBG= 0.9  , bgError=  0.6 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ij80_1bjet.txt", "txt" , objectName =  "GtGrid_SR_8ij80_1bjet.txt", index = None , dataset = "GtGrid_SR_8ij80_1bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_1bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 1 ,  expectedBG=  1.5 , bgError=  0.9 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_8ij80_2ibjet.txt", "txt" , objectName =  "GtGrid_SR_8ij80_2ibjet.txt", index = None , dataset = "GtGrid_SR_8ij80_2ibjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_2ibjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 3 ,  expectedBG= 3.3  , bgError= 2.2  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_9ej50_0bjet.txt", "txt" , objectName =  "GtGrid_SR_9ej50_0bjet.txt", index = None , dataset = "GtGrid_SR_9ej50_0bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_0bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 5 ,  expectedBG= 3.3  , bgError=  0.7 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_9ej50_1bjet.txt", "txt" , objectName =  "GtGrid_SR_9ej50_1bjet.txt", index = None , dataset = "GtGrid_SR_9ej50_1bjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_1bjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 8 ,  expectedBG= 6.1  , bgError= 1.7  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/GtGrid_SR_9ej50_2ibjet.txt", "txt" , objectName =  "GtGrid_SR_9ej50_2ibjet.txt", index = None , dataset = "GtGrid_SR_9ej50_2ibjet" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_2ibjet.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 7 ,  expectedBG= 8.0  , bgError= 2.7  )
databaseCreator.create(True)



'''
These maps refer to the other type of analysis - JETSTREAM
T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ340.10ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ340.10ij50.GttOffShell.txt", index = None , dataset = "MJ340_10ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ340.10ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 1 ,  expectedBG=  3.2 , bgError=  3.2 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ340.8ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ340.8ij50.GttOffShell.txt", index = None , dataset = "MJ340_8ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ340.8ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 69 ,  expectedBG= 75  , bgError= 19 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ340.9ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ340.9ij50.GttOffShell.txt", index = None , dataset = "MJ340_9ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ340.9ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 13 ,  expectedBG= 17  , bgError= 7  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ420.10ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ420.10ij50.GttOffShell.txt", index = None , dataset = "MJ420_10ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ420.10ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN=  1,  expectedBG= 2.2   , bgError=  2.0 )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ420.8ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ420.8ij50.GttOffShell.txt", index = None , dataset = "MJ420_8ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ420.8ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 37 ,  expectedBG=  45 , bgError= 14  )
databaseCreator.create(True)

T1tttt.efficiencyMap.setSource( "./orig/HEPdata.MJ420.9ij50.GttOffShell.txt", "txt" , objectName =  "HEPdata.MJ420.9ij50.GttOffShell.txt", index = None , dataset = "MJ420_9ij50_GttOffShell" )
T1tttt.dataUrl = "http://hepdata.cedar.ac.uk/resource/6095/mjstream/HEPdata.MJ420.9ij50.GttOffShell.txt"
T1tttt.efficiencyMap.setStatistics( observedN= 9 ,  expectedBG=  11 , bgError=  5 )
databaseCreator.create(True)
'''


# MA5 Home Made Maps ++++++++++++++++++++++++



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
#T5WW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----figure----
T5WW_1.figure =''
T5WW_1.figureUrl =''
#----exclusion source----
T5WW_1.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5WW_1.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5WW_1.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5WW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)


#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5WW_1.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_1.efficiencyMap.setSource( 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5WW_1.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)



#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y )
#T5WW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----exclusion source----
T5WW_2.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5WW_2.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5WW_2.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5WW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5WW_2.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_2.efficiencyMap.setSource( 'orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5WW_2.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)

#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y )
#T5WW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----exclusion source----
T5WW_3.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5WW_3.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5WW_3.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5WW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5WW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)


#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5WW_3.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5WW_3.efficiencyMap.setSource( 'orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5WW_3.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)



#+++++++ next txName block ++++++++++++++
T5ZZ = TxNameInput('T5ZZ')
T5ZZ.on.checked =''
T5ZZ.off.checked =''
T5ZZ.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5ZZ.off.constraint ="2.1*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZ.on.conditionDescription =None
T5ZZ.off.conditionDescription =''
T5ZZ.on.condition =None
T5ZZ.off.condition =''
#T5ZZ.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y )
#T5ZZ_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----figure----
T5ZZ_1.figure =''
T5ZZ_1.figureUrl =''
#----exclusion source----
T5ZZ_1.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5ZZ_1.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5ZZ_1.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5ZZ_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)



#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_1.efficiencyMap.setSource( 'orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5ZZ_1.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)


#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.05*x + 0.95*y, lspMass = y )
#T5ZZ_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----exclusion source----
T5ZZ_2.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5ZZ_2.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5ZZ_2.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5ZZ_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_2.efficiencyMap.setSource( 'orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5ZZ_2.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)




#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane(motherMass = x, interMass0 = 0.95*x + 0.05*y, lspMass = y )
#T5ZZ_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----exclusion source----
T5ZZ_3.obsExclusion.setSource( 'orig/Exclusion_T5WW_x05.txt', 'txt', objectName = None, index = None )
T5ZZ_3.obsExclusionM1.setSource( 'orig/T5WW_Plus.txt', 'txt', objectName = None, index = None )
T5ZZ_3.obsExclusionP1.setSource( 'orig/T5WW_Minus.txt', 'txt', objectName = None, index = None )
#T5ZZ_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5ZZ_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_0bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=12, expectedBG=11, bgError=2.2 )
databaseCreator.create(True)


#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_1bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=17, expectedBG=17, bgError=6 )
databaseCreator.create(True)


#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_7ej80_2ibjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=13, expectedBG=25, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_0bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=40, expectedBG=35, bgError= 4)
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_1bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=44, expectedBG=40, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ej50_2ibjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=44, expectedBG=50, bgError=10 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,0bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_0bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,1bjet.dat','txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=8, expectedBG=6.1, bgError=1.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_9ej50_1bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=7, expectedBG=8, bgError=2.7 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,0bjet.dat','txt',  objectName = None, index = None, dataset="GtGrid_SR_8ij80_0bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=2, expectedBG=0.9, bgError=0.6 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,1bjet.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_1bjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=1, expectedBG=1.5, bgError=0.9 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,>=2bjets.dat', 'txt', objectName = None, index = None, dataset="GtGrid_SR_8ij80_2ibjet" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=3, expectedBG=3.3, bgError=2.2 )
databaseCreator.create(True)

#---- new efficiency map -----
T5ZZ_3.efficiencyMap.setSource( 'orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=10j50.dat', 'txt',objectName = None, index = None, dataset="GtGrid_SR_10ij50_bjetblind" )
T5ZZ_3.efficiencyMap.setStatistics( observedN=3, expectedBG=1.37, bgError=0.35)
databaseCreator.create(True)


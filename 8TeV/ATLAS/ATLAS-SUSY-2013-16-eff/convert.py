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
info = MetaInfoInput('ATLAS-SUSY-2013-16')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-16/'
info.sqrts = '8'
info.lumi = '20.1'
info.prettyName = ''
info.private = False
info.arxiv = 'http://arxiv.org/abs/1406.1122'
info.contact = ''
info.publication = 'http://link.springer.com/article/10.1007%2FJHEP09%282014%29015'
info.comment ='EM given for All SRs for one topo, only for 3 for the other. Only these 3 are implemented.'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked = ""
#T2tt.off.checked =
T2tt.on.constraint = "[[['t']],[['t']]]"
#T2tt.off.constraint =
T2tt.on.conditionDescription = "None"
#T2tt.off.conditionDescription =
T2tt.on.condition = "None"
#T2tt.off.condition =
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x , lspMass = y)
#---- new efficiency map -----
#----figure----
#T2tt_1.figure = ''
#T2tt_1.figureUrl = ''
#----exclusion source----
T2tt_1.obsExclusion.setSource( "./orig/T2tt_Exclusion.txt", "txt", objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2tt_1.efficiencyMap.setSource( "./orig/EffMap_T2tt_SRC1.txt", "txt", objectName = None, index = None, dataset="SRC1" )
T2tt_1.efficiencyMap.setStatistics( observedN=59, expectedBG=68, bgError=7)
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create()

#---- new efficiency map -----
#----figure----
#T2tt_1.figure = ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource( "./orig/EffMap_T2tt_SRC2.txt", "txt", objectName = None, index = None, dataset="SRC2" )
T2tt_1.efficiencyMap.setStatistics( observedN=30, expectedBG=34, bgError=5 )
#----global url settings ----
T2tt_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRC3.txt", "txt", objectName = None, index = None, dataset="SRC3" )
T2tt_1.efficiencyMap.setStatistics( observedN=15, expectedBG=20.3, bgError=3.0 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRA1.txt", "txt", objectName = None, index = None, dataset="SRA1" )
T2tt_1.efficiencyMap.setStatistics( observedN=11, expectedBG=15.8, bgError=1.9 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRA2.txt", "txt", objectName = None, index = None, dataset="SRA2" )
T2tt_1.efficiencyMap.setStatistics( observedN=4, expectedBG=4.1, bgError=0.8 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRA3.txt", "txt", objectName = None, index = None, dataset="SRA3" )
T2tt_1.efficiencyMap.setStatistics( observedN=5, expectedBG=4.1, bgError=0.9 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRA4.txt", "txt", objectName = None, index = None, dataset="SRA4" )
T2tt_1.efficiencyMap.setStatistics( observedN=4, expectedBG=2.4, bgError=0.7 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRC1.txt", "txt", objectName = None, index = None, dataset="SRC1" )
T2tt_1.efficiencyMap.setStatistics( observedN=59, expectedBG=68, bgError=7 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRC2.txt", "txt", objectName = None, index = None, dataset="SRC2" )
T2tt_1.efficiencyMap.setStatistics( observedN=30, expectedBG=34, bgError=5 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =  ''
#T2tt_1.figureUrl = ''
#----limit source----
T2tt_1.efficiencyMap.setSource(  "./orig/EffMap_T2tt_SRC3.txt", "txt", objectName = None, index = None, dataset="SRC3" )
T2tt_1.efficiencyMap.setStatistics( observedN=15, expectedBG=20.3, bgError=3.0 )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/d27/input'
#----efficiency map url settings ----
#T2tt_1.efficiencyMap.dataUrl =
databaseCreator.create(True)







#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
#T6bbWW.on.checked =''
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="[[['b'],['W']],[['b'],['jet','jet']]]"
T6bbWW.on.conditionDescription ="None"
T6bbWW.off.conditionDescription ="None"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="None"
#T6bbWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T6bbWW_1 = T6bbWW.addMassPlane(motherMass = x , interMass0 = 2*y, lspMass = y)
#T6bbWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#---- new efficiency map -----
#----figure----
#T6bbWW_1.figure =
#T6bbWW_1.figureUrl =
#----exclusion source----
T6bbWW_1.obsExclusion.setSource( "./orig/T6bbWW_Exclusion.txt" ,"txt", objectName = None, index = None )
#T6bbWW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T6bbWW_1.efficiencyMap.setSource( "./orig/EffMap_T6bbWW_SRC1.txt", "txt", objectName = None, index = None, dataset="SRC1" )
T6bbWW_1.efficiencyMap.setStatistics( observedN=59, expectedBG=68, bgError=7 )
#----global url settings ----
T6bbWW_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/next'
#----efficiency map url settings ----
#T6bbWW_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T6bbWW_1.figure =
#T6bbWW_1.figureUrl =
#----limit source----
T6bbWW_1.efficiencyMap.setSource( "./orig/EffMap_T6bbWW_SRC2.txt", "txt", objectName = None, index = None, dataset="SRC2" )
T6bbWW_1.efficiencyMap.setStatistics( observedN=30, expectedBG=34, bgError=5 )
#----global url settings ----
T6bbWW_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1299143/next'
#----efficiency map url settings ----
#T6bbWW_1.efficiencyMap.dataUrl =
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
#T6bbWW_1.figure =
#T6bbWW_1.figureUrl =
#----limit source----
T6bbWW_1.efficiencyMap.setSource( "./orig/EffMap_T6bbWW_SRC3.txt", "txt", objectName = None, index = None, dataset="SRC3" )
T6bbWW_1.efficiencyMap.setStatistics( observedN=15, expectedBG=20.3, bgError=3.0 )
#----global url settings ----
T6bbWW_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1299143/next'
#----efficiency map url settings ----
#T6bbWW_1.efficiencyMap.dataUrl =
databaseCreator.create(True)



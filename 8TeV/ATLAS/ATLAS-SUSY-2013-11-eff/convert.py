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
info = MetaInfoInput('ATLAS-SUSY-2013-11')
info.comment = 'TSlepSlep efficiency maps created by the SModelS collaboration using MadAnalysis5'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP05(2014)071'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/'
#info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1403.5294'
info.contact = 'SModelS'
info.prettyName = 'ATLAS dilepton'
info.supersedes = 'ATLAS-CONF-2013-049'

#+++++++ next txName block ++++++++++++++
TSlepSlep = TxNameInput('TSlepSlep')
#TSlepSlep.on.checked =
#TSlepSlep.off.checked =
TSlepSlep.on.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
#TSlepSlep.off.constraint =
TSlepSlep.on.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
#TSlepSlep.off.conditionDescription =
TSlepSlep.on.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
#TSlepSlep.off.condition =

#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----exclusion source----
TSlepSlep_1.obsExclusion.setSource( "orig/exclusion_TSlepSlep.txt", "txt", objectName = None, index = None )
#TSlepSlep_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#TSlepSlep_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#TSlepSlep_1.expExclusion.setSource( path, type, objectName = None, index = None )
#TSlepSlep_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#TSlepSlep_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-90-SF.dat', 'txt', objectName = None, index = None, dataset="mT2-90-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=21, expectedBG=23.3, bgError=3.7 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create()

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-90-DF.dat', 'txt', objectName = None, index = None, dataset="mT2-90-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=33, expectedBG=38.2, bgError=5.1 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-120-SF.dat', 'txt', objectName = None, index = None, dataset="mT2-120-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=5, expectedBG=8.9, bgError=2.1 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-120-DF.dat', 'txt', objectName = None, index = None, dataset="mT2-120-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=5, expectedBG=3.6, bgError=1.2 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-150-SF.dat', 'txt', objectName = None, index = None, dataset="mT2-150-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=3, expectedBG=3.2, bgError=0.7 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_mT2-150-DF.dat', 'txt', objectName = None, index = None, dataset="mT2-150-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=2, expectedBG=1.0, bgError= 0.5)
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWa-SF.dat', 'txt', objectName = None, index = None, dataset="WWa-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=73, expectedBG=86.5, bgError=7.4 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWa-DF.dat', 'txt', objectName = None, index = None, dataset="WWa-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=70, expectedBG=73.6, bgError=7.9 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWb-SF.dat', 'txt', objectName = None, index = None, dataset="WWb-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=26, expectedBG=30.2, bgError=3.5 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWb-DF.dat', 'txt', objectName = None, index = None, dataset="WWb-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=17, expectedBG=18.1, bgError=2.6 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWc-SF.dat', 'txt', objectName = None, index = None, dataset="WWc-SF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=10, expectedBG=20.1, bgError=3.5 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_WWc-DF.dat', 'txt', objectName = None, index = None, dataset="WWc-DF" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=11, expectedBG=9.0, bgError=2.2 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TSlepSlep_1.figure =''
TSlepSlep_1.figureUrl =''
#----limit source----
TSlepSlep_1.efficiencyMap.setSource( 'orig/MA5_EM_Zjets.dat', 'txt', objectName = None, index = None, dataset="Zjets" )
TSlepSlep_1.efficiencyMap.setStatistics( observedN=1, expectedBG=1.4, bgError=0.6 )
#----global url settings ----
TSlepSlep_1.dataUrl =''
#----efficiency map url settings ----
TSlepSlep_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

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
info = MetaInfoInput('ATLAS-SUSY-2014-03-eff')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2014-03/'
info.sqrts = 8
info.lumi = 20.3 
#info.prettyName =
#info.private = False
info.arxiv = 'http://arxiv.org/abs/1501.01325'
#info.contact =
info.publication = 'http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.114.161801'
info.comment = ''
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
TScharm = TxNameInput('TScharm')
TScharm.on.checked = 'NO'
#TScharm.off.checked =
TScharm.on.constraint ="[[['c']],[['c']]]"
#TScharm.off.constraint =
TScharm.on.conditionDescription = "None"
#TScharm.off.conditionDescription =
TScharm.on.condition ='None'
#TScharm.off.condition =
#TScharm.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TScharm_1 = TScharm.addMassPlane(motherMass = x , lspMass = y )
#---- new efficiency map -----
#----figure----
TScharm_1.figure = 'Figure2'
TScharm_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1337472/thumb_figFigure2.png'
#----exclusion source----
TScharm_1.obsExclusion.setSource( 'orig/TScharm_Exclusion.txt', 'txt', objectName = None, index = None )
#TScharm_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#TScharm_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#TScharm_1.expExclusion.setSource( path, type, objectName = None, index = None )
#TScharm_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#TScharm_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
TScharm_1.efficiencyMap.setSource( 'orig/mCT150.dat', 'txt', objectName = None, index = None, dataset="mCT150" )
TScharm_1.efficiencyMap.setStatistics( observedN=19, expectedBG=30, bgError=6 )
#----global url settings ----
TScharm_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1337472/first'
#----efficiency map url settings ----
TScharm_1.efficiencyMap.dataUrl = ''
databaseCreator.create()

#---- new efficiency map -----
#----figure----
TScharm_1.figure = 'Figure9b'
TScharm_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1337472/figAuxiliaryFigure9b.png'
#----limit source----
TScharm_1.efficiencyMap.setSource( 'orig/mCT200.dat', 'txt', objectName = None, index = None, dataset="mCT200" )
TScharm_1.efficiencyMap.setStatistics( observedN=11, expectedBG=16, bgError=3 )
#----global url settings ----
TScharm_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1337472/first'
#----efficiency map url settings ----
TScharm_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
TScharm_1.figure = 'Figure9c'
TScharm_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1337472/figAuxiliaryFigure9c.png'
#----limit source----
TScharm_1.efficiencyMap.setSource( 'orig/mCT250.dat', 'txt', objectName = None, index = None, dataset="mCT250" )
TScharm_1.efficiencyMap.setStatistics( observedN=4, expectedBG=8.2, bgError=1.9 )
#----global url settings ----
TScharm_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1337472/first'
#----efficiency map url settings ----
TScharm_1.efficiencyMap.dataUrl =''
databaseCreator.create(True)



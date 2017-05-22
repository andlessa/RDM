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
info = MetaInfoInput('ATLAS-SUSY-2015-01')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/"
info.sqrts = 13
info.lumi = 3.2
info.prettyName = "2b"
info.private = False
info.arxiv =  'https://arxiv.org/abs/1606.08772v2'
info.contact = 'ATLAS collaboration'
info.publication ='http://link.springer.com/article/10.1140/epjc/s10052-016-4382-4'
#info.comment =
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked = ''
T2bb.off.checked =''
T2bb.on.constraint ="[[['b']],[['b']]]"
#T2bb.off.constraint = None
T2bb.on.conditionDescription = None
#T2bb.off.conditionDescription =
T2bb.on.condition = None
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass =x , lspMass =y )
#---- new efficiency map -----
#----figure----
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06b.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07b.png'
T2bb_1.figure = 'Fig.6b,Fig.7b'
#----exclusion source----
T2bb_1.obsExclusion.setSource( 'orig/T2bb_Obs_Excl.dat', 'txt', objectName = None, index = None )
#T2bb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T2bb_1.expExclusion.setSource( 'orig/T2bb_Exp_Excl.dat', 'txt', objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRA250.txt', 'txt', objectName = None, index = None, dataset="SRA250" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=23, expectedBG=29, bgError=5 )
#----global url settings ----
T2bb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/d28/input,http://hepdata.cedar.ac.uk/view/ins1472822/d33/input'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6c,Fig.7c'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06c.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07c.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRA350.txt', 'txt', objectName = None, index = None, dataset="SRA350" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=6, expectedBG=7, bgError=1.2 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d29/input,http://hepdata.cedar.ac.uk/view/ins1472822/d34/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6d,Fig.7d'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06d.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07d.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRA450.txt', 'txt', objectName = None, index = None, dataset="SRA450" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=1, expectedBG=1.8, bgError=0.4 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/d30/input,http://hepdata.cedar.ac.uk/view/ins1472822/d35/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6e,Fig.7e'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06e.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07e.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRB.txt', 'txt', objectName = None, index = None, dataset="SRB" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=6, expectedBG=12, bgError=2.5 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d31/input,http://hepdata.cedar.ac.uk/view/ins1472822/d36/input'
databaseCreator.create(True)



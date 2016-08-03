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
info = MetaInfoInput('ATLAS-SUSY-2013-15')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/"
info.sqrts = 8
info.lumi = 20.3
info.prettyName = "ATLAS (asymmetric) stop"
info.private = False
info.arxiv = "http://arxiv.org/abs/1407.0583"
info.contact = "ATLAS Collaboration"
info.publication = "http://link.springer.com/article/10.1007/JHEP11(2014)118"
info.comment = "Only T2tt 'can' be impl., but 1 SR EM is missing (3 are given out of 4). tNdiag is MET>150,mT>140 ."
info.supersedes = 'ATLAS-CONF-2013-037; CONF-2012-166'
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked = ""
#T2tt.off.checked =""
T2tt.on.constraint = "[[['t']],[['t']]]"
#T2tt.off.constraint =
T2tt.on.conditionDescription ="None"
#T2tt.off.conditionDescription =
T2tt.on.condition ="None"
#T2tt.off.condition =
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass =y )
#---- new efficiency map -----
#----figure----
#T2tt_1.figure = ""
#T2tt_1.figureUrl = "http://hepdata.cedar.ac.uk/resource/1304456/figAUXF23.png"
#----exclusion source----
T2tt_1.obsExclusion.setSource( "orig/exclusion_T2tt.txt", "txt", objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2tt_1.efficiencyMap.setSource( "orig/EffMap_T2tt_tNdiag.txt", "txt", objectName = None, index = None, dataset="tNdiag" )
T2tt_1.efficiencyMap.setStatistics( observedN=217, expectedBG=236, bgError=29 )
#----global url settings ----
T2tt_1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1304456"
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl ="http://hepdata.cedar.ac.uk/view/ins1304456/d65/input http://hepdata.cedar.ac.uk/view/ins1304456/d51/input"
databaseCreator.create()

#---- new efficiency map -----
#----figure----
#T2tt_1.figure =
#T2tt_1.figureUrl = "http://hepdata.cedar.ac.uk/view/ins1304456"
#----limit source----
T2tt_1.efficiencyMap.setSource( "orig/EffMap_T2tt_tNboost.txt", "txt", objectName = None, index = None, dataset="tNboost" )
T2tt_1.efficiencyMap.setStatistics( observedN=5, expectedBG=3.3, bgError=0.7 )
#----global url settings ----
T2tt_1.dataUrl ="http://hepdata.cedar.ac.uk/view/ins1304456"
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl ="http://hepdata.cedar.ac.uk/view/ins1304456/d67/input http://hepdata.cedar.ac.uk/view/ins1304456/d53/input"
databaseCreator.create(True)


#---- new efficiency map -----
#----figure----
#T2tt_1.figure =
#T2tt_1.figureUrl = "http://hepdata.cedar.ac.uk/view/ins1304456"
#----limit source----
T2tt_1.efficiencyMap.setSource( "orig/EffMap_T2tt_tNmed.txt", "txt", objectName = None, index = None, dataset="tNmed" )
T2tt_1.efficiencyMap.setStatistics( observedN=12, expectedBG=13, bgError=2.2 )
#----global url settings ----
T2tt_1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1304456"
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1304456/d66/input http://hepdata.cedar.ac.uk/view/ins1304456/d52/input"
databaseCreator.create(True)



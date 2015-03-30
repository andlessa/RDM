#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description =  
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
info = MetaInfoInput('ATLAS-SUSY-2013-02')
info.comment = 'T5WWLSP060 and T6WWLSP060 originally have xvalue on y-axes, changed by us to M2'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP09%282014%29176'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/'
#info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1405.7875'
#info.contact = 
info.prettyname =  "jets and met"
info.supersedes = 'ATLAS-CONF-2013-047'

#+++++++ next txName block ++++++++++++++
TGQ = TxNameInput('TGQ')
#TGQ.on.checked =
#TGQ.off.checked =
TGQ.on.constraint ="[[['jet']],[['jet','jet']]]"
# TGQ.off.constraint ="[[['jet','jet']],[['jet']]]"
#TGQ.off.constraint =
TGQ.on.condition ="None"
#TGQ.off.condition =
TGQ.on.fuzzycondition ="None"
#TGQ.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TGQ0 = TGQ.addMassPlane(motherMass = 0.96 * x, lspMass = y )
TGQ0.setBranch_1 ( motherMass = 0.96 * x, lspMass = y )
TGQ0.setBranch_2 ( motherMass = x, lspMass = y )
#----limit source----
TGQ0.obsUpperLimit.setSource( "orig/limit_TGQ.txt", "txt", objectName = None, index = None )
TGQ0.obsUpperLimit.unit = 'fb' 
# TGQ.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TGQ0.obsExclusion.setSource( "orig/exclusion_TGQ.txt", "txt", objectName = None, index = None )
#TGQ.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TGQ.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TGQ.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TGQ.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TGQ.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TGQ.dataUrl =
#TGQ.histoDataUrl =
#TGQ.exclusionDataUrl =
#----figure----
TGQ0.figure = "fig(aux) 9b"
TGQ0.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_09b.png"
#----limit url settings ----
#TGQ.obsUpperLimit.dataUrl =
#TGQ.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TGQ.obsExclusion.dataUrl =
#TGQ.obsExclusionM1.dataUrl =
#TGQ.obsExclusionP1.dataUrl =
#TGQ.expExclusion.dataUrl =
#TGQ.expExclusionM1.dataUrl =
#TGQ.expExclusionP1.dataUrl =

"""
#+++++++ next txName block ++++++++++++++
T6WW = TxNameInput('T6WW')
T6WW.on.checked =
T6WW.off.checked =
T6WW.on.constraint ="[[['jet'],['W']],[['jet'],['W']]]"
T6WW.off.constraint =
T6WW.on.condition ="None"
T6WW.off.condition =
T6WW.on.fuzzycondition ="None"
T6WW.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T6WWLSP060 = T6WW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T6WWLSP060.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6WWLSP060.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6WWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6WWLSP060.dataUrl =
T6WWLSP060.histoDataUrl =
T6WWLSP060.exclusionDataUrl =
#----figure----
T6WWLSP060.figure =
T6WWLSP060.figureUrl =
#----limit url settings ----
T6WWLSP060.obsUpperLimit.dataUrl =
T6WWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6WWLSP060.obsExclusion.dataUrl =
T6WWLSP060.obsExclusionM1.dataUrl =
T6WWLSP060.obsExclusionP1.dataUrl =
T6WWLSP060.expExclusion.dataUrl =
T6WWLSP060.expExclusionM1.dataUrl =
T6WWLSP060.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6WW050 = T6WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T6WW050.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6WW050.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6WW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6WW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6WW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6WW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6WW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6WW050.dataUrl =
T6WW050.histoDataUrl =
T6WW050.exclusionDataUrl =
#----figure----
T6WW050.figure =
T6WW050.figureUrl =
#----limit url settings ----
T6WW050.obsUpperLimit.dataUrl =
T6WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6WW050.obsExclusion.dataUrl =
T6WW050.obsExclusionM1.dataUrl =
T6WW050.obsExclusionP1.dataUrl =
T6WW050.expExclusion.dataUrl =
T6WW050.expExclusionM1.dataUrl =
T6WW050.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
#T2.on.checked =
#T2.off.checked =
T2.on.constraint ="[[['jet']],[['jet']]]"
#T2.off.constraint =
T2.on.condition ="None"
#T2.off.condition =
T2.on.fuzzycondition ="None"
#T2.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T2 = T2.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2.obsUpperLimit.setSource( "orig/limit_T2.txt", "txt", objectName = None, index = None )
T2.obsUpperLimit.unit = 'fb' 
#T2.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2.obsExclusion.setSource( "orig/exclusion_T2.txt", "txt", objectName = None, index = None )
#T2.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T2.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T2.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T2.dataUrl =
#T2.histoDataUrl =
#T2.exclusionDataUrl =
#----figure----
T2.figure = "Fig(aux) 8b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_08b.png"
#----limit url settings ----
"""
T2.obsUpperLimit.dataUrl =
T2.expUpperLimit.dataUrl =
#----exclusion url settings ----
T2.obsExclusion.dataUrl =
T2.obsExclusionM1.dataUrl =
T2.obsExclusionP1.dataUrl =
T2.expExclusion.dataUrl =
T2.expExclusionM1.dataUrl =
T2.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
#T1.on.checked =
#T1.off.checked =
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =
T1.on.condition ="None"
#T1.off.condition =
T1.on.fuzzycondition ="None"
#T1.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1 = T1.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1.obsUpperLimit.setSource( "orig/limit_T1.txt", "txt", objectName = None, index = None )
T1.obsUpperLimit.unit = 'fb' 
#T1.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1.obsExclusion.setSource( "orig/exclusion_T1.txt", "txt", objectName = None, index = None )
#T1.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T1.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T1.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T1.dataUrl =
#T1.histoDataUrl =
#T1.exclusionDataUrl =
#----figure----
T1.figure = "Fig(aux) 9a"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_09a.png"
#----limit url settings ----
#T1.obsUpperLimit.dataUrl =
#T1.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T1.obsExclusion.dataUrl =
#T1.obsExclusionM1.dataUrl =
#T1.obsExclusionP1.dataUrl =
#T1.expExclusion.dataUrl =
#T1.expExclusionM1.dataUrl =
#T1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
#T5WW.on.checked =
#T5WW.off.checked =
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
#T5WW.off.constraint =
T5WW.on.condition ="None"
#T5WW.off.condition =
T5WW.on.fuzzycondition ="None"
#T5WW.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5WWLSP060 = T5WW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T5WWLSP060.obsUpperLimit.setSource( "orig/limit_T5WWLSP060.txt", "txt", objectName = None, index = None )
#T5WWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WWLSP060.obsExclusion.setSource( "orig/exclusion_T5WWLSP060.txt", "txt", objectName = None, index = None )
#T5WWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T5WWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T5WWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T5WWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T5WWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T5WWLSP060.dataUrl =
#T5WWLSP060.histoDataUrl =
#T5WWLSP060.exclusionDataUrl =
#----figure----
T5WWLSP060.figure = "fig(aux) 10a"
T5WWLSP060.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_10a.png"
#----limit url settings ----
"""
T5WWLSP060.obsUpperLimit.dataUrl =
T5WWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WWLSP060.obsExclusion.dataUrl =
T5WWLSP060.obsExclusionM1.dataUrl =
T5WWLSP060.obsExclusionP1.dataUrl =
T5WWLSP060.expExclusion.dataUrl =
T5WWLSP060.expExclusionM1.dataUrl =
T5WWLSP060.expExclusionP1.dataUrl =
"""

"""
#+++++++ next mass plane block ++++++++++++++
T5WW050 = T5WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T5WW050.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WW050.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5WW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5WW050.dataUrl =
T5WW050.histoDataUrl =
T5WW050.exclusionDataUrl =
#----figure----
T5WW050.figure =
T5WW050.figureUrl =
#----limit url settings ----
T5WW050.obsUpperLimit.dataUrl =
T5WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WW050.obsExclusion.dataUrl =
T5WW050.obsExclusionM1.dataUrl =
T5WW050.obsExclusionP1.dataUrl =
T5WW050.expExclusion.dataUrl =
T5WW050.expExclusionM1.dataUrl =
T5WW050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5ttcc = TxNameInput('T5ttcc')
T5ttcc.on.checked =
T5ttcc.off.checked =
T5ttcc.on.constraint ="[[['t'],['jet']],[['t'],['jet']]]"
T5ttcc.off.constraint =
T5ttcc.on.condition ="None"
T5ttcc.off.condition =
T5ttcc.on.fuzzycondition ="None"
T5ttcc.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5ttccD020 = T5ttcc.addMassPlane(motherMass = x, interMass0 = y, lspMass = y + 20.0)
#----limit source----
T5ttccD020.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5ttccD020.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttccD020.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5ttccD020.dataUrl =
T5ttccD020.histoDataUrl =
T5ttccD020.exclusionDataUrl =
#----figure----
T5ttccD020.figure =
T5ttccD020.figureUrl =
#----limit url settings ----
T5ttccD020.obsUpperLimit.dataUrl =
T5ttccD020.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5ttccD020.obsExclusion.dataUrl =
T5ttccD020.obsExclusionM1.dataUrl =
T5ttccD020.obsExclusionP1.dataUrl =
T5ttccD020.expExclusion.dataUrl =
T5ttccD020.expExclusionM1.dataUrl =
T5ttccD020.expExclusionP1.dataUrl =
"""

databaseCreator.create()

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
info = MetaInfoInput('ATLAS-SUSY-2013-15')
info.comment = 'so far no data available -> no axes entry'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication =  'link.springer.com/article/10.1007/JHEP11(2014)118'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/'
# info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1407.0583'
info.contact =  "ATLAS collaboration"
info.prettyname = 'ATLAS (aysmmetric) stop'
info.supersedes = 'ATLAS-CONF-2013-037; CONF-2012-166'

#+++++++ next txName block ++++++++++++++
T2bbWW = TxNameInput('T2bbWW')
#T2bbWW.on.checked =
#T2bbWW.off.checked =
T2bbWW.on.constraint ="[[['b','W']],[['b','W']]]"
T2bbWW.off.constraint ="2.3*([[['b','L','nu']],[['b','jet','jet']]])"
T2bbWW.on.condition ="None"
T2bbWW.off.condition ="[[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','ta','nu']],[['b','jet','jet']]], [[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','e','nu']],[['b','jet','jet']]]"
T2bbWW.on.fuzzycondition ="None"
T2bbWW.off.fuzzycondition ="Cgtr([[['b','L','nu']],[['b','jet','jet']]],3.*[[['b','ta','nu']],[['b','jet','jet']]]);Cgtr([[['b','L','nu']],[['b','jet','jet']]],3.*[[['b','e','nu']],[['b','jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T2bbWW = T2bbWW.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2bbWW.obsUpperLimit.setSource( "orig/limit_T2bbWW.txt", "txt", objectName = None, index = None )
#T2bbWW.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2bbWW.obsExclusion.setSource( "orig/exclusion_T2bbWW.txt", "txt", objectName = None, index = None )
#T2bbWW.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T2bbWW.dataUrl =
#T2bbWW.histoDataUrl =
#T2bbWW.exclusionDataUrl =
#----figure----
T2bbWW.figure = 'Fig.(aux) 14'
T2bbWW.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_014.png'
#----limit url settings ----
T2bbWW.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304456/d4'
#T2bbWW.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T2bbWW.obsExclusion.dataUrl =
#T2bbWW.obsExclusionM1.dataUrl =
#T2bbWW.obsExclusionP1.dataUrl =
#T2bbWW.expExclusion.dataUrl =
#T2bbWW.expExclusionM1.dataUrl =
#T2bbWW.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked =
#T2tt.off.checked =
T2tt.on.constraint ="[[['t']],[['t']]]"
#T2tt.off.constraint =
T2tt.on.condition ="None"
#T2tt.off.condition =
T2tt.on.fuzzycondition ="None"
#T2tt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T2tt = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2tt.obsUpperLimit.setSource( "orig/limit_T2tt.txt", "txt", objectName = None, index = None )
#T2tt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2tt.obsExclusion.setSource( "orig/exclusion_T2tt.txt", "txt", objectName = None, index = None )
#T2tt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2tt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T2tt.dataUrl =
#T2tt.histoDataUrl =
#T2tt.exclusionDataUrl =
#----figure----
T2tt.figure = 'Fig.(aux) 13'
T2tt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_013.png'
#----limit url settings ----
T2tt.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304456/d1'
"""
T2tt.expUpperLimit.dataUrl =
#----exclusion url settings ----
T2tt.obsExclusion.dataUrl =
T2tt.obsExclusionM1.dataUrl =
T2tt.obsExclusionP1.dataUrl =
T2tt.expExclusion.dataUrl =
T2tt.expExclusionM1.dataUrl =
T2tt.expExclusionP1.dataUrl =
"""


#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
#T6bbWW.on.checked =
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="2.3*([[['b'],['L','nu']],[['b'],['jet','jet']]])"
T6bbWW.on.condition = "None"
T6bbWW.off.condition ="[[['b'],['L','nu']],[['b'],['jet','jet']]] > 2.7* [[['b'],['ta','nu']],[['b'],['jet','jet']]],[[['b'],['L','nu']],[['b'],['jet','jet']]] > 2.7* [[['b'],['e','nu']],[['b'],['jet','jet']]]"
T6bbWW.on.fuzzycondition = "None"
T6bbWW.off.fuzzycondition ="Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['ta','nu']],[['b'],['jet','jet']]]);Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['e','nu']],[['b'],['jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffD10 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x-10., lspMass = y)
#----limit source----
T6bbWWoffD10.obsUpperLimit.setSource( "orig/limit_T6bbWWoffD010.txt", "txt", objectName = None, index = None )
#T6bbWWoffD10.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffD10.obsExclusion.setSource( "orig/exclusion_T6bbWWoffD010.txt", "txt", objectName = None, index = None )
#T6bbWWoffD10.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD10.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD10.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD10.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD10.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWoffD10.dataUrl =
#T6bbWWoffD10.histoDataUrl =
#T6bbWWoffD10.exclusionDataUrl =
#----figure----
T6bbWWoffD10.figure = "fig(aux) 21"
T6bbWWoffD10.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_021.png"
#----limit url settings ----
"""
T6bbWWoffD10.obsUpperLimit.dataUrl =
T6bbWWoffD10.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffD10.obsExclusion.dataUrl =
T6bbWWoffD10.obsExclusionM1.dataUrl =
T6bbWWoffD10.obsExclusionP1.dataUrl =
T6bbWWoffD10.expExclusion.dataUrl =
T6bbWWoffD10.expExclusionM1.dataUrl =
T6bbWWoffD10.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffD5 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y+5., lspMass = y)
#----limit source----
T6bbWWoffD5.obsUpperLimit.setSource( "orig/limit_T6bbWWoffD005.txt", "txt", objectName = None, index = None )
#T6bbWWoffD5.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffD5.obsExclusion.setSource( "orig/exclusion_T6bbWWoffD005.txt", "txt", objectName = None, index = None )
#T6bbWWoffD5.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD5.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )#
#T6bbWWoffD5.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD5.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD5.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWoffD5.dataUrl =
#T6bbWWoffD5.histoDataUrl =
#T6bbWWoffD5.exclusionDataUrl =
#----figure----
T6bbWWoffD5.figure = "fig(aux) 19"
T6bbWWoffD5.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_019.png"
#----limit url settings ----
"""
T6bbWWoffD5.obsUpperLimit.dataUrl =
T6bbWWoffD5.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffD5.obsExclusion.dataUrl =
T6bbWWoffD5.obsExclusionM1.dataUrl =
T6bbWWoffD5.obsExclusionP1.dataUrl =
T6bbWWoffD5.expExclusion.dataUrl =
T6bbWWoffD5.expExclusionM1.dataUrl =
T6bbWWoffD5.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffD20 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y+20, lspMass = y)
#----limit source----
T6bbWWoffD20.obsUpperLimit.setSource( "orig/limit_T6bbWWoffD020.txt", "txt", objectName = None, index = None )
#T6bbWWoffD20.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffD20.obsExclusion.setSource( "orig/exclusion_T6bbWWoffD20.txt", "txt", objectName = None, index = None )
#T6bbWWoffD20.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD20.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD20.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD20.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffD20.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWoffD20.dataUrl =
#T6bbWWoffD20.histoDataUrl =
#T6bbWWoffD20.exclusionDataUrl =
#----figure----
T6bbWWoffD20.figure = "fig(aux) 20"
T6bbWWoffD20.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_020.png"
#----limit url settings ----
"""
T6bbWWoffD20.obsUpperLimit.dataUrl =
T6bbWWoffD20.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffD20.obsExclusion.dataUrl =
T6bbWWoffD20.obsExclusionM1.dataUrl =
T6bbWWoffD20.obsExclusionP1.dataUrl =
T6bbWWoffD20.expExclusion.dataUrl =
T6bbWWoffD20.expExclusionM1.dataUrl =
T6bbWWoffD20.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffM1300 = T6bbWW.addMassPlane(motherMass = 300, interMass0 = x, lspMass = y)
#----limit source----
T6bbWWoffM1300.obsUpperLimit.setSource( "orig/limit_T6bbWWoffM1300.txt", "txt", objectName = None, index = None )
#T6bbWWoffM1300.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffM1300.obsExclusion.setSource( "orig/exclusion_T6bbWWoffM1300.txt", "txt", objectName = None, index = None )
"""
T6bbWWoffM1300.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffM1300.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffM1300.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffM1300.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffM1300.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWWoffM1300.dataUrl =
T6bbWWoffM1300.histoDataUrl =
T6bbWWoffM1300.exclusionDataUrl =
#----figure----
"""
T6bbWWoffM1300.figure = "fig(aux) 22"
T6bbWWoffM1300.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_022.png"
"""
#----limit url settings ----
T6bbWWoffM1300.obsUpperLimit.dataUrl =
T6bbWWoffM1300.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffM1300.obsExclusion.dataUrl =
T6bbWWoffM1300.obsExclusionM1.dataUrl =
T6bbWWoffM1300.obsExclusionP1.dataUrl =
T6bbWWoffM1300.expExclusion.dataUrl =
T6bbWWoffM1300.expExclusionM1.dataUrl =
T6bbWWoffM1300.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffx200 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y * 2.0, lspMass = y)
#----limit source----
T6bbWWoffx200.obsUpperLimit.setSource( "orig/limit_T6bbWWoffx200.txt", "txt", objectName = None, index = None )
#T6bbWWoffx200.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffx200.obsExclusion.setSource( "orig/exclusion_T6bbWWoffx200.txt", "txt", objectName = None, index = None )
"""
T6bbWWoffx200.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffx200.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffx200.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffx200.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffx200.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWWoffx200.dataUrl =
T6bbWWoffx200.histoDataUrl =
T6bbWWoffx200.exclusionDataUrl =
#----figure----
"""
T6bbWWoffx200.figure = "fig(aux) 16"
T6bbWWoffx200.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_016.png"
#----limit url settings ----
"""
T6bbWWoffx200.obsUpperLimit.dataUrl =
T6bbWWoffx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffx200.obsExclusion.dataUrl =
T6bbWWoffx200.obsExclusionM1.dataUrl =
T6bbWWoffx200.obsExclusionP1.dataUrl =
T6bbWWoffx200.expExclusion.dataUrl =
T6bbWWoffx200.expExclusionM1.dataUrl =
T6bbWWoffx200.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffC106 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 106.0, lspMass = y)
#----limit source----
T6bbWWoffC106.obsUpperLimit.setSource( "orig/limit_T6bbWWoffC106.txt" , "txt", objectName = None, index = None )
#T6bbWWoffC106.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffC106.obsExclusion.setSource( "orig/exclusion_T6bbWWoffC106.txt", "txt", objectName = None, index = None )
"""
T6bbWWoffC106.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffC106.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffC106.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffC106.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffC106.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWWoffC106.dataUrl =
T6bbWWoffC106.histoDataUrl =
T6bbWWoffC106.exclusionDataUrl =
#----figure----
"""
T6bbWWoffC106.figure = "fig(aux) 18"
T6bbWWoffC106.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_018.png"
"""
#----limit url settings ----
T6bbWWoffC106.obsUpperLimit.dataUrl =
T6bbWWoffC106.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffC106.obsExclusion.dataUrl =
T6bbWWoffC106.obsExclusionM1.dataUrl =
T6bbWWoffC106.obsExclusionP1.dataUrl =
T6bbWWoffC106.expExclusion.dataUrl =
T6bbWWoffC106.expExclusionM1.dataUrl =
T6bbWWoffC106.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T6bbWWoffC150 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 150.0, lspMass = y)
#----limit source----
T6bbWWoffC150.obsUpperLimit.setSource( "orig/limit_T6bbWWoffC150.txt", "txt", objectName = None, index = None )
#T6bbWWoffC150.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffC150.obsExclusion.setSource( "orig/exclusion_T6bbWWoffC150.txt", "txt", objectName = None, index = None )
#T6bbWWoffC150.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffC150.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffC150.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffC150.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWoffC150.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWoffC150.dataUrl =
#T6bbWWoffC150.histoDataUrl =
#T6bbWWoffC150.exclusionDataUrl =
#----figure----
T6bbWWoffC150.figure = "fig(aux) 17"
T6bbWWoffC150.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-15/figaux_017.png"
#----limit url settings ----
"""
T6bbWWoffC150.obsUpperLimit.dataUrl =
T6bbWWoffC150.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffC150.obsExclusion.dataUrl =
T6bbWWoffC150.obsExclusionM1.dataUrl =
T6bbWWoffC150.obsExclusionP1.dataUrl =
T6bbWWoffC150.expExclusion.dataUrl =
T6bbWWoffC150.expExclusionM1.dataUrl =
T6bbWWoffC150.expExclusionP1.dataUrl =
"""

databaseCreator.create()

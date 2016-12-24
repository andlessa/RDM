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
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2013-19')
info.comment = 'T2tt UL are from DF channel only, no combined UL map available'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP06(2014)124'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/'
#info.supersededBy = 
info.arxiv = 'http://arxiv.org/abs/1403.4853'
#info.contact = 
info.prettyName = 'ATLAS stop dilepton'
info.supersedes = 'ATLAS-CONF-2013-048'

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked =
#T2tt.off.checked =
T2tt.on.constraint ="[[['t+']],[['t-']]]"
#T2tt.off.constraint =
T2tt.on.conditionDescription ="None"
#T2tt.off.conditionDescription =
T2tt.on.condition ="None"
#T2tt.off.condition =

#+++++++ next mass plane block ++++++++++++++
T2tt = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2tt.obsUpperLimit.setSource( "orig/T2tt.txt", "txt", objectName = None, index = None )
#T2tt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2tt.obsExclusion.setSource( "orig/exclusionline_T2tt_DF.txt", "txt", objectName = None, index = None )
#T2tt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2tt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2tt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
# T2tt.dataUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_10a.png"
T2tt.histoDataUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_10a.png"
#T2tt.exclusionDataUrl =
#----figure----
T2tt.figure = "fig 10a"
T2tt.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_10a.png"
#----limit url settings ----
#T2tt.obsUpperLimit.dataUrl = 
#T2tt.expUpperLimit.dataUrl =
#----exclusion url settings ----
T2tt.obsExclusion.dataUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/fig_10a.png"
#T2tt.obsExclusionM1.dataUrl =
#T2tt.obsExclusionP1.dataUrl =
#T2tt.expExclusion.dataUrl =
#T2tt.expExclusionM1.dataUrl =
#T2tt.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T2bbWW = TxNameInput('T2bbWW')
#T2bbWW.on.checked =
#T2bbWW.off.checked =
T2bbWW.on.constraint ="[[['b','W+']],[['b','W-']]]"
#T2bbWW.off.constraint =
T2bbWW.on.conditionDescription ="None"
#T2bbWW.off.conditionDescription =
T2bbWW.on.condition ="None"
#T2bbWW.off.condition =
#
##+++++++ next mass plane block ++++++++++++++
T2bbWW = T2bbWW.addMassPlane(motherMass = x, lspMass = y)
##----limit source----
T2bbWW.obsUpperLimit.setSource( "orig/T2bbWW.txt", "txt", objectName = None, index = None )
#T2bbWW.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T2bbWW.obsExclusion.setSource( "orig/exclusionline_T2bbWW.txt", "txt", objectName = None, index = None )
#T2bbWW.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T2bbWW.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T2bbWW.dataUrl = 
#T2bbWW.histoDataUrl =
# T2bbWW.exclusionDataUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_03e.png"
##----figure----
T2bbWW.figure = 'Fig.(aux) 3e'
T2bbWW.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_03e.png'
##----limit url settings ----
T2bbWW.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d42'
#T2bbWW.expUpperLimit.dataUrl =
##----exclusion url settings ----
T2bbWW.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d22'
#T2bbWW.obsExclusionM1.dataUrl =
T2bbWW.obsExclusionP1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d24'
T2bbWW.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d20'
#T2bbWW.expExclusionM1.dataUrl =
#T2bbWW.expExclusionP1.dataUrl =
#
##+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked ="VM"
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W+']],[['b'],['W-']]]"
T6bbWW.off.constraint ="22*([[['b'],['l+','nu']],[['b'],['l-','nu']]])"
T6bbWW.on.conditionDescription ="None"
T6bbWW.off.conditionDescription="[[['b'],['l+','nu']],[['b'],['l-','nu']]] > 2*[[['b'],['e+','nu']],[['b'],['e-','nu']]]"
T6bbWW.on.condition ="None"
T6bbWW.off.condition="Cgtr([[['b'],['l+','nu']],[['b'],['l-','nu']]],2*[[['b'],['e+','nu']],[['b'],['e-','nu']]])"
#
##+++++++ next mass plane block ++++++++++++++
T6bbWWLSP001 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 1.0)
##----limit source----
T6bbWWLSP001.obsUpperLimit.setSource( "orig/T6bbWWLSP001.txt", "txt", objectName = None, index = None )
#T6bbWWLSP001.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T6bbWWLSP001.obsExclusion.setSource( "orig/exclusionline_T6bbWWLSP001.txt", "txt", objectName = None, index = None )
#T6bbWWLSP001.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T6bbWWLSP001.dataUrl =
#T6bbWWLSP001.histoDataUrl =
#T6bbWWLSP001.exclusionDataUrl =
##----figure----
T6bbWWLSP001.figure = 'Fig.(aux) 3a'
T6bbWWLSP001.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_3a.png'
##----limit url settings ----
T6bbWWLSP001.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d30'
#T6bbWWLSP001.expUpperLimit.dataUrl =
##----exclusion url settings ----
T6bbWWLSP001.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d7'
#T6bbWWLSP001.obsExclusionM1.dataUrl =
T6bbWWLSP001.obsExclusionP1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d9'
T6bbWWLSP001.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d8'
#T6bbWWLSP001.expExclusionM1.dataUrl =
#T6bbWWLSP001.expExclusionP1.dataUrl =
#
##+++++++ next mass plane block ++++++++++++++
T6bbWWD010 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x - 10.0, lspMass = y)
##----limit source----
T6bbWWD010.obsUpperLimit.setSource( "orig/T6bbWWD010.txt", "txt", objectName = None, index = None )
#T6bbWWD010.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T6bbWWD010.obsExclusion.setSource( "orig/exclusionline_T6bbWWD10.txt", "txt", objectName = None, index = None )
#T6bbWWD010.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T6bbWWD010.dataUrl =
#T6bbWWD010.histoDataUrl =
#T6bbWWD010.exclusionDataUrl =
##----figure----
T6bbWWD010.figure = "fig(aux) 3b"
T6bbWWD010.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/figaux_3b.png'
##----limit url settings ----
#T6bbWWD010.obsUpperLimit.dataUrl =
#T6bbWWD010.expUpperLimit.dataUrl =
##----exclusion url settings ----
#T6bbWWD010.obsExclusion.dataUrl =
#T6bbWWD010.obsExclusionM1.dataUrl =
#T6bbWWD010.obsExclusionP1.dataUrl =
#T6bbWWD010.expExclusion.dataUrl =
#T6bbWWD010.expExclusionM1.dataUrl =
#T6bbWWD010.expExclusionP1.dataUrl =
#
##+++++++ next mass plane block ++++++++++++++
T6bbWWM1300 = T6bbWW.addMassPlane(motherMass = 300.0, interMass0 = x, lspMass = y)
##----limit source----
T6bbWWM1300.obsUpperLimit.setSource( "orig/T6bbWWM1300.txt", "txt", objectName = None, index = None )
#T6bbWWM1300.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T6bbWWM1300.obsExclusion.setSource( "orig/exclusionline_T6bbWWM1300.txt", "txt", objectName = None, index = None )
#T6bbWWM1300.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T6bbWWM1300.dataUrl =
#T6bbWWM1300.histoDataUrl =
#T6bbWWM1300.exclusionDataUrl =
##----figure----
T6bbWWM1300.figure = 'Fig.(aux) 3c'
T6bbWWM1300.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/fig_16.png'
##----limit url settings ----
T6bbWWM1300.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d36'
#T6bbWWM1300.expUpperLimit.dataUrl =
##----exclusion url settings ----
T6bbWWM1300.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d13'
#T6bbWWM1300.obsExclusionM1.dataUrl =
T6bbWWM1300.obsExclusionP1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d15'
T6bbWWM1300.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d14'
#T6bbWWM1300.expExclusionM1.dataUrl =
#T6bbWWM1300.expExclusionP1.dataUrl =
#
##+++++++ next mass plane block ++++++++++++++
T6bbWWC106 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 106.0, lspMass = y)
##----limit source----
T6bbWWC106.obsUpperLimit.setSource( "orig/T6bbWWC106.txt", "txt", objectName = None, index = None )
#T6bbWWC106.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T6bbWWC106.obsExclusion.setSource( "orig/exclusionline_T6bbWWC106.txt", "txt", objectName = None, index = None )
#T6bbWWC106.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC106.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC106.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC106.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC106.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T6bbWWC106.dataUrl =
#T6bbWWC106.histoDataUrl =
#T6bbWWC106.exclusionDataUrl =
##----figure----
T6bbWWC106.figure = 'Fig.(aux) 3f'
T6bbWWC106.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/fig_20.png'
##----limit url settings ----
T6bbWWC106.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d68'
#T6bbWWC106.expUpperLimit.dataUrl =
##----exclusion url settings ----
T6bbWWC106.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d25'
#T6bbWWC106.obsExclusionM1.dataUrl =
T6bbWWC106.obsExclusionP1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d27'
T6bbWWC106.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d26'
#T6bbWWC106.expExclusionM1.dataUrl =
#T6bbWWC106.expExclusionP1.dataUrl =
#
##+++++++ next mass plane block ++++++++++++++
T6bbWWx200 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y * 2.0, lspMass = y)
##----limit source----
T6bbWWx200.obsUpperLimit.setSource( "orig/T6bbWWx200.txt", "txt", objectName = None, index = None )
#T6bbWWx200.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
T6bbWWx200.obsExclusion.setSource( "orig/exclusionline_T6bbWWx200.txt", "txt", objectName = None, index = None )
#T6bbWWx200.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#T6bbWWx200.dataUrl =
#T6bbWWx200.histoDataUrl =
#T6bbWWx200.exclusionDataUrl =
##----figure----
T6bbWWx200.figure = 'Fig.(aux) 3d'
T6bbWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-19/fig_17.png'
##----limit url settings ----
T6bbWWx200.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d39'
#T6bbWWx200.expUpperLimit.dataUrl =
##----exclusion url settings ----
T6bbWWx200.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d16'
#T6bbWWx200.obsExclusionM1.dataUrl =
T6bbWWx200.obsExclusionP1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d18'
T6bbWWx200.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286444/d17'
#T6bbWWx200.expExclusionM1.dataUrl =
#T6bbWWx200.expExclusionP1.dataUrl =

databaseCreator.create()

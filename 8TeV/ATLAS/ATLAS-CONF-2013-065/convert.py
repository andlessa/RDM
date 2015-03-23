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
info = MetaInfoInput('ATLAS-CONF-2013-065')
info.comment = 'T6bbWWM1300 combines the T6bbWW result from ATLAS-CONF-2013-065 and from ATLAS-CONF-2013-048'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-065/ http://cds.cern.ch/record/1562840'
info.superseded_by =  "SUSY-2013-19"
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS dileptonic stop'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked ="VM"
#T2tt.off.checked =
T2tt.on.constraint ="[[['t+']],[['t-']]]"
#T2tt.off.constraint =
T2tt.on.condition ="None"
#T2tt.off.condition =
T2tt.on.fuzzycondition ="None"
#T2tt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T2tt = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2tt.obsUpperLimit.setSource( "orig/T2ttOF.data", "txt", objectName = None, index = None )
#T2tt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2tt.obsExclusion.setSource( "orig/exclusion_T2tt.txt", "txt", objectName = None, index = None )
"""
T2tt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T2tt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T2tt.expExclusion.setSource( path, filetype, objectName = None, index = None )
T2tt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T2tt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T2tt.dataUrl =
T2tt.histoDataUrl =
T2tt.exclusionDataUrl =
"""
#----figure----
T2tt.figure = 'Fig. 7a'
T2tt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-065/fig_07a.png'
#----limit url settings ----
T2tt.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-065/fig_07a_PRELIMINARY.data'
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
T6bbWW.on.checked ="VM"
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W+']],[['b'],['W-']]]"
T6bbWW.off.constraint ="9.18*([[['b'],['L-','nu']],[['b'],['L+','nu']]])"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="[[['b'],['L','nu']],[['b'],['jet','> 2.7* [[['b'],['ta','nu']],[['b'],['jet','jet']]],[[['b'],['L','nu']],[jet','jet']]] > 2.7* [[['b'],['e','nu']],[['b'],['jet','jet']]]"
T6bbWW.on.fuzzycondition ="None"
T6bbWW.off.fuzzycondition ="Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['ta','nu']],[['b'],['jet','jet']]]);Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['e','nu']],[['b'],['jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T6bbWWM1300 = T6bbWW.addMassPlane(motherMass = 300.0, interMass0 = x, lspMass = y)
#----limit source----
T6bbWWM1300.obsUpperLimit.setSource( "orig/T6bbWWCombination.data","txt", objectName = None, index = None )
#T6bbWWM1300.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWM1300.obsExclusion.setSource( "orig/exclusion_T6bbWWM1300.txt", "txt", objectName = None, index = None )
#T6bbWWM1300.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWM1300.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWM1300.dataUrl =
#T6bbWWM1300.histoDataUrl =
#T6bbWWM1300.exclusionDataUrl =
#----figure----
T6bbWWM1300.figure = 'Fig. 11'
T6bbWWM1300.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-065/fig_11.png'
#----limit url settings ----
T6bbWWM1300.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-065/fig_11_PRELIMINARY.data'
#T6bbWWM1300.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWM1300.obsExclusion.dataUrl =
#T6bbWWM1300.obsExclusionM1.dataUrl =
#T6bbWWM1300.obsExclusionP1.dataUrl =
#T6bbWWM1300.expExclusion.dataUrl =
#T6bbWWM1300.expExclusionM1.dataUrl =
#T6bbWWM1300.expExclusionP1.dataUrl =

databaseCreator.create()

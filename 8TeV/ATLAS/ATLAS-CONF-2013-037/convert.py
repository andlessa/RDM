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
info = MetaInfoInput('ATLAS-CONF-2013-037')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-037/'
info.supersededBy = 'ATLAS-SUSY-2013-15'
# info.arxiv = 
info.contact = 'Sophio Pataria <Sophio.Pataraia@cern.ch>, Tobias Golling <tobias.golling@cern.ch>'
info.prettyName = 'ATLAS leptonic stop'
info.supersedes = 'ATLAS-CONF-2012-166'

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked ="A"
#T2tt.off.checked =
T2tt.on.constraint ="[[['t']],[['t']]]"
#T2tt.off.constraint =
T2tt.on.conditionDescription ="None"
#T2tt.off.conditionDescription =
T2tt.on.condition ="None"
#T2tt.off.condition =

#+++++++ next mass plane block ++++++++++++++
T2tt = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2tt.obsUpperLimit.setSource( "orig/T2tt_corr.txt", "txt", objectName = None, index = None )
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
T2tt.figure = 'Fig. 4'
T2tt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-037/figaux_04.png'
#----limit url settings ----
#T2tt.obsUpperLimit.dataUrl =
#T2tt.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T2tt.obsExclusion.dataUrl =
#T2tt.obsExclusionM1.dataUrl =
#T2tt.obsExclusionP1.dataUrl =
#T2tt.expExclusion.dataUrl =
#T2tt.expExclusionM1.dataUrl =
#T2tt.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
#T6bbWW.on.checked ="A"
#T6bbWW.off.checked ="A"
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="3.5*([[['b'],['L','nu']],[['b'],['jet','jet']]])"
T6bbWW.on.conditionDescription ="None"
T6bbWW.off.conditionDescription ="[[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','ta','nu']],[['b','jet','jet']]], [[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','e','nu']],[['b','jet','jet']]]"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['ta','nu']],[['b'],['jet','jet']]]);Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['e','nu']],[['b'],['jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T6bbWWC150 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 150.0, lspMass = y)
#----limit source----
T6bbWWC150.obsUpperLimit.setSource( "orig/T6bbWWC150_corr.txt", "txt", objectName = None, index = None )
#T6bbWWC150.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWC150.obsExclusion.setSource( "orig/exclusion_T6bbWWC150.txt", "txt", objectName = None, index = None )
#T6bbWWC150.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC150.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC150.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC150.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWC150.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWC150.dataUrl =
#T6bbWWC150.histoDataUrl =
#T6bbWWC150.exclusionDataUrl =
#----figure----
T6bbWWC150.figure = 'Fig.(aux) 5'
T6bbWWC150.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-037/figaux_05.png'
#----limit url settings ----
#T6bbWWC150.obsUpperLimit.dataUrl =
#T6bbWWC150.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWC150.obsExclusion.dataUrl =
#T6bbWWC150.obsExclusionM1.dataUrl =
#T6bbWWC150.obsExclusionP1.dataUrl =
#T6bbWWC150.expExclusion.dataUrl =
#T6bbWWC150.expExclusionM1.dataUrl =
#T6bbWWC150.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWx200 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y * 2.0, lspMass = y)
#----limit source----
T6bbWWx200.obsUpperLimit.setSource( "orig/T6bbWWx200_corr.txt", "txt", objectName = None, index = None )
# T6bbWWx200.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWx200.obsExclusion.setSource( "orig/exclusion_T6bbWWx200.txt", "txt", objectName = None, index = None )
#T6bbWWx200.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWx200.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWx200.dataUrl =
#T6bbWWx200.histoDataUrl =
#T6bbWWx200.exclusionDataUrl =
#----figure----
T6bbWWx200.figure = 'Fig.(aux) 6'
T6bbWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-037/figaux_06.png'
#----limit url settings ----
#T6bbWWx200.obsUpperLimit.dataUrl =
#T6bbWWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWx200.obsExclusion.dataUrl =
#T6bbWWx200.obsExclusionM1.dataUrl =
#T6bbWWx200.obsExclusionP1.dataUrl =
#T6bbWWx200.expExclusion.dataUrl =
#T6bbWWx200.expExclusionM1.dataUrl =
#T6bbWWx200.expExclusionP1.dataUrl =

databaseCreator.create()

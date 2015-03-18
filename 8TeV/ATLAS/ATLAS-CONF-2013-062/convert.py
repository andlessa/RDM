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
info = MetaInfoInput('ATLAS-CONF-2013-062')
info.comment = 'T5WWLSP060 and T6WWLSP060 originally have xvalue on y-axes, changed by us to M2'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.0'
info.publication =  'SUSY-2013-20'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/ http://cds.cern.ch/record/1557779'
#info.superseded_by = 
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS soft leptons'
#info.supersedes = 

"""
#+++++++ next txName block ++++++++++++++
T6WW = TxNameInput('T6WW')
T6WW.on.checked ="VM"
#T6WW.off.checked =
T6WW.on.constraint ="[[['jet'],['W']],[['jet'],['W']]]"
#T6WW.off.constraint =
T6WW.on.condition ="None"
#T6WW.off.condition =
T6WW.on.fuzzycondition ="None"
#T6WW.off.fuzzycondition =

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
T6WWLSP060.figure = 'Fig 14b'
T6WWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_14b.png'
#----limit url settings ----
T6WWLSP060.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_14b_PRELIMINARY.data'
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
T6WW050.figure = 'Fig. 13b'
T6WW050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_13b.png'
#----limit url settings ----
T6WW050.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_13b_PRELIMINARY.data'
T6WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6WW050.obsExclusion.dataUrl =
T6WW050.obsExclusionM1.dataUrl =
T6WW050.obsExclusionP1.dataUrl =
T6WW050.expExclusion.dataUrl =
T6WW050.expExclusionM1.dataUrl =
T6WW050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked =
T6bbWW.off.checked ="VM"
T6bbWW.on.constraint =
T6bbWW.off.constraint ="[[['b'],['L','nu']],[['b'],['L','nu']]] + [[['b'],['L','nu']],[['b'],['jet','jet']]] + [[['b'],['jet','jet']],[['b'],['jet','jet']]]"
T6bbWW.on.condition =
T6bbWW.off.condition ="None"
T6bbWW.on.fuzzycondition =
T6bbWW.off.fuzzycondition ="None"

#+++++++ next mass plane block ++++++++++++++
T6bbWWD020 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y + 20.0, lspMass = y)
#----limit source----
T6bbWWoffD020.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffD020.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD020.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWWoffD020.dataUrl =
T6bbWWoffD020.histoDataUrl =
T6bbWWoffD020.exclusionDataUrl =
#----figure----
T6bbWWoffD020.figure =
T6bbWWoffD020.figureUrl =
#----limit url settings ----
T6bbWWoffD020.obsUpperLimit.dataUrl =
T6bbWWoffD020.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffD020.obsExclusion.dataUrl =
T6bbWWoffD020.obsExclusionM1.dataUrl =
T6bbWWoffD020.obsExclusionP1.dataUrl =
T6bbWWoffD020.expExclusion.dataUrl =
T6bbWWoffD020.expExclusionM1.dataUrl =
T6bbWWoffD020.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWD005 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y + 5.0, lspMass = y)
#----limit source----
T6bbWWoffD005.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWoffD005.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6bbWWoffD005.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWWoffD005.dataUrl =
T6bbWWoffD005.histoDataUrl =
T6bbWWoffD005.exclusionDataUrl =
#----figure----
T6bbWWoffD005.figure =
T6bbWWoffD005.figureUrl =
#----limit url settings ----
T6bbWWoffD005.obsUpperLimit.dataUrl =
T6bbWWoffD005.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6bbWWoffD005.obsExclusion.dataUrl =
T6bbWWoffD005.obsExclusionM1.dataUrl =
T6bbWWoffD005.obsExclusionP1.dataUrl =
T6bbWWoffD005.expExclusion.dataUrl =
T6bbWWoffD005.expExclusionM1.dataUrl =
T6bbWWoffD005.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked ="VM"
#T5WW.off.checked =
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint ="2.3 * [[['jet','jet'],['L','nu']],[['jet','jet'],['jet','jet']]]"
T5WW.on.condition ="None"
T5WW.off.condition = "[[['jet','jet'],['L','nu']],[['jet','jet'],['jet','jet']]] > 2.7* [[['jet','jet'],['ta','nu']],[['jet','jet'],['jet','jet']]], [[['jet','jet'],['L','nu']],[['jet','jet'],['jet','jet']]] > 2.7* [[['jet','jet'],['e','nu']],[['jet','jet'],['jet','jet']]]" 
T5WW.on.fuzzycondition ="None"
T5WW.off.fuzzycondition = "Cgtr([[['jet','jet'],['L','nu']],[['jet','jet'],['jet','jet']]],3.*[[['jet','jet'],['ta','nu']],[['jet','jet'],['jet','jet']]]);Cgtr([[['jet','jet'],['L','nu']],[['jet','jet'],['jet','jet']]],3.*[[['jet','jet'],['e','nu']],[['jet','jet'],['jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T5WW050 = T5WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T5WW050.obsUpperLimit.setSource( "orig/Fig13a.txt", "txt", objectName = None, index = None )
#T5WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WW050.obsExclusion.setSource( "orig/exclusion_T5WW.txt", "txt", objectName = None, index = None )
#T5WW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T5WW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T5WW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T5WW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T5WW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T5WW050.dataUrl =
#T5WW050.histoDataUrl =
#T5WW050.exclusionDataUrl =
#----figure----
T5WW050.figure = 'Fig. 13a'
T5WW050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_13a.png'
#----limit url settings ----
T5WW050.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_13a_PRELIMINARY.data'
"""
T5WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WW050.obsExclusion.dataUrl =
T5WW050.obsExclusionM1.dataUrl =
T5WW050.obsExclusionP1.dataUrl =
T5WW050.expExclusion.dataUrl =
T5WW050.expExclusionM1.dataUrl =
T5WW050.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T5WWLSP060 = T5WW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T5WWLSP060.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WWLSP060.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5WWLSP060.dataUrl =
T5WWLSP060.histoDataUrl =
T5WWLSP060.exclusionDataUrl =
#----figure----
T5WWLSP060.figure = 'Fig. 14a'
T5WWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_14a.png'
#----limit url settings ----
T5WWLSP060.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/fig_14a_PRELIMINARY.data'
T5WWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WWLSP060.obsExclusion.dataUrl =
T5WWLSP060.obsExclusionM1.dataUrl =
T5WWLSP060.obsExclusionP1.dataUrl =
T5WWLSP060.expExclusion.dataUrl =
T5WWLSP060.expExclusionM1.dataUrl =
T5WWLSP060.expExclusionP1.dataUrl =
"""

databaseCreator.create()

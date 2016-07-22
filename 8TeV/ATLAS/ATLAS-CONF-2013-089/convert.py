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
info = MetaInfoInput('ATLAS-CONF-2013-089')
info.comment = 'T5WWLSP060 and T6WWLSP060 originally have xvalue on y-axes, changed by us to M2 - there are more topologies (with more then three masses). Will be superseeded by ATLAS-SUSY-2013-20'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/ https://cds.cern.ch/record/1595272'
#info.supersededBy =  "ATLAS-SUSY-2013-20"
#info.arxiv = 
#info.contact = 
info.prettyName = '2l'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T6WW = TxNameInput('T6WW')
T6WW.on.checked ="VM"
#T6WW.off.checked =
T6WW.on.constraint ="[[['jet'],['W+']],[['jet'],['W-']]]"
T6WW.off.constraint = "9.48*[[['jet'],['L+','nu']],[['jet'],['L-','nu']]]"
T6WW.on.conditionDescription ="None"
T6WW.off.conditionDescription = "[[['jet'],['L+','nu']],[['jet'],['L-','nu']]] > 9 * [[['jet'],['ta+','nu']],[['jet'],['ta-','nu']]]"
T6WW.on.condition ="None"
T6WW.off.condition = "Cgtr([[['jet'],['L','nu']],[['jet'],['L','nu']]], 3 * [[['jet'],['ta','nu']],[['jet'],['L','nu']]]); Cgtr([[['jet'],['L','nu']],[['jet'],['L','nu']]], 3 * [[['jet'],['e','nu']],[['jet'],['L','nu']]])"

#+++++++ next mass plane block ++++++++++++++
T6WW050 = T6WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T6WW050.obsUpperLimit.setSource( "orig/T6WW050.data", "txt", objectName = None, index = None )
#T6WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6WW050.obsExclusion.setSource( "orig/exclusion_T6WW050.txt", "txt", objectName = None, index = None )
#T6WW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6WW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6WW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6WW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6WW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6WW050.dataUrl =
#T6WW050.histoDataUrl =
#T6WW050.exclusionDataUrl =
#----figure----
T6WW050.figure = 'Fig. 22a'
T6WW050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22a.png'
#----limit url settings ----
T6WW050.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22a_PRELIMINARY.data'
#T6WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6WW050.obsExclusion.dataUrl =
#T6WW050.obsExclusionM1.dataUrl =
#T6WW050.obsExclusionP1.dataUrl =
#T6WW050.expExclusion.dataUrl =
#T6WW050.expExclusionM1.dataUrl =
#T6WW050.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6WWLSP060 = T6WW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T6WWLSP060.obsUpperLimit.setSource( "orig/T6WWLSP060corr.data", "txt", objectName = None, index = None )
# T6WWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6WWLSP060.obsExclusion.setSource( "orig/exclusion_T6WWLSP060.corr.txt", "txt", objectName = None, index = None )
# T6WWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
# T6WWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
# T6WWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
# T6WWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
# T6WWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
# T6WWLSP060.dataUrl =
# T6WWLSP060.histoDataUrl =
# T6WWLSP060.exclusionDataUrl =
#----figure----
T6WWLSP060.figure = 'Fig. 23b'
T6WWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_23b.png'
#----limit url settings ----
T6WWLSP060.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_23b_PRELIMINARY.data'
"""
T6WWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6WWLSP060.obsExclusion.dataUrl =
T6WWLSP060.obsExclusionM1.dataUrl =
T6WWLSP060.obsExclusionP1.dataUrl =
T6WWLSP060.expExclusion.dataUrl =
T6WWLSP060.expExclusionM1.dataUrl =
T6WWLSP060.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked ="VM"
#T5WW.off.checked =
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint ="9.48*[[['jet','jet'],['L','nu']],[['jet','jet'],['L','nu']]]"
T5WW.on.conditionDescription ="None"
T5WW.off.conditionDescription = "[[['jet','jet'],['L','nu']],[['jet','jet'],['L','nu']]] > 9 * [[['jet','jet'],['ta','nu']],[['jet','jet'],['ta','nu']]]"
T5WW.on.condition ="None"
T5WW.off.condition = "Cgtr([[['jet','jet'],['L','nu']],[['jet','jet'],['L','nu']]], 3 * [[['jet','jet'],['ta','nu']],[['jet','jet'],['L','nu']]]); Cgtr([[['jet','jet'],['L','nu']],[['jet','jet'],['L','nu']]], 3 * [[['jet','jet'],['e','nu']],[['jet','jet'],['L','nu']]])"
#T5WW.off.condition =

#+++++++ next mass plane block ++++++++++++++
T5WWLSP060 = T5WW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T5WWLSP060.obsUpperLimit.setSource( "orig/T5WWLSP060corr.data", "txt", objectName = None, index = None )
#T5WWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WWLSP060.obsExclusion.setSource( "orig/exclusion_T5WWLSP060.corr.txt", "txt", objectName = None, index = None )
"""
T5WWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5WWLSP060.dataUrl =
T5WWLSP060.histoDataUrl =
T5WWLSP060.exclusionDataUrl =
"""
#----figure----
T5WWLSP060.figure = 'Fig (aux). 22b'
T5WWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22b.png'
#----limit url settings ----
T5WWLSP060.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22b_PRELIMINARY.data'
"""
T5WWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WWLSP060.obsExclusion.dataUrl =
T5WWLSP060.obsExclusionM1.dataUrl =
T5WWLSP060.obsExclusionP1.dataUrl =
T5WWLSP060.expExclusion.dataUrl =
T5WWLSP060.expExclusionM1.dataUrl =
T5WWLSP060.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
T5WW050 = T5WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T5WW050.obsUpperLimit.setSource( "orig/T5WW050.data", "txt", objectName = None, index = None )
#T5WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WW050.obsExclusion.setSource( "orig/exclusion_T5WW050.txt", "txt", objectName = None, index = None )
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
T5WW050.figure = 'Fig. 22a'
T5WW050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22a.png'
#----limit url settings ----
T5WW050.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-089/fig_22a_PRELIMINARY.data'
"""
T5WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WW050.obsExclusion.dataUrl =
T5WW050.obsExclusionM1.dataUrl =
T5WW050.obsExclusionP1.dataUrl =
T5WW050.expExclusion.dataUrl =
T5WW050.expExclusionM1.dataUrl =
T5WW050.expExclusionP1.dataUrl =
"""

databaseCreator.create()

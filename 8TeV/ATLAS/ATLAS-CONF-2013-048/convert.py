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
info = MetaInfoInput('ATLAS-CONF-2013-048')
info.comment = 'T6bbWWM1300 can also be found in ATLAS-CONF-2013-065 as combination'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/ http://cds.cern.ch/record/1547564'
info.supersededBy = 'ATLAS-SUSY-2013-19'
#info.arxiv = 
#info.contact = 
info.prettyName = 'ATLAS dileptonic stop'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T2bbWW = TxNameInput('T2bbWW')
T2bbWW.on.checked ="VM"
#T2bbWW.off.checked =
T2bbWW.on.constraint ="[[['b','W+']],[['b','W-']]]"
#T2bbWW.off.constraint =
T2bbWW.on.conditionDescription ="None"
#T2bbWW.off.conditionDescription =
T2bbWW.on.condition ="None"
#T2bbWW.off.condition =

#+++++++ next mass plane block ++++++++++++++
T2bbWW = T2bbWW.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2bbWW.obsUpperLimit.setSource( "orig/T2bbWW.dat", "txt", objectName = None, index = None )
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
T2bbWW.figure = 'Fig. 13f'
T2bbWW.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13f.png'
#----limit url settings ----
#T2bbWW.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13f_PRELIMINARY.data'
#T2bbWW.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T2bbWW.obsExclusion.dataUrl =
#T2bbWW.obsExclusionM1.dataUrl =
#T2bbWW.obsExclusionP1.dataUrl =
#T2bbWW.expExclusion.dataUrl =
#T2bbWW.expExclusionM1.dataUrl =
#T2bbWW.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked ="VM"
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W+']],[['b'],['W-']]]"
T6bbWW.off.constraint = "9.18*([[['b'],['L-','nu']],[['b'],['L+','nu']]])"
T6bbWW.on.conditionDescription ="None"
T6bbWW.off.conditionDescription = "None"
T6bbWW.on.condition ="None"
T6bbWW.off.condition = "None"

#+++++++ next mass plane block ++++++++++++++
T6bbWWLSP001 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 1.0)
#----limit source----
T6bbWWLSP001.obsUpperLimit.setSource( "orig/T6bbWWLSP001.dat", "txt", objectName = None, index = None )
#T6bbWWLSP001.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWLSP001.obsExclusion.setSource( "orig/exclusion_T6bbWWLSP001.txt", "txt", objectName = None, index = None )
#T6bbWWLSP001.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWLSP001.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWLSP001.dataUrl =
#T6bbWWLSP001.histoDataUrl =
#T6bbWWLSP001.exclusionDataUrl =
#----figure----
T6bbWWLSP001.figure = 'Fig. 13a'
T6bbWWLSP001.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13a.png'
#----limit url settings ----
T6bbWWLSP001.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13a_PRELIMINARY.data'
#T6bbWWLSP001.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWLSP001.obsExclusion.dataUrl =
#T6bbWWLSP001.obsExclusionM1.dataUrl =
#T6bbWWLSP001.obsExclusionP1.dataUrl =
#T6bbWWLSP001.expExclusion.dataUrl =
#T6bbWWLSP001.expExclusionM1.dataUrl =
#T6bbWWLSP001.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWC150 = T6bbWW.addMassPlane(motherMass = x, interMass0 = 150.0, lspMass = y)
#----limit source----
T6bbWWC150.obsUpperLimit.setSource( "orig/T6bbWWC150.dat", "txt", objectName = None, index = None )
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
T6bbWWC150.figure = 'Fig. 13e'
T6bbWWC150.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13e.png'
#----limit url settings ----
T6bbWWC150.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13e_PRELIMINARY.data'
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
T6bbWWx200.obsUpperLimit.setSource( "orig/T6bbWWx200.dat", "txt", objectName = None, index = None )
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
T6bbWWx200.figure = 'Fig. 13b'
T6bbWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13b.png'
#----limit url settings ----
T6bbWWx200.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13b_PRELIMINARY.data'
#T6bbWWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWx200.obsExclusion.dataUrl =
#T6bbWWx200.obsExclusionM1.dataUrl =
#T6bbWWx200.obsExclusionP1.dataUrl =
#T6bbWWx200.expExclusion.dataUrl =
#T6bbWWx200.expExclusionM1.dataUrl =
#T6bbWWx200.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWD010 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x - 10.0, lspMass = y)
#----limit source----
T6bbWWD010.obsUpperLimit.setSource( "orig/T6bbWWD010.dat", "txt", objectName = None, index = None )
# T6bbWWD010.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6bbWWD010.obsExclusion.setSource( "orig/exclusion_T6bbWWD010.txt", "txt", objectName = None, index = None )
#T6bbWWD010.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWWD010.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T6bbWWD010.dataUrl =
#T6bbWWD010.histoDataUrl =
#T6bbWWD010.exclusionDataUrl =
#----figure----
T6bbWWD010.figure = "fig 13c"
T6bbWWD010.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13c.png"
#----limit url settings ----
#T6bbWWD010.obsUpperLimit.dataUrl =
#T6bbWWD010.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWD010.obsExclusion.dataUrl =
#T6bbWWD010.obsExclusionM1.dataUrl =
#T6bbWWD010.obsExclusionP1.dataUrl =
#T6bbWWD010.expExclusion.dataUrl =
#T6bbWWD010.expExclusionM1.dataUrl =
#T6bbWWD010.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWM1300 = T6bbWW.addMassPlane(motherMass = 300.0, interMass0 = x, lspMass = y)
#----limit source----
T6bbWWM1300.obsUpperLimit.setSource( "orig/T6bbWWM1300.dat", "txt", objectName = None, index = None )
# T6bbWWM1300.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
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
T6bbWWM1300.figure = 'Fig. 13d'
T6bbWWM1300.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13d.png'
#----limit url settings ----
T6bbWWM1300.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-048/fig_13d_PRELIMINARY.data'
#T6bbWWM1300.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWM1300.obsExclusion.dataUrl =
#T6bbWWM1300.obsExclusionM1.dataUrl =
#T6bbWWM1300.obsExclusionP1.dataUrl =
#T6bbWWM1300.expExclusion.dataUrl =
#T6bbWWM1300.expExclusionM1.dataUrl =
#T6bbWWM1300.expExclusionP1.dataUrl =

databaseCreator.create()

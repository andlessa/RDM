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
info = MetaInfoInput('ATLAS-CONF-2013-053')
info.comment = 'More data in ATLAS-SUSY-2013-05'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.1'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-053/'
info.supersededBy = 'ATLAS-SUSY-2013-05'
#info.arxiv = 
#info.contact = 
info.prettyName = 'ATLAS 2 b + \slash{E}_{T}'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked ="VM"
#T2bb.off.checked =
T2bb.on.constraint ="[[['b']],[['b']]]"
#T2bb.off.constraint =
T2bb.on.conditionDescription ="None"
#T2bb.off.conditionDescription =
T2bb.on.condition ="None"
#T2bb.off.condition =

#+++++++ next mass plane block ++++++++++++++
T2bb = T2bb.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2bb.obsUpperLimit.setSource( "orig/Fig4.txt", "txt", objectName = None, index = None )
#T2bb.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T2bb.obsExclusion.setSource( "orig/exclusion_T2bb.txt", "txt", objectName = None, index = None )
"""
T2bb.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T2bb.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T2bb.expExclusion.setSource( path, filetype, objectName = None, index = None )
T2bb.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T2bb.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T2bb.dataUrl =
T2bb.histoDataUrl =
T2bb.exclusionDataUrl =
"""
#----figure----
T2bb.figure = 'Fig.(aux) 4'
T2bb.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-053/fig_05a.png'
"""
#----limit url settings ----
T2bb.obsUpperLimit.dataUrl =
T2bb.expUpperLimit.dataUrl =
#----exclusion url settings ----
T2bb.obsExclusion.dataUrl =
T2bb.obsExclusionM1.dataUrl =
T2bb.obsExclusionP1.dataUrl =
T2bb.expExclusion.dataUrl =
T2bb.expExclusionM1.dataUrl =
T2bb.expExclusionP1.dataUrl =
"""

databaseCreator.create()

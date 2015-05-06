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
info = MetaInfoInput('ATLAS-CONF-2013-093')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
# info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-093/'
info.supersededBy =  'SUSY-2013-23'
#info.arxiv = 
#info.contact = 
info.prettyName = 'ATLAS ew higgs'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
TChiWH.on.checked ="VM"
#TChiWH.off.checked =
TChiWH.on.constraint ="[[['higgs']],[['W']]]"
#TChiWH.off.constraint =
TChiWH.on.conditionDescription ="None"
#TChiWH.off.conditionDescription =
TChiWH.on.condition ="None"
# TChiWH.off.condition =

#+++++++ next mass plane block ++++++++++++++
TChiWH = TChiWH.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWH.obsUpperLimit.setSource( "orig/TChiWH.dat", "txt", objectName = None, index = None )
#TChiWH.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiWH.obsExclusion.setSource( "orig/TChiWH_exc.dat", "txt", objectName = None, index = None )
#TChiWH.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWH.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiWH.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiWH.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWH.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiWH.dataUrl =
#TChiWH.histoDataUrl =
#TChiWH.exclusionDataUrl =
#----figure----
TChiWH.figure = "fig 10"
TChiWH.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-093/fig_10.png" 
#----limit url settings ----
"""
TChiWH.obsUpperLimit.dataUrl =
TChiWH.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiWH.obsExclusion.dataUrl =
TChiWH.obsExclusionM1.dataUrl =
TChiWH.obsExclusionP1.dataUrl =
TChiWH.expExclusion.dataUrl =
TChiWH.expExclusionM1.dataUrl =
TChiWH.expExclusionP1.dataUrl =
"""

databaseCreator.create()

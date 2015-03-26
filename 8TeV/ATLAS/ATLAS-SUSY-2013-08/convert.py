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
info = MetaInfoInput('ATLAS-SUSY-2013-08')
info.comment = ""
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1140/epjc/s10052-014-2883-6'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-08/'
info.superseded_by = ""
info.arxiv = 'http://arxiv.org/abs/1403.5222'
info.contact = "ATLAS collaboration"
info.prettyname = 'ATLAS heavy stop'
info.supersedes = 'ATLAS-CONF-2013-025'

#+++++++ next txName block ++++++++++++++
T6ZZtt = TxNameInput('T6ZZtt')
#T6ZZtt.on.checked = 
#T6ZZtt.off.checked =
T6ZZtt.on.constraint ="[[['Z'],['t']],[['Z'],['t']]]"
#T6ZZtt.off.constraint = None
T6ZZtt.on.condition ="None"
#T6ZZtt.off.condition =
T6ZZtt.on.fuzzycondition ="None"
#T6ZZtt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T6ZZttD180 = T6ZZtt.addMassPlane(motherMass = x, interMass0 = y + 180.0, lspMass = y)
#----limit source----
T6ZZttD180.obsUpperLimit.setSource( "orig/limit_T6ZZtt.txt" , "txt", objectName = None, index = None )
T6ZZttD180.obsUpperLimit.unit = 'fb'
#T6ZZttD180.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6ZZttD180.obsExclusion.setSource( "orig/exclusion_T6ZZtt.txt", "txt", objectName = None, index = None )
T6ZZttD180.obsExclusionM1.setSource( "orig/exclusionm1_T6ZZtt.txt", "txt", objectName = None, index = None )
T6ZZttD180.obsExclusionP1.setSource( "orig/exclusionp1_T6ZZtt.txt", "txt", objectName = None, index = None )
T6ZZttD180.expExclusion.setSource( "orig/expectexclusion_T6ZZtt.txt", "txt", objectName = None, index = None )
T6ZZttD180.expExclusionM1.setSource( "orig/expectexclusionm1_T6ZZtt.txt", "txt", objectName = None, index = None )
T6ZZttD180.expExclusionP1.setSource( "orig/expectexclusionp1_T6ttZZ.txt", "txt", objectName = None, index = None )
#----global url settings ----
# T6ZZttD180.dataUrl = ""
# T6ZZttD180.histoDataUrl =
# T6ZZttD180.exclusionDataUrl =
#----figure----
T6ZZttD180.figure = "Fig 6"
T6ZZttD180.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-08/figaux_06.png"
##----limit url settings ----
#T6ZZttD180.obsUpperLimit.dataUrl =
#T6ZZttD180.expUpperLimit.dataUrl =
##----exclusion url settings ----
#T6ZZttD180.obsExclusion.dataUrl = 
#T6ZZttD180.obsExclusionM1.dataUrl =
#T6ZZttD180.obsExclusionP1.dataUrl =
#T6ZZttD180.expExclusion.dataUrl =
#T6ZZttD180.expExclusionM1.dataUrl =
#T6ZZttD180.expExclusionP1.dataUrl =

databaseCreator.create()

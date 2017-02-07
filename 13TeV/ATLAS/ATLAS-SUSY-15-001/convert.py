#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
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
info = MetaInfoInput('ATLAS-SUSY-15-001')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/"
info.sqrts = 13
info.lumi = 3.2
info.prettyName = "2b"
info.private = False
info.arxiv =  'https://arxiv.org/abs/1606.08772v2'
info.contact = 'ATLAS collaboration'
info.publication ='http://link.springer.com/article/10.1140/epjc/s10052-016-4382-4'
#info.comment =
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked = ''
T2bb.off.checked =''
T2bb.on.constraint ="[[['b']],[['b']]]"
#T2bb.off.constraint = None
T2bb.on.conditionDescription = None
#T2bb.off.conditionDescription =
T2bb.on.condition = None
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x , lspMass =y )
#----figure----
T2bb_1.figure = 'Fig.4'
T2bb_1.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/.thumb_fig_04.png'
#----limit source----
T2bb_1.obsUpperLimit.setSource( 'orig/T2bb_Obs_UL.dat', 'txt', objectName = None, index = None )
#T2bb_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2bb_1.obsExclusion.setSource( 'orig/T2bb_Obs_Excl.dat', 'txt', objectName = None, index = None )
#T2bb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T2bb_1.expExclusion.setSource( 'orig/T2bb_Exp_Excl.dat', 'txt', objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2bb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d4/input'
#----limit url settings ----
T2bb_1.histoDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d4/input'
T2bb_1.obsUpperLimit.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/d4/input'
#T2bb_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2bb_1.exclusionDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d4/input'
T2bb_1.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d2/input'
#T2bb_1.obsExclusionM1.dataUrl =
#T2bb_1.obsExclusionP1.dataUrl =
T2bb_1.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d1/input'
#T2bb_1.expExclusionM1.dataUrl =
#T2bb_1.expExclusionP1.dataUrl =

databaseCreator.create()

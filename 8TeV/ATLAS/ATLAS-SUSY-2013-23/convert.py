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
info = MetaInfoInput('ATLAS-SUSY-2013-23')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-23/'
info.sqrts = 8
info.lumi = 20.3
info.prettyName = 'ATLAS ew higgs'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1501.07110'
#info.contact =''
info.publication = 'http://link.springer.com/article/10.1140/epjc/s10052-015-3408-7'
info.comment = "Used combined limit"
info.supersedes = 'ATLAS-CONF-2013-093'
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
TChiWH.on.checked =''
#TChiWH.off.checked =''
TChiWH.on.constraint = "[[['higgs']],[['W']]]"
#TChiWH.off.constraint =
TChiWH.on.conditionDescription = None
#TChiWH.off.conditionDescription =
TChiWH.on.condition = None
#TChiWH.off.condition =
#TChiWH.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiWH_1 = TChiWH.addMassPlane(motherMass = x, lspMass = y)
#----figure----
TChiWH_1.figure = 'Fig. Aux1'
TChiWH_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-23/.thumb_fig_08d.png'
#----limit source----
TChiWH_1.obsUpperLimit.setSource( 'orig/TChiWH-ATLAS-SUSY-2013-23-UL.dat', 'txt', objectName = None, index = None )
#TChiWH_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiWH_1.obsExclusion.setSource( 'orig/TChiWH-ATLAS-SUSY-2013-23-Obs_Excl.dat', 'txt', objectName = None, index = None )
#TChiWH_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#TChiWH_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
TChiWH_1.expExclusion.setSource( 'orig/TChiWH-ATLAS-SUSY-2013-23-Exp_Excl.dat', 'txt', objectName = None, index = None )
#TChiWH_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#TChiWH_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
TChiWH_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1341609'
#----limit url settings ----
TChiWH_1.histoDataUrl ='http://hepdata.cedar.ac.uk/view/ins1341609'
TChiWH_1.obsUpperLimit.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1341609/d34/input'
#TChiWH_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiWH_1.exclusionDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1341609'
TChiWH_1.obsExclusion.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1341609/d33/input'
#TChiWH_1.obsExclusionM1.dataUrl =
#TChiWH_1.obsExclusionP1.dataUrl =
TChiWH_1.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1341609/d32/input'
#TChiWH_1.expExclusionM1.dataUrl =
#TChiWH_1.expExclusionP1.dataUrl =

databaseCreator.create()

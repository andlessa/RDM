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
info = MetaInfoInput('ATLAS-SUSY-2015-09')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-09/'
info.sqrts = 13
info.lumi = 3.2
info.prettyName = '2 SS or 3 lep'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1602.09058'
info.contact = ''
info.publication = ''
info.comment =''
# info.supersedes ='None'
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked = ''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription = None
T1tttt.off.conditionDescription = None
T1tttt.on.condition = None
T1tttt.off.condition = None
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure = 'Fig 4.d'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-09/.thumb_fig_04d.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/ UL-ATLAS-SUSY-2015-09.dat', 'txt', objectName = None, index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_ATLAS-SUSY-2015-09-Obs_Excl.dat', 'txt', objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1424844/all'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1424844/all'
T1tttt_1.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1424844/all'
#T1tttt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1424844/all'
T1tttt_1.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1424844/all'
#T1tttt_1.obsExclusionM1.dataUrl =
#T1tttt_1.obsExclusionP1.dataUrl =
#T1tttt_1.expExclusion.dataUrl =
#T1tttt_1.expExclusionM1.dataUrl =
#T1tttt_1.expExclusionP1.dataUrl =

databaseCreator.create()

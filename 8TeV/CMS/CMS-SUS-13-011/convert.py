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
info = MetaInfoInput('CMS-SUS-13-011')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
info.sqrts = 8
info.lumi = 19.5
info.prettyName = ''
info.private = False
info.arxiv = 'arXiv:1308.1586v2'
info.contact =''
info.publication = 'Eur. Phys. J. C 73 (2013) 2677'
info.comment = ''
info.supersedes =''
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint ="[[['W','b']],[['W','b']]]"
T2tt.on.conditionDescription ="None"
T2tt.off.conditionDescription ="None"
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T2tt_1.figure = '20a'
T2tt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/fig20a.pdf'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/topneutralino_cutbased.root', 'root', objectName = 'xsec_upperlimit', index = None )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/SUS13011_T2tt_exclusion.txt', 'txt', objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( 'orig/topneutralino_cutbased.root', 'root', objectName = 'expected_exclusion', index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
T2tt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.root'
#T2tt_1.expUpperlimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.root'
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.C'
T2tt_1.obsExclusion.dataUrl = ''
T2tt_1.obsExclusionM1.dataUrl =''
T2tt_1.obsExclusionP1.dataUrl =''
T2tt_1.expExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.C'
T2tt_1.expExclusionM1.dataUrl =''
T2tt_1.expExclusionP1.dataUrl =''

'''
#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked =
T6bbWW.off.checked =
T6bbWW.on.constraint =
T6bbWW.off.constraint =
T6bbWW.on.conditionDescription =
T6bbWW.off.conditionDescription =
T6bbWW.on.condition =
T6bbWW.off.condition =
#T6bbWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T6bbWW_1 = T6bbWW.addMassPlane(motherMass = , interMass0 = , lspMass = )
#T6bbWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_1.figure =
T6bbWW_1.figureUrl =
#----limit source----
T6bbWW_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
T6bbWW_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_1.obsExclusion.setSource( path, type, objectName = None, index = None )
T6bbWW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
T6bbWW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T6bbWW_1.expExclusion.setSource( path, type, objectName = None, index = None )
T6bbWW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
T6bbWW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_1.dataUrl =
#----limit url settings ----
T6bbWW_1.histoDataUrl =
T6bbWW_1.obsUpperLimit.dataUrl =
T6bbWW_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T6bbWW_1.exclusionDataUrl =
T6bbWW_1.obsExclusion.dataUrl =
T6bbWW_1.obsExclusionM1.dataUrl =
T6bbWW_1.obsExclusionP1.dataUrl =
T6bbWW_1.expExclusion.dataUrl =
T6bbWW_1.expExclusionM1.dataUrl =
T6bbWW_1.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWW_2 = T6bbWW.addMassPlane(motherMass = , interMass0 = , lspMass = )
#T6bbWW_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_2.figure =
T6bbWW_2.figureUrl =
#----limit source----
T6bbWW_2.obsUpperLimit.setSource( path, type, objectName = None, index = None )
T6bbWW_2.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_2.obsExclusion.setSource( path, type, objectName = None, index = None )
T6bbWW_2.obsExclusionM1.setSource( path, type, objectName = None, index = None )
T6bbWW_2.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T6bbWW_2.expExclusion.setSource( path, type, objectName = None, index = None )
T6bbWW_2.expExclusionM1.setSource( path, type, objectName = None, index = None )
T6bbWW_2.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_2.dataUrl =
#----limit url settings ----
T6bbWW_2.histoDataUrl =
T6bbWW_2.obsUpperLimit.dataUrl =
T6bbWW_2.expUpperlimit.dataUrl =
#----exclusion url settings ----
T6bbWW_2.exclusionDataUrl =
T6bbWW_2.obsExclusion.dataUrl =
T6bbWW_2.obsExclusionM1.dataUrl =
T6bbWW_2.obsExclusionP1.dataUrl =
T6bbWW_2.expExclusion.dataUrl =
T6bbWW_2.expExclusionM1.dataUrl =
T6bbWW_2.expExclusionP1.dataUrl =
'''
databaseCreator.create()

#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt, txname.txt, twiki.txt and sms.py.

.. moduleauthor:: Michael Traub <michael.traub@gmx.at>

"""   
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', \
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
from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfo('CMS-SUS-14-011')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14011'
info.sqrts = 8
info.lumi = 19.3
info.prettyname = 'razor'
info.private = False
#info.arxiv = 
info.contact = 'jduarte@caltech.edu, maurizio.pierini@cern.ch, r.lucas11@imperial.ac.uk'
#info.publication =
info.comment = 'combination of SUS13004 and SUS13011'
info.supersedes = 'CMS-PAS-SUS-13-004'
#info.superseded_by =

#+++++++ next txName block ++++++++++++++
T4tbW = TxName('T4tbW')
#T4tbW.on.checked =
#T4tbW.off.checked =
T4tbW.on.constraint = "[[['b'],['W']],[['t']]]"
T4tbW.off.constraint = "not yet assigned"
#T4tbW.on.condition =
T4tbW.off.condition = "not yet assigned"
#T4tbW.on.fuzzycondition =
T4tbW.off.fuzzycondition = "not yet assigned"

#+++++++ next mass plane block ++++++++++++++
T4tbW_1 = T4tbW.addMassPlane(motherMass = x, interMass0 = y + 5., lspMass = y)
T4tbW_1.setBranch_2(motherMass = x, lspMass = y)
#----figure----
T4tbW_1.figure = 'Fig. 5'
T4tbW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/T2tbHybridNew0Lp1Lp2LXSEC.pdf'
#----limit source----
T4tbW_1.obsUpperLimit.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Obs_xsec_T2tb_0Lp1Lp2L' )
T4tbW_1.expUpperLimit.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Exp_xsec_T2tb_0Lp1Lp2L' )
#----exclusion source----
T4tbW_1.obsExclusion.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Obs_contour_T2tb_0Lp1Lp2L' )
#T4tbW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T4tbW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T4tbW_1.expExclusion.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Exp_contour_T2tb_0Lp1Lp2L' )
T4tbW_1.expExclusionM1.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'ExpPlus_contour_T2tb_0Lp1Lp2L' )
T4tbW_1.expExclusionP1.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'ExpMinus_contour_T2tb_0Lp1Lp2L' )
#----global url settings ----
#T4tbW_1.dataUrl =
#----limit url settings ----
T4tbW_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
#T4tbW_1.obsUpperLimit.dataUrl =
#T4tbW_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
#T4tbW_1.exclusionDataUrl =
T4tbW_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
#T4tbW_1.obsExclusionM1.dataUrl =
#T4tbW_1.obsExclusionP1.dataUrl =
T4tbW_1.expExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T4tbW_1.expExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T4tbW_1.expExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'

##+++++++ next txName block ++++++++++++++
#T1tttt = TxName('T1tttt')
#T1tttt.on.checked =
#T1tttt.off.checked =
#T1tttt.on.constraint =
#T1tttt.off.constraint =
#T1tttt.on.condition =
#T1tttt.off.condition =
#T1tttt.on.fuzzycondition =
#T1tttt.off.fuzzycondition =
##T1tttt.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T1tttt_1 = T1tttt.addMassPlane(motherMass = , lspMass = )
##----figure----
#T1tttt_1.figure =
#T1tttt_1.figureUrl =
##----limit source----
#T1tttt_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T1tttt_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T1tttt_1.dataUrl =
##----limit url settings ----
#T1tttt_1.histoDataUrl =
#T1tttt_1.obsUpperLimit.dataUrl =
#T1tttt_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T1tttt_1.exclusionDataUrl =
#T1tttt_1.obsExclusion.dataUrl =
#T1tttt_1.obsExclusionM1.dataUrl =
#T1tttt_1.obsExclusionP1.dataUrl =
#T1tttt_1.expExclusion.dataUrl =
#T1tttt_1.expExclusionM1.dataUrl =
#T1tttt_1.expExclusionP1.dataUrl =

##+++++++ next txName block ++++++++++++++
#T5tbtbWW = TxName('T5tbtbWW')
#T5tbtbWW.on.checked =
#T5tbtbWW.off.checked =
#T5tbtbWW.on.constraint =
#T5tbtbWW.off.constraint =
#T5tbtbWW.on.condition =
#T5tbtbWW.off.condition =
#T5tbtbWW.on.fuzzycondition =
#T5tbtbWW.off.fuzzycondition =
##T5tbtbWW.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T5tbtbWW_1 = T5tbtbWW.addMassPlane(motherMass = , interMass0 = , lspMass = )
##T5tbtbWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
##----figure----
#T5tbtbWW_1.figure =
#T5tbtbWW_1.figureUrl =
##----limit source----
#T5tbtbWW_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T5tbtbWW_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5tbtbWW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T5tbtbWW_1.dataUrl =
##----limit url settings ----
#T5tbtbWW_1.histoDataUrl =
#T5tbtbWW_1.obsUpperLimit.dataUrl =
#T5tbtbWW_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T5tbtbWW_1.exclusionDataUrl =
#T5tbtbWW_1.obsExclusion.dataUrl =
#T5tbtbWW_1.obsExclusionM1.dataUrl =
#T5tbtbWW_1.obsExclusionP1.dataUrl =
#T5tbtbWW_1.expExclusion.dataUrl =
#T5tbtbWW_1.expExclusionM1.dataUrl =
#T5tbtbWW_1.expExclusionP1.dataUrl =

##+++++++ next txName block ++++++++++++++
#T2tt = TxName('T2tt')
#T2tt.on.checked =
#T2tt.off.checked =
#T2tt.on.constraint =
#T2tt.off.constraint =
#T2tt.on.condition =
#T2tt.off.condition =
#T2tt.on.fuzzycondition =
#T2tt.off.fuzzycondition =
##T2tt.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T2tt_1 = T2tt.addMassPlane(motherMass = , lspMass = )
##----figure----
#T2tt_1.figure =
#T2tt_1.figureUrl =
##----limit source----
#T2tt_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T2tt_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T2tt_1.dataUrl =
##----limit url settings ----
#T2tt_1.histoDataUrl =
#T2tt_1.obsUpperLimit.dataUrl =
#T2tt_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T2tt_1.exclusionDataUrl =
#T2tt_1.obsExclusion.dataUrl =
#T2tt_1.obsExclusionM1.dataUrl =
#T2tt_1.obsExclusionP1.dataUrl =
#T2tt_1.expExclusion.dataUrl =
#T2tt_1.expExclusionM1.dataUrl =
#T2tt_1.expExclusionP1.dataUrl =

##+++++++ next txName block ++++++++++++++
#T1bbbb = TxName('T1bbbb')
#T1bbbb.on.checked =
#T1bbbb.off.checked =
#T1bbbb.on.constraint =
#T1bbbb.off.constraint =
#T1bbbb.on.condition =
#T1bbbb.off.condition =
#T1bbbb.on.fuzzycondition =
#T1bbbb.off.fuzzycondition =
##T1bbbb.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T1bbbb_1 = T1bbbb.addMassPlane(motherMass = , lspMass = )
##----figure----
#T1bbbb_1.figure =
#T1bbbb_1.figureUrl =
##----limit source----
#T1bbbb_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T1bbbb_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T1bbbb_1.dataUrl =
##----limit url settings ----
#T1bbbb_1.histoDataUrl =
#T1bbbb_1.obsUpperLimit.dataUrl =
#T1bbbb_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T1bbbb_1.exclusionDataUrl =
#T1bbbb_1.obsExclusion.dataUrl =
#T1bbbb_1.obsExclusionM1.dataUrl =
#T1bbbb_1.obsExclusionP1.dataUrl =
#T1bbbb_1.expExclusion.dataUrl =
#T1bbbb_1.expExclusionM1.dataUrl =
#T1bbbb_1.expExclusionP1.dataUrl =

##+++++++ next txName block ++++++++++++++
#T3tbbbW = TxName('T3tbbbW')
#T3tbbbW.on.checked =
#T3tbbbW.off.checked =
#T3tbbbW.on.constraint =
#T3tbbbW.off.constraint =
#T3tbbbW.on.condition =
#T3tbbbW.off.condition =
#T3tbbbW.on.fuzzycondition =
#T3tbbbW.off.fuzzycondition =
##T3tbbbW.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T3tbbbW_1 = T3tbbbW.addMassPlane(motherMass = , interMass0 = , lspMass = )
##T3tbbbW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
##----figure----
#T3tbbbW_1.figure =
#T3tbbbW_1.figureUrl =
##----limit source----
#T3tbbbW_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T3tbbbW_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T3tbbbW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T3tbbbW_1.dataUrl =
##----limit url settings ----
#T3tbbbW_1.histoDataUrl =
#T3tbbbW_1.obsUpperLimit.dataUrl =
#T3tbbbW_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T3tbbbW_1.exclusionDataUrl =
#T3tbbbW_1.obsExclusion.dataUrl =
#T3tbbbW_1.obsExclusionM1.dataUrl =
#T3tbbbW_1.obsExclusionP1.dataUrl =
#T3tbbbW_1.expExclusion.dataUrl =
#T3tbbbW_1.expExclusionM1.dataUrl =
#T3tbbbW_1.expExclusionP1.dataUrl =

##+++++++ next txName block ++++++++++++++
#T3tttbW = TxName('T3tttbW')
#T3tttbW.on.checked =
#T3tttbW.off.checked =
#T3tttbW.on.constraint =
#T3tttbW.off.constraint =
#T3tttbW.on.condition =
#T3tttbW.off.condition =
#T3tttbW.on.fuzzycondition =
#T3tttbW.off.fuzzycondition =
##T3tttbW.branchingRatio =

##+++++++ next mass plane block ++++++++++++++
#T3tttbW_1 = T3tttbW.addMassPlane(motherMass = , interMass0 = , lspMass = )
##T3tttbW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
##----figure----
#T3tttbW_1.figure =
#T3tttbW_1.figureUrl =
##----limit source----
#T3tttbW_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
##----exclusion source----
#T3tttbW_1.obsExclusion.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T3tttbW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
#T3tttbW_1.dataUrl =
##----limit url settings ----
#T3tttbW_1.histoDataUrl =
#T3tttbW_1.obsUpperLimit.dataUrl =
#T3tttbW_1.expUpperlimit.dataUrl =
##----exclusion url settings ----
#T3tttbW_1.exclusionDataUrl =
#T3tttbW_1.obsExclusion.dataUrl =
#T3tttbW_1.obsExclusionM1.dataUrl =
#T3tttbW_1.obsExclusionP1.dataUrl =
#T3tttbW_1.expExclusion.dataUrl =
#T3tttbW_1.expExclusionM1.dataUrl =
#T3tttbW_1.expExclusionP1.dataUrl =

databaseCreator.create()

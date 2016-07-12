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
info = MetaInfoInput('CMS-SUS-PAS-14-011')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14011'
info.sqrts = 8
info.lumi = 19.3
info.prettyName = "RAZOR"
info.private = False
info.arxiv = ""
info.contact = ""
info.publication = ""
info.comment = 'Only PAS document https://cms-physics.web.cern.ch/cms-physics/public/SUS-14-011-pas.pdf'
info.supersedes = 'CMS-SUS-13-004'
info.supersededBy = ''

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked =''
T1bbbb.off.checked =''
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription = None
#T1bbbb.off.conditionDescription =
T1bbbb.on.condition = None
#T1bbbb.off.condition =
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure = 'Fig. 4'
T1bbbb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/T1bbbbHybridNew0LXSEC.pdf'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Obs_xsec_T1bbbb_0L', index = None )
T1bbbb_1.expUpperLimit.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Exp_xsec_T1bbbb_0L', index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Obs_contour_T1bbbb_0L', index = None )
T1bbbb_1.expExclusion.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Exp_contour_T1bbbb_0L', index = None )
T1bbbb_1.expExclusionP1.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'ExpPlus_contour_T1bbbb_0L', index = None )
T1bbbb_1.expExclusionP1.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'ExpMinus_contour_T1bbbb_0L', index = None )
#T1bbbb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14011'
#----limit url settings ----
T1bbbb_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1bbbb_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1bbbb_1.expUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1bbbb_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
#T1bbbb_1.obsExclusionM1.dataUrl =
#T1bbbb_1.obsExclusionP1.dataUrl =
T1bbbb_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1bbbb_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1bbbb_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint =  "[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription = None
T2tt.off.conditionDescription = None
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure = 'Fig. 5'
T2tt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/T2ttHybridNew0Lp1Lp2LXSEC.pdf'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Obs_xsec_T2tt_0Lp1Lp2L', index = None)
T2tt_1.expUpperLimit.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Exp_xsec_T2tt_0Lp1Lp2L', index = None)
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'Obs_contour_T2tt_0Lp1Lp2L', index = None)
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T2tt_1.expExclusion.setSource( 'orig/StopLimitsRazor2014.root', 'root',   objectName = 'Exp_contour_T2tt_0Lp1Lp2L', index = None )
T2tt_1.expExclusionM1.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'ExpMinus_contour_T2tt_0Lp1Lp2L', index = None )
T2tt_1.expExclusionP1.setSource( 'orig/StopLimitsRazor2014.root', 'root', objectName = 'ExpPlus_contour_T2tt_0Lp1Lp2L', index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14011'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T2tt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T2tt_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T2tt_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
#T2tt_1.obsExclusionM1.dataUrl =
#T2tt_1.obsExclusionP1.dataUrl =
T2tt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T2tt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'
T2tt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/StopLimitsRazor2014.root'

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription = None
T1tttt.off.conditionDescription =None
T1tttt.on.condition = None
T1tttt.off.condition =None
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T1tttt_1.figure = 'Fig. 4'
T1tttt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/T1ttttHybridNew0Lp1Lp2LXSEC.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Obs_xsec_T1tttt_0Lp1Lp2L', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Exp_xsec_T1tttt_0Lp1Lp2L', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Obs_contour_T1tttt_0Lp1Lp2L', index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T1tttt_1.expExclusion.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'Exp_contour_T1tttt_0Lp1Lp2L', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'ExpMinus_contour_T1tttt_0Lp1Lp2L', index = None  )
T1tttt_1.expExclusionP1.setSource( 'orig/GluinoLimitsRazor2014.root', 'root', objectName = 'ExpPlus_contour_T1tttt_0Lp1Lp2L', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14011'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1tttt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1tttt_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1tttt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
#T1tttt_1.obsExclusionM1.dataUrl =
#T1tttt_1.obsExclusionP1.dataUrl =
T1tttt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1tttt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'
T1tttt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14011/GluinoLimitsRazor2014.root'

databaseCreator.create()

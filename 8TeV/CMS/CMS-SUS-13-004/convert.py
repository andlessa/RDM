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
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-004')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13004'
info.sqrts = 8
info.lumi = 19.3
info.prettyname = 'Razor with b-jets'
info.private  = False
#info.arxiv =
#info.contact =
#info.publication =
info.comment = 'Not updated with arXiv publication results, superseded_by to be set after arXiv results?'
#info.supersedes =
#info.superseded_by =
info.implemented_by = 'Suchita Kulkarni'

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
#T1bbbb.on.checked =
#T1bbbb.off.checked =
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.condition = None
#T1bbbb.off.condition =
T1bbbb.on.fuzzycondition = None
T1bbbb.off.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure = 'Figure 12'
T1bbbb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T1bbbbRazorXSEC.pdf'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = "xsecUL_Obs_T1bbbb_MultiJet_Jet2b")
T1bbbb_1.expUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'xsecUL_Exp_T1bbbb_MultiJet_Jet2b', index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Obs_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.obsExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsMinus_T1bbbb_MultiJet_Jet2b' , index = None )
T1bbbb_1.obsExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsPlus_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Exp_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpMinus_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpPlus_T1bbbb_MultiJet_Jet2b', index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/xsecUL_SMS_Razor.root'
#----limit url settings ----
#T1bbbb_1.obsUpperLimit.dataUrl =
#T1bbbb_1.expUpperLimit.dataUrl =
#T1bbbb_1.histoDataUrl =
#----exclusion url settings ----
#T1bbbb_1.exclusionDataUrl =
#T1bbbb_1.obsExclusion.dataUrl =
#T1bbbb_1.obsExclusionM1.dataUrl =
#T1bbbb_1.obsExclusionP1.dataUrl =
#T1bbbb_1.expExclusion.dataUrl =
#T1bbbb_1.expExclusionM1.dataUrl =
#T1bbbb_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked =
#T2tt.off.checked =
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint = "[[['b','W']],[['b','W']]]"
T2tt.on.condition = None
T2tt.off.condition = None
T2tt.on.fuzzycondition = None
T2tt.off.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T2tt_1.figure = 'Figure 13'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T1ttttRazorXSEC.pdf'
#----limit source----
T2tt_1.obsUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'xsecUL_Obs_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.expUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'xsecUL_Exp_T2tt_MultiJet_Jet2b_MuJet', index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Obs_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.obsExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsMinus_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.obsExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsPlus_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.expExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Exp_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.expExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpMinus_T2tt_MultiJet_Jet2b_MuJet', index = None )
T2tt_1.expExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpPlus_T2tt_MultiJet_Jet2b_MuJet', index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/xsecUL_SMS_Razor.root'
#T2tt_1.histoDataUrl =
#----limit url settings ----
#T2tt_1.obsUpperLimit.dataUrl =
#T2tt_1.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T2tt_1.exclusionDataUrl =
#T2tt_1.obsExclusion.dataUrl =
#T2tt_1.obsExclusionM1.dataUrl =
#T2tt_1.obsExclusionP1.dataUrl =
#T2tt_1.expExclusion.dataUrl =
#T2tt_1.expExclusionM1.dataUrl =
#T2tt_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
#T1tttt.on.checked = 
#T1tttt.off.checked =
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.condition = None
T1tttt.off.condition = None
T1tttt.on.fuzzycondition = None
T1tttt.off.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y)
#----figure----
T1tttt_1.figure = 'Figure14'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T2ttRazorXSEC.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'xsecUL_Obs_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.expUpperLimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'xsecUL_Exp_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName= 'Obs_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.obsExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'ObsMinus_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.obsExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'ObsPlus_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.expExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'Exp_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.expExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'ExpMinus_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
T1tttt_1.expExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root',  objectName = 'ExpPlus_T1tttt_MultiJet_EleMultiJet_MuMultiJet', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/xsecUL_SMS_Razor.root'
#T1tttt_1.histoDataUrl =
#----limit url settings ----
#T1tttt_1.obsUpperLimit.dataUrl =
#T1tttt_1.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T1tttt_1.exclusionDataUrl =
#T1tttt_1.obsExclusion.dataUrl =
#T1tttt_1.obsExclusionM1.dataUrl =
#T1tttt_1.obsExclusionP1.dataUrl =
#T1tttt_1.expExclusion.dataUrl =
#T1tttt_1.expExclusionM1.dataUrl =
#T1tttt_1.expExclusionP1.dataUrl =

databaseCreator.create()

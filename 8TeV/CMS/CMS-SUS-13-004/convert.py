#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt,sms.py,sms.root and newSms.py.

"""
import sys
import os
sys.path.append(os.path.abspath('../../../../smodels-utils'))
from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfo('CMS-SUS-13-004')
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
T1bbbb = TxName('T1bbbb')
#T1bbbb.on.checked =
#T1bbbb.off.checked =
T1bbbb.on.constraint = "[[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.condition = None
#T1bbbb.off.condition =
T1bbbb.on.fuzzycondition = None
T1bbbb.off.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure = 'T1bbbbRazorXSEC.pdf'
T1bbbb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T1bbbbRazorXSEC.pdf'
#----limit source----
T1bbbb_1.limit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = "xsecUL_Obs_T1bbbb_MultiJet_Jet2b")
T1bbbb_1.expectedlimit.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'xsecUL_Exp_T1bbbb_MultiJet_Jet2b', index = None )
#----exclusion source----
T1bbbb_1.exclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Obs_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.exclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsMinus_T1bbbb_MultiJet_Jet2b' , index = None )
T1bbbb_1.exclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ObsPlus_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expectedExclusion.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'Exp_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expectedExclusionM1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpMinus_T1bbbb_MultiJet_Jet2b', index = None )
T1bbbb_1.expectedExclusionP1.setSource( './orig/xsecUL_SMS_Razor.root', 'root', objectName = 'ExpPlus_T1bbbb_MultiJet_Jet2b', index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/xsecUL_SMS_Razor.root'
#----limit url settings ----
#T1bbbb_1.limit.dataUrl =
#T1bbbb_1.expectedlimit.dataUrl =
#T1bbbb_1.histoDataUrl =
#----exclusion url settings ----
#T1bbbb_1.exclusionDataUrl =
#T1bbbb_1.exclusion.dataUrl =
#T1bbbb_1.exclusionM1.dataUrl =
#T1bbbb_1.exclusionP1.dataUrl =
#T1bbbb_1.expectedExclusion.dataUrl =
#T1bbbb_1.expectedExclusionM1.dataUrl =
#T1bbbb_1.expectedExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
'''T2tt = TxName('T2tt')
T2tt.on.checked =
T2tt.off.checked =
T2tt.on.constraint =
T2tt.off.constraint =
T2tt.on.condition =
T2tt.off.condition =
T2tt.on.fuzzycondition =
T2tt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.setMassPlane(motherMass = , lspMass = )
#----figure----
T2tt_1.figure =
T2tt_1.figureUrl =
#----limit source----
T2tt_1.limit.setSource( path, type, object = None, index = None )
T2tt_1.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T2tt_1.exclusion.setSource( path, type, object = None, index = None )
T2tt_1.exclusionM1.setSource( path, type, object = None, index = None )
T2tt_1.exclusionP1.setSource( path, type, object = None, index = None )
T2tt_1.expectedExclusion.setSource( path, type, object = None, index = None )
T2tt_1.expectedExclusionM1.setSource( path, type, object = None, index = None )
T2tt_1.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
T2tt_1.dataUrl =
T2tt_1.histoDataUrl =
#----limit url settings ----
T2tt_1.limit.dataUrl =
T2tt_1.expectedlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl =
T2tt_1.exclusion.dataUrl =
T2tt_1.exclusionM1.dataUrl =
T2tt_1.exclusionP1.dataUrl =
T2tt_1.expectedExclusion.dataUrl =
T2tt_1.expectedExclusionM1.dataUrl =
T2tt_1.expectedExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1tttt = TxName('T1tttt')
T1tttt.on.checked =
T1tttt.off.checked =
T1tttt.on.constraint =
T1tttt.off.constraint =
T1tttt.on.condition =
T1tttt.off.condition =
T1tttt.on.fuzzycondition =
T1tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.setMassPlane(motherMass = , lspMass = )
#----figure----
T1tttt_1.figure =
T1tttt_1.figureUrl =
#----limit source----
T1tttt_1.limit.setSource( path, type, object = None, index = None )
T1tttt_1.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T1tttt_1.exclusion.setSource( path, type, object = None, index = None )
T1tttt_1.exclusionM1.setSource( path, type, object = None, index = None )
T1tttt_1.exclusionP1.setSource( path, type, object = None, index = None )
T1tttt_1.expectedExclusion.setSource( path, type, object = None, index = None )
T1tttt_1.expectedExclusionM1.setSource( path, type, object = None, index = None )
T1tttt_1.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
T1tttt_1.dataUrl =
T1tttt_1.histoDataUrl =
#----limit url settings ----
T1tttt_1.limit.dataUrl =
T1tttt_1.expectedlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl =
T1tttt_1.exclusion.dataUrl =
T1tttt_1.exclusionM1.dataUrl =
T1tttt_1.exclusionP1.dataUrl =
T1tttt_1.expectedExclusion.dataUrl =
T1tttt_1.expectedExclusionM1.dataUrl =
T1tttt_1.expectedExclusionP1.dataUrl ='''

databaseCreator.create()
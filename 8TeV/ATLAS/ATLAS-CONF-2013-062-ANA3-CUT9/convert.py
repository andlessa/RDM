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
from smodels_utils.dataPreparation.origPlotObjects import x, y, z

#+++++++ global info block ++++++++++++++
info = MetaInfo('ATLAS-CONF-2013-062')
info.signalRegion = 'ANA3-CUT9'
info.url ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-062/' 
info.sqrts = 8
info.lumi = 20.
info.prettyname = 'leptons + jets + met'
info.private = True
#info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='fastlim'
info.publication = 'http://cds.cern.ch/record/1557779'
info.comment = 'created from fastlim-1.0'
info.superseded_by ='SUSY-2013-20'
info.implemented_by = 'WW'
info.observedN = 4
info.expectedBG = 3.6
info.bgError = 1.0
#
##+++++++ next txName block ++++++++++++++
#T1 = TxName('T1')
#T1.on.constraint = "[[['jet','jet']],[['jet','jet']]]"
#T1.on.condition = None
#T1.on.fuzzycondition = None
#
##+++++++ next mass plane block ++++++++++++++
#T1_1 = T1.addMassPlane(motherMass = x , lspMass = y )
##----figure----
#T1_1.figure = 'fig_07a.pdf'
#T1_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'
## ----limit source----
### T1_1.obsUpperLimit.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
#T1_1.efficiencyMap.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
## T1_1.obsUpperLimit.unit = 'fb'
## T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
## ----exclusion source----
#T1_1.obsExclusion.setSource( './orig/T1_exc.dat', 'txt', objectName = None, index = None )
##T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
##T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
##T1_1.expExclusion.setSource( path, type, objectName = None, index = None )
##T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
##T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
##----global url settings ----
##T1_1.dataUrl = 
##T1_1.histoDataUrl = 
##----limit url settings ----
## T1_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_A.txt'
##T1_1.expectedlimit.dataUrl =
##----exclusion url settings ----
##T1_1.exclusionDataUrl =
##T1_1.exclusion.dataUrl =
##T1_1.exclusionM1.dataUrl =
##T1_1.exclusionP1.dataUrl =
##T1_1.expectedExclusion.dataUrl =
##T1_1.expectedExclusionM1.dataUrl =
##T1_1.expectedExclusionP1.dataUrl =
#
#T2tt = TxName('T2tt')
#T2tt.on.constraint = "[[['t']],[['t']]]"
#T2tt.on.condition = None
#T2tt.on.fuzzycondition = None
#T2tt_1 = T2tt.addMassPlane(motherMass = x , lspMass = y )
#T2tt_1.efficiencyMap.setSource( './orig/T2tt.effi', 'effi', objectName = None, index = None )
#
#T2bb = TxName('T2bb')
#T2bb.on.constraint = "[[['b']],[['b']]]"
#T2bb.on.condition = None
#T2bb.on.fuzzycondition = None
#T2bb_1 = T2bb.addMassPlane(motherMass = x , lspMass = y )
#T2bb_1.efficiencyMap.setSource( './orig/T2bb.effi', 'effi', objectName = None, index = None )
#
#T2bt = TxName('T2bt')
#T2bt.on.constraint = "[[['b']],[['t']]]"
#T2bt.on.condition = None
#T2bt.on.fuzzycondition = None
#T2bt_1 = T2bt.addMassPlane(motherMass = x , lspMass = y )
#T2bt_1.efficiencyMap.setSource( './orig/T2bt.effi', 'effi', objectName = None, index = None )
#
T1tttt = TxName('T1tttt')
T1tttt.on.constraint = "[[['t+','t-']],[['t+','t-']]]"
T1tttt.on.condition = None
T1tttt.on.fuzzycondition = None
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y )
T1tttt_1.efficiencyMap.setSource( './orig/T1tttt.effi', 'effi', objectName = None, index = None )

T1bbbb = TxName('T1bbbb')
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
T1bbbb.on.condition = None
T1bbbb.on.fuzzycondition = None
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x , lspMass = y )
T1bbbb_1.efficiencyMap.setSource( './orig/T1bbbb.effi', 'effi', objectName = None, index = None )

T5tttt = TxName('T5tttt')
T5tttt.on.constraint = "[[['t+'],['t-']],[['t+'],['t-']]]"
T5tttt.on.condition = None
T5tttt.on.fuzzycondition = None
T5tttt_1 = T5tttt.addMassPlane(motherMass = x , intermediateMass = y, lspMass = z )
T5tttt_1.efficiencyMap.setSource( './orig/T5tttt.effi', 'effi', objectName = None, index = None )

#T5bbbb = TxName('T5bbbb')
#T5bbbb.on.constraint = "[[['b'],['b']],[['b'],['b']]]"
#T5bbbb.on.condition = None
#T5bbbb.on.fuzzycondition = None
#T5bbbb_1 = T5bbbb.addMassPlane(motherMass = x , lspMass = y )
#T5bbbb_1.efficiencyMap.setSource( './orig/T5bbbb.effi', 'effi', objectName = None, index = None )
#
#T5bbbt = TxName('T5bbbt')
#T5bbbt.on.constraint = "[[['b'],['b']],[['b'],['t']]]"
#T5bbbt.on.condition = None
#T5bbbt.on.fuzzycondition = None
#T5bbbt_1 = T5bbbt.addMassPlane(motherMass = x , lspMass = y )
#T5bbbt_1.efficiencyMap.setSource( './orig/T5bbbt.effi', 'effi', objectName = None, index = None )

T1bbbt = TxName('T1bbbt')
T1bbbt.on.constraint = "[[['b','b']],[['b','t']]]"
T1bbbt.on.condition = None
T1bbbt.on.fuzzycondition = None
T1bbbt_1 = T1bbbt.addMassPlane(motherMass = x , lspMass = y )
T1bbbt_1.efficiencyMap.setSource( './orig/T1bbbt.effi', 'effi', objectName = None, index = None )

T1bbqq = TxName('T1bbqq')
T1bbqq.on.constraint = "[[['b','b']],[['q','q']]]"
T1bbqq.on.condition = None
T1bbqq.on.fuzzycondition = None
T1bbqq_1 = T1bbqq.addMassPlane(motherMass = x , lspMass = y )
T1bbqq_1.efficiencyMap.setSource( './orig/T1bbqq.effi', 'effi', objectName = None, index = None )

TGQttq = TxName('TGQttq')
TGQttq.on.constraint = "[[['t+','t-']],[['jet']]]"
TGQttq.on.condition = None
TGQttq.on.fuzzycondition = None
TGQttq_1 = TGQttq.addMassPlane(motherMass = x , lspMass = y )
TGQttq_1.efficiencyMap.setSource( './orig/TGQttq.effi', 'effi', objectName = None, index = None )
#
#T1qqtt = TxName('T1qqtt')
#T1qqtt.on.constraint = "[[['jet','jet']],[['t','t']]]"
#T1qqtt.on.condition = None
#T1qqtt.on.fuzzycondition = None
#T1qqtt_1 = T1qqtt.addMassPlane(motherMass = x , lspMass = y )
#T1qqtt_1.efficiencyMap.setSource( './orig/T1qqtt.effi', 'effi', objectName = None, index = None )
#
#T1bttt = TxName('T1bttt')
#T1bttt.on.constraint = "[[['b','t']],[['t','t']]]"
#T1bttt.on.condition = None
#T1bttt.on.fuzzycondition = None
#T1bttt_1 = T1bttt.addMassPlane(motherMass = x , lspMass = y )
#T1bttt_1.efficiencyMap.setSource( './orig/T1bttt.effi', 'effi', objectName = None, index = None )
#
databaseCreator.create()

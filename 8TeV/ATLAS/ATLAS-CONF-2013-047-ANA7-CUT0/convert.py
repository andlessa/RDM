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
info = MetaInfo('ATLAS-CONF-2013-047')
info.signalRegion = 'ANA7-CUT0'
info.url ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/' 
info.sqrts = 8
info.lumi = 20.3
info.prettyname = '0 leptons + jets + met'
info.private = True
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='fastlim'
info.publication = 'http://cds.cern.ch/record/1547563'
info.comment = 'created from fastlim-1.0'
info.superseded_by ='SUSY-2013-02'
info.implemented_by = 'Wolfgang Waltenberger'
info.observedN = 5333
info.expectedBG = 4700
info.bgError = 500

#+++++++ next txName block ++++++++++++++
T1 = TxName('T1')
T1.on.constraint = "[[['jet','jet']],[['jet','jet']]]"
T1.on.condition = None
T1.on.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x , lspMass = y )
#----figure----
T1_1.figure = 'fig_07a.pdf'
T1_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'
# ----limit source----
## T1_1.obsUpperLimit.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
T1_1.efficiencyMap.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
# T1_1.obsUpperLimit.unit = 'fb'
# T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
# ----exclusion source----
T1_1.obsExclusion.setSource( './orig/T1_exc.dat', 'txt', objectName = None, index = None )
#T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T1_1.dataUrl = 
#T1_1.histoDataUrl = 
#----limit url settings ----
# T1_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_A.txt'
#T1_1.expectedlimit.dataUrl =
#----exclusion url settings ----
#T1_1.exclusionDataUrl =
#T1_1.exclusion.dataUrl =
#T1_1.exclusionM1.dataUrl =
#T1_1.exclusionP1.dataUrl =
#T1_1.expectedExclusion.dataUrl =
#T1_1.expectedExclusionM1.dataUrl =
#T1_1.expectedExclusionP1.dataUrl =

T2tt = TxName('T2tt')
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.on.condition = None
T2tt.on.fuzzycondition = None
T2tt_1 = T2tt.addMassPlane(motherMass = x , lspMass = y )
T2tt_1.efficiencyMap.setSource( './orig/T2tt.effi', 'effi', objectName = None, index = None )

T2bb = TxName('T2bb')
T2bb.on.constraint = "[[['b']],[['b']]]"
T2bb.on.condition = None
T2bb.on.fuzzycondition = None
T2bb_1 = T2bb.addMassPlane(motherMass = x , lspMass = y )
T2bb_1.efficiencyMap.setSource( './orig/T2bb.effi', 'effi', objectName = None, index = None )

T2bt = TxName('T2bt')
T2bt.on.constraint = "[[['b']],[['t']]]"
T2bt.on.condition = None
T2bt.on.fuzzycondition = None
T2bt_1 = T2bt.addMassPlane(motherMass = x , lspMass = y )
T2bt_1.efficiencyMap.setSource( './orig/T2bt.effi', 'effi', objectName = None, index = None )

T1tttt = TxName('T1tttt')
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.on.condition = None
T1tttt.on.fuzzycondition = None
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y )
T1tttt_1.efficiencyMap.setSource( './orig/T1tttt.effi', 'effi', objectName = None, index = None )

T1bbtt = TxName('T1bbtt')
T1bbtt.on.constraint = "[[['b','b']],[['t','t']]]"
T1bbtt.on.condition = None
T1bbtt.on.fuzzycondition = None
T1bbtt_1 = T1bbtt.addMassPlane(motherMass = x , lspMass = y )
T1bbtt_1.efficiencyMap.setSource( './orig/T1bbtt.effi', 'effi', objectName = None, index = None )

T1btbt = TxName('T1btbt')
T1btbt.on.constraint = "[[['b','t']],[['b','t']]]"
T1btbt.on.condition = None
T1btbt.on.fuzzycondition = None
T1btbt_1 = T1btbt.addMassPlane(motherMass = x , lspMass = y )
T1btbt_1.efficiencyMap.setSource( './orig/T1btbt.effi', 'effi', objectName = None, index = None )

T1btqq = TxName('T1btqq')
T1btqq.on.constraint = "[[['b','t']],[['jet','jet']]]"
T1btqq.on.condition = None
T1btqq.on.fuzzycondition = None
T1btqq_1 = T1btqq.addMassPlane(motherMass = x , lspMass = y )
T1btqq_1.efficiencyMap.setSource( './orig/T1btqq.effi', 'effi', objectName = None, index = None )

T1qqtt = TxName('T1qqtt')
T1qqtt.on.constraint = "[[['jet','jet']],[['t','t']]]"
T1qqtt.on.condition = None
T1qqtt.on.fuzzycondition = None
T1qqtt_1 = T1qqtt.addMassPlane(motherMass = x , lspMass = y )
T1qqtt_1.efficiencyMap.setSource( './orig/T1qqtt.effi', 'effi', objectName = None, index = None )

T1bttt = TxName('T1bttt')
T1bttt.on.constraint = "[[['b','t']],[['t','t']]]"
T1bttt.on.condition = None
T1bttt.on.fuzzycondition = None
T1bttt_1 = T1bttt.addMassPlane(motherMass = x , lspMass = y )
T1bttt_1.efficiencyMap.setSource( './orig/T1bttt.effi', 'effi', objectName = None, index = None )

databaseCreator.create()

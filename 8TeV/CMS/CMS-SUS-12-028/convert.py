#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description =  
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', 
help = 'path to the package smodels_utils',\
type = types.StringType)
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-12-028')
info.url ="https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12028"
info.sqrts = 8
info.lumi = 11.7
info.prettyName ="alphaT"
info.private = False
info.arxiv ='http://arxiv.org/abs/1303.2985'
info.contact ='Edward Laird <edward.laird@cern.ch>, Rob Bainbridge <robert.bainbridge@cern.ch>'
info.publication ='Eur. Phys. J. C 73 (2013) 2568'
info.comment ="Only the expected upper limit exclusion line is present - no observed one"
info.supersedes ='CMS-PAS-SUS-12-016'
info.supersededBy =""

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =""
T1tttt.off.checked =""
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription = "None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition ="None"
#T1tttt.off.condition =
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T1tttt_1.figure ="Figure 8"
T1tttt_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t1tttt.pdf"
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/T1tttt.root', 'root', objectName = "UpperLimit", index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/T1tttt.root', 'root', objectName = "ExpectedUpperLimit", index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt.root', 'root', objectName = "UpperLimit_graph", index = None )
#T1tttt_1.obsExclusionM1.setSource( 'orig/T1tttt.root', 'root', objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( 'orig/T1tttt.root', 'root', objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( 'orig/T1tttt.root', 'root', objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( 'orig/T1tttt.root', 'root', objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( 'orig/T1tttt.root', 'root', objectName = None, index = None )
#----global url settings ----
T1tttt_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1tttt.root"
#----limit url settings ----
T1tttt_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1tttt.pdf"
T1tttt_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1tttt.root"
T1tttt_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1tttt.root"
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1tttt.root"
T1tttt_1.obsExclusion.dataUrl =""
T1tttt_1.obsExclusionM1.dataUrl =""
T1tttt_1.obsExclusionP1.dataUrl =""
T1tttt_1.expExclusion.dataUrl =""
T1tttt_1.expExclusionM1.dataUrl =""
T1tttt_1.expExclusionP1.dataUrl =""

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =""
T2tt.off.checked =""
T2tt.on.constraint = "[[['t']],[['t']]]"
#T2tt.off.constraint ="None"
T2tt.on.conditionDescription ="None"
#T2tt.off.conditionDescription =
T2tt.on.condition ="None"
#T2tt.off.condition =
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure ="t2tt"
T2tt_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t2tt.pdf"
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/T2tt.root', 'root', objectName = "UpperLimit", index = None )
T2tt_1.expUpperLimit.setSource( 'orig/T2tt.root', 'root', objectName = "ExpectedUpperLimit", index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource('orig/T2tt_exc.dat', 'txt', objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( 'orig/T2tt.root', 'root', objectName = "ExpectedUpperLimit_graph", index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2tt_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2tt.root"
#----limit url settings ----
T2tt_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2tt.pdf"
T2tt_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2tt.root"
T2tt_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2tt.root"
#----exclusion url settings ----
T2tt_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2tt.root"
#T2tt_1.obsExclusion.dataUrl =
#T2tt_1.obsExclusionM1.dataUrl =
#T2tt_1.obsExclusionP1.dataUrl =
#T2tt_1.expExclusion.dataUrl =
#T2tt_1.expExclusionM1.dataUrl =
#T2tt_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked =""
T1bbbb.off.checked =""
T1bbbb.on.constraint ="[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription ="None"
#T1bbbb.off.conditionDescription ="None"
T1bbbb.on.condition ="None"
#T1bbbb.off.condition =
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure ="Figure 8"
T1bbbb_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t1bbbb.pdf"
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/T1bbbb.root', 'root', objectName = "UpperLimit", index = None )
T1bbbb_1.expUpperLimit.setSource( 'orig/T1bbbb.root', 'root', objectName = "ExpectedUpperLimit", index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/T1bbbb.root', 'root', objectName = "UpperLimit_graph", index = None )
#T1bbbb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1bbbb_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1bbbb.root"
#----limit url settings ----
T1bbbb_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t1bbbb.pdf"
T1bbbb_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1bbbb.root"
T1bbbb_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1bbbb.root"
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1bbbb.root"
#T1bbbb_1.exclusionDataUrl =
#T1bbbb_1.obsExclusion.dataUrl =
#T1bbbb_1.obsExclusionM1.dataUrl =
#T1bbbb_1.obsExclusionP1.dataUrl =
#T1bbbb_1.expExclusion.dataUrl =
#T1bbbb_1.expExclusionM1.dataUrl =
#T1bbbb_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
T2.on.checked =""
T2.off.checked =""
T2.on.constraint ="[[['jet']],[['jet']]]"
#T2.off.constraint =
T2.on.conditionDescription ="None"
#T2.off.conditionDescription =
T2.on.condition ="None"
#T2.off.condition =
#T2.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2_1.figure ="Figure 8"
T2_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t2.pdf"
#----limit source----
T2_1.obsUpperLimit.setSource( 'orig/T2.root', 'root', objectName = "T2_UpperLimit", index = None )
T2_1.expUpperLimit.setSource( 'orig/T2.root', 'root', objectName = "T2_ExpectedUpperLimit", index = None )
#----exclusion source----
T2_1.obsExclusion.setSource( 'orig/T2.root', 'root', objectName = "UpperLimit_xs0p8", index = None )
#T2_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2.root"
#----limit url settings ----
T2_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t2.pdf"
T2_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2.root"
T2_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2.root"
#----exclusion url settings ----
T2_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2.root"
#T2_1.obsExclusion.dataUrl =
#T2_1.obsExclusionM1.dataUrl =
#T2_1.obsExclusionP1.dataUrl =
#T2_1.expExclusion.dataUrl =
#T2_1.expExclusionM1.dataUrl =
#T2_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
T1.on.checked =""
T1.off.checked =""
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =
T1.on.conditionDescription ="None"
#T1.off.conditionDescription =
T1.on.condition ="None"
#T1.off.condition =
#T1.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T1_1.figure ="Figure 8"
T1_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t1.pdf"
#----limit source----
T1_1.obsUpperLimit.setSource( 'orig/T1.root', 'root', objectName = "UpperLimit", index = None )
T1_1.expUpperLimit.setSource( 'orig/T1.root', 'root', objectName = "ExpectedUpperLimit", index = None )
#----exclusion source----
T1_1.obsExclusion.setSource( 'orig/T1.root', 'root', objectName = "UpperLimit_graph", index = None )
#T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1.root"
#----limit url settings ----
T1_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t1.pdf"
T1_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1.root"
T1_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1.root"
#----exclusion url settings ----
T1_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T1.root"
#T1_1.obsExclusion.dataUrl =
#T1_1.obsExclusionM1.dataUrl =
#T1_1.obsExclusionP1.dataUrl =
#T1_1.expExclusion.dataUrl =
#T1_1.expExclusionM1.dataUrl =
#T1_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =""
T2bb.off.checked =""
T2bb.on.constraint ="[[['b']],[['b']]]"
#T2bb.off.constraint =
T2bb.on.conditionDescription ="None"
#T2bb.off.conditionDescription =
T2bb.on.condition ="None"
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2bb_1.figure ="Figure 8"
T2bb_1.figureUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t2bb.pdf"
#----limit source----
T2bb_1.obsUpperLimit.setSource( 'orig/T2bb.root', 'root', objectName = "UpperLimit", index = None )
T2bb_1.expUpperLimit.setSource( 'orig/T2bb.root', 'root', objectName = "ExpectedUpperLimit", index = None )
#----exclusion source----
T2bb_1.obsExclusion.setSource( 'orig/T2bb.root', 'root', objectName = "UpperLimit_graph", index = None )
#T2bb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2bb_1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2bb.root"
#----limit url settings ----
T2bb_1.histoDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/t2bb.pdf"
T2bb_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2bb.root"
T2bb_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2bb.root"
#----exclusion url settings ----
T2bb_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12028/T2bb.root"
#T2bb_1.obsExclusion.dataUrl =
#T2bb_1.obsExclusionM1.dataUrl =
#T2bb_1.obsExclusionP1.dataUrl =
#T2bb_1.expExclusion.dataUrl =
#T2bb_1.expExclusionM1.dataUrl =
#T2bb_1.expExclusionP1.dataUrl =

databaseCreator.create()

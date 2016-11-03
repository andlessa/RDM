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
info = MetaInfoInput('CMS-SUS-13-004')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13004'
info.sqrts = 8
info.lumi = 19.3
info.prettyName = 'Razor with b-jets'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1502.00300v2'
#info.contact =
info.publication = 'http://dx.doi.org/10.1103/PhysRevD.91.052018'
info.comment ='Other topologies have a compressed mass spectrum (decays with intermediate charginos, <= 5 GeV mass difference)'
#info.supersedes =
#info.supersededBy = 'CMS-SUS-PAS-14-011'

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
T2tt_1 = T2tt.addMassPlane(motherMass =x , lspMass =y)
#----figure----
T2tt_1.figure = 'Fig. 15c'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T2ttCOMBINED.pdf'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 2 )
#T2tt_1.expUpperLimit.setSource( 'orig/T2tt_Comb.root', 'root', objectName = 'cCONT_', index = None)
#----exclusion source----
T2tt_1.obsExclusion.setSource(  'orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 8 )
T2tt_1.obsExclusionM1.setSource('orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 10 )
T2tt_1.obsExclusionP1.setSource('orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 9 )
T2tt_1.expExclusion.setSource(  'orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 5 )
T2tt_1.expExclusionM1.setSource('orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 7 )
T2tt_1.expExclusionP1.setSource('orig/T2tt_Comb.root', 'canvas', objectName = 'cCONT_', index = 6 )
#----global url settings ----
T2tt_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#T2tt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T2tt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'

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
T1bbbb_1 = T1bbbb.addMassPlane(motherMass =x , lspMass =y )
#----figure----
T1bbbb_1.figure = 'Fig. 13a'
T1bbbb_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T1bbbbHybridNew0LXSEC.png'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 2  )
#T1bbbb_1.expUpperLimit.setSource( 'orig/T1bbbb.root', 'root', objectName = 'cCONT_', index = None   )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource(  'orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 8  )
T1bbbb_1.obsExclusionM1.setSource('orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 10   )
T1bbbb_1.obsExclusionP1.setSource('orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 9   )
T1bbbb_1.expExclusion.setSource(  'orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 5   )
T1bbbb_1.expExclusionM1.setSource('orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 7   )
T1bbbb_1.expExclusionP1.setSource('orig/T1bbbb.root', 'canvas', objectName = 'cCONT_', index = 6   )
#----global url settings ----
T1bbbb_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#----limit url settings ----
T1bbbb_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#T1bbbb_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1bbbb_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'

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
T1tttt_1 = T1tttt.addMassPlane(motherMass =x, lspMass =y )
#----figure----
T1tttt_1.figure = 'Fig. 13e'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/T1ttttHybridNew0Lp1Lp2LXSEC.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource(  'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 2  )
#T1tttt_1.expUpperLimit.setSource(  'orig/T1tttt.root', 'root', objectName = 'cCONT_', index = None  )
#----exclusion source----
T1tttt_1.obsExclusion.setSource(   'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 8  )
T1tttt_1.obsExclusionM1.setSource( 'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 10   )
T1tttt_1.obsExclusionP1.setSource( 'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 9  )
T1tttt_1.expExclusion.setSource(   'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 5  )
T1tttt_1.expExclusionM1.setSource( 'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 7  )
T1tttt_1.expExclusionP1.setSource( 'orig/T1tttt.root', 'canvas', objectName = 'cCONT_', index = 6  )
#----global url settings ----
T1tttt_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#----limit url settings ----
T1tttt_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
#T1tttt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'
T1tttt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13004/razor_8TeV_sms_results.root'

databaseCreator.create()

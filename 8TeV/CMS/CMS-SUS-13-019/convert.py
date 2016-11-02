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
info = MetaInfoInput('CMS-SUS-13-019')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
info.sqrts = 8
info.lumi = 19.5
info.prettyName = 'MT2'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1502.04358'
info.contact =''
info.publication ='http://link.springer.com/article/10.1007%2FJHEP05%282015%29078'
info.comment =''
info.supersedes =''
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]" 
T1tttt.on.conditionDescription = 'None'
T1tttt.off.conditionDescription ='None'
T1tttt.on.condition = 'None'
T1tttt.off.condition ='None'
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T1tttt_1.figure = 'Fig. 13c'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1tttt-SUS13019-final_XSEC.png'		     
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T1tttt_1.expExclusion.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/Extracted_T1tttt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
#T1tttt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T1tttt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'

'''
#+++++++ next txName block ++++++++++++++
T5WH = TxNameInput('T5WH')
T5WH.on.checked =''
#T5WH.off.checked =
T5WH.on.constraint = "[[['jet','jet'],['W']],[['jet','jet'],['higgs']]]"
#T5WH.off.constraint = 
T5WH.on.conditionDescription ='None'
#T5WH.off.conditionDescription =
T5WH.on.condition ='None'
#T5WH.off.condition =

#+++++++ next mass plane block ++++++++++++++
T5WH_1 = T5WH.addMassPlane(motherMass = x, interMass0 = x -200, lspMass = y)
#T5WH_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T5WH_1.figure = 'Fig. 14'
T5WH_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.png'
#----limit source----
T5WH_1.obsUpperLimit.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'h_Limit', index = None )
#T5WH_1.expUpperLimit.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = None, index = None )
#----exclusion source----
T5WH_1.obsExclusion.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_Obs', index = None )
T5WH_1.obsExclusionM1.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_ObsMS', index = None )
T5WH_1.obsExclusionP1.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_ObsPS', index = None )
T5WH_1.expExclusion.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_Exp', index = None )
T5WH_1.expExclusionM1.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_ExpMS', index = None )
T5WH_1.expExclusionP1.setSource( 'orig/Extracted_T5WH-SUS13019-final_XSEC.root', 'root', objectName = 'gr_ExpPS', index = None )
#----global url settings ----
T5WH_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T5WH_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
#T5WH_1.expUpperlimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
#----exclusion url settings ----
T5WH_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'
T5WH_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T5WH-SUS13019-final_XSEC.root'

'''

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
#T2tt.off.checked =
T2tt.on.constraint ="[[['t']],[['t']]]"
T2tt.off.constraint ="[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription = 'None'
T2tt.off.conditionDescription ='None'
T2tt.on.condition ='None'
T2tt.off.condition ='None'
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure = 'Fig. 12c'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.png'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T2tt_1.obsExclusionM1.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T2tt_1.obsExclusionP1.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T2tt_1.expExclusion.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T2tt_1.expExclusionM1.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
T2tt_1.expExclusionP1.setSource( 'orig/Extracted_T2tt-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
#T2tt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'
T2tt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2tt-SUS13019-final_XSEC.root'

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked = ''
#T1bbbb.off.checked =
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription = 'None'
#T1bbbb.off.conditionDescription =
T1bbbb.on.condition = 'None'
#T1bbbb.off.condition =
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure ='Fig. 13b'
T1bbbb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.png'
#----limit source----
T1bbbb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.png'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T1bbbb_1.obsExclusionM1.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T1bbbb_1.obsExclusionP1.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T1bbbb_1.expExclusion.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T1bbbb_1.expExclusionM1.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
T1bbbb_1.expExclusionP1.setSource( 'orig/Extracted_T1bbbb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T1bbbb_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
#T1bbbb_1.expUpperlimit.dataUrl =''
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'
T1bbbb_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1bbbb-SUS13019-final_XSEC.root'

#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
T2.on.checked =''
T2.off.checked =''
T2.on.constraint ="[[['jet']],[['jet']]]"
#T2.off.constraint =
T2.on.conditionDescription = "None"
#T2.off.conditionDescription =
T2.on.condition = "None"
#T2.off.condition =
#T2.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(motherMass = x, lspMass =y )
#----figure----
T2_1.figure ='Fig. 13a'
T2_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2qq-SUS13019-final_XSEC.png'
#----limit source----
T2_1.obsUpperLimit.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2_1.obsExclusion.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T2_1.obsExclusionM1.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T2_1.obsExclusionP1.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T2_1.expExclusion.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T2_1.expExclusionM1.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
T2_1.expExclusionP1.setSource( 'orig/Extracted_T2qq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
#----global url settings ----
T2_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T2_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
#T2_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T2_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'

#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
#T1.on.checked =
#T1.off.checked =
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =
T1.on.conditionDescription ="None"
#T1.off.conditionDescription =
T1.on.condition ="None"
#T1.off.condition =
#T1.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1_1.figure ='Fig. 13a'
T1_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.png'
#----limit source----
T1_1.obsUpperLimit.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1_1.obsExclusion.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T1_1.obsExclusionM1.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T1_1.obsExclusionP1.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T1_1.expExclusion.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T1_1.expExclusionM1.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
T1_1.expExclusionP1.setSource( 'orig/Extracted_T1qqqq-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
#----global url settings ----
T1_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T1_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
#T1_1.expUpperlimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
#----exclusion url settings ----
T1_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'
T1_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T1qqqq-SUS13019-final_XSEC.root'

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =''
#T2bb.off.checked =
T2bb.on.constraint = "[[['b']],[['b']]]"
#T2bb.off.constraint = 'None'
T2bb.on.conditionDescription ='None'
#T2bb.off.conditionDescription =
T2bb.on.condition ='None'
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2bb_1.figure ='Fig. 12b'
T2bb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.png'
#----limit source----
T2bb_1.obsUpperLimit.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'XSec_limit_combined', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2bb_1.obsExclusion.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_obs_combined', index = None )
T2bb_1.obsExclusionM1.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_mTH_obs_combined', index = None )
T2bb_1.obsExclusionP1.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_pTH_obs_combined', index = None )
T2bb_1.expExclusion.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_exp_combined', index = None )
T2bb_1.expExclusionM1.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_msig_combined', index = None )
T2bb_1.expExclusionP1.setSource( 'orig/Extracted_T2bb-SUS13019-final_XSEC.root', 'root', objectName = 'gr_cTH_psig_combined', index = None )
#----global url settings ----
T2bb_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13019'
#----limit url settings ----
T2bb_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
#T2bb_1.expUpperlimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
#----exclusion url settings ----
T2bb_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'
T2bb_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13019/T2bb-SUS13019-final_XSEC.root'

databaseCreator.create()

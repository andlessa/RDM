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
info = MetaInfoInput('CMS-PAS-SUS-16-024')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/'
info.sqrts = 13
info.lumi = 12.9
#info.prettyName =
info.private = False 
#info.arxiv = 
#info.contact =
#info.publication =
info.comment = 'https://cds.cern.ch/record/2205168'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
TChiChipmStauL = TxNameInput('TChiChipmStauL')
TChiChipmStauL.on.checked = '' 
TChiChipmStauL.off.checked = ''
TChiChipmStauL.on.constraint = "[[['ta'],['ta']],[['nu'],['L']]]"
#TChiChipmStauL.off.constraint =
TChiChipmStauL.on.conditionDescription = None
#TChiChipmStauL.off.conditionDescription =
TChiChipmStauL.on.condition = None
#TChiChipmStauL.off.condition =
#TChiChipmStauL.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiChipmStauL_1 = TChiChipmStauL.addMassPlane(motherMass = x, interMass0 = .5*(x+y), lspMass = y)
#TChiChipmStauL_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmStauL_1.figure = 'Figure 9'
TChiChipmStauL_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.png'
#----limit source----
TChiChipmStauL_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'obs_mu0', index = None )
TChiChipmStauL_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'exp_mu0', index = None )
#----exclusion source----
TChiChipmStauL_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_obs_smoothed', index = None )
TChiChipmStauL_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_om1s_smoothed', index = None )
TChiChipmStauL_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_op1s_smoothed', index = None )
TChiChipmStauL_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_exp_smoothed', index = None )
TChiChipmStauL_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_em1s_smoothed', index = None )
TChiChipmStauL_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_009.root', 'root', objectName = 'gr_ep1s_smoothed', index = None )
#----global url settings ----
TChiChipmStauL_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
#----limit url settings ----
TChiChipmStauL_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
#----exclusion url settings ----
TChiChipmStauL_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'
TChiChipmStauL_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_009.root'

#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
TChiWH.on.checked = ''
TChiWH.off.checked = ''
TChiWH.on.constraint = "[[['W']],[['higgs']]]"
#TChiWH.off.constraint = 
TChiWH.on.conditionDescription = None
#TChiWH.off.conditionDescription =
TChiWH.on.condition = None
#TChiWH.off.condition =
#TChiWH.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiWH_1 = TChiWH.addMassPlane(motherMass = x, lspMass = y)
#----figure----
TChiWH_1.figure = 'Figure 10-b'
TChiWH_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.png'
#----limit source----
TChiWH_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'obs_mu0', index = None )
TChiWH_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'exp_mu0', index = None )
#----exclusion source----
TChiWH_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_obs', index = None )
TChiWH_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_om1s', index = None )
TChiWH_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_op1s', index = None )
TChiWH_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_exp', index = None )
TChiWH_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_em1s', index = None )
TChiWH_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-b.root', 'root', objectName = 'gr_ep1s', index = None )
#----global url settings ----
TChiWH_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
#----limit url settings ----
TChiWH_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
#----exclusion url settings ----
TChiWH_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'
TChiWH_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-b.root'

'''
#+++++++ next txName block ++++++++++++++
TChiChipmStauStau = TxNameInput('TChiChipmStauStau')
TChiChipmStauStau.on.checked = ''
TChiChipmStauStau.off.checked = ''
TChiChipmStauStau.on.constraint = "[[['ta'],['ta']],[['nu'],['ta']]]"
TChiChipmStauStau.off.constraint =None
TChiChipmStauStau.on.conditionDescription =None
TChiChipmStauStau.off.conditionDescription =None
TChiChipmStauStau.on.condition =None
TChiChipmStauStau.off.condition =None
#TChiChipmStauStau.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiChipmStauStau_1 = TChiChipmStauStau.addMassPlane(motherMass = , interMass0 = , lspMass = )
#TChiChipmStauStau_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmStauStau_1.figure =
TChiChipmStauStau_1.figureUrl =
#----limit source----
TChiChipmStauStau_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmStauStau_1.obsExclusion.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.expExclusion.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
TChiChipmStauStau_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
TChiChipmStauStau_1.dataUrl =
#----limit url settings ----
TChiChipmStauStau_1.histoDataUrl =
TChiChipmStauStau_1.obsUpperLimit.dataUrl =
TChiChipmStauStau_1.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmStauStau_1.exclusionDataUrl =
TChiChipmStauStau_1.obsExclusion.dataUrl =
TChiChipmStauStau_1.obsExclusionM1.dataUrl =
TChiChipmStauStau_1.obsExclusionP1.dataUrl =
TChiChipmStauStau_1.expExclusion.dataUrl =
TChiChipmStauStau_1.expExclusionM1.dataUrl =
TChiChipmStauStau_1.expExclusionP1.dataUrl =
'''
#+++++++ next txName block ++++++++++++++
TChiWZ = TxNameInput('TChiWZ')
TChiWZ.on.checked = ''
TChiWZ.off.checked = ''
TChiWZ.on.constraint = "[[['W']],[['Z']]]"
TChiWZ.off.constraint = "[[['e+','e-']],[['l','nu']]]+[[['mu+','mu-']],[['l','nu']]]"
TChiWZ.on.conditionDescription = None
TChiWZ.off.conditionDescription = None
TChiWZ.on.condition = None
TChiWZ.off.condition = None
#TChiWZ.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiWZ_1 = TChiWZ.addMassPlane(motherMass = x, lspMass = y)
#----figure----
TChiWZ_1.figure = 'Figure 10-a'
TChiWZ_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.png'
#----limit source----
TChiWZ_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'obs_mu0', index = None )
TChiWZ_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'exp_mu0', index = None )
#----exclusion source----
TChiWZ_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_obs_smoothed', index = None )
TChiWZ_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_om1s_smoothed', index = None )
TChiWZ_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_op1s_smoothed', index = None )
TChiWZ_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_exp_smoothed', index = None )
TChiWZ_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_em1s_smoothed', index = None )
TChiWZ_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-024_Figure_010-a.root', 'root', objectName = 'gr_ep1s_smoothed', index = None )
#----global url settings ----
TChiWZ_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
#----limit url settings ----
TChiWZ_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
#----exclusion url settings ----
TChiWZ_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
TChiWZ_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-024/CMS-PAS-SUS-16-024_Figure_010-a.root'
'''
#+++++++ next txName block ++++++++++++++
TChiChipmSlepL = TxNameInput('TChiChipmSlepL')
TChiChipmSlepL.on.checked = ''
TChiChipmSlepL.off.checked = ''
TChiChipmSlepL.on.constraint = "[[['L'],['L']],[['L'],['nu']]]+[[['L'],['L']],[['nu'],['L']]]"
TChiChipmSlepL.off.constraint =
TChiChipmSlepL.on.conditionDescription =
TChiChipmSlepL.off.conditionDescription =
TChiChipmSlepL.on.condition =
TChiChipmSlepL.off.condition =
#TChiChipmSlepL.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL_1 = TChiChipmSlepL.addMassPlane(motherMass = , interMass0 = , lspMass = )
#TChiChipmSlepL_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmSlepL_1.figure =
TChiChipmSlepL_1.figureUrl =
#----limit source----
TChiChipmSlepL_1.obsUpperLimit.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL_1.obsExclusion.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.expExclusion.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
TChiChipmSlepL_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
TChiChipmSlepL_1.dataUrl =
#----limit url settings ----
TChiChipmSlepL_1.histoDataUrl =
TChiChipmSlepL_1.obsUpperLimit.dataUrl =
TChiChipmSlepL_1.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepL_1.exclusionDataUrl =
TChiChipmSlepL_1.obsExclusion.dataUrl =
TChiChipmSlepL_1.obsExclusionM1.dataUrl =
TChiChipmSlepL_1.obsExclusionP1.dataUrl =
TChiChipmSlepL_1.expExclusion.dataUrl =
TChiChipmSlepL_1.expExclusionM1.dataUrl =
TChiChipmSlepL_1.expExclusionP1.dataUrl =
'''
databaseCreator.create()

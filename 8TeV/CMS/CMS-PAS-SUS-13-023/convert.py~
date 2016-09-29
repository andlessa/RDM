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
info = MetaInfoInput('CMS-SUS-PAS-13-023')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13023'
info.sqrts = 8
info.lumi = 18.9 
info.prettyName = 'Fully hadronic Stop'
info.private = False
#info.arxiv = 
#info.contact =
#info.publication =
info.comment = 'PAS:http://inspirehep.net/record/1387812/files/SUS-13-023-pas.pdf'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint ="[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription = None
T2tt.off.conditionDescription = None
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure = 'Figure 13'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.png'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/T2tt__observed_xsection_UL.root', 'canvas', objectName = 'T2tt__observed_xsection_UL', index = 2 )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/T2tt_Obs.txt', 'txt', objectName = None, index = None )
T2tt_1.obsExclusionM1.setSource( 'orig/T2tt_ObsMinus.txt', 'txt', objectName = None, index = None )
T2tt_1.obsExclusionP1.setSource( 'orig/T2tt_ObsPlus.txt', 'txt', objectName = None, index = None )
#T2tt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13023'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
T2tt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
#T2tt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
T2tt_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
T2tt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
T2tt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2tt__observed_xsection_UL.root'
#T2tt_1.expExclusion.dataUrl =
#T2tt_1.expExclusionM1.dataUrl =
#T2tt_1.expExclusionP1.dataUrl =


#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked = ''
T6bbWW.off.checked =''
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="2.3*([[['b'],['jet','jet']],[['b'],['jet','jet']]])"
T6bbWW.on.conditionDescription = None
T6bbWW.off.conditionDescription = None
T6bbWW.on.condition = None
T6bbWW.off.condition = None
#T6bbWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T6bbWW_1 = T6bbWW.addMassPlane(motherMass = x , interMass0 = (0.75*x + 0.25*y) , lspMass = y)
#T6bbWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_1.figure = 'Figure 13'
T6bbWW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.png'
#----limit source----
T6bbWW_1.obsUpperLimit.setSource( 'orig/T2bw_0p25_observed_xsection_UL.root', 'canvas', objectName = 'T2bw_0p25_observed_xsection_UL', index = 2 )
#T6bbWW_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_1.obsExclusion.setSource( 'orig/T2bbWW_x025_Obs.txt', 'txt', objectName = None, index = None )
#T6bbWW_1.obsExclusionM1.setSource( 'orig/T2bbWW_x025_ObsMinus.txt', 'txt', objectName = None, index = None )
#T6bbWW_1.obsExclusionP1.setSource( 'orig/T2bbWW_x025_ObsPlus.txt', 'txt', objectName = None, index = None )
#T6bbWW_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
#----limit url settings ----
T6bbWW_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
#T6bbWW_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T6bbWW_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.obsExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.obsExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'
T6bbWW_1.expExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root' 
T6bbWW_1.expExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p25_observed_xsection_UL.root'


#+++++++ next mass plane block ++++++++++++++
T6bbWW_2 = T6bbWW.addMassPlane(motherMass = x , interMass0 = (0.25*x + 0.75*y)  , lspMass = y )
#T6bbWW_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_2.figure = 'Figure 13'
T6bbWW_2.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023//T2bw_0p75_observed_xsection_UL.pdf'
#----limit source----
T6bbWW_2.obsUpperLimit.setSource('orig/T2bw_0p75_observed_xsection_UL.root', 'canvas', objectName = 'T2bw_0p75_observed_xsection_UL', index = 2 )
#T6bbWW_2.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_2.obsExclusion.setSource( 'orig/T2bbWW_x075_Obs.txt', 'txt', objectName = None, index = None)
#T6bbWW_2.obsExclusionM1.setSource('orig/T2bbWW_x075_ObsMinus.txt', 'txt', objectName = None, index = None )
#T6bbWW_2.obsExclusionP1.setSource( 'orig/T2bbWW_x075_ObsPlus.txt', 'txt', objectName = None, index = None )
#T6bbWW_2.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_2.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
#----limit url settings ----
T6bbWW_2.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
#T6bbWW_2.expUpperlimit.dataUrl =
#----exclusion url settings ----
T6bbWW_2.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'
T6bbWW_2.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p75_observed_xsection_UL.root'

#+++++++ next mass plane block ++++++++++++++
T6bbWW_3 = T6bbWW.addMassPlane(motherMass = x , interMass0 = (0.5*x + 0.5*y)  , lspMass = y  )
#T6bbWW_3.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_3.figure = 'Figure 13'
T6bbWW_3.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023//T2bw_0p75_observed_xsection_UL.pdf'
#----limit source----
T6bbWW_3.obsUpperLimit.setSource('orig/T2bw_0p50_observed_xsection_UL.root', 'canvas', objectName = 'T2bw_0p50_observed_xsection_UL', index = 2  )
#T6bbWW_3.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_3.obsExclusion.setSource( 'orig/T2bbWW_x050_Obs.txt', 'txt', objectName = None, index = None )
#T6bbWW_3.obsExclusionM1.setSource('orig/T2bbWW_x050_ObsMinus.txt', 'txt', objectName = None, index = None )
#T6bbWW_3.obsExclusionP1.setSource( 'orig/T2bbWW_x050_ObsPlus.txt', 'txt', objectName = None, index = None )
#T6bbWW_3.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_3.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_3.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_3.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
#----limit url settings ----
T6bbWW_3.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
#T6bbWW_3.expUpperlimit.dataUrl =
#----exclusion url settings ----
T6bbWW_3.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'
T6bbWW_3.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13023/T2bw_0p50_observed_xsection_UL.root'

databaseCreator.create()


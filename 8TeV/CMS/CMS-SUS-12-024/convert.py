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
info = MetaInfoInput('CMS-SUS-12-024')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '19.4'
info.publication = 'http://www.sciencedirect.com/science/article/pii/S0370269313005339'
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12024'
#info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1305.2390'
info.contact = 'Keith Ulmer <keith.ulmer@cern.ch>, Josh Thompson <joshua.thompson@cern.ch>, Alessandro Gaz <alessandro.gaz@cern.ch>'
info.prettyName = '\slash{E}_{T}+b'
# info.supersedes = 

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked ="A"
#T1bbbb.off.checked =
T1bbbb.on.constraint ="[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription ="None"
#T1bbbb.off.condition =
T1bbbb.on.condition ="None"
#T1bbbb.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1bbbb = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1bbbb.obsUpperLimit.setSource( "orig/T1bbbb_exclusion_corrected.C", "cMacro", objectName = "hXsec_exp_corr", index = None )
## T1bbbb.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1bbbb.obsExclusion.setSource( "orig/T1bbbb_exclusion_corrected.C", "cMacro", objectName = "graph_smoothed_Obs_T1bbbb", index = None )
#T1bbbb.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1bbbb.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T1bbbb.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T1bbbb.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1bbbb.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T1bbbb.dataUrl =
#T1bbbb.histoDataUrl =
#T1bbbb.exclusionDataUrl =
#----figure----
T1bbbb.figure = "Fig 7 (left)"
T1bbbb.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1bbbb_exclusions_corrected.pdf"
#----limit url settings ----
T1bbbb.obsUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1bbbb_exclusions_corrected.C"
#T1bbbb.expUpperLimit.dataUrl =
#----exclusion url settings ----
T1bbbb.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1bbbb_exclusions_corrected.C"
#T1bbbb.obsExclusionM1.dataUrl =
#T1bbbb.obsExclusionP1.dataUrl =
#T1bbbb.expExclusion.dataUrl =
#T1bbbb.expExclusionM1.dataUrl =
#T1bbbb.expExclusionP1.dataUrl =

# +++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked ="A"
T1tttt.off.checked ="A"
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','b','W','W']],[['b','b','W','W']]]"
T1tttt.on.conditionDescription ="None"
T1tttt.off.conditionDescription ="None"
T1tttt.on.condition ="None"
T1tttt.off.condition ="None"

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tttt.obsUpperLimit.setSource( "orig/T1tttt_exclusion_corrected.C", "cMacro", objectName = "hXsec_obs_final", index = None )
# T1tttt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/T1tttt_exclusion_corrected.C", "cMacro", objectName = "graph_smoothed_Obs_T1tttt", index = None )
#T1tttt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T1tttt.dataUrl =
#T1tttt.histoDataUrl =
#T1tttt.exclusionDataUrl =
#----figure----
T1tttt.figure = "Fig 7 (right)"
T1tttt.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1tttt_exclusions_corrected.pdf"
#----limit url settings ----
T1tttt.obsUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1tttt_exclusion_corrected.C"
# T1tttt.expUpperLimit.dataUrl =
#----exclusion url settings ----
T1tttt.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12024/T1tttt_exclusion_corrected.C"
#T1tttt.obsExclusionM1.dataUrl =
#T1tttt.obsExclusionP1.dataUrl =
#T1tttt.expExclusion.dataUrl =
#T1tttt.expExclusionM1.dataUrl =
#T1tttt.expExclusionP1.dataUrl =

"""
#+++++++ next txName block ++++++++++++++
T5tttt = TxNameInput('T5tttt')
T5tttt.on.checked ="A"
T5tttt.off.checked =
T5tttt.on.constraint ="[[['t'],['t']],[['t'],['t']]]"
T5tttt.off.constraint =
T5tttt.on.condition ="None"
T5tttt.off.condition =
T5tttt.on.fuzzycondition ="None"
T5tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5ttttM11000 = T5tttt.addMassPlane(motherMass = 1000.0, interMass0 = x, lspMass = y)
#----limit source----
T5ttttM11000.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5ttttM11000.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttM11000.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5ttttM11000.dataUrl =
T5ttttM11000.histoDataUrl =
T5ttttM11000.exclusionDataUrl =
#----figure----
T5ttttM11000.figure =
T5ttttM11000.figureUrl =
#----limit url settings ----
T5ttttM11000.obsUpperLimit.dataUrl =
T5ttttM11000.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5ttttM11000.obsExclusion.dataUrl =
T5ttttM11000.obsExclusionM1.dataUrl =
T5ttttM11000.obsExclusionP1.dataUrl =
T5ttttM11000.expExclusion.dataUrl =
T5ttttM11000.expExclusionM1.dataUrl =
T5ttttM11000.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T5ttttLSP050 = T5tttt.addMassPlane(motherMass = x, interMass0 = y, lspMass = 50.0)
#----limit source----
T5ttttLSP050.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5ttttLSP050.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5ttttLSP050.dataUrl =
T5ttttLSP050.histoDataUrl =
T5ttttLSP050.exclusionDataUrl =
#----figure----
T5ttttLSP050.figure =
T5ttttLSP050.figureUrl =
#----limit url settings ----
T5ttttLSP050.obsUpperLimit.dataUrl =
T5ttttLSP050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5ttttLSP050.obsExclusion.dataUrl =
T5ttttLSP050.obsExclusionM1.dataUrl =
T5ttttLSP050.obsExclusionP1.dataUrl =
T5ttttLSP050.expExclusion.dataUrl =
T5ttttLSP050.expExclusionM1.dataUrl =
T5ttttLSP050.expExclusionP1.dataUrl =
"""

databaseCreator.create()

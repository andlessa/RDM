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
info = MetaInfoInput('CMS-SUS-13-012')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '19.5'
info.publication = 'JHEP06(2014)055'
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13012'
#info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1402.4770'
info.contact = 'cms-pag-conveners-sus@NOSPAMcernSPAMNOT.ch'
info.prettyName = ''
info.implementedBy = 'Federico A.'
# info.supersedes =







#+++++++ T2 Block  ++++++++++++++
T2 = TxNameInput('T2')
#T2.on.checked =" "
#T1bbbb.off.checked =
T2.on.constraint ="[[['jet']],[['jet']]]"
#T1bbbb.off.constraint =
T2.on.conditionDescription ="None"
#T1bbbb.off.condition =
T2.on.condition ="None"

T2 = T2.addMassPlane(motherMass = x, lspMass = y)

#+++++++ next mass plane block ++++++++++++++

T2.expUpperLimit.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expLimit", index = None )
T2.obsUpperLimit.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsLimit", index = None )
#----exclusion source----
T2.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T2.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T2.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T2.expExclusion.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T2.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T2.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )

#T1bbbb.dataUrl =
#T1bbbb.histoDataUrl =
#T1bbbb.exclusionDataUrl =
#----figure----
T2.figure = "Fig_7a"
T2.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7a.pdf"
T2.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T2qq.root"
#----limit url settings ----
T2.efficiencyMap.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/c_AccEffMap_T2qq.tar"
T2.expUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T2qq.root"
#----exclusion url settings ----
T2.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T2qq.root"







# +++++++ #T5VV block ++++++++++++++
#T5VV = TxNameInput('#T5VV')
##T5VV.on.checked =" "
##T5VV.off.checked =
#T5VV.on.constraint =""
##T5VV.off.constraint =
#T5VV.on.conditionDescription ="None"
##T5VV.off.condition =
#T5VV.on.condition ="None"
#T5VV = #T5VV.addMassPlane(motherMass = x, interMass0 = 0.5*(x+y), lspMass = y)


#+++++++ next mass plane block ++++++++++++++

#----limit source----
#T5VV.obsUpperLimit.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_obsLimit", index = None )
#T5VV.expUpperLimit.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_expLimit", index = None )
#----exclusion source----
#T5VV.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
#T5VV.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
#T5VV.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
#T5VV.expExclusion.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
#T5VV.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
#T5VV.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T5VV.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )
#----global url settings ----
#T1.dataUrl =
#T1.histoDataUrl =
#T1.exclusionDataUrl =
#----figure----
#T5VV.figure = "Fig_7d"
#T5VV.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7d.pdf"
#----limit url settings ----
#T5VV.efficiencyMap.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/c_AccEffMap_T5VV.tar"
#T5VV.expUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T5VV.root"
#----exclusion url settings ----
#T5VV.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T5VV.root"









#+++++++ T1tttt Block  ++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription ="None"
T1tttt.off.conditionDescription ="None"
T1tttt.off.condition = "None"
T1tttt.on.condition ="None"
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)


#+++++++ next mass plane block ++++++++++++++

#----limit source----
T1tttt.expUpperLimit.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root",  objectName = "combined_expLimit", index = None )
T1tttt.obsUpperLimit.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root",  objectName = "combined_obsLimit", index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T1tttt.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T1tttt.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T1tttt.expExclusion.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T1tttt.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T1tttt.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )
#----global url settings ----
#----figure----
T1tttt.figure = "Fig_7c"
T1tttt.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7c.pdf"
T1tttt.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1tttt.root"
#----limit url settings ----
T1tttt.efficiencyMap.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/c_AccEffMap_T1tttt.tar"
T1tttt.expUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1tttt.root"
#----exclusion url settings ----
T1tttt.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1tttt.root"












# +++++++ T1 block ++++++++++++++
T1 = TxNameInput('T1')
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.on.conditionDescription ="None"
T1.on.condition ="None"
T1 = T1.addMassPlane(motherMass = x, lspMass = y)


#+++++++ next mass plane block ++++++++++++++

#----limit source----

T1.expUpperLimit.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expLimit", index = None )
T1.obsUpperLimit.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsLimit", index = None )
#----exclusion source----
T1.obsExclusion.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclOneTimesProspino", index = None )
T1.obsExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclMinusSysErrProspino", index = None )
T1.obsExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclPlusSysErrProspino", index = None )
T1.expExclusion.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclOneTimesProspino", index = None )
T1.expExclusionM1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino", index = None )
T1.expExclusionP1.setSource( "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino", index = None )

#----global url settings ----
#T1.dataUrl =
#T1.histoDataUrl =
#T1.exclusionDataUrl =
#----figure----
T1.figure = "Fig_7b"
T1.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7b.pdf"
T1.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1qqqq.root"
#----limit url settings ----
T1.efficiencyMap.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/c_AccEffMap_T1qqqq.tar"
T1.expUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1qqqq.root"
#----exclusion url settings ----
T1.obsExclusion.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/SUS13012_XsecLimits_T1qqqq.root"


databaseCreator.create()
















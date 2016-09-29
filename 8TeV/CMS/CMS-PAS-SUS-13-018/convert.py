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
info = MetaInfoInput('CMS-PAS-SUS-13-018')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13018'
info.sqrts = 8
info.lumi = 19.4
info.prettyName = ''
info.private = False
info.arxiv = ''
info.contact = ''
info.publication = ''
info.comment = 'Only https://cds.cern.ch/record/1693164?ln=it document,will be superseeded by CMS-SUS-14-001'
info.supersedes =''
info.supersededBy = ''

#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =''
T2bb.off.checked =''
T2bb.on.constraint = "[[['b']],[['b']]]"
#T2bb.off.constraint = ''
T2bb.on.conditionDescription = None
T2bb.off.conditionDescription =''
T2bb.on.condition = None
#T2bb.off.condition =
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2bb_1.figure = 'Fig. 6'
T2bb_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.png'
#----limit source----
T2bb_1.obsUpperLimit.setSource( 'orig/combined_expLimit.root', 'root', objectName = 'combined_expLimit', index = None )
#T2bb_1.expUpperLimit.setSource( 'orig/T2bbXSEC.C', 'cMacro', objectName = None, index = None )
#----exclusion source----
T2bb_1.obsExclusionM1.setSource( 'orig/combined_obsExclMinusSysErrProspino.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino', index = None )
T2bb_1.obsExclusion.setSource( 'orig/combined_obsExclOneTimesProspino.root', 'root', objectName = 'combined_obsExclOneTimesProspino', index = None )
T2bb_1.obsExclusionP1.setSource( 'orig/combined_obsExclPlusSysErrProspino.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino', index = None )
T2bb_1.expExclusion.setSource( 'orig/combined_expExclOneTimesProspino.root', 'root', objectName = 'combined_expExclOneTimesProspino', index = None )
T2bb_1.expExclusionM1.setSource( 'orig/combined_expExclMinusOneSigmaProspino.root', 'root', objectName = 'combined_expExclMinusOneSigmaProspino', index = None )
T2bb_1.expExclusionP1.setSource( 'orig/combined_expExclPlusOneSigmaProspino.root', 'root', objectName = 'combined_expExclPlusOneSigmaProspino', index = None )
#----global url settings ----
T2bb_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13018'
#----limit url settings ----
T2bb_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
T2bb_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.expUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#----exclusion url settings ----
T2bb_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
T2bb_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.obsExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'
#T2bb_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13018/T2bbXSEC.C'

databaseCreator.create()

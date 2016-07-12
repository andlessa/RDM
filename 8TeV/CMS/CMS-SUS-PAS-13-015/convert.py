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
info = MetaInfoInput('CMS-SUS-PAS-13-015')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13015'
info.sqrts = 8
info.lumi = 19.4
info.prettyName =''
info.private = False
info.arxiv = ''
info.contact =''
info.publication ='http://cds.cern.ch/record/1635353/files/SUS-13-015-pas.pdf'
info.comment ='PAS so no arxiv publication - only cds.cern. SuperseedeBy CMS-SUS-14-001 which has no public data.'
info.supersedes =''
#info.supersededBy ='CMS-SUS-14-001'

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint ="[[['W','b']],[['W','b']]]"
T2tt.on.conditionDescription =None
T2tt.off.conditionDescription =None
T2tt.on.condition =None
T2tt.off.condition =None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x , lspMass =  y)
#----figure----
T2tt_1.figure ='Fig. 8'
T2tt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.png'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_expLimit', index = None )
#T2tt_1.expUpperLimit.setSource( 'orig/SUS-13-015-Extracted_Limits.root/', type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_obsExclOneTimesProspino', index = None )
T2tt_1.obsExclusionM1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino', index = None )
T2tt_1.obsExclusionP1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino', index = None )
T2tt_1.expExclusion.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_expExclOneTimesProspino', index = None )
T2tt_1.expExclusionM1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino', index = None )
T2tt_1.expExclusionP1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino', index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13015'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
#T2tt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.obsExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.obsExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.expExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.expExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'
T2tt_1.expExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/T2tt_alt_combined_all_fullToysXSEC.C'

databaseCreator.create()

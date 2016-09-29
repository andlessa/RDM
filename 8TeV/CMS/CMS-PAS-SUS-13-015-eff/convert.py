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
info = MetaInfoInput('CMS-PAS-SUS-13-015')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13015'
info.sqrts = 8
info.lumi = 19.4
info.prettyName =''
info.private = False
info.arxiv = ''
info.contact =''
info.publication ='http://cds.cern.ch/record/1635353/files/SUS-13-015-pas.pdf'
info.comment ='PAS so no arxiv publication - only cds.cern; whenever the error on the expected SM background is asymmetric for some signal regions, the largest value is used'
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
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass =  y)
#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'Fig. 11'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_baseline.png'
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_obsExclOneTimesProspino', index = None )
T2tt_1.obsExclusionM1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino', index = None )
T2tt_1.obsExclusionP1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino', index = None )
T2tt_1.expExclusion.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_expExclOneTimesProspino', index = None )
T2tt_1.expExclusionM1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino', index = None )
T2tt_1.expExclusionP1.setSource( 'orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino', index = None )
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/eff_baseline.root', 'root', objectName = 'eff_baseline', index = None, dataset="pTmiss200_Nb1" )
T2tt_1.efficiencyMap.setStatistics( observedN= 254, expectedBG= 254.3, bgError=35 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_baseline.C'
databaseCreator.create()


#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'Fig. 11'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_highMET.png'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/eff_baseline_2b.root', 'root', objectName = 'eff_baseline_2b', index = None, dataset="pTmiss350_Nb1" )
T2tt_1.efficiencyMap.setStatistics( observedN= 45, expectedBG=40.9, bgError=9.6 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_baseline_2b.C'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure ='Fig. 11'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_baseline_2b.png'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/eff_highMET.root', 'root', objectName = 'eff_highMET', index = None, dataset="pTmiss200_Nb2" )
T2tt_1.efficiencyMap.setStatistics( observedN=83, expectedBG=88.4, bgError=19.8 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_highMET.C'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'Fig. 11'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_highMET_2b.png'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/eff_highMET_2b.root', 'root', objectName = 'eff_highMET_2b', index = None, dataset="pTmiss350_Nb2" )
T2tt_1.efficiencyMap.setStatistics( observedN=15, expectedBG=8.6, bgError=7.1 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13015/picked_eff_T2tt_highMET_2b.C'
databaseCreator.create(True)



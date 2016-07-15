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
info = MetaInfoInput('CMS-SUS-14-021')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
info.sqrts = 8
info.lumi = 19.7
info.prettyName = 'stop 4body decay'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1512.08002'
info.contact = ''
info.publication =''
info.comment ='ISR production'
info.supersedes =''
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T2bbWW = TxNameInput('T2bbWW')
T2bbWW.on.checked = ''
T2bbWW.off.checked = ''
T2bbWW.on.constraint = "[[['b','W']],[['b','W']]]"
T2bbWW.off.constraint = "[[['b','L','nu']],[['b','L','nu']]]+[[['b','q','q']],[['b','q','q']]]+[[['b','q','q']],[['b','L','nu']]]"
T2bbWW.on.conditionDescription = None
T2bbWW.off.conditionDescription =None
T2bbWW.on.condition =None
T2bbWW.off.condition =None
#T2bbWW.branchingRatio =x

#+++++++ next mass plane block ++++++++++++++
T2bbWW_1 = T2bbWW.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T2bbWW_1.figure = 'efficienciesSRSL1a'
T2bbWW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL1a.png'
#----exclusion source----
T2bbWW_1.obsExclusion.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObserved', index = None )
T2bbWW_1.obsExclusionM1.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObservedDown', index = None )
T2bbWW_1.obsExclusionP1.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gObservedUp', index = None )
T2bbWW_1.expExclusion.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpected', index = None )
T2bbWW_1.expExclusionM1.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpectedDown', index = None )
T2bbWW_1.expExclusionP1.setSource( 'orig/singleLeptonLimitHistograms.root', 'root', objectName = 'gExpectedUp', index = None )
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/efficienciesSRSL.root', 'root', objectName = 'effSRSL1a',  index = None, dataset="SRSL1a" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=121, expectedBG=134.5, bgError=19.8 )
#----global url settings ----
T2bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL.root'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2bbWW_1.figure ='efficienciesSRSL1b'
T2bbWW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL1b.png'
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/efficienciesSRSL.root', 'root', objectName = 'effSRSL1b', index = None, dataset="SRSL1b" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=59, expectedBG=81.3, bgError=19.1 )
#----global url settings ----
T2bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bbWW_1.figure = 'efficienciesSRSL1c'
T2bbWW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL1c.png'
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/efficienciesSRSL.root', 'root', objectName = 'effSRSL1c', index = None, dataset="SRSL1c" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=12, expectedBG=12.3, bgError=4.0 )
#----global url settings ----
T2bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bbWW_1.figure = 'efficienciesSRSL2'
T2bbWW_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL2.png'
#----limit source----
T2bbWW_1.efficiencyMap.setSource( 'orig/efficienciesSRSL.root', 'root', objectName = 'effSRSL2', index = None, dataset="SRSL2" )
T2bbWW_1.efficiencyMap.setStatistics( observedN=41, expectedBG=32.1, bgError=7.7 )
#----global url settings ----
T2bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14021'
#----efficiency map url settings ----
T2bbWW_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14021/efficienciesSRSL.root'
databaseCreator.create(True)



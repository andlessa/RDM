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
info = MetaInfoInput('CMS-SUS-13-011')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
info.sqrts = 8
info.lumi = 19.5
info.prettyName = ''
info.private = False
info.arxiv = 'arXiv:1308.1586v2'
info.contact =''
info.publication = 'Eur. Phys. J. C 73 (2013) 2677'
info.comment = ''
info.supersedes =''
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint =  "[[['t']],[['t']]]"
T2tt.off.constraint = "[[['W','b']],[['W','b']]]"
T2tt.on.conditionDescription ="None"
T2tt.off.conditionDescription ="None"
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/SUS13011_T2tt_exclusion.txt', 'txt', objectName = 'observed_exclusion', index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( 'orig/topneutralino_cutbased.root', 'root', objectName = 'expected_exclusion', index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_LM150', index = None, dataset="LM150" )
T2tt_1.efficiencyMap.setStatistics( observedN=227, expectedBG=251, bgError=50 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create()


#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_LM200', index = None, dataset="LM200" )
T2tt_1.efficiencyMap.setStatistics( observedN=69, expectedBG=83, bgError=21 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_LM250', index = None, dataset="LM250" )
T2tt_1.efficiencyMap.setStatistics( observedN=21, expectedBG=31, bgError=8 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_LM300', index = None, dataset="LM300" )
T2tt_1.efficiencyMap.setStatistics( observedN=9, expectedBG=11.5, bgError=3.6 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_HM150', index = None, dataset="HM150" )
T2tt_1.efficiencyMap.setStatistics( observedN=23, expectedBG=29, bgError=7 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_HM200', index = None, dataset="HM200" )
T2tt_1.efficiencyMap.setStatistics( observedN=11, expectedBG=17, bgError=5 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_HM250', index = None, dataset="HM250" )
T2tt_1.efficiencyMap.setStatistics( observedN=3, expectedBG=9.5, bgError=2.8 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2tt_1.figure = 'topneutralino_cutbased_efficiencies'
T2tt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.pdf'
#----limit source----
T2tt_1.efficiencyMap.setSource( 'orig/topneutralino_cutbased_efficiencies.root', 'root', objectName = 'efficiency_HM300', index = None, dataset="HM300" )
T2tt_1.efficiencyMap.setStatistics( observedN=2, expectedBG=4.7, bgError=1.4 )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----efficiency map url settings ----
T2tt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased_efficiencies.root'
databaseCreator.create(True)



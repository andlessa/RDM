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
info = MetaInfoInput('CMS-SUS-14-010')
info.url = "https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS14010"
info.sqrts = 8
info.lumi = 19.5
info.prettyName =""
info.private = False
info.arxiv ="http://arxiv.org/abs/arXiv:1412.4109"
info.contact =""
info.publication ="Phys. Lett. B 745 (2015) 5"
info.comment =""
info.supersedes =""
info.supersededBy =""

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =""
T1tttt.off.checked =""
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription ="None"
T1tttt.off.conditionDescription ="None"
T1tttt.on.condition ="None"
T1tttt.off.condition ="None"
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure ='5a'
T1tttt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1CombXSEC.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'observedUL', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'expectedUL', index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
T1tttt_1.expUpperLimit.unit = 'fb'
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'observed_graph', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'observed_minus_graph', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'observed_plus_graph' , index= None )
T1tttt_1.expExclusion.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'expected_graph', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'expected_minus_graph', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/T1tttt_combination.root', 'root', objectName = 'expected_plus_graph', index = None )
#----global url settings ----
T1tttt_1.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1tttt_combination.root"
#----limit url settings ----
T1tttt_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1CombXSEC.pdf'
T1tttt_1.obsUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1tttt_combination.root"
T1tttt_1.expUpperLimit.dataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1tttt_combination.root"
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ="https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS14010/T1tttt_combination.root"
T1tttt_1.obsExclusion.dataUrl =''
T1tttt_1.obsExclusionM1.dataUrl =''
T1tttt_1.obsExclusionP1.dataUrl =''
T1tttt_1.expExclusion.dataUrl =''
T1tttt_1.expExclusionM1.dataUrl =''
T1tttt_1.expExclusionP1.dataUrl =''

databaseCreator.create()

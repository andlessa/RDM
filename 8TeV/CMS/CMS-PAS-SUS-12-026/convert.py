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
info = MetaInfoInput('CMS-PAS-SUS-12-026')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12026'
info.sqrts = 8
info.lumi = 9.2
info.prettyName = ''
info.private = False
info.arxiv = ''
info.contact =''
info.publication = ''
info.comment = 'Only CDS entry http://cdsweb.cern.ch/record/1496879/files/SUS-12-026-pas.pdf'
info.supersedes = 'None'
info.supersededBy = 'CMS-SUS-13-002'

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription = None
T1tttt.off.conditionDescription = None
T1tttt.on.condition = None
T1tttt.off.condition = None
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure = 'Fig. 7'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/curve_T1tttt_overlay_observed.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/Limit_T1tttt.root', 'root', objectName = 'LimitObs', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/Limit_T1tttt.root', 'root', objectName = 'LimitExp', index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
T1tttt_1.expUpperLimit.unit = 'fb'
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_Excl.txt', 'txt', objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12026'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'
T1tttt_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12026/Limit_T1tttt.root'

databaseCreator.create()

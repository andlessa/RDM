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
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-002')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13002'
info.sqrts = 8
info.lumi =  19.5
info.prettyName = ''
info.private = False
info.arxiv = 'http://arxiv.org/abs/1404.5801v2'
info.contact =''
info.publication = 'http://journals.aps.org/prd/abstract/10.1103/PhysRevD.90.032006'
info.comment =''
info.supersedes = 'CMS-PAS-SUS-12-026'
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription = None
#T1tttt.off.conditionDescription =
T1tttt.on.condition =None
#T1tttt.off.condition =
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass =y )
#----figure----
T1tttt_1.figure = 'Figure 11'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/curve_T1tttt_overlay_observed.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/Limit_T1tttt.root', 'root', objectName = 'hrObs', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/Limit_T1tttt.root', 'root', objectName = 'hrExp', index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
#----exclusion source----
T1tttt_1.obsExclusion.setSource(   'orig/contours_T1tttt.root', 'root', objectName = 'Observed', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/contours_T1tttt.root', 'root', objectName = 'Observed1m', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/contours_T1tttt.root', 'root', objectName = 'Observed1p', index = None )
T1tttt_1.expExclusion.setSource(   'orig/contours_T1tttt.root', 'root', objectName = 'Expected', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/contours_T1tttt.root', 'root', objectName = 'Expected1m', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/contours_T1tttt.root', 'root', objectName = 'Expected1p', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13002'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/curve_T1tttt_overlay_observed.pdf'
T1tttt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/Limit_T1tttt.root'
T1tttt_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/Limit_T1tttt.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13002'
T1tttt_1.obsExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'
T1tttt_1.obsExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'
T1tttt_1.obsExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'
T1tttt_1.expExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'
T1tttt_1.expExclusionM1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'
T1tttt_1.expExclusionP1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13002/contours_T1tttt.root'

databaseCreator.create()

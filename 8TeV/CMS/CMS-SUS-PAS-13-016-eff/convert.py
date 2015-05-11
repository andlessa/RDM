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
info = MetaInfoInput('CMS-SUS-PAS-13-016')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '19.7'
#info.publication = 
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13016'
#info.superseded_by = 
#info.arxiv = 
#info.contact = 
info.prettyName = 'OS + b'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked ="VM"
#T1tttt.off.checked =
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','b','W','W']],[['b','b','W','W']]]"
T1tttt.on.condition ="None"
T1tttt.off.condition ="None"
T1tttt.on.conditionDescription ="None"
T1tttt.off.conditionDescription ="None"

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tttt.efficiencyMapList.addSource( "sr0", "orig/Acceptance_OS_T1tttt.root", "root", objectName = "AccANN", index = None )
# T1tttt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_ns", index = None )
T1tttt.obsExclusionM1.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_ns0", index = None )
T1tttt.obsExclusionP1.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_ns1", index = None )
T1tttt.expExclusion.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_nsE", index = None )
T1tttt.expExclusionM1.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_nsE0", index = None )
T1tttt.expExclusionP1.setSource( "orig/Results_SUS13016.root", "root", objectName = "GR_nsE1", index = None )
#----global url settings ----
#----limit url settings ----
T1tttt.obsUpperLimit.dataUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13016/Results_SUS13016.root"
#T1tttt.expUpperLimit.dataUrl =
##----exclusion url settings ----
#T1tttt.obsExclusion.dataUrl =
#T1tttt.obsExclusionM1.dataUrl =
#T1tttt.obsExclusionP1.dataUrl =
#T1tttt.expExclusion.dataUrl =
#T1tttt.expExclusionM1.dataUrl =
#T1tttt.expExclusionP1.dataUrl =

databaseCreator.create()

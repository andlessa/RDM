#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt, txname.txt, twiki.txt and sms.py.

.. moduleauthor: Wolfgang Waltenberger

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', \
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
from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y


#+++++++ global info block ++++++++++++++
info = MetaInfo('ATLAS-CONF-2013-047-ANA7-CUT0')
info.url ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/' 
info.sqrts = 8
info.lumi = 20.3
info.prettyname = '0 leptons + jets + met'
info.private = True
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='fastlim'
info.publication = 'http://cds.cern.ch/record/1547563'
info.comment = 'created from fastlim-1.0'
info.superseded_by ='SUSY-2013-02'
info.implemented_by = 'Wolfgang Waltenberger'
info.observedN = 5333
info.expectedBG = 4700
info.bgError = 500

#+++++++ next txName block ++++++++++++++
T1 = TxName('T1')
T1.on.constraint = "[[['jet','jet']],[['jet','jet']]]"
T1.on.condition = None
T1.on.fuzzycondition = None

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x , lspMass = y )
#----figure----
T1_1.figure = 'fig_07a.pdf'
T1_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'
# ----limit source----
T1_1.efficiencyMap.setSource( './orig/ana_7_cut_0.effi', 'txt', objectName = None, index = None )
# T1_1.obsUpperLimit.unit = 'fb'
# T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
# ----exclusion source----
T1_1.obsExclusion.setSource( './orig/T1_exc.dat', 'txt', objectName = None, index = None )
#T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T1_1.dataUrl = 
#T1_1.histoDataUrl = 
#----limit url settings ----
# T1_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_A.txt'
#T1_1.expectedlimit.dataUrl =
#----exclusion url settings ----
#T1_1.exclusionDataUrl =
#T1_1.exclusion.dataUrl =
#T1_1.exclusionM1.dataUrl =
#T1_1.exclusionP1.dataUrl =
#T1_1.expectedExclusion.dataUrl =
#T1_1.expectedExclusionM1.dataUrl =
#T1_1.expectedExclusionP1.dataUrl =

databaseCreator.create()

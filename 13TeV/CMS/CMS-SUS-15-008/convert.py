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
info = MetaInfoInput('CMS-SUS-15-008')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/index.html'
info.sqrts = 13
info.lumi = 2.3
info.prettyName = 'same-sign dilepton'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1605.03171'
#info.contact =
info.publication = 'http://dx.doi.org/10.1140/epjc/s10052-016-4261-z'
info.comment = 'Only T1tttt can be implemneted (other topologies have only up to 2 mass planes)'
#info.supersedes = 
#info.supersededBy =

T1tttt = TxNameInput('T1tttt')
#T1tttt.on.checked =
#T1tttt.off.checked =
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','W','b','W']],[['b','W','b','W']]]"
T1tttt.on.conditionDescription = None
T1tttt.off.conditionDescription = None
T1tttt.on.condition = None
T1tttt.off.condition = None

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass =x , lspMass =y )


#----figure----
T1tttt_1.figure = 'Fig.4a'
T1tttt_1.figureUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/CMS-SUS-15-008_Figure_004-a.root', 'root', objectName = 'xsec', index = None )
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/CMS-SUS-15-008_Figure_004-a.root', 'root', objectName ='ssobs' , index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/CMS-SUS-15-008_Figure_004-a.root', 'root', objectName = 'ssobs_m1s', index = None )
T1tttt_1.obsExclusionP1.setSource('orig/CMS-SUS-15-008_Figure_004-a.root', 'root' , objectName = 'ssobs_p1s', index = None )
T1tttt_1.expExclusion.setSource('orig/CMS-SUS-15-008_Figure_004-a.root', 'root' , objectName = 'ssexp', index = None )
T1tttt_1.expExclusionM1.setSource('orig/CMS-SUS-15-008_Figure_004-a.root', 'root' , objectName = 'ssexp_m1s', index = None )
T1tttt_1.expExclusionP1.setSource('orig/CMS-SUS-15-008_Figure_004-a.root', 'root' , objectName = 'ssexp_p1s', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
#T1tttt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.obsExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.obsExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.obsExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.expExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.expExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'
T1tttt_1.expExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-15-008/CMS-SUS-15-008_Figure_004-a.root'

databaseCreator.create()

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
info = MetaInfoInput('CMS-PAS-SUS-16-019')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/index.html'
info.sqrts = 13
info.lumi = 12.9
#info.prettyName =
info.private = False
#info.arxiv = 
#info.contact =
#info.publication =
info.comment = 'https://cds.cern.ch/record/2204932'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"	
T1tttt.on.conditionDescription =None
T1tttt.off.conditionDescription =None
T1tttt.on.condition =None
T1tttt.off.condition =None
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure = 'Figure 6-a'
T1tttt_1.figureUrl = 'cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'canvas', objectName = 'cCONT_XSEC', index = 2 )
T1tttt_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'hXsec_exp_corr', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_ObsM', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T1tttt_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_Exp', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_ObsM', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-a.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
#T1tttt_1.obsUpperLimit.dataUrl =
T1tttt_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'
T1tttt_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-a.root'

'''
#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked =''
T5WW.off.checked =''
T5WW.on.constraint = "[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint =None
T5WW.on.conditionDescription =None	
T5WW.off.conditionDescription =None
T5WW.on.condition =None
T5WW.off.condition =None
#T5WW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane(motherMass = x, interMass0 = .5*(x+y), lspMass = y)
#T5WW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T5WW_1.figure = 'Figure 6-b'
T5WW_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.png'
#----limit source----
T5WW_1.obsUpperLimit.setSource(  'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'canvas', objectName = 'cCONT_XSEC', index = 2 )
T5WW_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'hXsec_exp_corr', index = None )
#----exclusion source----
T5WW_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T5WW_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_ObsM', index = None )
T5WW_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T5WW_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_Exp', index = None )
T5WW_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_ExpM', index = None )
T5WW_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-019_Figure_006-b.root', 'root', objectName = 'graph_smoothed_', index = None )
#----global url settings ----
T5WW_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
#----limit url settings ----
T5WW_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
#----exclusion url settings ----
T5WW_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
T5WW_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-019/CMS-PAS-SUS-16-019_Figure_006-b.root'
'''
databaseCreator.create()

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
type = str )
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
help = 'path to the package smodels_utils',\
type = str )
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
info = MetaInfoInput('CMS-PAS-SUS-16-022')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/'
info.sqrts = 13
info.lumi = 12.9
#info.prettyName =
#info.private =
#info.arxiv = 
#info.contact =
#info.publication =
info.comment = 'https://cds.cern.ch/record/2205165'
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
T1tttt_1.figure = 'Figure 5-a'
T1tttt_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'obs_xs0', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'exp_xs0', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'gr_obs_smoothed', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'gr_om1s_smoothed', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'gr_op1s_smoothed', index = None )
T1tttt_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'gr_exp_smoothed', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root', objectName = 'gr_em1s_smoothed', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-022_Figure_005-a.root', 'root' , objectName = 'gr_ep1s_smoothed', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
#----exclusion url settings ---- 
T1tttt_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root' 
T1tttt_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'
T1tttt_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-022/CMS-PAS-SUS-16-022_Figure_005-a.root'


databaseCreator.create()

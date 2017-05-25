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
info = MetaInfoInput('CMS-PAS-SUS-16-016')
info.url = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
info.sqrts = 13
info.lumi = 12.9
#info.prettyName =
info.private = False
#info.arxiv =
#info.contact =
#info.publication =
info.comment = "Only CDS entry https://cds.cern.ch/record/2205163"
#info.supersedes =
#info.supersededBy = 'SUS-16-016'

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked =''
T1bbbb.off.checked =''
T1bbbb.on.constraint ="[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription =None
#T1bbbb.off.conditionDescription =
T1bbbb.on.condition =None
#T1bbbb.off.condition =
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure = "Figure 5-a"
T1bbbb_1.figureUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.png"
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( "orig/CMS-PAS-SUS-16-016_Figure_005-a.root", "root", objectName = 'observed_limit_xs_noInterpolation', index = None )
T1bbbb_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-a.root', 'root', objectName = 'expected_limit_xs_noInterpolation', index = None )
#T1bbbb_1.obsUpperLimit.setSource( "orig/CMS-PAS-SUS-16-016_Figure_005-a.root", "root", objectName = 'observed_limit_mu', index = None )
#T1bbbb_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-a.root', 'root', objectName = 'expected_limit_mu', index = None )

#----exclusion source----
T1bbbb_1.obsExclusion.setSource( "orig/T1bbbbObs.dat", "txt", objectName = None, index = None )
#T1bbbb_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-a.root', 'root', objectName = 'ObsLimSdn', index = None )
#T1bbbb_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-a.root', 'root', objectName = 'ObsLimSup', index = None )
T1bbbb_1.expExclusion.setSource( 'orig/T1bbbbExp.dat', 'txt', objectName = None, index = None )
#T1bbbb_1.obsUpperLimit.setSource( "orig/CMS-PAS-SUS-16-016_Figure_005-a.root", "root", objectName = 'observed_limit_mu_noInterpolation', index = None )
#T1bbbb_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-a.root', 'root', objectName = 'expected_limit_mu_noInterpolation', index = None )
#---- global url settings ----
T1bbbb_1.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"

#----limit url settings ----
T1bbbb_1.histoDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T1bbbb_1.obsUpperLimit.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root"
T1bbbb_1.expUpperLimit.dataUrl =  "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root"

#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T1bbbb_1.obsExclusion.dataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root'
T1bbbb_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.roott'
T1bbbb_1.obsExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root'
T1bbbb_1.expExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root'
T1bbbb_1.expExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root'
T1bbbb_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-a.root'

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
T1tttt.off.checked =''
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]" 
T1tttt.on.conditionDescription =None
T1tttt.off.conditionDescription =None
T1tttt.on.condition =None
T1tttt.off.condition =None
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure = "Figure 5-b"
T1tttt_1.figureUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html#Figure_005-b"
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'observed_limit_xs_noInterpolation', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'expected_limit_xs_noInterpolation', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1ttttObs.dat', 'txt', objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'ObsLimSdn', index = None )
#T1tttt_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'ObsLimSup', index = None )
T1tttt_1.expExclusion.setSource( 'orig/T1ttttExp.dat', 'txt', objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'ExpLimSdn', index = None )
#T1tttt_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-b.root', 'root', objectName = 'ExpLimSup', index = None  )
#----global url settings ----
T1tttt_1.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
#----limit url settings ----
T1tttt_1.histoDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T1tttt_1.obsUpperLimit.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root"
#T1tttt_1.expUpperLimit.dataUrl = 
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T1tttt_1.obsExclusion.dataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root'
T1tttt_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.roott'
T1tttt_1.obsExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root'
T1tttt_1.expExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root'
T1tttt_1.expExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root'
T1tttt_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-b.root'















#+++++++ next mass plane block ++++++++++++++

T2 = TxNameInput('T2bb')
T2.on.checked =''
T2.off.checked =''
T2.on.constraint ="[[['b']],[['b']]]"
T2.off.constraint =None
T2.on.conditionDescription =None
T2.off.conditionDescription =None
T2.on.condition =None
T2.off.condition =None
#T2.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2_1.figure = "Figure 5-c"
T2_1.figureUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.png"
#----limit source----
T2_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'observed_limit_xs_noInterpolation', index = None )
T2_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'expected_limit_xs_noInterpolation', index = None )
#----exclusion source----
T2_1.obsExclusion.setSource( 'orig/T2bbObs.dat', 'txt', objectName = None, index = None )
#T2_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'ObsLimSdn', index = None )
#T2_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'ObsLimSup', index = None )
T2_1.expExclusion.setSource( 'orig/T2bbExp.dat', 'txt', objectName = None, index = None )
#T2_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'ExpLimSdn', index = None )
#T2_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-c.root', 'root', objectName = 'ExpLimSup', index = None  )
#----global url settings ----
T2_1.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
#----limit url settings ----
T2_1.histoDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T2_1.obsUpperLimit.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root"
#T2_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2_1.exclusionDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T2_1.obsExclusion.dataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root'
T2_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.roott'
T2_1.obsExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root'
T2_1.expExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root'
T2_1.expExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root'
T2_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-c.root'



T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint ="[[['t']],[['t']]]"
T2tt.off.constraint = "[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription =None
T2tt.off.conditionDescription =None
T2tt.on.condition =None
T2tt.off.condition =None
#T2.branchingRatio =    

#+++++++ next mass plane block ++++++++++++++
T2tt_2 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_2.figure = "Figure 5-d"
T2tt_2.figureUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.png"
#----limit source----
T2tt_2.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = "observed_limit_xs_noInterpolation", index = None )
T2tt_2.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = 'expected_limit_xs_noInterpolation', index = None )
#----exclusion source----
T2tt_2.obsExclusion.setSource( 'orig/T2ttObs.dat', 'txt', objectName = None, index = None )
#T2_2.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = 'ObsLimSdn', index = None )
#T2_2.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = 'ObsLimSup', index = None )
T2tt_2.expExclusion.setSource( 'orig/T2ttExp.dat', 'txt', objectName = None, index = None )
#T2_2.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = 'ExpLimSdn', index = None )
#T2_2.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-016_Figure_005-d.root', 'root', objectName = 'ExpLimSup', index = None  )
#----global url settings ----
T2tt_2.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
#----limit url settings ----
T2tt_2.histoDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T2tt_2.obsUpperLimit.dataUrl = "http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root"
#T2_2.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_2.exclusionDataUrl ="http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/index.html"
T2tt_2.obsExclusion.dataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root'
T2tt_2.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.roott'
T2tt_2.obsExclusionP1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root'
T2tt_2.expExclusion.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root'
T2tt_2.expExclusionM1.dataUrl ='http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root'
T2tt_2.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-016/CMS-PAS-SUS-16-016_Figure_005-d.root'


databaseCreator.create()

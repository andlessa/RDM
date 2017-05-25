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
info = MetaInfoInput('CMS-PAS-SUS-16-014')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/'
info.sqrts = 13
info.lumi = 12.9
#info.prettyName =
info.private = False
#info.arxiv = 
#info.contact =
#info.publication =
info.comment ='Only CDS entry:https://cds.cern.ch/record/2205158'
#info.supersedes =
#info.supersededBy =

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
T1tttt_1.figure = 'Figure 10-a'
T1tttt_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'MassScan2D', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'MassScan2DExp', index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ObsLim', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ObsLimSdn', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ObsLimSup', index = None )
T1tttt_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ExpLim', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ExpLimSdn', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-a.root', 'root', objectName = 'ExpLimSup', index = None )
#----global url settings ----
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'
T1tttt_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-a.root'

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint ="[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription = None
T2tt.off.conditionDescription = None
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure = 'Figure 9-a'
T2tt_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.png'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'MassScan2D', index = None )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ObsLim2', index = None )
T2tt_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ObsLimSdn2', index = None )
T2tt_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ObsLimSup2', index = None )
T2tt_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ExpLim', index = None )
T2tt_1.expExclusionM1.setSource('orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ExpLimSdn2', index = None )
T2tt_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-a.root', 'root', objectName = 'ExpLimSup', index = None )
# The lables of the histograms are correct, they messed up with the namings (the offshell region is not considered in the plots )x
#----global url settings ----
T2tt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/index.html'
#----limit url settings ----
T2tt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/index.html'
T2tt_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'
T2tt_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-a.root'

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked =''
#T1bbbb.off.checked =''
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =
T1bbbb.on.conditionDescription = None
#T1bbbb.off.conditionDescription = None
T1bbbb.on.condition = None
#T1bbbb.off.condition = None
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1bbbb_1.figure = 'Figure 10-b'
T1bbbb_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'MassScan2D', index = None )
#T1bbbb_1.expUpperLimit.setSource( path, 'root', objectName = None, index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ObsLim', index = None )
T1bbbb_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ObsLimSdn', index = None )
T1bbbb_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ObsLimSup', index = None )
T1bbbb_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ExpLim', index = None )
T1bbbb_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ExpLimSdn', index = None )
T1bbbb_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-b.root', 'root', objectName = 'ExpLimSup', index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
#----limit url settings ----
T1bbbb_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'
T1bbbb_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-b.root'

#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
T2.on.checked =''
#T2.off.checked =''
T2.on.constraint = "[[['jet']],[['jet']]]"
#T2.off.constraint =None
T2.on.conditionDescription =None
#T2.off.conditionDescription =None
T2.on.condition =None
#T2.off.condition =None
#T2.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2_1.figure = 'Figure 9-c'
T2_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.png'
#----limit source----
T2_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'MassScan2D', index = None )
#T2_1.expUpperLimit.setSource( path, 'root', objectName = None, index = None )
#----exclusion source----
T2_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ObsLim', index = None )
T2_1.obsExclusionM1.setSource(  'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ObsLimSdn', index = None )
T2_1.obsExclusionP1.setSource(  'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ObsLimSup', index = None )
T2_1.expExclusion.setSource(  'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ExpLim', index = None )
T2_1.expExclusionM1.setSource(  'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ExpLimSdn', index = None )
T2_1.expExclusionP1.setSource(  'orig/CMS-PAS-SUS-16-014_Figure_009-c.root', 'root', objectName = 'ExpLimSup', index = None )
#----global url settings ----
T2_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
#----limit url settings ----
T2_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
#----exclusion url settings ----
T2_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'
T2_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-c.root'

#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
T1.on.checked =''
#T1.off.checked =''
T1.on.constraint = "[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =None
T1.on.conditionDescription =None
#T1.off.conditionDescription =None
T1.on.condition =None
#T1.off.condition =None
#T1.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1_1.figure = 'Figure 10-c'
T1_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.png'
#----limit source----
T1_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'MassScan2D', index = None )
#T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ObsLim', index = None )
T1_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ObsLimSdn', index = None )
T1_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ObsLimSup', index = None )
T1_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ExpLim', index = None )
T1_1.expExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ExpLimSdn', index = None )
T1_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_010-c.root', 'root', objectName = 'ExpLimSup', index = None )
#----global url settings ----
T1_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
#----limit url settings ----
T1_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
#----exclusion url settings ----
T1_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'
T1_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_010-c.root'



#+++++++ next txName block ++++++++++++++
T2bb = TxNameInput('T2bb')
T2bb.on.checked =''
#T2bb.off.checked =''
T2bb.on.constraint = "[[['b']],[['b']]]"
#T2bb.off.constraint =None
T2bb.on.conditionDescription =None
#T2bb.off.conditionDescription =None
T2bb.on.condition =None
#T2bb.off.condition =None
#T2bb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2bb_1.figure = 'Figure 9-b'
T2bb_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.png'
#----limit source----
T2bb_1.obsUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'MassScan2D', index = None )
T2bb_1.expUpperLimit.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'MassScan2DExp', index = None )
#----exclusion source----
T2bb_1.obsExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'ObsLim', index = None )
T2bb_1.obsExclusionM1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'ObsLimSdn', index = None )
T2bb_1.obsExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'ObsLimSup', index = None )
T2bb_1.expExclusion.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'ExpLim', index = None )
T2bb_1.expExclusionM1.setSource('orig/CMS-PAS-SUS-16-014_Figure_009-b.root','root', objectName = 'ExpLimSdn', index = None )
T2bb_1.expExclusionP1.setSource( 'orig/CMS-PAS-SUS-16-014_Figure_009-b.root', 'root', objectName = 'ExpLimSup', index = None )
#----global url settings ----
T2bb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/index.html'
#----limit url settings ----
T2bb_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/index.html'
T2bb_1.obsUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.expUpperLimit.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/pretliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
#----exclusion url settings ----
T2bb_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.obsExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.obsExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.obsExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.expExclusion.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.expExclusionM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'
T2bb_1.expExclusionP1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/preliminary-results/SUS-16-014/CMS-PAS-SUS-16-014_Figure_009-b.root'

databaseCreator.create()

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
#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-013')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13013'
info.sqrts = 8
info.lumi = 19.5
info.prettyName =''
info.private = False
info.arxiv = 'http://arxiv.org/pdf/1311.6736v2.pdf'
info.contact =''
info.publication ='http://link.springer.com/article/10.1007%2FJHEP01%282014%29163'
info.comment =''
info.supersedes ='CMS-SUS-12-017'
info.supersededBy =''


#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =''
#T1tttt.off.checked =''
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.off.constraint ="[[['b','b','W','W']],[['b','b','W','W']]]"
T1tttt.on.conditionDescription = 'None'
T1tttt.off.conditionDescription ='None'
T1tttt.on.condition = 'None'
T1tttt.off.condition ="None"
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T1tttt_1.figure ='Figure 5'
T1tttt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/Figure5_A1.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/ModelA1.root', 'root', objectName = 'observedUL', index = None )
T1tttt_1.expUpperLimit.setSource( 'orig/ModelA1.root', 'root', objectName = "expectedUL", index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
T1tttt_1.expUpperLimit.unit = 'fb'
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T1tttt_1.obsExclusionM1.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ObsM', index = None )
T1tttt_1.obsExclusionP1.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T1tttt_1.expExclusion.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_Exp', index = None )
T1tttt_1.expExclusionM1.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ExpM', index = None )
T1tttt_1.expExclusionP1.setSource( 'orig/ModelA1.root', 'root', objectName = 'graph_smoothed_ExpP', index = None )
#----global url settings ----
T1tttt_1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelA1.root'
#----limit url settings ----
T1tttt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/Figure5_A1.pdf'
T1tttt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelA1.root'
T1tttt_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelA1.root'
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelA1.root'
T1tttt_1.obsExclusion.dataUrl =''
T1tttt_1.obsExclusionM1.dataUrl =''
T1tttt_1.obsExclusionP1.dataUrl =''
T1tttt_1.expExclusion.dataUrl =''
T1tttt_1.expExclusionM1.dataUrl =''
T1tttt_1.expExclusionP1.dataUrl =''

#+++++++ next txName block ++++++++++++++
T6ttWW = TxNameInput('T6ttWW')
T6ttWW.on.checked =''
T6ttWW.off.checked =''
T6ttWW.on.constraint ="[[['t'],['W']],[['t'],['W']]]"
T6ttWW.off.constraint ="2.3*([[['t'],['L','nu']],[['t'],['jet','jet']]])"
T6ttWW.on.conditionDescription = "None"
T6ttWW.off.conditionDescription ="[[['b'],['L','nu']],[['b'],['jet','jet']]] > 2.7* [[['b'],['ta','nu']],[['b'],['jet','jet']]],[[['b'],['L','nu']],[['b'],['jet','jet']]] > 2.7* [[['b'],['e','nu']],[['b'],['jet','jet']]]"
T6ttWW.on.condition = "None"
T6ttWW.off.condition ="Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['ta','nu']],[['b'],['jet','jet']]]);Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['e','nu']],[['b'],['jet','jet']]])"
#T6ttWW.off.constraint = None
T6ttWW.on.conditionDescription = None
#T6ttWW.off.conditionDescription =
T6ttWW.on.condition =None
#T6ttWW.off.condition =
#T6ttWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T6ttWW_1 = T6ttWW.addMassPlane(motherMass = x, interMass0 = y, lspMass = 50 )
#T6ttWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6ttWW_1.figure = 'Fig.6'
T6ttWW_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/Figure6_B1a.pdf'
#----limit source----
T6ttWW_1.obsUpperLimit.setSource( 'orig/ModelB1.root', 'root', objectName = 'observedUL', index = None )
T6ttWW_1.expUpperLimit.setSource( 'orig/ModelB1.root', 'root', objectName = 'expectedUL', index = None  )
T6ttWW_1.obsUpperLimit.unit = 'fb'
T6ttWW_1.expUpperLimit.unit = 'fb'
#----exclusion source----
T6ttWW_1.obsExclusion.setSource( 'orig/ModelB1.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T6ttWW_1.obsExclusionM1.setSource( 'orig/ModelB1.root', 'root',  objectName = 'graph_smoothed_ObsM', index = None)
T6ttWW_1.obsExclusionP1.setSource( 'orig/ModelB1.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T6ttWW_1.expExclusion.setSource( 'orig/ModelB1.root', 'root', objectName = 'graph_smoothed_Exp', index = None  )
T6ttWW_1.expExclusionM1.setSource( 'orig/ModelB1.root', 'root', objectName = 'graph_smoothed_ExpM', index = None )
T6ttWW_1.expExclusionP1.setSource( 'orig/ModelB1.root', 'root', objectName = 'graph_smoothed_ExpP', index = None)
#----global url settings ----
T6ttWW_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13013'
#----limit url settings ----
T6ttWW_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
#----exclusion url settings ----
T6ttWW_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'
T6ttWW_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1.root'

#+++++++ next mass plane block ++++++++++++++
T6ttWW_2 = T6ttWW.addMassPlane(motherMass = x, interMass0 = y/(0.5), lspMass = y)
#T6ttWW_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6ttWW_2.figure = 'No Fig'
T6ttWW_2.figureUrl =''
#----limit source----
T6ttWW_2.obsUpperLimit.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'observedUL', index = None)
T6ttWW_2.expUpperLimit.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'expectedUL', index = None  )
T6ttWW_2.obsUpperLimit.unit = 'fb'
T6ttWW_2.expUpperLimit.unit = 'fb'
#----exclusion source----
T6ttWW_2.obsExclusion.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T6ttWW_2.obsExclusionM1.setSource( 'orig/ModelB1_x0p5.root', 'root',  objectName = 'graph_smoothed_ObsM', index = None)
T6ttWW_2.obsExclusionP1.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T6ttWW_2.expExclusion.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'graph_smoothed_Exp', index = None  )
T6ttWW_2.expExclusionM1.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'graph_smoothed_ExpM', index = None)
T6ttWW_2.expExclusionP1.setSource( 'orig/ModelB1_x0p5.root', 'root', objectName = 'graph_smoothed_ExpP', index = None)
#----global url settings ----
T6ttWW_2.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13013'
#----limit url settings ----
T6ttWW_2.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.expUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
#----exclusion url settings ----
T6ttWW_2.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'
T6ttWW_2.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p5.root'

#+++++++ next mass plane block ++++++++++++++
T6ttWW_3 = T6ttWW.addMassPlane(motherMass = x, interMass0 = y/(0.8), lspMass = y)
#T6ttWW_3.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6ttWW_3.figure = 'No Fig'
T6ttWW_3.figureUrl =''
#----limit source----
T6ttWW_3.obsUpperLimit.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'observedUL', index = None)
T6ttWW_3.expUpperLimit.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'expectedUL', index = None  )
T6ttWW_3.obsUpperLimit.unit = 'fb'
T6ttWW_3.expUpperLimit.unit = 'fb'
#----exclusion source----
T6ttWW_3.obsExclusion.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'graph_smoothed_Obs', index = None )
T6ttWW_3.obsExclusionM1.setSource( 'orig/ModelB1_x0p8.root', 'root',  objectName = 'graph_smoothed_ObsM', index = None)
T6ttWW_3.obsExclusionP1.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'graph_smoothed_ObsP', index = None )
T6ttWW_3.expExclusion.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'graph_smoothed_Exp', index = None  )
T6ttWW_3.expExclusionM1.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'graph_smoothed_ExpM', index = None)
T6ttWW_3.expExclusionP1.setSource( 'orig/ModelB1_x0p8.root', 'root', objectName = 'graph_smoothed_ExpP', index = None)
#----global url settings ----
T6ttWW_3.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13013'
#----limit url settings ----
T6ttWW_3.histoDataUrl =  'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.expUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
#----exclusion url settings ----
T6ttWW_3.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'
T6ttWW_3.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13013/ModelB1_x0p8.root'

databaseCreator.create()

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
info = MetaInfoInput('ATLAS-SUSY-2013-18')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/'
info.sqrts = '8.0*TeV'
info.lumi = 20.1
info.prettyName ='Atlas Three b'
info.private =False
info.arxiv = 'http://arxiv.org/abs/1407.0600'
info.contact =''
info.publication ='http://link.springer.com/article/10.1007/JHEP10(2014)024'
info.comment ='Used 1lep+3b UL result, since they give the two analyses UL separately and no combination.T1btbt result lost wrt ATLAS-CONF-2013-061'
info.supersedes ='ATLAS-CONF-2013-061'
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked = ''
T1bbbb.off.checked =''
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
#T1bbbb.off.constraint =''
T1bbbb.on.conditionDescription ="None"
#T1bbbb.off.conditionDescription =
T1bbbb.on.condition ="None"
#T1bbbb.off.condition =
#T1bbbb.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T1bbbb_1.figure = "Figure 13a"
T1bbbb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_03.png'
#----limit source----
T1bbbb_1.obsUpperLimit.setSource( 'orig/T1bbbb_ATLAS-SUSY-2013-18_UL.dat', 'txt', objectName = None, index = None )
T1bbbb_1.obsUpperLimit.unit = 'fb'
#T1bbbb_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/T1bbbb_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt', objectName = None, index = None )
#T1bbbb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1bbbb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----limit url settings ----
T1bbbb_1.histoDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
T1bbbb_1.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d28/input'
#T1bbbb_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1bbbb_1.exclusionDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
T1bbbb_1.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#T1bbbb_1.obsExclusionM1.dataUrl =
#T1bbbb_1.obsExclusionP1.dataUrl =
#T1bbbb_1.expExclusion.dataUrl =
#T1bbbb_1.expExclusionM1.dataUrl =
#T1bbbb_1.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked = ''
T1tttt.off.checked =''
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =''
T1tttt.on.conditionDescription ="None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition ="None"
#T1tttt.off.condition =
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y )
#----figure----
T1tttt_1.figure ='Figure 12b aux'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_12b.png'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( 'orig/T1tttt_ATLAS-SUSY-2013-18_UL.dat', 'txt', objectName = None, index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt', objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T1tttt_1.dataUrl = ''
#----limit url settings ----
T1tttt_1.histoDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
T1tttt_1.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d41/input'
#T1tttt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T1tttt_1.exclusionDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
T1tttt_1.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#T1tttt_1.obsExclusionM1.dataUrl =
#T1tttt_1.obsExclusionP1.dataUrl =
#T1tttt_1.expExclusion.dataUrl =
#T1tttt_1.expExclusionM1.dataUrl =
#T1tttt_1.expExclusionP1.dataUrl =

databaseCreator.create()

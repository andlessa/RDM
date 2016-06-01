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
info = MetaInfoInput('CMS-SUS-13-006')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
info.sqrts = 8
info.lumi = 19.5
info.prettyName ='CMS electroweakinos'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1405.7570'
info.contact = ''
info.publication = 'http://link.springer.com/article/10.1140%2Fepjc%2Fs10052-014-3036-7'
info.comment ='TSlepSlep only LeftHanded'
info.supersedes ='CMS-PAS-SUS-12-022'
#info.supersededBy =


#+++++++ next txName block ++++++++++++++
TChiWZ = TxNameInput('TChiWZ')
TChiWZ.on.checked =''
TChiWZ.off.checked =''
TChiWZ.on.constraint = "[[['W']],[['Z']]]"
TChiWZ.off.constraint = "71.*([[['mu+','mu-']],[['l','nu']]] + [[['e+','e-']],[['l','nu']]])"
TChiWZ.on.conditionDescription =None
TChiWZ.off.conditionDescription =None
TChiWZ.on.condition =None
TChiWZ.off.condition = "cGtr([[['mu+','mu-']],[['l','nu']]],[[['e+','e-']],[['l','nu']]])" 
#TChiWZ.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiWZ_1 = TChiWZ.addMassPlane(motherMass = x , lspMass = y)
#----figure----
TChiWZ_1.figure = 'Fig. 16(left)'
TChiWZ_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig16_exclusion_TChiWZ.png'
#----limit source----
TChiWZ_1.obsUpperLimit.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 2 )
#TChiWZ_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
TChiWZ_1.obsUpperLimit.unit = 'fb'
#----exclusion source----
TChiWZ_1.obsExclusion.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 12 )
TChiWZ_1.obsExclusionM1.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 8 )
TChiWZ_1.obsExclusionP1.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 7 )
TChiWZ_1.expExclusion.setSource("orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 9 )
TChiWZ_1.expExclusionM1.setSource("orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 5 )
TChiWZ_1.expExclusionP1.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 6 )
#----global url settings ----
TChiWZ_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiWZ_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
#TChiWZ_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiWZ_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'
TChiWZ_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWZ.root'



#+++++++ next txName block ++++++++++++++
TChiChipmSlepStau = TxNameInput('TChiChipmSlepStau')
TChiChipmSlepStau.on.checked =''
#TChiChipmSlepStau.off.checked =
TChiChipmSlepStau.on.constraint = "[[['L'],['L']],[['nu'],['ta']]]"
#TChiChipmSlepStau.off.constraint =
TChiChipmSlepStau.on.conditionDescription = None
#TChiChipmSlepStau.off.conditionDescription =
TChiChipmSlepStau.on.condition =  "cGtr([[['L'],['L']],[['nu'],['ta']]],3.*[[['ta'],['ta']],[['nu'],['ta']]]);cGtr([[['L'],['L']],[['nu'],['ta']]],3.*[[['e'],['e']],[['nu'],['ta']]])"
#TChiChipmSlepStau.off.condition =
#TChiChipmSlepStau.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau_1 = TChiChipmSlepStau.addMassPlane(motherMass = x, interMass0 = 0.05*x+0.95*y , lspMass = y )
#TChiChipmSlepStau_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmSlepStau_1.figure ='Fig. 14(top-left)'
TChiChipmSlepStau_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig14_exclusion_TChiSlepSnu_2a_0_05.pdf'
#----limit source----
TChiChipmSlepStau_1.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 2 )
TChiChipmSlepStau_1.obsUpperLimit.unit = 'fb'
#TChiChipmSlepStau_1.expUpperLimit.setSource( "", "canvas", objectName = "interpret", index =  )
#----exclusion source----
TChiChipmSlepStau_1.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 11 )
TChiChipmSlepStau_1.obsExclusionM1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 7 )
TChiChipmSlepStau_1.obsExclusionP1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 6 )
TChiChipmSlepStau_1.expExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 8 )
TChiChipmSlepStau_1.expExclusionM1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 4 )
TChiChipmSlepStau_1.expExclusionP1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 5 )
#----global url settings ----
TChiChipmSlepStau_1.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepStau_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
#TChiChipmSlepStau_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'
TChiChipmSlepStau_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_05.root'

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau_2 = TChiChipmSlepStau.addMassPlane(motherMass =x , interMass0 = 0.5*x+0.5*y , lspMass = y)
#TChiChipmSlepStau_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmSlepStau_2.figure ='Fig. 14(top-right)'
TChiChipmSlepStau_2.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig14_exclusion_TChiSlepSnu_2a_0_5.pdf'
#----limit source----
TChiChipmSlepStau_2.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 2 )
TChiChipmSlepStau_2.obsUpperLimit.unit = 'fb'
#TChiChipmSlepStau_2.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepStau_2.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 9 )
TChiChipmSlepStau_2.obsExclusionM1.setSource("orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 7 )
TChiChipmSlepStau_2.obsExclusionP1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 6  )
TChiChipmSlepStau_2.expExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 8  )
TChiChipmSlepStau_2.expExclusionM1.setSource("orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 4  )
TChiChipmSlepStau_2.expExclusionP1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 5  )
#----global url settings ----
TChiChipmSlepStau_2.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepStau_2.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
#TChiChipmSlepStau_2.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau_2.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'
TChiChipmSlepStau_2.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_5.root'

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau_3 = TChiChipmSlepStau.addMassPlane(motherMass = x, interMass0 =0.95*x+0.05*y , lspMass =y )
#TChiChipmSlepStau_3.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
TChiChipmSlepStau_3.figure ='Fig. 14(bottom)'
TChiChipmSlepStau_3.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig14_exclusion_TChiSlepSnu_2a_0_95.pdf'
#----limit source----
TChiChipmSlepStau_3.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 2 )
TChiChipmSlepStau_3.obsUpperLimit.unit = 'fb'
#TChiChipmSlepStau_3.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepStau_3.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 11 )
TChiChipmSlepStau_3.obsExclusionM1.setSource("orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 7  )
TChiChipmSlepStau_3.obsExclusionP1.setSource(  "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 6  )
TChiChipmSlepStau_3.expExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 8  )
TChiChipmSlepStau_3.expExclusionM1.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 4   )
TChiChipmSlepStau_3.expExclusionP1.setSource(  "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 5   )
#----global url settings ----
TChiChipmSlepStau_3.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepStau_3.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
#TChiChipmSlepStau_3.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau_3.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'
TChiChipmSlepStau_3.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2a_0_95.root'


#+++++++ next txName block ++++++++++++++
TSlepSlep = TxNameInput('TSlepSlep')
TSlepSlep.on.checked =''
#TSlepSlep.off.checked =
TSlepSlep.on.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
#TSlepSlep.off.constraint =
TSlepSlep.on.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
#TSlepSlep.off.conditionDescription =
TSlepSlep.on.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
#TSlepSlep.off.condition =
#TSlepSlep.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane(motherMass =x , lspMass =y )
#----figure----
TSlepSlep_1.figure ='Fig.18 (upper-right)'
TSlepSlep_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig18_exclusion_TSlepSlepL.png'
#----limit source----
TSlepSlep_1.obsUpperLimit.setSource(  "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 2 )
TSlepSlep_1.obsUpperLimit.unit = 'fb'
#TSlepSlep_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TSlepSlep_1.obsExclusion.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 8  )
TSlepSlep_1.obsExclusionM1.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 6  )
TSlepSlep_1.obsExclusionP1.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 5  )
TSlepSlep_1.expExclusion.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 7  )
TSlepSlep_1.expExclusionM1.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 3  )
TSlepSlep_1.expExclusionP1.setSource( "orig/exclusion_TSlepSlepL.root", "canvas", objectName = "interpret", index = 4  )
#----global url settings ----
TSlepSlep_1.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TSlepSlep_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
#TSlepSlep_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TSlepSlep_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'
TSlepSlep_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TSlepSlepL.root'



#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
TChiWH.on.checked =''
TChiWH.off.checked =''
TChiWH.on.constraint = "[[['W']],[['higgs']]]"
#TChiWH.off.constraint = ''
TChiWH.on.conditionDescription =None
#TChiWH.off.conditionDescription =None
TChiWH.on.condition =None
#TChiWH.off.condition = "" 
#TChiWZ.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
TChiWH_1 = TChiWH.addMassPlane(motherMass = x , lspMass = y)
#----figure----
TChiWH_1.figure = 'Fig. 16(right)'
TChiWH_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig16_exclusion_TChiWH.png'
#----limit source----
TChiWH_1.obsUpperLimit.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 2 )
#TChiWH_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
TChiWH_1.obsUpperLimit.unit = 'fb'
#----exclusion source----
TChiWH_1.obsExclusion.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 9 )
TChiWH_1.obsExclusionM1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 7 )
TChiWH_1.obsExclusionP1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 6 )
TChiWH_1.expExclusion.setSource("orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 8 )
TChiWH_1.expExclusionM1.setSource("orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 4 )
TChiWH_1.expExclusionP1.setSource( "orig/exclusion_TChiWH.root", "canvas", objectName = "interpret", index = 5 )
#----global url settings ----
TChiWH_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiWH_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
#TChiWZ_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiWH_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'
TChiWH_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiWH.root'



#+++++++ next txName block ++++++++++++++
TChiChipmSlepL = TxNameInput('TChiChipmSlepL')
TChiChipmSlepL.on.checked =''
TChiChipmSlepL.off.checked =''
TChiChipmSlepL.on.constraint = "2.*([[['L'],['L']],[['L'],['nu']]] + [[['L'],['L']],[['nu'],['L']]])"
#TChiChipmSlepL.off.constraint =
TChiChipmSlepL.on.conditionDescription = None
#TChiChipmSlepL.off.conditionDescription =
TChiChipmSlepL.on.condition = "cSim([[['L'],['L']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]]); cGtr([[['L'],['L']],[['nu'],['L']]],3.*[[['ta'],['ta']],[['nu'],['L']]]); cGtr([[['L'],['L']],[['L'],['nu']]],3.*[[['ta'],['ta']],[['L'],['nu']]]); cGtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['ta']]]); cGtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['ta'],['nu']]]);cGtr([[['L'],['L']],[['nu'],['L']]],3.*[[['e'],['e']],[['nu'],['L']]]); cGtr([[['L'],['L']],[['L'],['nu']]],3.*[[['e'],['e']],[['L'],['nu']]]); cGtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['e']]]); cGtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['e'],['nu']]])"
#TChiChipmSlepL.off.condition =
#TChiChipmSlepL.branchingRatio =


#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL_1 = TChiChipmSlepL.addMassPlane(motherMass = x , interMass0 = 0.05*x+0.95*y , lspMass = y)
#----figure----
TChiChipmSlepL_1.figure = 'Fig. 13'
TChiChipmSlepL_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig13_exclusion_TChiSlepSnu_2i_0_05.png'
#----limit source----
TChiChipmSlepL_1.obsUpperLimit.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret', index = 2 )
TChiChipmSlepL_1.obsUpperLimit.unit = 'fb'
#TChiChipmSlepL_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL_1.obsExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret',index = 8 ) # Cant find correct line in canvas
TChiChipmSlepL_1.obsExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret', index = 8 )
TChiChipmSlepL_1.obsExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret',index = 7 )
TChiChipmSlepL_1.expExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret', index = 9 )
TChiChipmSlepL_1.expExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret' ,index = 5 )
TChiChipmSlepL_1.expExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_05.root', 'canvas', objectName = 'interpret', index = 6 )
#----global url settings ----
TChiChipmSlepL_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepL_1.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
#TChiChipmSlepL_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepL_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'
TChiChipmSlepL_1.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_05.root'

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL_2 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = 0.5*x+0.5*y, lspMass = y)
#----figure----
TChiChipmSlepL_2.figure ='Fig. 12'
TChiChipmSlepL_2.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig13_exclusion_TChiSlepSnu_2i_0_5.png'
#----limit source----
TChiChipmSlepL_2.obsUpperLimit.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret', index = 2 )
TChiChipmSlepL_2.obsUpperLimit.unit = 'fb'
#TChiChipmSlepL_2.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL_2.obsExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 9 )
TChiChipmSlepL_2.obsExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 7 )
TChiChipmSlepL_2.obsExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 6 )
TChiChipmSlepL_2.expExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 8 )
TChiChipmSlepL_2.expExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 4 )
TChiChipmSlepL_2.expExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_5.root', 'canvas', objectName = 'interpret',  index = 5 )
#----global url settings ----
TChiChipmSlepL_2.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepL_2.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
#TChiChipmSlepL_2.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepL_2.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'
TChiChipmSlepL_2.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_5.root'


#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL_3 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = 0.95*x+0.05*y, lspMass = y)
#----figure----
TChiChipmSlepL_3.figure ='Fig. 14'
TChiChipmSlepL_3.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/Fig13_exclusion_TChiSlepSnu_2i_0_95.png'
#----limit source----
TChiChipmSlepL_3.obsUpperLimit.setSource('orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret',  index = 2 )
TChiChipmSlepL_3.obsUpperLimit.unit = 'fb'
#TChiChipmSlepL_3.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL_3.obsExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 11 )
TChiChipmSlepL_3.obsExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 7 )
TChiChipmSlepL_3.obsExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 6 )
TChiChipmSlepL_3.expExclusion.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 8 )
TChiChipmSlepL_3.expExclusionM1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 4 )
TChiChipmSlepL_3.expExclusionP1.setSource( 'orig/exclusion_TChiSlepSnu_2i_0_95.root', 'canvas', objectName = 'interpret', index = 5 )
#----global url settings ----
TChiChipmSlepL_3.dataUrl ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13006'
#----limit url settings ----
TChiChipmSlepL_3.histoDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
#TChiChipmSlepL_3.expUpperlimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepL_3.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.obsExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.obsExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.obsExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.expExclusion.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.expExclusionM1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'
TChiChipmSlepL_3.expExclusionP1.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13006/exclusion_TChiSlepSnu_2i_0_95.root'

databaseCreator.create()

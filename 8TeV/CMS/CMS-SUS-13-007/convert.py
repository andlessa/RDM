#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt, txname.txt, twiki.txt and sms.py.

.. moduleauthor:: Michael Traub <michael.traub@gmx.at>

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
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y


#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-007')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
info.sqrts = 8
info.lumi = 19.3
info.prettyName = 'e/\mu DP'
info.private = False
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='Loukas Gouskos <loukas.gouskos@cern.ch>, Markus Stoye <Markus.Stoye@cern.ch>'
info.publication = 'http://www.sciencedirect.com/science/article/pii/S037026931400255X'
info.comment = 'Only two mass planes for T5tttt'
info.supersedes =''
#info.supersededBy =
info.implementedBy = 'Federico Ambrogi'

#+++++++ next txName block ++++++++++++++
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
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y )
#----figure----
T1tttt_1.figure = 'combLimit_T1tttt_b.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/combLimit_T1tttt_b.pdf'
#----limit source----
T1tttt_1.obsUpperLimit.setSource( './orig/T1tttt.txt', 'txt', objectName = None, index = None )
T1tttt_1.obsUpperLimit.unit = 'fb'
#T1tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T1tttt_1.obsExclusion.setSource( './orig/T1tttt_excl.txt', 'txt' )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T1tttt_1.dataUrl = 
#T1tttt_1.histoDataUrl = 
#----limit url settings ----
T1tttt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_A.txt'
#T1tttt_1.expectedlimit.dataUrl =
#----exclusion url settings ----
#T1tttt_1.exclusionDataUrl =
#T1tttt_1.exclusion.dataUrl =
#T1tttt_1.exclusionM1.dataUrl =
#T1tttt_1.exclusionP1.dataUrl =
#T1tttt_1.expectedExclusion.dataUrl =
#T1tttt_1.expectedExclusionM1.dataUrl =
#T1tttt_1.expectedExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5tttt = TxNameInput('T5tttt')
#T5tttt.on.checked =
#T5tttt.off.checked =
T5tttt.on.constraint = "[[['t'],['t']],[['t'],['t']]]"
T5tttt.off.constraint = "[[['b','W'],['b','W']],[['b','W'],['b','W']]]"
T5tttt.on.conditionDescription = None
T5tttt.off.conditionDescription = None
T5tttt.on.condition = None
T5tttt.off.condition = None

#+++++++ next mass plane block ++++++++++++++
T5tttt_1 = T5tttt.addMassPlane(motherMass = 1000. , interMass0 = x , lspMass = y )
#----figure----
T5tttt_1.figure = 'combLimit_T1t1t_b.pdf'
T5tttt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/combLimit_T1t1t_b.png'
#----limit source----
T5tttt_1.obsUpperLimit.setSource( './orig/T5tttt_mg1TeV.txt', 'txt', objectName = None, index = None )
T5tttt_1.obsUpperLimit.unit = 'fb'
#T5tttt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T5tttt_1.obsExclusion.setSource( './orig/T5tttt_mg1TeV_excl.txt', 'txt' )
#T5tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T5tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T5tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T5tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T5tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T5tttt_1.dataUrl = 
#T5tttt_1.histoDataUrl =
#----limit url settings ----
T5tttt_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_B.txt'
#T5tttt_1.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T5tttt_1.exclusionDataUrl =
#T5tttt_1.exclusion.dataUrl =
#T5tttt_1.exclusionM1.dataUrl =
#T5tttt_1.exclusionP1.dataUrl =
#T5tttt_1.expectedExclusion.dataUrl =
#T5tttt_1.expectedExclusionM1.dataUrl =
#T5tttt_1.expectedExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T5tttt_2 = T5tttt.addMassPlane(motherMass = x , interMass0 = y , lspMass = 50. )
#----figure----
T5tttt_2.figure = 'combLimit_T5tttt_b.pdf'
T5tttt_2.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/combLimit_T5tttt_b.png'
#----limit source----
T5tttt_2.obsUpperLimit.setSource( './orig/T5tttt_mLSP50GeV.txt', 'txt', objectName = None, index = None )
T5tttt_2.obsUpperLimit.unit = 'fb'
#T5tttt_2.expexpectedlimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T5tttt_2.obsExclusion.setSource( './orig/T5tttt_mLSP50GeV_excl.txt', 'txt' )
#T5tttt_2.exclusionM1.setSource( path, type, objectName = None, index = None )
#T5tttt_2.exclusionP1.setSource( path, type, objectName = None, index = None )
#T5tttt_2.expectedExclusion.setSource( path, type, objectName = None, index = None )
#T5tttt_2.expectedExclusionM1.setSource( path, type, objectName = None, index = None )
#T5tttt_2.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T5tttt_2.dataUrl = 
#T5tttt_2.histoDataUrl = 
#----limit url settings ----
T5tttt_2.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_C.txt'
#T5tttt_2.expectedlimit.dataUrl =
#----exclusion url settings ----
#T5tttt_2.exclusionDataUrl =
#T5tttt_2.exclusion.dataUrl =
#T5tttt_2.exclusionM1.dataUrl =
#T5tttt_2.exclusionP1.dataUrl =
#T5tttt_2.expectedExclusion.dataUrl =
#T5tttt_2.expectedExclusionM1.dataUrl =
#T5tttt_2.expectedExclusionP1.dataUrl =

databaseCreator.create()

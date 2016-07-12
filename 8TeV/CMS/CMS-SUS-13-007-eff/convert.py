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
info = MetaInfoInput('CMS-SUS-13-007')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
info.sqrts = 8
info.lumi = 19.3
info.prettyName = 'e/\mu DP'
info.private = False
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='Loukas Gouskos <loukas.gouskos@cern.ch>, Markus Stoye <Markus.Stoye@cern.ch>'
info.publication = 'http://www.sciencedirect.com/science/article/pii/S037026931400255X'
info.comment = 'Only two mass planes for T5tttt; implemented Delta Phi method'
#info.supersedes =''
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
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x , lspMass = y )
#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_250_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_250_Nb2.pdf'
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_excl.txt', 'txt' )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-250-sig-Nb2', index = None, dataset="mu250Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=9, expectedBG=6, bgError=2.37 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_250_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_250_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource(  'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-250-sig-Nb3', index = None, dataset="mu250Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=1.9, bgError=0.89 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_350_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_350_Nb2.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource(  'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-350-sig-Nb2',  index = None, dataset="mu350Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=2, expectedBG=1.4, bgError=1.17 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_350_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_350_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-350-sig-Nb3',  index = None, dataset="mu350Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0.6, bgError=0.58 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_450_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_250_Nb2.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-450-sig-Nb2', index = None, dataset="mu450Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0, bgError=0.72 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Muons_450_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Muons_450_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_mu-450-sig-Nb3', index = None, dataset="mu450Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0, bgError=0.22 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_250_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_250_Nb2.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-250-sig-Nb2',  index = None, dataset="el250Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=9, expectedBG=3.8, bgError=1.89 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_250_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_250_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-250-sig-Nb3', index = None, dataset="el250Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=4, expectedBG=1.9, bgError=0.98 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_350_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_350_Nb2.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-350-sig-Nb2', index = None, dataset="el350Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=2, expectedBG=2.7, bgError=2.06 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_350_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_350_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-350-sig-Nb3', index = None, dataset="el350Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0.9, bgError=0.80 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_450_Nb2.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_450_Nb2.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource('orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-450-sig-Nb2', index = None, dataset="el450Nb2" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0, bgError=0.44 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure ='DPhi_Method_T1tttt_Elect_450_Nb3.pdf'
T1tttt_1.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/DPhi_Method_T1tttt_Elect_450_Nb3.pdf'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_el-450-sig-Nb3',  index = None, dataset="el450Nb3" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=0, bgError=0.10 )
#----global url settings ----
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
databaseCreator.create(True)



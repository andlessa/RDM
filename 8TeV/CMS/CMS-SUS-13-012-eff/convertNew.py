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
type = types.StringType)
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-012')
info.comment = 'T1,T2,T1tttt official efficiency maps from the CMS collaboration; T5WW and T5ZZ created by the SModelS collaboration using MadAnalysis5' 
info.sqrts = '8.0'
info.private = False
info.lumi = '19.5'
info.publication = 'JHEP06(2014)055'
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13012'
info.arxiv = 'http://arxiv.org/abs/1402.4770'
info.contact = 'cms-pag-conveners-sus@NOSPAMcernSPAMNOT.ch, SModelS collaboration'
info.implementedBy = 'Federico A.'




#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("3NJet6_800HT1000_450MHT600")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "3NJet6_800HT1000_450MHT600", observedN = 124, expectedBG = 108 , bgError = 15)
#+++++++ next txName block ++++++++++++++
T2 = dataset.addTxName('T2')
T2.checked =''
T2.constraint ="[[['jet']],[['jet']]]"
T2.conditionDescription ="None"
T2.condition ="None"
T2.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T2qq = T2.addMassPlane([[x,y]]*2)
T2qq.figure = "Fig_7a"
T2qq.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7a.pdf"
T2qq.dataUrl = None
T2qq.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclOneTimesProspino")
T2qq.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T2qq.addSource('obsExclusionP1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T2qq.addSource('expExclusion', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclOneTimesProspino")
T2qq.addSource('expExclusionM1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T2qq.addSource('expExclusionP1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T2qq.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_450MHT600")
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.massConstraint = None
T1tttt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1ttttoff.conditionDescription ="None"
T1ttttoff.condition = "None"
T1ttttoff.massConstraint = [['dm <= 338.']]*2
T1ttttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.figure = "Fig_7c"
T1tttt.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7c.pdf"
T1tttt.dataUrl = None
T1tttt.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclOneTimesProspino")
T1tttt.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T1tttt.addSource('obsExclusionP1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T1tttt.addSource('expExclusion', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclOneTimesProspino")
T1tttt.addSource('expExclusionM1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T1tttt.addSource('expExclusionP1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T1tttt.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_450MHT600")
T1ttttoff.addMassPlane(T1tttt)
#+++++++ next txName block ++++++++++++++
T1 = dataset.addTxName('T1')
T1.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.conditionDescription ="None"
T1.condition ="None"
T1.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1qqqq = T1.addMassPlane([[x,y]]*2)
T1qqqq.figure = "Fig_7b"
T1qqqq.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7b.pdf"
T1qqqq.dataUrl = None
T1qqqq.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclOneTimesProspino")
T1qqqq.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T1qqqq.addSource('obsExclusionP1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T1qqqq.addSource('expExclusion', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclOneTimesProspino")
T1qqqq.addSource('expExclusionM1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T1qqqq.addSource('expExclusionP1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T1qqqq.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_450MHT600")
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.checked = ' '
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription ="None"
T5ZZ.condition ="None"
T5ZZ.massConstraint = None
T5ZZ.source = 'SModelS'
#+++++++ next txName block ++++++++++++++
T5ZZoff = dataset.addTxName('T5ZZoff')
T5ZZoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZoff.conditionDescription ="None"
T5ZZoff.condition =None
T5ZZoff.massConstraint = [['dm >= 0.0','dm <= 86.']]*2
T5ZZoff.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x05 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_x05.dataUrl = None
T5ZZ_x05.addSource('obsExclusion', "orig/CMS_T5VV_x05.dat", "txt")
T5ZZ_x05.addSource('efficiencyMap',"orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_450MHT600.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x005 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_x005.dataUrl = None
T5ZZ_x005.addSource('efficiencyMap',"orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_450MHT600.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x095 = T5ZZ.addMassPlane([[x,0.95*x + 0.05*y,y]]*2)
T5ZZ_x095.dataUrl = None
T5ZZ_x095.addSource('efficiencyMap',"orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_450MHT600.dat", "txt")
T5ZZoff.addMassPlane(T5ZZ_x05)
T5ZZoff.addMassPlane(T5ZZ_x005)
T5ZZoff.addMassPlane(T5ZZ_x095)
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.checked = ' '
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription ="None"
T5WW.condition ="None"
T5WW.massConstraint = None
T5WW.source = 'SModelS'
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription ="None"
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
T5WW_x05 = T5WW.addMassPlane([[x,0.5*(x+y),y]]*2)
T5WW_x05.dataUrl = None
T5WW_x05.addSource('obsExclusion', "orig/CMS_T5VV_x05.dat", "txt")
T5WW_x05.addSource('efficiencyMap',"orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_450MHT600.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5WW_x005 = T5WW.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5WW_x005.dataUrl = None
T5WW_x005.addSource('efficiencyMap',"orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_450MHT600.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5WW_x095 = T5WW.addMassPlane([[x,0.95*x + 0.05*y,y]]*2)
T5WW_x095.dataUrl = None
T5WW_x095.addSource('efficiencyMap',"orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_450MHT600.dat", "txt")
T5WWoff.addMassPlane(T5WW_x05)
T5WWoff.addMassPlane(T5WW_x005)
T5WWoff.addMassPlane(T5WW_x095)


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("3NJet6_800HT1000_600MHTinf")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "3NJet6_800HT1000_600MHTinf", observedN = 52, expectedBG = 54.8 , bgError = 9.7)
#+++++++ next txName block ++++++++++++++
T2 = dataset.addTxName('T2')
T2.checked =''
T2.constraint ="[[['jet']],[['jet']]]"
T2.conditionDescription ="None"
T2.condition ="None"
T2.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T2qq = T2.addMassPlane([[x,y]]*2)
T2qq.figure = "Fig_7a"
T2qq.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7a.pdf"
T2qq.dataUrl = None
T2qq.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclOneTimesProspino")
T2qq.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T2qq.addSource('obsExclusionP1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T2qq.addSource('expExclusion', "orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclOneTimesProspino")
T2qq.addSource('expExclusionM1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T2qq.addSource('expExclusionP1',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T2qq.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T2qq.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_600MHTinf")
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.massConstraint = None
T1tttt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1ttttoff.conditionDescription ="None"
T1ttttoff.condition = "None"
T1ttttoff.massConstraint = [['dm <= 338.']]*2
T1ttttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.figure = "Fig_7c"
T1tttt.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7c.pdf"
T1tttt.dataUrl = None
T1tttt.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclOneTimesProspino")
T1tttt.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T1tttt.addSource('obsExclusionP1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T1tttt.addSource('expExclusion', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclOneTimesProspino")
T1tttt.addSource('expExclusionM1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T1tttt.addSource('expExclusionP1', "orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T1tttt.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T1tttt.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_600MHTinf")
T1ttttoff.addMassPlane(T1tttt)
#+++++++ next txName block ++++++++++++++
T1 = dataset.addTxName('T1')
T1.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.conditionDescription ="None"
T1.condition ="None"
T1.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1qqqq = T1.addMassPlane([[x,y]]*2)
T1qqqq.figure = "Fig_7b"
T1qqqq.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13012/Fig_7b.pdf"
T1qqqq.dataUrl = None
T1qqqq.addSource('obsExclusion', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclOneTimesProspino")
T1qqqq.addSource('obsExclusionM1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclMinusSysErrProspino")
T1qqqq.addSource('obsExclusionP1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_obsExclPlusSysErrProspino")
T1qqqq.addSource('expExclusion', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclOneTimesProspino")
T1qqqq.addSource('expExclusionM1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclMinusOneSigmaProspino")
T1qqqq.addSource('expExclusionP1', "orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName = "combined_expExclPlusOneSigmaProspino")
T1qqqq.addSource('efficiencyMap',"orig/SUS13012_XsecLimits_T1qqqq.root", "root", objectName ="h_EffAcc_3NJet6_800HT1000_600MHTinf")
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.checked = ' '
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription ="None"
T5ZZ.condition ="None"
T5ZZ.massConstraint = None
T5ZZ.source = 'SModelS'
#+++++++ next txName block ++++++++++++++
T5ZZoff = dataset.addTxName('T5ZZoff')
T5ZZoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZoff.conditionDescription ="None"
T5ZZoff.condition =None
T5ZZoff.massConstraint = [['dm >= 0.0','dm <= 86.']]*2
T5ZZoff.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x05 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_x05.dataUrl = None
T5ZZ_x05.addSource('obsExclusion', "orig/CMS_T5VV_x05.dat", "txt")
T5ZZ_x05.addSource('efficiencyMap',"orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_3NJet6_800HT1000_600MHTinf.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x005 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_x005.dataUrl = None
T5ZZ_x005.addSource('efficiencyMap',"orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_3NJet6_800HT1000_600MHTinf.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5ZZ_x095 = T5ZZ.addMassPlane([[x,0.95*x + 0.05*y,y]]*2)
T5ZZ_x095.dataUrl = None
T5ZZ_x095.addSource('efficiencyMap',"orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_3NJet6_800HT1000_600MHTinf.dat", "txt")
T5ZZoff.addMassPlane(T5ZZ_x05)
T5ZZoff.addMassPlane(T5ZZ_x005)
T5ZZoff.addMassPlane(T5ZZ_x095)
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.checked = ' '
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription ="None"
T5WW.condition ="None"
T5WW.massConstraint = None
T5WW.source = 'SModelS'
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription ="None"
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
T5WW_x05 = T5WW.addMassPlane([[x,0.5*(x+y),y]]*2)
T5WW_x05.dataUrl = None
T5WW_x05.addSource('obsExclusion', "orig/CMS_T5VV_x05.dat", "txt")
T5WW_x05.addSource('efficiencyMap',"orig/T5WW_x05/MA5_EM_T5WW_x05_3NJet6_800HT1000_600MHTinf.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5WW_x005 = T5WW.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5WW_x005.dataUrl = None
T5WW_x005.addSource('efficiencyMap',"orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_3NJet6_800HT1000_600MHTinf.dat", "txt")
#+++++++ next mass plane block ++++++++++++++
T5WW_x095 = T5WW.addMassPlane([[x,0.95*x + 0.05*y,y]]*2)
T5WW_x095.dataUrl = None
T5WW_x095.addSource('efficiencyMap',"orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_3NJet6_800HT1000_600MHTinf.dat", "txt")
T5WWoff.addMassPlane(T5WW_x05)
T5WWoff.addMassPlane(T5WW_x005)
T5WWoff.addMassPlane(T5WW_x095)

databaseCreator.create()

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
info = MetaInfoInput('ATLAS-SUSY-2013-04')
info.comment = 'Erratum: JHEP01(2014)109. T1tttt official efficiency maps from ATLAS collaboration; T5WW and T5ZZ efficiency maps created by the SModelS collaboration using MadAnalysis5'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP10%282013%29130'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/'
# info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1308.1841'
info.contact = "ATLAS collaboration for T1tttt models;SModelS for T5WW and T5ZZ models"
info.prettyName = 'ATLAS \ge 7 jets'
info.supersedes = 'ATLAS-CONF-2012-103'



#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ij80_0bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ij80_0bjet", observedN = 2, expectedBG = 0.9 , bgError = 0.6, upperLimit = '2.736E-01*fb', expectedUpperLimit = '1.477E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ij80_0bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_0bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,0bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,0bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,0bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,0bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,0bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,0bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_9ej50_0bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_9ej50_0bjet", observedN = 5, expectedBG = 3.3 , bgError = 0.7, upperLimit = '3.734E-01*fb', expectedUpperLimit = '2.666E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_9ej50_0bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_0bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,0bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,0bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,0bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,0bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,0bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,0bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ej50_0bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ej50_0bjet", observedN = 40, expectedBG = 35 , bgError = 4, upperLimit = '9.750E-01*fb', expectedUpperLimit = '7.643E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ej50_0bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_0bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,0bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,0bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,0bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,0bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,0bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,0bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ij80_2ibjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ij80_2ibjet", observedN = 3, expectedBG = 3.3 , bgError = 2.2, upperLimit = '2.976E-01*fb', expectedUpperLimit = '2.970E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ij80_2ibjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_2ibjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,>=2bjets.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,>=2bjets.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,>=2bjets.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,>=2bjets.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,>=2bjets.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,>=2bjets.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ej50_2ibjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ej50_2ibjet", observedN = 44, expectedBG = 50 , bgError = 10, upperLimit = '1.030E+00*fb', expectedUpperLimit = '1.238E+00*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ej50_2ibjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_2ibjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,>=2bjets.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,>=2bjets.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,>=2bjets.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,>=2bjets.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,>=2bjets.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,>=2bjets.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_7ej80_0bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_7ej80_0bjet", observedN = 12, expectedBG = 11.0 , bgError = 2.2, upperLimit = '5.076E-01*fb', expectedUpperLimit = '4.618E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_7ej80_0bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_0bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,0bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,0bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,0bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,0bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,0bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,0bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_7ej80_1bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_7ej80_1bjet", observedN = 17, expectedBG = 17 , bgError = 6, upperLimit = '7.487E-01*fb', expectedUpperLimit = '7.487E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_7ej80_1bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_1bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,1bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,1bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,1bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,1bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,1bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,1bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_9ej50_2ibjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_9ej50_2ibjet", observedN = 7, expectedBG = 8.0 , bgError = 2.7, upperLimit = '4.019E-01*fb', expectedUpperLimit = '4.457E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_9ej50_2ibjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_2ibjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,>=2bjets.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,>=2bjets.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,>=2bjets.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,>=2bjets.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,>=2bjets.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,>=2bjets.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_7ej80_2ibjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_7ej80_2ibjet", observedN = 13, expectedBG = 25 , bgError = 10, upperLimit = '6.480E-01*fb', expectedUpperLimit = '1.083E+00*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_7ej80_2ibjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_7ej80_2ibjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_7j80,>=2bjets.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_7j80,>=2bjets.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_7j80,>=2bjets.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_7j80,>=2bjets.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_7j80,>=2bjets.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_7j80,>=2bjets.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ej50_1bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ej50_1bjet", observedN = 44, expectedBG = 40 , bgError = 10, upperLimit = '1.348E+00*fb', expectedUpperLimit = '1.193E+00*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ej50_1bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ej50_1bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_8j50,1bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_8j50,1bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_8j50,1bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_8j50,1bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_8j50,1bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_8j50,1bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_8ij80_1bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_8ij80_1bjet", observedN = 1, expectedBG = 1.5 , bgError = 0.9, upperLimit = '2.020E-01*fb', expectedUpperLimit = '2.023E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_8ij80_1bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_8ij80_1bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=8j80,1bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=8j80,1bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=8j80,1bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=8j80,1bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=8j80,1bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=8j80,1bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_9ej50_1bjet")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_9ej50_1bjet", observedN = 8, expectedBG = 6.1 , bgError = 1.7, upperLimit = '4.640E-01*fb', expectedUpperLimit = '3.662E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_9ej50_1bjet.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_9ej50_1bjet.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_9j50,1bjet.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_9j50,1bjet.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_9j50,1bjet.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_9j50,1bjet.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_9j50,1bjet.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_9j50,1bjet.dat', 'txt')
T5ZZ_3.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("GtGrid_SR_10ij50_bjetblind")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "GtGrid_SR_10ij50_bjetblind", observedN = 3, expectedBG = 1.37 , bgError = 0.35, upperLimit = '3.214E-01*fb', expectedUpperLimit = '1.981E-01*fb')
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/GtGrid_SR_10ij50_bjetblind.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/GtGrid_SR_10ij50_bjetblind.txt"
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#+++++++ next txName block ++++++++++++++
T5WW = dataset.addTxName('T5WW')
T5WW.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.conditionDescription =None
T5WW.condition =None
T5WW.massConstraint = None
T5WW.source = "SModelS"
#+++++++ next txName block ++++++++++++++
T5WWoff = dataset.addTxName('T5WWoff')
T5WWoff.constraint ="2.23*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5WWoff.conditionDescription =None
T5WWoff.condition =None
T5WWoff.massConstraint = [['dm >= 0.0','dm <= 76.']]*2
T5WWoff.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5WW_1 = T5WW.addMassPlane([[x, 0.5*(x+y), y]]*2)
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_>=10j50.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_>=10j50.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_>=10j50.dat','txt')
T5WW_3.addSource('obsExclusion', 'orig/Null_Line.txt', 'txt')
T5WW_3.dataUrl = None
T5WWoff.addMassPlane(T5WW_1)
T5WWoff.addMassPlane(T5WW_2)
T5WWoff.addMassPlane(T5WW_3)
#+++++++ next txName block ++++++++++++++
T5ZZ = dataset.addTxName('T5ZZ')
T5ZZ.constraint ="[[['jet','jet'],['Z']],[['jet','jet'],['Z']]]"
T5ZZ.conditionDescription =None
T5ZZ.condition =None
T5ZZ.massConstraint = None
T5ZZ.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_>=10j50.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_>=10j50.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_>=10j50.dat', 'txt')
T5ZZ_3.dataUrl = None

databaseCreator.create()

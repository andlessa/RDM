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
info = MetaInfoInput('ATLAS-SUSY-2013-11')
info.comment = 'TSlepSlep efficiency maps created by the SModelS collaboration using MadAnalysis5'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP05(2014)071'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/'
info.arxiv = 'http://arxiv.org/abs/1403.5294'
info.contact = 'SModelS'
info.prettyName = 'ATLAS dilepton'
info.supersedes = 'ATLAS-CONF-2013-049'



#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWb-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWb-SF", observedN = 26, expectedBG = 30.2 , bgError = 3.5, upperLimit = '5.59E-01*fb', expectedUpperLimit = '6.94E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWb-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWa-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWa-SF", observedN = 73, expectedBG = 86.5 , bgError = 7.4, upperLimit = '8.19E-01*fb', expectedUpperLimit = '1.20E+00*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWa-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWb-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWb-DF", observedN = 17, expectedBG = 18.1 , bgError = 2.6, upperLimit = '5.16E-01*fb', expectedUpperLimit = '5.55E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWb-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-90-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-90-DF", observedN = 21, expectedBG = 23.3 , bgError = 3.7, upperLimit = '5.74E-01*fb', expectedUpperLimit = '6.48E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-90-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-120-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-120-SF", observedN = 5, expectedBG = 8.9 , bgError = 2.1, upperLimit = '2.79E-01*fb', expectedUpperLimit = '3.92E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-120-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWc-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWc-SF", observedN = 10, expectedBG = 20.1 , bgError = 3.5, upperLimit = '3.16E-01*fb', expectedUpperLimit = '6.20E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWc-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWa-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWa-DF", observedN = 70, expectedBG = 73.6 , bgError = 7.9, upperLimit = '1.07E+00*fb', expectedUpperLimit = '1.17E+00*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWa-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-90-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-90-SF", observedN = 33, expectedBG = 38.2 , bgError = 5.1, upperLimit = '6.62E-01*fb', expectedUpperLimit = '8.34E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-90-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("WWc-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "WWc-DF", observedN = 11, expectedBG = 9.0 , bgError = 2.2, upperLimit = '5.30E-01*fb', expectedUpperLimit = '4.36E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_WWc-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-120-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-120-DF", observedN = 5, expectedBG = 3.6 , bgError = 1.2, upperLimit = '3.76E-01*fb', expectedUpperLimit = '2.73E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-120-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("Zjets")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "Zjets", observedN = 1, expectedBG = 1.4 , bgError = 0.6, upperLimit = '2.01E-01*fb', expectedUpperLimit = '2.02E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_Zjets.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-150-SF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-150-SF", observedN = 3, expectedBG = 3.2 , bgError = 0.7, upperLimit = '2.68E-01*fb', expectedUpperLimit = '2.70E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-150-SF.dat', 'txt')
TSlepSlep_1.dataUrl = None


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput("mT2-150-DF")
dataset.setInfo(dataType = 'efficiencyMap', dataId = "mT2-150-DF", observedN = 2, expectedBG = 1.0 , bgError = 0.5, upperLimit = '2.70E-01*fb', expectedUpperLimit = '2.06E-01*fb')
#+++++++ next txName block ++++++++++++++
#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = 'SModelS'
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane([[x,y]]*2)
TSlepSlep_1.addSource('obsExclusion', "orig/exclusion_TSlepSlep.txt", "txt")
TSlepSlep_1.addSource('efficiencyMap','orig/MA5_EM_mT2-150-DF.dat', 'txt')
TSlepSlep_1.dataUrl = None

databaseCreator.create()

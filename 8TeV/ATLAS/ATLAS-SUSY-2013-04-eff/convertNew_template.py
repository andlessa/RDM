#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse

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
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z

# DataSetInput.ntoys = 10
# databaseCreator.ncpus = 1

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

BEGIN_AUXILIARY_BLOCK
datasetShortStr = {
'GtGrid_SR_10ij50_bjetblind' : '>=10j50',
'GtGrid_SR_7ej80_0bjet' : '7j80,0bjet',
'GtGrid_SR_7ej80_1bjet' : '7j80,1bjet',
'GtGrid_SR_7ej80_2ibjet' : '7j80,>=2bjets',
'GtGrid_SR_8ej50_0bjet' : '8j50,0bjet',
'GtGrid_SR_8ej50_1bjet' : '8j50,1bjet',
'GtGrid_SR_8ej50_2ibjet' : '8j50,>=2bjets',
'GtGrid_SR_9ej50_0bjet' : '9j50,0bjet',
'GtGrid_SR_8ij80_1bjet' : '>=8j80,1bjet',
'GtGrid_SR_8ij80_0bjet' : '>=8j80,0bjet',
'GtGrid_SR_8ij80_2ibjet' : '>=8j80,>=2bjets',
'GtGrid_SR_9ej50_1bjet' : '9j50,1bjet',
'GtGrid_SR_9ej50_2ibjet' : '9j50,>=2bjets'
}
END_AUXILIARY_BLOCK


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked ="None"
T1tttt.constraint ="[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription ="None"
T1tttt.condition ="None"
T1tttt.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane([[x,y]]*2)
T1tttt.addSource('efficiencyMap',"./orig/$datasetStr$.txt", "txt")
T1tttt.addSource('obsExclusion', "orig/exclusion_T1tttt.txt", "txt")
T1tttt.dataUrl="http://hepdata.cedar.ac.uk/resource/6095/bjetstream/$datasetStr$.txt"
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
T5WW_1.addSource('efficiencyMap', 'orig/T5WW_x05/MA5_EM_T5WW_x05_$datasetShortStr$.dat', 'txt')
T5WW_1.addSource('obsExclusion', 'orig/Exclusion_T5WW_x05.txt', 'txt')
T5WW_1.addSource('obsExclusionM1', 'orig/T5WW_Plus.txt', 'txt')
T5WW_1.addSource('obsExclusionP1', 'orig/T5WW_Minus.txt', 'txt')
T5WW_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_2 = T5WW.addMassPlane([[x, 0.05*x + 0.95*y, y]]*2)
T5WW_2.addSource('efficiencyMap','orig/T5WW_x005/MA5_EM_T5WW_Glu005Neu095_$datasetShortStr$.dat','txt')
T5WW_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5WW_3 = T5WW.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5WW_3.addSource('efficiencyMap','orig/T5WW_x095/MA5_EM_T5WW_Glu095Neu005_$datasetShortStr$.dat','txt')
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
#+++++++ next txName block ++++++++++++++
#+++++++ next mass plane block ++++++++++++++
T5ZZ_1 = T5ZZ.addMassPlane([[x,0.5*(x+y),y]]*2)
T5ZZ_1.addSource('efficiencyMap','orig/T5ZZ_x05/MA5_EM_T5ZZ_x05_$datasetShortStr$.dat', 'txt')
T5ZZ_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_2 = T5ZZ.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5ZZ_2.addSource('efficiencyMap','orig/T5ZZ_x005/MA5_EM_T5ZZ_Glu005Neu095_$datasetShortStr$.dat', 'txt')
T5ZZ_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5ZZ_3 = T5ZZ.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5ZZ_3.addSource('efficiencyMap','orig/T5ZZ_x095/MA5_EM_T5ZZ_Glu095Neu005_$datasetShortStr$.dat', 'txt')
T5ZZ_3.dataUrl = None
"""
T5ZZoff = dataset.addTxName('T5ZZoff')
T5ZZoff.constraint ="2.1*[[['jet','jet'],['jet','jet']],[['jet','jet'],['jet','jet']]]"
T5ZZoff.conditionDescription =None
T5ZZoff.condition =None
T5ZZoff.massConstraint = [['dm >= 0.0','dm <= 86.']]*2
T5ZZoff.source = "SModelS"
T5ZZoff.addMassPlane(T5ZZ_1)
T5ZZoff.addMassPlane(T5ZZ_2)
T5ZZoff.addMassPlane(T5ZZ_3)
"""

#+++++++ next mass plane block ++++++++++++++
fullpath = "./orig/atlas_susy_2013_04_T2tt_1_EM_MAPS/MA5_EM_T2tt_1_$datasetShortStr$.dat"
T2tt = dataset.addTxName('T2tt')
T2tt.checked ="None"
T2tt.constraint ="[[['t']],[['t']]]"
T2tt.conditionDescription ="None"
T2tt.condition ="None"
T2tt.source = "SModelS"
T2tt_1 = T2tt.addMassPlane([[x,y]]*2)
T2tt_1.addSource('efficiencyMap', fullpath , "txt")
T2tt_1.dataUrl=None

#+++++++ next mass plane block ++++++++++++++
T2ttoff = dataset.addTxName('T2ttoff')
T2ttoff.checked ="None"
T2ttoff.constraint ="[[['W','b']],[['W','b']]]"
T2ttoff.conditionDescription ="None"
T2ttoff.condition ="None"
T2ttoff.source = "SModelS"
T2ttoff_1 = T2ttoff.addMassPlane([[x,y]]*2)
T2ttoff.massConstraint = [['dm <= 169.0']]*2
T2ttoff_1.addSource('efficiencyMap', fullpath , "txt")
T2ttoff_1.dataUrl=None

T1bbbb = dataset.addTxName('T1bbbb')
T1bbbb.checked ="None"
T1bbbb.constraint ="[[['b','b']],[['b','b']]]"
T1bbbb.conditionDescription ="None"
T1bbbb.condition ="None"
T1bbbb.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T1bbbb = T1bbbb.addMassPlane([[x,y]]*2)
T1bbbb.addSource('efficiencyMap',"./orig/atlas_susy_2013_04_T1bbbb_1_EM_MAPS/MA5_EM_T1bbbb_1_$datasetShortStr$.dat", "txt")
T1bbbb.dataUrl= None

T1btbt = dataset.addTxName('T1btbt')
T1btbt.checked ="None"
T1btbt.constraint ="[[['b','t']],[['b','t']]]"
T1btbt.conditionDescription ="None"
T1btbt.condition ="None"
T1btbt.source = "SModelS"
#+++++++ next mass plane block ++++++++++++++
T1btbt = T1btbt.addMassPlane([[x,y]]*2)
T1btbt.addSource('efficiencyMap',"./orig/atlas_susy_2013_04_T1btbt_1_EM_MAPS/MA5_EM_T1btbt_1_$datasetShortStr$.dat", "txt")
T1btbt.dataUrl= None

T5 = dataset.addTxName('T5')
T5.constraint ="[[['jet'],['jet']],[['jet'],['jet']]]"
T5.conditionDescription =None
T5.condition =None
T5.massConstraint = None
T5.source = "SModelS"
T5.massConstraint = [['dm >= 0.0','dm > 76.']]*2
#+++++++ next txName block ++++++++++++++
#+++++++ next mass plane block ++++++++++++++
T5_1 = T5.addMassPlane([[x,0.5*(x+y),y]]*2)
T5_1.addSource('efficiencyMap','orig/atlas_susy_2013_04_T5_x05_EM_MAPS/MA5_EM_T5_x05_$datasetStr$.dat', 'txt')
T5_1.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5_2 = T5.addMassPlane([[x,0.05*x + 0.95*y,y]]*2)
T5_2.addSource('efficiencyMap','orig/atlas_susy_2013_04_T5_x005_EM_MAPS/MA5_EM_T5_x005_$datasetStr$.dat', 'txt')
T5_2.dataUrl = None
#+++++++ next mass plane block ++++++++++++++
T5_3 = T5.addMassPlane([[x, 0.95*x + 0.05*y, y]]*2)
T5_3.addSource('efficiencyMap','orig/atlas_susy_2013_04_T5_x095_EM_MAPS/MA5_EM_T5_x095_$datasetStr$.dat', 'txt')
T5_3.dataUrl = None

T6bbWW = dataset.addTxName('T6bbWW')
T6bbWW.constraint = "[[['b'],['W']],[['b'],['W']]]"
T6bbWW.conditionDescription =None
T6bbWW.condition =None
T6bbWW.massConstraint = None
T6bbWW.source = "SModelS"
T6bbWW.dataUrl = None
T6bbWW_1 = T6bbWW.addMassPlane([[x, 0.1*y + 0.9*x, y]]*2)
T6bbWW_1.addSource('efficiencyMap', 'orig/atlas_susy_2013_04_T6bbWW_x01_EM_MAPS/MA5_EM_T6bbWW_x01_$datasetStr$.dat', 'txt')
#+++++++ next mass plane block ++++++++++++++
T6bbWW_2 = T6bbWW.addMassPlane([[x, 0.5*x + 0.5*y, y]]*2)
T6bbWW_2.addSource('efficiencyMap','orig/atlas_susy_2013_04_T6bbWW_x05_EM_MAPS/MA5_EM_T6bbWW_x05_$datasetStr$.dat','txt')
#+++++++ next mass plane block ++++++++++++++
T6bbWW_3 = T6bbWW.addMassPlane([[x, 0.9*y + 0.1*x, y]]*2)
T6bbWW_3.addSource('efficiencyMap','orig/atlas_susy_2013_04_T6bbWW_x09_EM_MAPS/MA5_EM_T6bbWW_x09_$datasetStr$.dat','txt')

END_BLOCK_TO_FILL

databaseCreator.create()

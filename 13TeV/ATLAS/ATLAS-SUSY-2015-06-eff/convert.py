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
info = MetaInfoInput('ATLAS-SUSY-2015-06')
info.url = 'http://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-06/'
info.sqrts = 13
info.lumi = 3.2
info.prettyName = 'ATLAS 2-6jets 0lep'
info.private = False
info.arxiv =  'https://arxiv.org/abs/1605.03814'
#info.contact =
info.publication = 'http://link.springer.com/article/10.1140/epjc/s10052-016-4184-8'
info.comment = 'UL analyses does not have digital data available'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2 = TxNameInput('T2')
T2.on.checked =''
#T2.off.checked =
T2.on.constraint = "[[['jet']],[['jet']]]"
#T2.off.constraint = 
T2.on.conditionDescription = None
#T2.off.conditionDescription =
T2.on.condition = None
#T2.off.condition =
#T2.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(motherMass = x, lspMass =y )
#---- new efficiency map -----
#----figure----
T2_1.figure ='Fig. Aux. 19b'
T2_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure19b.png'
#----exclusion source----
T2_1.obsExclusion.setSource( 'orig/Obs_Line_T2.dat','txt',objectName = None, index = None )
#T2_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T2_1.expExclusion.setSource( 'orig/Exp_Line_T2.dat','txt', objectName = None, index = None )
#T2_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR2jl.dat', 'txt', objectName = None, index = None, dataset="SR2jl" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=263, expectedBG=283, bgError=24 )
#----global url settings ----
T2_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d65/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d65/input'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2_1.figure = 'Fig. Aux. 20b'
T2_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/figAuxiliaryFigure20b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR2jm.dat', 'txt', objectName = None, index = None, dataset="SR2jm" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=191, expectedBG=191, bgError=21 )
#----global url settings ----
T2_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d67/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d67/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2_1.figure = 'Fig. Aux. 21b'
T2_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/figAuxiliaryFigure21b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR2jt.dat', 'txt', objectName = None, index = None, dataset="SR2jt" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=26, expectedBG=23, bgError=4 )
#----global url settings ----
T2_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d69/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d69/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2_1.figure ='Fig. Aux. 22b'
T2_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1458270/figAuxiliaryFigure22b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR4jt.dat', 'txt', objectName = None, index = None, dataset="SR4jt" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=7, expectedBG=4.1, bgError=1.1 )
#----global url settings ----
T2_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d71/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d71/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2_1.figure = 'Fig. Aux. 23b'
T2_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/figAuxiliaryFigure23b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR5j.dat', 'txt', objectName = None, index = None, dataset="SR5j" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=7, expectedBG=13.2, bgError=2.2 )
#----global url settings ----
T2_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d73/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d73/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2_1.figure ='Fig. Aux. 24b'
T2_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure24b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR6jm.dat', 'txt', objectName = None, index = None, dataset="SR6jm" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=4, expectedBG=6.9, bgError=1.5 )
#----global url settings ----
T2_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d75/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d75/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2_1.figure ='Fig.Aux. 25b'
T2_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure25b.png'
#----limit source----
T2_1.efficiencyMap.setSource( 'orig/AccXEff_T2_SR6jt.dat', 'txt', objectName = None, index = None, dataset="SR6jt" )
T2_1.efficiencyMap.usePercentage(False)
T2_1.efficiencyMap.setStatistics( observedN=3, expectedBG=4.2, bgError=1.2 )
#----global url settings ----
T2_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d77/input'
#----efficiency map url settings ----
T2_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d77/input'
databaseCreator.create(True)


#+++++++ next txName block ++++++++++++++
T1 = TxNameInput('T1')
T1.on.checked =''
#T1.off.checked =
T1.on.constraint = "[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =
T1.on.conditionDescription = None
#T1.off.conditionDescription =
T1.on.condition = None
#T1.off.condition =
#T1.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(motherMass = x, lspMass = y )
#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 26b'
T1_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1458270/figAuxiliaryFigure26b.png'
#----exclusion source----
T1_1.obsExclusion.setSource( 'orig/Obs_Line_T1.dat', 'txt', objectName = None, index = None )
#T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T1_1.expExclusion.setSource( 'orig/Exp_Line_T1.dat', 'txt', objectName = None, index = None )
#T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR2jl.dat', 'txt', objectName = None, index = None, dataset="SR2jl" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=263, expectedBG=283, bgError=24 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d79/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d79/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 27b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure27b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR2jm.dat', 'txt', objectName = None, index = None, dataset="SR2jm" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=191, expectedBG=191, bgError=21 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d79/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d79/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 28b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure28b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR2jt.dat', 'txt', objectName = None, index = None, dataset="SR2jt" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=26, expectedBG=23, bgError=4 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d81/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d81/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 29b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure29b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR4jt.dat', 'txt', objectName = None, index = None, dataset="SR4jt" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=7, expectedBG=4.6, bgError=1.1 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d85/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d85/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 30b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure30b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR5j.dat', 'txt', objectName = None, index = None, dataset="SR5j" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=7, expectedBG=13.2, bgError=2.2 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d87/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d87/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure ='Fig. Aux. 31b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure31b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR6jm.dat', 'txt', objectName = None, index = None, dataset="SR6jm" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=4, expectedBG=6.9, bgError=1.5 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d89/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1458270/d89/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1_1.figure = 'Fig. Aux. 32b'
T1_1.figureUrl = 'http://hepdata.cedar.ac.uk/resource/1458270/thumb_figAuxiliaryFigure32b.png'
#----limit source----
T1_1.efficiencyMap.setSource( 'orig/AccXEff_T1_SR6jt.dat', 'txt', objectName = None, index = None, dataset="SR6jt" )
T1_1.efficiencyMap.usePercentage(False)
T1_1.efficiencyMap.setStatistics( observedN=3, expectedBG=4.2, bgError=1.2 )
#----global url settings ----
T1_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d91/input'
#----efficiency map url settings ----
T1_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1458270/d91/input'
databaseCreator.create(True)



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
info.prettyName ='Three b'
info.private =False
info.arxiv = 'http://arxiv.org/abs/1407.0600'
info.contact =''
info.publication ='http://link.springer.com/article/10.1007/JHEP10(2014)024'
info.comment ='Using combined Exclusion line'
info.supersedes =''
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
T1bbbb_1 = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
#---- new efficiency map -----
#----figure----
T1bbbb_1.figure = 'Figure 5a and Figure 6a'
T1bbbb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_05a.png'
#----exclusion source----
T1bbbb_1.obsExclusion.setSource( 'orig/T1bbbb_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt', objectName = None, index = None )
#T1bbbb_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1bbbb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T1bbbb_1.efficiencyMap.setSource( 'orig/EffMap_T1bbbb_SR-0l-4j-A.txt', 'txt', objectName = None, index = None, dataset="SR-0l-4j-A" )
T1bbbb_1.efficiencyMap.setStatistics( observedN=2, expectedBG=1.6, bgError=0.9 )
#----global url settings ----
T1bbbb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1bbbb_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1304457/d30/input http://hepdata.cedar.ac.uk/view/ins1304457/d31/input'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T1bbbb_1.figure = 'Figure 5b and Figure 6b'
T1bbbb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_05b.png'
#----limit source----
T1bbbb_1.efficiencyMap.setSource( 'orig/EffMap_T1bbbb_SR-0l-4j-B.txt', 'txt', objectName = None, index = None, dataset="SR-0l-4j-B" )
T1bbbb_1.efficiencyMap.setStatistics( observedN=3, expectedBG=1.3, bgError=0.9 )
#----global url settings ----
T1bbbb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1bbbb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d30/input http://hepdata.cedar.ac.uk/view/ins1304457/d31/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1bbbb_1.figure = 'Figure 5c and Figure 6c'
T1bbbb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_05c.png'
#----limit source----
T1bbbb_1.efficiencyMap.setSource( 'orig/EffMap_T1bbbb_SR-0l-4j-C.txt', 'txt', objectName = None, index = None, dataset="SR-0l-4j-C" )
T1bbbb_1.efficiencyMap.setStatistics( observedN= 1, expectedBG=1.6, bgError=0.7 )
#----global url settings ----
T1bbbb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1bbbb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d30/input http://hepdata.cedar.ac.uk/view/ins1304457/d31/input'
databaseCreator.create(True)




#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked =""
#T1tttt.off.checked =
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription ="None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition ="None"
#T1tttt.off.condition =
#T1tttt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(motherMass = x, lspMass = y )
#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 13b'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14a.png'
#----exclusion source----
T1tttt_1.obsExclusion.setSource( 'orig/T1tttt_ATLAS-SUSY-2013-18-Obs_Excl.dat', 'txt', objectName = None, index = None )
#T1tttt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1tttt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-0l-7j-A.txt', 'txt', objectName = None, index = None, dataset="SR-0l-7j-A" )
T1tttt_1.efficiencyMap.setStatistics( observedN=21, expectedBG=21.2, bgError=4.6 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 14b and Figure 15b'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14b.png'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-0l-7j-B.txt', 'txt', objectName = None, index = None, dataset="SR-0l-7j-B" )
T1tttt_1.efficiencyMap.setStatistics( observedN=3, expectedBG=3.2, bgError=1.6 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 14c and Figure 15c'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14c.png'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-0l-7j-C.txt', 'txt', objectName = None, index = None, dataset="SR-0l-7j-C" )
T1tttt_1.efficiencyMap.setStatistics( observedN=1, expectedBG=0.9, bgError=1 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 14d and Figure 15d'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14d.png'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-1l-6j-A.txt', 'txt', objectName = None, index = None, dataset="SR-1l-6j-A" )
T1tttt_1.efficiencyMap.setStatistics( observedN=7, expectedBG=13.5, bgError=3.2 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 14e and Figure 15e'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14e.png'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-1l-6j-B.txt', 'txt', objectName = None, index = None, dataset="SR-1l-6j-B" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=6.1, bgError=1.8 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T1tttt_1.figure = 'Figure 14f and Figure 15f'
T1tttt_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-18/figaux_14f.png'
#----limit source----
T1tttt_1.efficiencyMap.setSource( 'orig/EffMap_T1tttt_SR-1l-6j-C.txt', 'txt', objectName = None, index = None, dataset="SR-1l-6j-C" )
T1tttt_1.efficiencyMap.setStatistics( observedN=0, expectedBG=2.3, bgError=0.7 )
#----global url settings ----
T1tttt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/all'
#----efficiency map url settings ----
T1tttt_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304457/d43/input http://hepdata.cedar.ac.uk/view/ins1304457/d44/input'
databaseCreator.create(True)



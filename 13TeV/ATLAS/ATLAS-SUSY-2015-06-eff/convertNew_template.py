#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse

argparser = argparse.ArgumentParser(description = \
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ( '-utilsPath', '--utilsPath',
			                   help = 'path to the package smodels_utils',\
					               type = str )
argparser.add_argument ( '-smodelsPath', '--smodelsPath',
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

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2015-06')
info.url = 'http://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-06/'
info.sqrts = 13
info.lumi = 3.2
info.prettyName = 'ATLAS 2-6jets 0lep'
info.private = False
info.arxiv =  'https://arxiv.org/abs/1605.03814'
info.contact = 'ATLAS collaboration'
info.publication = 'http://link.springer.com/article/10.1140/epjc/s10052-016-4184-8'
info.comment = 'UL analyses does not have digital data available'
#info.supersedes =
#info.supersededBy =

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)

T2 = dataset.addTxName('T2')
T2.checked = 'NO'
T2.constraint ="[[['jet']],[['jet']]]"
T2.conditionDescription = None
T2.condition = None
T2.source = "ATLAS"

#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane( [[x,y]]*2 )
#---- new efficiency map -----
#----figure----
T2_1.figureUrl = $$
T2_1.figure = $$
#----exclusion source----
T2_1.addSource( 'obsExclusion', 'orig/Obs_Line_T2.dat', 'txt', objectName = None, index = None )
T2_1.addSource( 'expExclusion', 'orig/Exp_Line_T2.dat', 'txt', objectName = None, index = None )
T2_1.addSource( 'efficiencyMap', 'orig/AccXEff_T2_$datasetStr$.dat', 'txt', objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
T2_1.dataUrl = $$

T1 = dataset.addTxName('T1')
T1.checked = 'NO'
T1.constraint ="[[['jet','jet']],[['jet','jet']]]"
T1.conditionDescription = None
T1.condition = None
T1.source = "ATLAS"

#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane( [[x,y]]*2 )
#---- new efficiency map -----
#----figure----
T1_1.figureUrl = $$
T1_1.figure = $$
#----exclusion source----
T1_1.addSource( 'obsExclusion', 'orig/Obs_Line_T1.dat', 'txt', objectName = None, index = None )
T1_1.addSource( 'expExclusion', 'orig/Exp_Line_T1.dat', 'txt', objectName = None, index = None )
T1_1.addSource( 'efficiencyMap', 'orig/AccXEff_T1_$datasetStr$.dat', 'txt', objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
T1_1.dataUrl = $$


END_BLOCK_TO_FILL
databaseCreator.create()

"""
#----limit source----
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=23, expectedBG=29, bgError=5 )
#----global url settings ----
T2bb_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/d28/input,http://hepdata.cedar.ac.uk/view/ins1472822/d33/input'
databaseCreator.create()

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6c,Fig.7c'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06c.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07c.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRA350.txt', 'txt', objectName = None, index = None, dataset="SRA350" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=6, expectedBG=7, bgError=1.2 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d29/input,http://hepdata.cedar.ac.uk/view/ins1472822/d34/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6d,Fig.7d'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06d.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07d.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRA450.txt', 'txt', objectName = None, index = None, dataset="SRA450" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=1, expectedBG=1.8, bgError=0.4 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/d30/input,http://hepdata.cedar.ac.uk/view/ins1472822/d35/input'
databaseCreator.create(True)

#---- new efficiency map -----
#----figure----
T2bb_1.figure = 'Fig.6e,Fig.7e'
T2bb_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_06e.png,https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-01/figaux_07e.png'
#----limit source----
T2bb_1.efficiencyMap.setSource( 'orig/EffMap_T2bb_SRB.txt', 'txt', objectName = None, index = None, dataset="SRB" )
T2bb_1.efficiencyMap.usePercentage(False)
T2bb_1.efficiencyMap.setStatistics( observedN=6, expectedBG=12, bgError=2.5 )
#----global url settings ----
T2bb_1.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1472822/all'
#----efficiency map url settings ----
T2bb_1.efficiencyMap.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1472822/d31/input,http://hepdata.cedar.ac.uk/view/ins1472822/d36/input'
databaseCreator.create(True)
"""

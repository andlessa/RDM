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
info = MetaInfoInput('ATLAS-SUSY-2015-02')
info.url = 'http://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-02/'
info.sqrts = 13
info.lumi = 3.2
info.prettyName = 'Top 1l'
info.private = False
info.arxiv =  'https://arxiv.org/abs/1606.03903'
info.source = "ATLAS"
info.publication ='http://journals.aps.org/prd/abstract/10.1103/PhysRevD.94.052009' 
info.comment = 'Very weird exclusion due to best CLs selection, and fluctuation in the Obs data' 
#info.supersedes =
#info.supersededBy =

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)

T2tt = dataset.addTxName('T2tt')
T2tt.checked = 'NO'
T2tt.constraint ="[[['t']],[['t']]]"
T2tt.conditionDescription = None
T2tt.condition = None
T2tt.source = "ATLAS"

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane( [[x,y]]*2 )
#---- new efficiency map -----
#----figure----
T2tt_1.figureUrl = $$
T2tt_1.figure = $$
#----exclusion source----
T2tt_1.addSource( 'obsExclusion', 'orig/T2tt_ATLAS_SUSY_2015_02_Obs.txt', 'txt', objectName = None, index = None )
T2tt_1.addSource( 'expExclusion', 'orig/T2tt_ATLAS_SUSY_2015_02_Exp.txt', 'txt', objectName = None, index = None )
T2tt_1.addSource( 'efficiencyMap', 'orig/EffMap_T2tt_$datasetStr$.txt', 'txt', objectName = None, index = None )
#T2bb_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2bb_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
T2tt_1.dataUrl = $$
END_BLOCK_TO_FILL
databaseCreator.create()

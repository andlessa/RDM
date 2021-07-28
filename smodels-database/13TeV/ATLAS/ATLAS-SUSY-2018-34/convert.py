#!/usr/bin/env python3

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



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2018-34')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/"
info.sqrts = 13
info.lumi = 139.0
info.prettyName = "b-jets + Etmiss"
info.private = False
info.arxiv =  'https://arxiv.org/abs/2101.12527'
info.contact = 'atlas-phys-susy-conveners@cern.ch'
info.comment = 'Only T2bb upper limits implemented. Values digitized by hand.'
info.publication ='https://link.springer.com/article/10.1007/JHEP05(2021)093'


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++ next txName block ++++++++++++++
T2bb = dataset.addTxName('T2bb')
T2bb.checked = ''
T2bb.constraint ="[[['b']],[['b']]]"
T2bb.conditionDescription = None
T2bb.condition = None
T2bb.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(2*[[x, y]])
T2bb_1.figure = 'Figaux.1a'
T2bb_1.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01a.png'
T2bb_1.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01a.png'
T2bb_1.exclusionDataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01a.png'
T2bb_1.setSources(dataLabels= ['obsExclusion', 'upperLimits'],
                 dataFiles= ['orig/fig_aux01a_exclusion.csv' , 'orig/fig_aux01a_upperLimits.csv'],
                 dataFormats= ['csv', 'csv'],units=[None,'fb'])

T2bb_2 = T2bb.addMassPlane(2*[[x, x-y]])
T2bb_2.figure = 'Figaux.1b'
T2bb_2.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01b.png'
T2bb_2.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01b.png'
T2bb_2.exclusionDataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-34/figaux_01b.png'
T2bb_2.setSources(dataLabels= ['obsExclusion', 'upperLimits'],
                 dataFiles= ['orig/fig_aux01b_exclusion.csv' , 'orig/fig_aux01b_upperLimits.csv'],
                 dataFormats= ['csv', 'csv'],units=[None,'fb'])



databaseCreator.create()

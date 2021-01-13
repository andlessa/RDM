#!/usr/bin/env python3

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
    type = str, default = '~/smodels-utils' )
argparser.add_argument ('-smodelsPath', '--smodelsPath',
    help = 'path to the package smodels_utils',\
    type = str, default = '~/smodels' )
argparser.add_argument ('-no', '--noUpdate',
    help = 'do not update the lastUpdate field.',\
    action= "store_true" )
argparser.add_argument ('-r', '--resetValidation',
    help = 'reset the validation flag',\
    action= "store_true" )

args = argparser.parse_args()

if args.noUpdate:
    os.environ["SMODELS_NOUPDATE"]="1"

if args.resetValidation:
    os.environ["SMODELS_RESETVALIDATION"]="1"

utilsPath = args.utilsPath
sys.path.append(os.path.abspath(os.path.expanduser(utilsPath)))
sys.path.append(os.path.abspath(os.path.expanduser(args.smodelsPath)))



from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y,z

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-EXO-19-001')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-19-001/index.html'
info.sqrts = 13
info.lumi = 137.0
info.prettyName ='displaced vertices'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1906.06441'
info.contact ='CMS collaboration'
info.publication ='http://arxiv.org/abs/1906.06441.pdf'
info.comment ='Search for displaced jets plust MET. The data was digitized from the figures in the publication.'
particlesFile = os.path.abspath('../../../databaseParticles.py')

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('SR')
dataset.setInfo(dataType = 'efficiencyMap', dataId = 'SR',
            observedN=0,
            expectedBG=1.1, bgError=1.1)

#+++++++ txnames ++++++++++++++++++++
#+++++++ next txName block ++++++++++++++
T3Disp = dataset.addTxName('T2Disp')
T3Disp.checked =''
T3Disp.constraint = "[[[jet]],[[jet]]]"
T3Disp.condition =None
T3Disp.finalState = ['MET','MET']
T3Disp.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-19-001/CMS-EXO-19-001_Figure_003.pdf'
T3Disp.source = 'CMS'
T3Disp.setParticlesFromFile(particlesFile)
#Add plane for interpolation
plane_1 = T3Disp.addMassPlane([[(x,y),10.0]]*2)
plane_1.setSources(dataLabels= ['efficiencyMap'],
                    dataFiles=['./orig/CMS-EXO-19-001_Figure_003.txt'],
                    coordinates = [{x: 0, y:1, 'value' : 2}],
                    dataFormats=['txt'])


plane_2 = T3Disp.addMassPlane([[(x,y),0.0]]*2)
plane_2.setSources(dataLabels= ['efficiencyMap'],
                    dataFiles=['./orig/CMS-EXO-19-001_Figure_003.txt'],
                    coordinates = [{x: 0, y:1, 'value' : 2}],
                    dataFormats=['txt'])
plane_2.addSource(dataLabel= 'obsExclusion',
                    dataFile='./orig/CMS-EXO-19-001_Figure_004.csv',
                    coordinateMap = {x: 1, y: 2, 'value' : None},
                    dataFormat='csv')

databaseCreator.create()

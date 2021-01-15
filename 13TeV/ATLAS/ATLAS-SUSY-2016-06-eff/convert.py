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
from smodels_utils.dataPreparation.dataHandlerObjects import hbar
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2016-06')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-06/"
info.sqrts = 13
info.lumi = 36.1
info.prettyName = "disappearing track"
info.private = False
info.arxiv =  'https://arxiv.org/abs/1712.02118'
info.contact = 'ATLAS collaboration'
info.publication ='JHEP 06 (2018) 022'
particlesFile = os.path.abspath('../../../databaseParticles.py')

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('SR_EW')
dataset.setInfo(dataType = 'efficiencyMap', dataId = 'SR_EW',
                    observedN = 9, expectedBG = 11.8, bgError=3.1,
                    expectedUpperLimit = '0.28*fb', upperLimit = '0.22*fb')

#+++++++ next txName block ++++++++++++++
TDTM1F = dataset.addTxName('TDTM1F')
TDTM1F.setParticlesFromFile(particlesFile)
TDTM1F.checked = ''
TDTM1F.constraint ="[[['pion']],[['pion']]]"
TDTM1F.intermediateState = [['C1+'],['C1-']]
TDTM1F.finalState = ['MET','MET']
TDTM1F.conditionDescription = None
TDTM1F.condition = None
TDTM1F.source = "Recasting (F. Rojas and S. Belyaev)"

#+++++++ next mass plane block ++++++++++++++
labels = [ 'efficiencyMap' ]
formats = [ 'txt']
TDTM1F_1 = TDTM1F.addMassPlane(2*[[(x,y), x-0.15]])

TDTM1F_1.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1C1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )

#Add second plane for interpolation (assume 0.5 GeV is still safe)
TDTM1F_2 = TDTM1F.addMassPlane(2*[[(x,y), x-0.5]])
TDTM1F_2.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1C1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )


databaseCreator.create()

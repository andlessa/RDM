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
info.type = 'displaced'
info.source = "Based on the recasting implemented by A. Belyaev, S. Prestel, F. Rojas-Abbate and J. Zurita (arxiv 2008.08581)"
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
TDTM1F.constraint ="[['*'],['*']]"
TDTM1F.intermediateState = [['C1+'],['C1-']]
TDTM1F.finalState = ['MET','MET']
TDTM1F.conditionDescription = None
TDTM1F.condition = None
TDTM1F.source = "Recasting (F. Rojas and S. Belyaev)"

#+++++++ next mass plane block ++++++++++++++
labels = [ 'efficiencyMap' ]
formats = [ 'txt']
TDTM1F_1 = TDTM1F.addMassPlane(2*[[(x,y), x]])

TDTM1F_1.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1C1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )


#Add second plane for interpolation (assume 1.0 GeV is still safe)
TDTM1F_2 = TDTM1F.addMassPlane(2*[[(x,y), x-1.0]])
TDTM1F_2.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1C1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )
TDTM1F_2.addSource(dataLabel='obsExclusion',
                    dataFile='orig/HEPData-ins1641262-v4-Exclusion_contour_EW_2_obs_conv.txt',
                    coordinateMap = {x : 0, y: 1, 'value' : None}, dataFormat = 'txt')


#+++++++ next txName block ++++++++++++++
TDTM2F = dataset.addTxName('TDTM2F')
TDTM2F.setParticlesFromFile(particlesFile)
TDTM2F.checked = ''
TDTM2F.constraint ="[['*'],[]]"
TDTM2F.intermediateState = [['C1'],[]]
TDTM2F.finalState = ['MET','MET']
TDTM2F.conditionDescription = None
TDTM2F.condition = None
TDTM2F.source = "Recasting (F. Rojas and S. Belyaev)"

#+++++++ next mass plane block ++++++++++++++
TDTM2F_1 = TDTM2F.addMassPlane([[(x,y), x],[x]])

TDTM2F_1.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1N1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )

#Add second plane for interpolation (assume 1.0 GeV is still safe)
TDTM2F_2 = TDTM2F.addMassPlane([[(x,y), x-1.0],[x-1.0]])
TDTM2F_2.setSources(dataLabels= labels,
                 dataFiles= ['./orig/C1N1_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )
TDTM2F_2.addSource(dataLabel='obsExclusion',
                    dataFile='orig/HEPData-ins1641262-v4-Exclusion_contour_EW_2_obs_conv.txt',
                    coordinateMap = {x : 0, y: 1, 'value' : None}, dataFormat = 'txt')



#+++++++ next txName block ++++++++++++++
TDTM1S = dataset.addTxName('TDTM1S')
TDTM1S.setParticlesFromFile(particlesFile)
TDTM1S.checked = ''
TDTM1S.constraint ="[['*'],['*']]"
TDTM1S.intermediateState = [['H+'],['H-']]
TDTM1S.finalState = ['MET','MET']
TDTM1S.conditionDescription = None
TDTM1S.condition = None
TDTM1S.source = "Recasting (F. Rojas and S. Belyaev)"

#+++++++ next mass plane block ++++++++++++++
labels = [ 'efficiencyMap' ]
formats = [ 'txt']
TDTM1S_1 = TDTM1S.addMassPlane(2*[[(x,y), x]])

TDTM1S_1.setSources(dataLabels= labels,
                 dataFiles= ['./orig/HcHc_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )


#Add second plane for interpolation (assume 1.0 GeV is still safe)
TDTM1S_2 = TDTM1S.addMassPlane(2*[[(x,y), x-1.0]])
TDTM1S_2.setSources(dataLabels= labels,
                 dataFiles= ['./orig/HcHc_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )


#+++++++ next txName block ++++++++++++++
TDTM2S = dataset.addTxName('TDTM2S')
TDTM2S.setParticlesFromFile(particlesFile)
TDTM2S.checked = ''
TDTM2S.constraint ="[['*'],[]]"
TDTM2S.intermediateState = [['Hpm'],[]]
TDTM2S.finalState = ['MET','MET']
TDTM2S.conditionDescription = None
TDTM2S.condition = None
TDTM2S.source = "Recasting (F. Rojas and S. Belyaev)"

#+++++++ next mass plane block ++++++++++++++
TDTM2S_1 = TDTM2S.addMassPlane([[(x,y), x],[x]])

TDTM2S_1.setSources(dataLabels= labels,
                 dataFiles= ['./orig/HcH0_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )

#Add second plane for interpolation (assume 1.0 GeV is still safe)
TDTM2S_2 = TDTM2S.addMassPlane([[(x,y), x-1.0],[x-1.0]])
TDTM2S_2.setSources(dataLabels= labels,
                 dataFiles= ['./orig/HcH0_eff.txt'],
                 dataFormats= formats, coordinates = [{x : 0, y: 2, 'value' : 3}] )



databaseCreator.create()

#!/usr/bin/env python3

"""
.. module:: convert
   :synopsis: used to create info.dat and the <txname>.dat files.

"""
import sys
import os
import argparse
import types


argparser = argparse.ArgumentParser(description =
    'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath',
    help = 'path to the package smodels_utils',\
    type = str, default = os.path.expanduser('~/smodels-utils') )
argparser.add_argument ('-smodelsPath', '--smodelsPath',
    help = 'path to the package smodels_utils',\
    type = str, default = os.path.expanduser('~/smodels') )
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
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z


#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-EXO-12-026')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-12-026/index.html'
info.sqrts = 8
info.lumi = 18.8
info.prettyName ='hscp search'
info.private = False
info.contact ='cms-pag-conveners-exotica@cern.ch'
info.arxiv = 'https://arxiv.org/abs/1305.0491'
info.comment ='Upper limits digitized from Track+TOF png plots. Used conservative gluino bounds (50% gluino-gluon probability) and curve for the cloud model for the squark R-hadron constraints.'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++ txnames ++++++++++++++++++++
#+++++++ next txName block ++++++++++++++
HSCPM1 = dataset.addTxName('THSCPM1b')
HSCPM1.checked =''
HSCPM1.constraint = "[[],[]]"
HSCPM1.condition =None
HSCPM1.finalState = ['HSCP','HSCP']
HSCPM1.massConstraints = None
HSCPM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-12-026/CMS-EXO-12-026_Figure_008-d.png'
HSCPM1.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
plane = HSCPM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits'],
                    dataFiles=['orig/CMS-EXO-12-026_Figure_008-d_stau.dat'],
                    dataFormats=['txt'],units=['pb'])
plane.addSource(dataLabel='obsExclusion',dataFile='orig/Stau_ExclusionObs.csv',
                            coordinateMap = {x : 0, 'value' : None}, dataFormat = 'csv')


#+++++++ next txName block ++++++++++++++
RHadGM1 = dataset.addTxName('TRHadGM1')
RHadGM1.checked =''
RHadGM1.constraint = "[[],[]]"
RHadGM1.condition =None
RHadGM1.finalState = ['RHadronG','RHadronG']
RHadGM1.massConstraints = None
RHadGM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-12-026/CMS-EXO-12-026_Figure_008-d.png'
RHadGM1.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
plane = RHadGM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits'],
                    dataFiles=['orig/CMS-EXO-12-026_Figure_008-d_gluino50.dat'],
                    dataFormats=['txt'],units=['pb'])
plane.addSource(dataLabel='obsExclusion',dataFile='orig/Gluino_ExclusionObs.csv',
                            coordinateMap = {x : 0, 'value' : None}, dataFormat = 'csv')


#+++++++ next txName block ++++++++++++++
RHadUM1 = dataset.addTxName('TRHadUM1')
RHadUM1.checked =''
RHadUM1.constraint = "[[],[]]"
RHadUM1.condition =None
RHadUM1.finalState = ['RHadronU','RHadronU']
RHadUM1.massConstraints = None
RHadUM1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-12-026/CMS-EXO-12-026_Figure_008-d.png'
RHadUM1.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
plane = RHadUM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits'],
                    dataFiles=['orig/CMS-EXO-12-026_Figure_008-d_stop.dat'],
                    dataFormats=['txt'],units=['pb'])
plane.addSource(dataLabel='obsExclusion',dataFile='orig/Stop_ExclusionObs.csv',
                            coordinateMap = {x : 0, 'value' : None}, dataFormat = 'csv')


databaseCreator.create()
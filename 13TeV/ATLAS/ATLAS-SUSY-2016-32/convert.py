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
from smodels_utils.dataPreparation.massPlaneObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2016-32')
info.url = 'http://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-32/index.html'
info.sqrts = 13
info.lumi = 31.6
info.prettyName ='hscp search'
info.private = False
info.arxiv = 'https://arxiv.org/abs/1902.01636'
info.contact ='atlas-phys-susy-conveners@cern.ch'
info.publication ='https://arxiv.org/pdf/1902.01636.pdf'
info.comment ='Search for long-lived charged particles. The full-detector limits were considered for all topologies, except for the limits on meta-stable gluinos, which include the MS-agnostic limits.'
info.supersedes =''
particlesFile = os.path.abspath('../../../databaseParticles.py')

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
HSCPM1.dataUrl = 'https://www.hepdata.net/record/86565?version=1&table=Table13'
HSCPM1.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
plane = HSCPM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits','expectedUpperLimits','obsExclusion'],
                    dataFiles=['orig/Table13_ULobs.csv','orig/Table13_ULexp.csv','orig/Stau_ExclusionObs.csv'],
                    dataFormats=['csv','csv','csv'],units=['fb','fb',None],
                    coordinates = [{x : 0, 'value' : 1},{x : 0, 'value' : 1},{x : 0, 'value' : None}])

#+++++++ next txName block ++++++++++++++
RHadGM1 = dataset.addTxName('TRHadGM1')
RHadGM1.checked =''
RHadGM1.constraint = "[[],[]]"
RHadGM1.condition =None
RHadGM1.finalState = ['RHadronG','RHadronG']
RHadGM1.massConstraints = None
RHadGM1.dataUrl = 'https://www.hepdata.net/record/86565?version=1&table=Table17;https://www.hepdata.net/record/86565?version=1&table=Table10'
RHadGM1.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
plane = RHadGM1.addMassPlane([[(x, y)]]*2)
plane.setSources(dataLabels=['upperLimits','expectedUpperLimits','obsExclusion'],
                    dataFiles=['orig/Table17_ULobs.csv','orig/Table17_ULexp.csv','orig/Table15_ExclusionObs.csv'],
                    dataFormats=['csv','csv','csv'],units=['fb','fb',('GeV','GeV')],
                    coordinates = [{x: 1, y:0, 'value': 2},{x: 1, y:0, 'value': 2},{x: 1, y:0, 'value': None}])
#Add mass plane with stable limit in order to allow for interpolation:
planeStable = RHadGM1.addMassPlane([[(x, 0.0)]]*2)
planeStable.setSources(dataLabels=['upperLimits','expectedUpperLimits','obsExclusion'],
                    dataFiles=['orig/Table10_ULobs.csv','orig/Table10_ULexp.csv','orig/Gluino_ExclusionObs.csv'],
                    dataFormats=['csv','csv','csv'],units=['fb','fb',None],
                    coordinates = [{x: 0, 'value': 1},{x: 0, 'value': 2},{x : 0, 'value' : None}])



#+++++++ next txName block ++++++++++++++
RHadQM1 = dataset.addTxName('TRHadDM1')
RHadQM1.checked =''
RHadQM1.constraint = "[[],[]]"
RHadQM1.condition =None
RHadQM1.finalState = ['RHadronD','RHadronD']
RHadQM1.massConstraints = None
RHadQM1.dataUrl = 'https://www.hepdata.net/record/86565?version=1&table=Table11'
RHadQM1.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
plane = RHadQM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits','expectedUpperLimits','obsExclusion'],
                    dataFiles=['orig/Table11_ULobs.csv','orig/Table11_ULexp.csv','orig/Sbottom_ExclusionObs.csv'],
                    dataFormats=['csv','csv','csv'],units=['fb','fb',None],
                    coordinates = [{x : 0, 'value' : 1},{x : 0, 'value' : 1},{x : 0, 'value' : None}])

#+++++++ next txName block ++++++++++++++
RHadQM1 = dataset.addTxName('TRHadUM1')
RHadQM1.checked =''
RHadQM1.constraint = "[[],[]]"
RHadQM1.condition =None
RHadQM1.finalState = ['RHadronU','RHadronU']
RHadQM1.massConstraints = None
RHadQM1.dataUrl = 'https://www.hepdata.net/record/86565?version=1&table=Table12'
RHadQM1.source = 'ATLAS'
#+++++++ next mass plane block ++++++++++++++
plane = RHadQM1.addMassPlane([[x],[x]])
plane.setSources(dataLabels=['upperLimits','expectedUpperLimits','obsExclusion'],
                    dataFiles=['orig/Table12_ULobs.csv','orig/Table12_ULexp.csv','orig/Stop_ExclusionObs.csv'],
                    dataFormats=['csv','csv','csv'],units=['fb','fb',None],
                    coordinates = [{x : 0, 'value' : 1},{x : 0, 'value' : 1},{x : 0, 'value' : None}])


databaseCreator.create()

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
info = MetaInfoInput('ATLAS-SUSY-2016-08')
info.url = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-08/"
info.sqrts = 13
info.lumi = 32.8
info.prettyName = "displaced vertices"
info.private = False
info.arxiv =  'https://arxiv.org/abs/1710.04901'
info.contact = 'ATLAS collaboration'
info.publication ='Phys. Rev. D 97 (2018) 052012'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++ next txName block ++++++++++++++
T5Disp = dataset.addTxName('T5Disp')
T5Disp.checked = ''
T5Disp.constraint ="[[[q,q]],[[q,q]]]"
T5Disp.conditionDescription = None
T5Disp.condition = None
T5Disp.source = "ATLAS"
#+++++++ next mass plane block ++++++++++++++
labels = [ 'expExclusion','obsExclusion','upperLimits', 'expectedUpperLimits' ]
units = [ ("GeV","ns"), ("GeV","ns"), 'pb', 'pb' ]
formats = [ 'csv', 'csv', 'csv', 'csv' ]
T5Disp_1 = T5Disp.addMassPlane(2*[[(x,y), 100.]])
T5Disp_1.figure = 'Figaux. 9a'
T5Disp_1.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-08/figaux_09a.png'

T5Disp_1.setSources(dataLabels= labels,
                 dataFiles= ['orig/exp9.csv','orig/obs9.csv',
                             'orig/mchi100.csv','orig/mchi100exp.csv'],
                 units = units, dataFormats= formats )

T5Disp_2 = T5Disp.addMassPlane(2*[[(x,y), x-100.]])
T5Disp_2.figure = 'Figaux. 9b'
T5Disp_2.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-08/figaux_09b.png'
T5Disp_2.setSources(dataLabels= labels,
                 dataFiles= ['orig/exp12.csv','orig/obs12.csv',
                             'orig/mDelta100.csv','orig/mDelta100exp.csv'],
                 units = units, dataFormats= formats )

ns=1.
units = [ ("GeV","GeV"), ("GeV","GeV"), 'pb', 'pb' ]
T5Disp_3 = T5Disp.addMassPlane(2*[[(x,hbar/(1.*ns)),y]])
T5Disp_3.figure = 'Figaux. 9c'
T5Disp_3.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-08/figaux_09c.png'
T5Disp_3.setSources(dataLabels= labels,
                 dataFiles= ['orig/exp15.csv','orig/obs15.csv',
                             'orig/mTau.csv','orig/mTauExp.csv' ],
                 units = units, dataFormats= formats )

databaseCreator.create()

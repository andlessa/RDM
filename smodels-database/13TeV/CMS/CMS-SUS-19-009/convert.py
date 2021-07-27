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
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z


#+++++++ global info block ++++++++++++++
info             = MetaInfoInput('CMS-SUS-19-009')
info.url         = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/index.html'
info.sqrts       = 13
info.lumi        = 137
info.prettyName  = '1L + jets, MHT'
info.private     = False
info.arxiv       = 'https://arxiv.org/abs/1912.08887'
info.contact     = 'cms-phys-conveners-sus@cern.ch'
info.publication = 'JHEP 05 (2020) 032'
info.comment     = 'First attempt at PDF-based extraction'

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#====================   T2tt   ==============================

#+++++txName block +++++++++++++++++
T2tt=dataset.addTxName('T2tt')
T2tt.checked=''
T2tt.constraint="[[['t']],[['t']]]"
T2tt.condition=None
T2tt.conditionDescription = None
T2tt.massConstraint=[['dm>169'],['dm>169']]
T2tt.source="CMS"
#++++++next mass plane block+++++++++
T2tt_1 = T2tt.addMassPlane(2*[[x,y]])
T2tt_1.figure='Fig. 6'
T2tt_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.png'
T2tt_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.pdf'
T2tt_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.pdf'

T2tt_1.setSources( dataLabels=['upperLimits','obsExclusion','expExclusion'],
                   dataFiles=['orig/CMS-SUS-19-009_Figure_006.txt',
                              'orig/CMS-SUS-19-009_Figure_006_obsExclusion.txt',
                              'orig/CMS-SUS-19-009_Figure_006_expExclusion.txt'],
                   units = ['pb',None,None],
                   dataFormats=['txt','txt','txt']
)

#+++++txName block +++++++++++++++++
T2ttoff=dataset.addTxName('T2ttoff')
T2ttoff.checked=''
T2ttoff.constraint="[[['b','W']],[['b','W']]]"
T2ttoff.condition=None
T2ttoff.conditionDescription=None
T2ttoff.massConstraint=[['80<dm<169'],['80<dm<169']]
T2ttoff.source="CMS"
#++++++next mass plane block+++++++++
T2ttoff_1 = T2ttoff.addMassPlane(2*[[x,y]])
T2ttoff_1.figure='Fig. 6'
T2ttoff_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.png'
T2ttoff_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.pdf'
T2ttoff_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_006.pdf'
T2ttoff_1.setSources(dataLabels=['upperLimits','obsExclusion','expExclusion'],
                   dataFiles=['orig/CMS-SUS-19-009_Figure_006.txt',
                              'orig/CMS-SUS-19-009_Figure_006_obsExclusion.txt',
                              'orig/CMS-SUS-19-009_Figure_006_expExclusion.txt'],
                   units = ['pb',None,None],
                   dataFormats=['txt','txt','txt'])


#====================   T6bbWW   ==============================
#+++++txName block +++++++++++++++++
T6bbWW=dataset.addTxName('T6bbWW')
T6bbWW.checked=''
T6bbWW.constraint="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.condition=None
T6bbWW.conditionDescription = None
T6bbWW.source="CMS"
#++++++next mass plane block+++++++++
T6bbWW_1 = T6bbWW.addMassPlane(2*[[x,0.5*x+0.5*y,y]])
T6bbWW_1.figure='Fig. 7'
T6bbWW_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_007.png'
T6bbWW_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_007.pdf'
T6bbWW_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-009/CMS-SUS-19-009_Figure_007.pdf'
T6bbWW_1.setSources(dataLabels=['upperLimits','obsExclusion','expExclusion'],
                   dataFiles=['orig/CMS-SUS-19-009_Figure_007.txt',
                              'orig/CMS-SUS-19-009_Figure_007_obsExclusion.txt',
                              'orig/CMS-SUS-19-009_Figure_007_expExclusion.txt'],
                   units = ['pb',None,None],
                   dataFormats=['txt','txt','txt'])


databaseCreator.create()

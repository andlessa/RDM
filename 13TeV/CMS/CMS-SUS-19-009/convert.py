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
argparser.add_argument ('-no', '--noUpdate',
help = 'do not update the lastUpdate field.',\
action= "store_true" )
argparser.add_argument ('-r', '--resetValidation',
help = 'reset the validation flag',\
action= "store_true" )
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

T2tt_1.setSources( dataLabels=['upperLimits'],
                   dataFiles=['orig/CMS-SUS-19-009_Figure_006.pdf'], 
                   indices=['x[150,1400];y[0,1200];z[1e-4,10,log]'],
                   dataFormats=['pdf']
)

"""
T2ttoff=dataset.addTxName('T2ttoff')
T2ttoff.checked=''
T2ttoff.constraint="[[['b','W']],[['b','W']]]"
T2ttoff.condition=None
T2ttoff.conditionDescription=None
T2ttoff.massConstraint=[['80<dm<169'],['80<dm<169']]
T2ttoff.source="CMS"

T2tt_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits','expectedUpperLimits'],
                    dataFiles=['orig/T2ttexpectedmasslimitcurve.csv','orig/T2ttexpected-1s.d.masslimitcurve.csv','orig/T2ttexpected+1s.d.masslimitcurve.csv','orig/T2ttobservedmasslimitcurve.csv','orig/T2ttobserved-1s.d.(theory)masslimitcurve.csv','orig/T2ttobserved+1s.d.(theory)masslimitcurve.csv','orig/T2tt_obs_upperlimits.csv','orig/T2tt_exp_upperlimits.csv'],
                    dataFormats=['csv','csv','csv','csv','csv','csv','csv','csv'],units=[None,None,None,None,None,None,'pb','pb'])
"""
# T2ttoff.addMassPlane(T2tt_1)

databaseCreator.create()

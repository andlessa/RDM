#!/usr/bin/env python

import sys,os
sys.path.insert(0,"/home/walten/git/smodels-utils/validation/")
sys.path.insert(0,"/home/walten/git/smodels-utils/")


from validation.plotProducer import validateTxName,validatePlot,validateExpRes
from smodels.experiment.databaseBrowser import Browser
from smodels.experiment.databaseObjects import DataBase
import logging
from smodels.theory.crossSection import logger as cl
from smodels.theory.slhaDecomposer import logger as dl
from smodels.experiment.txnameObject import logger as tl
cl.setLevel(level=logging.DEBUG) 
dl.setLevel(level=logging.DEBUG)
tl.setLevel(level=logging.DEBUG)

database = DataBase("/home/walten/git/smodels-database/")

#How to validate all plots for all Txnames in one ExpRes:
expRes = database.getExpResults(analysisIDs=['ATLAS-CONF-2013-024'],datasetIDs=[None])

def validate (exp ):
    print exp
    slhamain = '/home/walten/git/smodels-utils/slha/'
    slhaDict = { # 'T1bbbb': os.path.join(slhamain,'T1bbbb'),
          #        'T6bbWW': os.path.join(slhamain,'T6bbWW'),
#                  'T6bbWWoff': os.path.join(slhamain,'T6bbWWoff'),
                 'T2tt': os.path.join(slhamain,'T2tt.tar'),
    }  
    print validateExpRes(exp,slhaDict)

if type(expRes)==list:
    for exp in expRes:
        validate (exp)
else:
    validate (expRes)

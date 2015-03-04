#!/usr/bin/env python

import sys,os
sys.path.insert(0,"/home/walten/git/smodels-utils/andre_validation/")
sys.path.insert(0,"/home/walten/git/smodels-utils/")


from plotProducer import validateTxName,validatePlot,validateExpRes
from smodels.experiment.databaseBrowser import Browser
from smodels.experiment.databaseObjects import DataBase
import logging
from smodels.theory.crossSection import logger as cl
from smodels.theory.slhaDecomposer import logger as dl
from smodels.experiment.txnameObject import logger as tl
from plotProducer import logger as pl
from validationObjs import logger as vl
cl.setLevel(level=logging.DEBUG) 
dl.setLevel(level=logging.DEBUG)
tl.setLevel(level=logging.DEBUG)
pl.setLevel(level=logging.DEBUG)
vl.setLevel(level=logging.DEBUG)

database = DataBase("/home/walten/git/smodels-database/")

#How to validate all plots for all Txnames in one ExpRes:
expRes = database.getExpResults(analysisIDs=['ATLAS-CONF-2013-061'],datasetIDs=[None])

for exp in expRes:
    print exp
#sys.exit(0)
    slhamain = '/home/walten/git/smodels-utils/myslha/'
    slhaDict = { 'T1bbbb': os.path.join(slhamain,'T1bbbb'),
                # 'T1tttt': os.path.join(slhamain,'T1tttt'),
                # 'T1tbtb': os.path.join(slhamain,'T1tbtb'),
    }  
    print validateExpRes(exp,slhaDict)

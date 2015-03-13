#!/usr/bin/env python

import sys
sys.path.insert(0,"../../../../../smodels-utils/")
sys.path.insert(0,"../../../../../smodels/")


from validation.plotProducer import validateExpRes, getExpIdFromPath, validatePlot, getDatasetIdsFromPath
from smodels.experiment.databaseObjects import DataBase
import logging
from smodels.theory.crossSection import logger as cl
from smodels.theory.slhaDecomposer import logger as dl
from smodels.experiment.txnameObject import logger as tl
cl.setLevel(level=logging.DEBUG) 
dl.setLevel(level=logging.DEBUG)
tl.setLevel(level=logging.DEBUG)


print "exp id=",getExpIdFromPath()
print "dataset ids=",getDatasetIdsFromPath()

database = DataBase("../../../../")
#How to validate all plots for all Txnames in one ExpRes:
expRes = database.getExpResults(analysisIDs=[getExpIdFromPath()],datasetIDs=getDatasetIdsFromPath() )

print "expRes=",expRes

slhamain = '../../../../../smodels-utils/slha/T2tt.tar'
txnameStr = 'T2tt'
axes = '2*Eq(mother,x)_Eq(lsp,y)'
validatePlot(expRes,txnameStr,axes,slhamain)


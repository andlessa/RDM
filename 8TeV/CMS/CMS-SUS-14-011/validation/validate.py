#!/usr/bin/env python

import sys,os
home = '/home/walten/'
sys.path.insert(0,os.path.join(home,"smodels-utils/"))
sys.path.insert(0,os.path.join(home,"smodels/"))


from validation.plotProducer import validateExpRes, getExpIdFromPath, getDatasetIdsFromPath
from smodels.experiment.databaseObj import Database
import logging
from smodels.theory.crossSection import logger as cl
from smodels.theory.slhaDecomposer import logger as dl
from smodels.experiment.txnameObj import logger as tl
from validation.gridSModelS import logger as gl
cl.setLevel(level=logging.INFO) 
dl.setLevel(level=logging.WARNING)
tl.setLevel(level=logging.INFO)
gl.setLevel(level=logging.INFO)


print "exp id=",getExpIdFromPath(),"datasetid=",getDatasetIdsFromPath()

database = Database(os.path.join(home,"smodels-database"))
#How to validate all plots for all Txnames in one ExpRes:
expRes = database.getExpResults(analysisIDs=[getExpIdFromPath()],datasetIDs=getDatasetIdsFromPath() )
if expRes == []:
    print "[validate.py] Error: could not find any experimental results."
    f=open("../globalInfo.txt")
    lines=f.readlines()
    f.close()
    for line in lines:
        if line[:3]=="id:":
            Id=line[4:]
            Id=Id.replace("\n","")
            if Id != getExpIdFromPath():
                print "[validate.py] Error: path directory ``%s'' does not match exp id ``%s'' in ../globalInfo.txt" % ( getExpIdFromPath(), Id  )
                sys.exit()

slhamain = os.path.join(home,"smodels-utils/slha")
kfactorDict = { "TChiWZ": 1.2, "TChiWW": 1.2, "TChiChipmSlepL": 1.2, 
                "TChiChipmSlepStau": 1.2, "TChiChipmStauStau": 1.2, 
                "TChiSlepSnu": 1.2, "TChiStauSnu": 1.2, "TChiWH": 1.2, 
                "TChiWZoff": 1.2 }
#kfactorDict= {} 
for i in expRes:
    validateExpRes(i,slhamain, kfactorDict = kfactorDict )


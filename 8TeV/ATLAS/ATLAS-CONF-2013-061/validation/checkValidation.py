#!/usr/bin/python

import sys,os
sys.path.insert(0,"/home/walten/git/smodels-utils/andre_validation/")
sys.path.insert(0,"/home/walten/git/smodels-utils/")

from smodels_utils import SModelSUtils

from smodels.tools.physicsUnits import pb,GeV
from smodels.experiment.databaseObjects import DataBase

from plotProducer import ValidationPlot

## ValidationPlot.computeWrongnessFactor = computeWrongnessFactor

filename="T1bbbb_2Eqmotherx_Eqlspy.py"
execfile(filename)

database = DataBase("/home/walten/git/smodels-database/")
expRes = database.getExpResults(analysisIDs=['ATLAS-CONF-2013-061'],datasetIDs=[None])


plot=ValidationPlot( expRes[0], "T1bbbb", "2*Eq(mother,x)_Eq(lsp,y)" )
plot.data=validationData
# wrongness = computeWrongnessFactor ( plot )
wrongness = plot.computeWrongnessFactor(1.0)
print "wrongness=",wrongness

# import IPython
# IPython.embed()

#!/usr/bin/python

import sys,os
sys.path.insert(0,"../../../../../smodels-utils/")
sys.path.insert(0,"../../../../../smodels/")

from smodels_utils import SModelSUtils
from smodels.tools.physicsUnits import pb,GeV
from smodels.experiment.databaseObjects import DataBase

from validation.plotProducer import ValidationPlot,getExpIdFromPath

## ValidationPlot.computeWrongnessFactor = computeWrongnessFactor

txname="TChipChimStauSnu"
## axes="2*Eq(mother,x)_Eq(inter0,2.0*y)_Eq(lsp,y)"
axes="2*Eq(mother,x)_Eq(inter0,0.5*x+0.5*y)_Eq(lsp,y)"
# T6bbWWoff_2Eqmotherx_Eqinter02.0y_Eqlspy
axesstraight=axes.replace("*","").replace("(","").replace(")","").replace(",","")

filename="%s_%s.py" % ( txname, axesstraight )
execfile(filename)

database = DataBase("../../../../")
expRes = database.getExpResults(analysisIDs=[getExpIdFromPath()],datasetIDs=[None])


plot=ValidationPlot( expRes, txname, axes )
plot.data=validationData
#wrongness = plot.computeWrongnessFactor()
#print "wrongness=",wrongness

plot.getPlot()
plot.savePlot()

# import IPython
# IPython.embed()

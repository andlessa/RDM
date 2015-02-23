#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt, txname.txt, twiki.txt and sms.py.

.. moduleauthor: Wolfgang Waltenberger

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', \
help = 'path to the package smodels_utils',\
type = types.StringType)
args = argparser.parse_args()

if args.utilsPath:
    utilsPath = args.utilsPath
else:
    databaseRoot = '../../../'
    sys.path.append(os.path.abspath(databaseRoot))
    from utilsPath import utilsPath
    utilsPath = databaseRoot + utilsPath

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y


#+++++++ global info block ++++++++++++++

import os, glob
dir=os.getcwd()
print dir
pos=dir.find("-ANA")
expid = dir[:pos]
print "expid=",expid
signalregion=dir[pos+1:]
print "signalregion=",signalregion

info = MetaInfoInput(expid)
info.signalRegion = signalregion
info.url ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/%s/' % expid 
info.sqrts = 8
info.lumi = 20.3
info.prettyname = '0 leptons + jets + met'
info.private = True
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='fastlim'
info.publication = 'http://cds.cern.ch/record/1547563'
info.comment = 'created from fastlim-1.0'
info.superseded_by ='SUSY-2013-02'
info.implemented_by = 'Wolfgang Waltenberger'
info.observedN = 5333
info.expectedBG = 4700
info.bgError = 500


constraints =  { "T2tt": "[[['t+']],[['t-']]]", "T2bb": "[[['b']],[['b']]]", 
                 "T2bt": "[[['b']],[['t']]]", "T1tttt": "[[['t+','t-']],[['t+','t-']]]",
                 "T1bbtt": "[[['b','b']],[['t','t']]]", "T1btbt": "[[['b','t']],[['b','t']]]",
                 "T1btqq": "[[['b','t']],[['jet','jet']]]", "T1qqtt": "[[['jet','jet']],[['t','t']]]",
                 "T1bttt": "[[['b','t']],[['t','t']]]", "T1": "[[['jet','jet']],[['jet','jet']]]" }

#+++++++ next txName block ++++++++++++++
#T1 = TxNameInput('T1')
#T1.on.constraint = constraints["T1"]
#T1.on.condition = None
#T1.on.fuzzycondition = None
#
##+++++++ next mass plane block ++++++++++++++
#T1_1 = T1.addMassPlane(motherMass = x , lspMass = y )
##----figure----
#T1_1.figure = 'fig_07a.pdf'
#T1_1.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'
## ----limit source----
### T1_1.obsUpperLimit.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
#T1_1.efficiencyMap.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
## T1_1.obsUpperLimit.unit = 'fb'
## T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
## ----exclusion source----
#T1_1.obsExclusion.setSource( './orig/T1_exc.dat', 'txt', objectName = None, index = None )
##T1_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusion.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T1_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
#T1_1.dataUrl = 
#T1_1.histoDataUrl = 
#----limit url settings ----
# T1_1.obsUpperLimit.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13007/limits_model_A.txt'
#T1_1.expectedlimit.dataUrl =
#----exclusion url settings ----
#T1_1.exclusionDataUrl =
#T1_1.exclusion.dataUrl =
#T1_1.exclusionM1.dataUrl =
#T1_1.exclusionP1.dataUrl =
#T1_1.expectedExclusion.dataUrl =
#T1_1.expectedExclusionM1.dataUrl =
#T1_1.expectedExclusionP1.dataUrl =

figure={}
figure["T1"]='fig_07a.pdf'

figureUrl={}
figureUrl["T1"]='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'

for i in os.listdir("orig/"):
    if i[-5:]!=".effi": continue
    txname=i[:-5]
    print txname 
    tmp= TxNameInput ( txname )
    tmp.on.constraint = constraints[txname]
    tmp.on.condition=None
    tmp.on.fuzzycondition = None
    tmp_1 = tmp.addMassPlane (motherMass = x , lspMass = y )
    tmp_1.efficiencyMap.setSource( './orig/%s.effi' % txname, 'effi', objectName = None, index = None ) 
    if os.path.exists ( './orig/%s_exc.dat' % txname ):
        tmp_1.obsExclusion.setSource( './orig/%s_exc.dat' % txname, 'txt', objectName = None, index = None )
    if txname in figure:
        tmp_1.figure = figure[txname]
    if txname in figureUrl:
        tmp_1.figureUrl = figureUrl[txname]
# ----limit source----
## T1_1.obsUpperLimit.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
#        tmp_1.efficiencyMap.setSource( './orig/T1.effi', 'txt', objectName = None, index = None )
# T1_1.obsUpperLimit.unit = 'fb'
# T1_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
# ----exclusion source----
        

#T2tt = TxNameInput('T2tt')
#T2tt.on.constraint = "[[['t']],[['t']]]"
#T2tt.on.condition = None
#T2tt.on.fuzzycondition = None
#T2tt_1 = T2tt.addMassPlane(motherMass = x , lspMass = y )
#T2tt_1.efficiencyMap.setSource( './orig/T2tt.effi', 'effi', objectName = None, index = None )


databaseCreator.create()

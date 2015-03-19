#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description =  
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', 
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
info = MetaInfoInput('ATLAS-SUSY-2013-04')
info.comment = 'there are exclusion lines for T5WWLSP060 and TWZWZ050050 also. Erratum:JHEP01(2014)109'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP10%282013%29130'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/'
# info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1308.1841'
info.contact = "ATLAS collaboration"
info.prettyname = 'ATLAS \ge 7 jets'
info.supersedes = 'ATLAS-CONF-2012-103'

"""
#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked =
T5WW.off.checked =
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint =
T5WW.on.condition ="None"
T5WW.off.condition =
T5WW.on.fuzzycondition ="None"
T5WW.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5WW050 = T5WW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
T5WW050.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5WW050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WW050.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5WW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5WW050.dataUrl =
T5WW050.histoDataUrl =
T5WW050.exclusionDataUrl =
#----figure----
T5WW050.figure = 'Fig. 11a'
T5WW050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/fig_11a.png'
#----limit url settings ----
T5WW050.obsUpperLimit.dataUrl =
T5WW050.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WW050.obsExclusion.dataUrl =
T5WW050.obsExclusionM1.dataUrl =
T5WW050.obsExclusionP1.dataUrl =
T5WW050.expExclusion.dataUrl =
T5WW050.expExclusionM1.dataUrl =
T5WW050.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked ="VM"
#T1tttt.off.checked =
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.condition ="None"
#T1tttt.off.condition =
T1tttt.on.fuzzycondition ="None"
#T1tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tttt.obsUpperLimit.setSource( "orig/T1tttt.txt", "txt", objectName = None, index = None )
T1tttt.obsUpperLimit.unit = 'fb'
# T1tttt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/exclusion_T1tttt.txt", "txt", objectName = None, index = None )
#T1tttt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
"""
T1tttt.dataUrl =
T1tttt.histoDataUrl =
T1tttt.exclusionDataUrl =
"""
#----figure----
T1tttt.figure = 'Fig (aux). 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-04/figaux_11a.png'
#----limit url settings ----
"""
T1tttt.obsUpperLimit.dataUrl =
T1tttt.expUpperLimit.dataUrl =
#----exclusion url settings ----
T1tttt.obsExclusion.dataUrl =
T1tttt.obsExclusionM1.dataUrl =
T1tttt.obsExclusionP1.dataUrl =
T1tttt.expExclusion.dataUrl =
T1tttt.expExclusionM1.dataUrl =
T1tttt.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5tttt = TxNameInput('T5tttt')
T5tttt.on.checked =
T5tttt.off.checked =
T5tttt.on.constraint ="[[['t'],['t']],[['t'],['t']]]"
T5tttt.off.constraint =
T5tttt.on.condition ="None"
T5tttt.off.condition =
T5tttt.on.fuzzycondition ="None"
T5tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5ttttLSP060 = T5tttt.addMassPlane(motherMass = x, interMass0 = y, lspMass = 60.0)
#----limit source----
T5ttttLSP060.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5ttttLSP060.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttttLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5ttttLSP060.dataUrl =
T5ttttLSP060.histoDataUrl =
T5ttttLSP060.exclusionDataUrl =
#----figure----
T5ttttLSP060.figure =
T5ttttLSP060.figureUrl =
#----limit url settings ----
T5ttttLSP060.obsUpperLimit.dataUrl =
T5ttttLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5ttttLSP060.obsExclusion.dataUrl =
T5ttttLSP060.obsExclusionM1.dataUrl =
T5ttttLSP060.obsExclusionP1.dataUrl =
T5ttttLSP060.expExclusion.dataUrl =
T5ttttLSP060.expExclusionM1.dataUrl =
T5ttttLSP060.expExclusionP1.dataUrl =
"""

databaseCreator.create()

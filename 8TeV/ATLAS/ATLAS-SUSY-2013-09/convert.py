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
info = MetaInfoInput('ATLAS-SUSY-2013-09')
info.comment = 'exclusionLines digitized by hand (MT)'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP06(2014)035'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/'
#info.supersededBy = 
info.arxiv = 'http://arxiv.org/abs/1404.2500'
info.contact = "ATLAS collaboration"
info.prettyName = 'ATLAS SS+b'
info.supersedes = 'ATLAS-CONF-2013-007; ATLAS-CONF-2012-151'

"""
#+++++++ next txName block ++++++++++++++
T6ttWW = TxNameInput('T6ttWW')
T6ttWW.on.checked =
T6ttWW.off.checked =
T6ttWW.on.constraint ="[[[t+],[W-]],[[t+],[W-]]]+[[[t-],[W+]],[[t-],[W+]]]+[[[t+],[W-]],[[t-],[W+]]]"
T6ttWW.off.constraint =
T6ttWW.on.conditionDescription ="None"
T6ttWW.off.conditionDescription =
T6ttWW.on.condition ="None"
T6ttWW.off.condition =

#+++++++ next mass plane block ++++++++++++++
T6ttWWx200 = T6ttWW.addMassPlane(motherMass = x, interMass0 = y * 2.0, lspMass = y)
#----limit source----
T6ttWWx200.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6ttWWx200.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6ttWWx200.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6ttWWx200.dataUrl =
T6ttWWx200.histoDataUrl =
T6ttWWx200.exclusionDataUrl =
#----figure----
T6ttWWx200.figure = 'Fig.(aux) 13b'
T6ttWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/fig_07b.png'
#----limit url settings ----
T6ttWWx200.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225/d43'
T6ttWWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6ttWWx200.obsExclusion.dataUrl =
T6ttWWx200.obsExclusionM1.dataUrl =
T6ttWWx200.obsExclusionP1.dataUrl =
T6ttWWx200.expExclusion.dataUrl =
T6ttWWx200.expExclusionM1.dataUrl =
T6ttWWx200.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6ttWWLSP060 = T6ttWW.addMassPlane(motherMass = ERROR, interMass0 = x, lspMass = y)
#----limit source----
T6ttWWLSP060.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T6ttWWLSP060.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.expExclusion.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T6ttWWLSP060.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6ttWWLSP060.dataUrl =
T6ttWWLSP060.histoDataUrl =
T6ttWWLSP060.exclusionDataUrl =
#----figure----
T6ttWWLSP060.figure = 'Fig.(aux) 13a'
T6ttWWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/fig_07a.png'
#----limit url settings ----
T6ttWWLSP060.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225/d41'
T6ttWWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
T6ttWWLSP060.obsExclusion.dataUrl =
T6ttWWLSP060.obsExclusionM1.dataUrl =
T6ttWWLSP060.obsExclusionP1.dataUrl =
T6ttWWLSP060.expExclusion.dataUrl =
T6ttWWLSP060.expExclusionM1.dataUrl =
T6ttWWLSP060.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
#T1tttt.on.checked =
#T1tttt.off.checked =
T1tttt.on.constraint ="[[['t','t']],[['t','t']]]"
#T1tttt.off.constraint =
T1tttt.on.conditionDescription ="None"
#T1tttt.off.conditionDescription =
T1tttt.on.condition ="None"
#T1tttt.off.condition =

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tttt.obsUpperLimit.setSource( "orig/limit_T1tttt.txt", "txt", objectName = None, index = None )
T1tttt.obsUpperLimit.unit="fb"
# T1tttt.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( "orig/exclusion_T1tttt.txt", "txt", objectName = None, index = None )
#T1tttt.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T1tttt.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#T1tttt.dataUrl =
#T1tttt.histoDataUrl =
#T1tttt.exclusionDataUrl =
#----figure----
T1tttt.figure = 'Fig.(aux) 11a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/figaux_11a.png'
#----limit url settings ----
T1tttt.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225/d39'
"""
T1tttt.expUpperLimit.dataUrl =
#----exclusion url settings ----
T1tttt.obsExclusion.dataUrl =
T1tttt.obsExclusionM1.dataUrl =
T1tttt.obsExclusionP1.dataUrl =
T1tttt.expExclusion.dataUrl =
T1tttt.expExclusionM1.dataUrl =
T1tttt.expExclusionP1.dataUrl =
"""

"""
#+++++++ next txName block ++++++++++++++
T5ttcc = TxNameInput('T5ttcc')
T5ttcc.on.checked =
T5ttcc.off.checked =
T5ttcc.on.constraint ="[[[t],[jet]],[[t],[jet]]]"
T5ttcc.off.constraint =
T5ttcc.on.conditionDescription ="None"
T5ttcc.off.conditionDescription =
T5ttcc.on.condition ="None"
T5ttcc.off.condition =

#+++++++ next mass plane block ++++++++++++++
T5ttccD20 = T5ttcc.addMassPlane(motherMass = y + 20.0, interMass0 = x, lspMass = y)
#----limit source----
T5ttccD20.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5ttccD20.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5ttccD20.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5ttccD20.dataUrl =
T5ttccD20.histoDataUrl =
T5ttccD20.exclusionDataUrl =
#----figure----
T5ttccD20.figure =
T5ttccD20.figureUrl =
#----limit url settings ----
T5ttccD20.obsUpperLimit.dataUrl =
T5ttccD20.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5ttccD20.obsExclusion.dataUrl =
T5ttccD20.obsExclusionM1.dataUrl =
T5ttccD20.obsExclusionP1.dataUrl =
T5ttccD20.expExclusion.dataUrl =
T5ttccD20.expExclusionM1.dataUrl =
T5ttccD20.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5WW = TxNameInput('T5WW')
T5WW.on.checked =
T5WW.off.checked =
T5WW.on.constraint ="[[[jet,jet],[W]],[[jet,jet],[W]]]"
T5WW.off.constraint =
T5WW.on.conditionDescription ="None"
T5WW.off.conditionDescription =
T5WW.on.condition ="None"
T5WW.off.condition =

#+++++++ next mass plane block ++++++++++++++
T5WWx200 = T5WW.addMassPlane(motherMass = x, interMass0 = y * 2.0, lspMass = y)
#----limit source----
T5WWx200.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
T5WWx200.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
T5WWx200.obsExclusion.setSource( path, filetype, objectName = None, index = None )
T5WWx200.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWx200.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
T5WWx200.expExclusion.setSource( path, filetype, objectName = None, index = None )
T5WWx200.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
T5WWx200.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T5WWx200.dataUrl =
T5WWx200.histoDataUrl =
T5WWx200.exclusionDataUrl =
#----figure----
T5WWx200.figure = 'Fig.(aux) 12a'
T5WWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-09/fig_06a.png'
#----limit url settings ----
T5WWx200.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1289225/d38'
T5WWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
T5WWx200.obsExclusion.dataUrl =
T5WWx200.obsExclusionM1.dataUrl =
T5WWx200.obsExclusionP1.dataUrl =
T5WWx200.expExclusion.dataUrl =
T5WWx200.expExclusionM1.dataUrl =
T5WWx200.expExclusionP1.dataUrl =
"""

databaseCreator.create()

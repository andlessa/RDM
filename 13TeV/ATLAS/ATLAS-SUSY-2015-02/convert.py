#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse
import types

argparser = argparse.ArgumentParser(description = \
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
info = MetaInfoInput('ATLAS-SUSY-2015-02')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2015-02/'
info.sqrts = 13
info.lumi = 3.2
info.prettyName = 'Top 1l'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1606.03903'
#info.contact =
info.publication ='http://journals.aps.org/prd/abstract/10.1103/PhysRevD.94.052009'
info.comment = 'Very weird exclusion due to best CLs selection, and fluctuation in the Obs data. Digitised by FA'
#info.supersedes =
#info.supersededBy =

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
#T2tt.on.checked =
#T2tt.off.checked =
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint =  "[[['b','W']],[['b','W']]]"
T2tt.on.conditionDescription = None
T2tt.off.conditionDescription = None
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----figure----
T2tt_1.figure = 'Aux.Fig.5b'
T2tt_1.figureUrl ='http://hepdata.cedar.ac.uk/resource/1469069/thumb_figAuxiliaryFigure5b.png'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/T2tt_ATLAS_SUSY_2015_02_Obs_UL.dat', 'txt', objectName = None, index = None )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/T2tt_ATLAS_SUSY_2015_02_Obs.txt','txt', objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
T2tt_1.expExclusion.setSource( 'orig/T2tt_ATLAS_SUSY_2015_02_Exp.txt','txt', objectName = None, index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2tt_1.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1469069/all'
#----limit url settings ----
T2tt_1.histoDataUrl = 'http://hepdata.cedar.ac.uk/view/ins1469069/d24/input'
T2tt_1.obsUpperLimit.dataUrl ='http://hepdata.cedar.ac.uk/view/ins1469069/d24/input'
#T2tt_1.expUpperlimit.dataUrl =
#----exclusion url settings ----
T2tt_1.exclusionDataUrl =  'http://hepdata.cedar.ac.uk/resource/1469069/figFigure8b.png'
#T2tt_1.obsExclusion.dataUrl = ''
#T2tt_1.obsExclusionM1.dataUrl =
#T2tt_1.obsExclusionP1.dataUrl =
#T2tt_1.expExclusion.dataUrl =
#T2tt_1.expExclusionM1.dataUrl =
#T2tt_1.expExclusionP1.dataUrl =

databaseCreator.create()

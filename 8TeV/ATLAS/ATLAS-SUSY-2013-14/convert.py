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
info = MetaInfoInput('ATLAS-SUSY-2013-14')
info.comment = 'added TStauStau result for left handed stau pairs'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'link.springer.com/article/10.1007/JHEP10(2014)096'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-14/'
# info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1407.0350'
info.contact = '?'
info.prettyname = 'ATLAS di-tau'
info.supersedes = 'ATLAS-CONF-2013-028'

##+++++++ next txName block ++++++++++++++
TChiChipmStauL = TxNameInput('TChiChipmStauL')
#TChiChipmStauL.on.checked =
#ChiChipmStauL.off.checked =
TChiChipmStauL.on.constraint ="2.*([[['ta'],['ta']],[['nu'],['ta']]]+[[['ta'],['ta']],[['ta'],['nu']]])"
#TChiChipmStauL.off.constraint =
TChiChipmStauL.on.condition ="[[['ta'],['ta']],[['nu'],['ta']]] ~ [[['ta'],['ta']],[['ta'],['nu']]]"
#TChiChipmStauL.off.condition =
TChiChipmStauL.on.fuzzycondition ="Csim([[['ta'],['ta']],[['nu'],['ta']]],[[['ta'],['ta']],[['ta'],['nu']]])"
#TChiChipmStauL.off.fuzzycondition =
#
##+++++++ next mass plane block ++++++++++++++
TChiChipmStauL050 = TChiChipmStauL.addMassPlane(motherMass = x,interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
##----limit source----
TChiChipmStauL050.obsUpperLimit.setSource( "orig/limit_TChiChipmStauL.txt", "txt", objectName = None, index = None )
##TChiChipmStauL050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
TChiChipmStauL050.obsExclusion.setSource( "orig/exclusion_TChiChipmStauL.txt", "txt", objectName = None, index = None )
##TChiChipmStauL050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
##TChiChipmStauL050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauL050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauL050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauL050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#TChiChipmStauL050.dataUrl =
#TChiChipmStauL050.histoDataUrl =
#TChiChipmStauL050.exclusionDataUrl =
##----figure----
TChiChipmStauL050.figure = 'Fig.(aux) 11b'
TChiChipmStauL050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-14/figaux_11b.png'
##----limit url settings ----
TChiChipmStauL050.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304288/d29'
#TChiChipmStauL050.expUpperLimit.dataUrl =
##----exclusion url settings ----
#TChiChipmStauL050.obsExclusion.dataUrl =
#TChiChipmStauL050.obsExclusionM1.dataUrl =
#TChiChipmStauL050.obsExclusionP1.dataUrl =
#TChiChipmStauL050.expExclusion.dataUrl =
#TChiChipmStauL050.expExclusionM1.dataUrl =
#TChiChipmStauStau050.expExclusionP1.dataUrl =
#
#+++++++ next txName block ++++++++++++++
#TStauStau = TxNameInput('TStauStau')
##TStauStau.on.checked =
##TStauStau.off.checked =
#TStauStau.on.constraint ="[[['ta+']],[['ta-']]]"
##TStauStau.off.constraint =
#TStauStau.on.condition ="None"
##TStauStau.off.condition =
#TStauStau.on.fuzzycondition ="None"
##TStauStau.off.fuzzycondition =
#
##+++++++ next mass plane block ++++++++++++++
#TStauStau = TStauStau.addMassPlane(motherMass = x, lspMass = y)
##----limit source----
#TStauStau.obsUpperLimit.setSource( "orig/TStauStau.txt", "txt", objectName = None, index = None )
##TStauStau.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
#TStauStau.obsExclusion.setSource( "orig/limit_TStauStau.txt", "txt", objectName = None, index = None )
#TStauStau.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TStauStau.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TStauStau.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TStauStau.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TStauStau.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#TStauStau.dataUrl =
#TStauStau.histoDataUrl =
#TStauStau.exclusionDataUrl =
##----figure----
#TStauStau.figure =
#TStauStau.figureUrl =
##----limit url settings ----
#TStauStau.obsUpperLimit.dataUrl =
#TStauStau.expUpperLimit.dataUrl =
##----exclusion url settings ----
#TStauStau.obsExclusion.dataUrl =
#TStauStau.obsExclusionM1.dataUrl =
#TStauStau.obsExclusionP1.dataUrl =
#TStauStau.expExclusion.dataUrl =
#TStauStau.expExclusionM1.dataUrl =
#TStauStau.expExclusionP1.dataUrl =
#
##+++++++ next txName block ++++++++++++++
#TChipChimStauSnu = TxNameInput('TChipChimStauSnu')
#TChipChimStauSnu.on.checked =
#TChipChimStauSnu.off.checked =
#TChipChimStauSnu.on.constraint ="[[['ta-'],['nu']],[['nu'],['ta+']]] + [[['ta+'],['nu']],[['nu'],['ta-']]] + [[['ta+'],['nu']],[['ta-'],['nu']]] + [[['nu'],['ta+']],[['nu'],['ta-']]]"
#TChipChimStauSnu.off.constraint =
#TChipChimStauSnu.on.condition ="[[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['ta+'],['nu']],[['nu'],['ta-']]], [[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['ta+'],['nu']],[['ta-'],['nu']]], [[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['nu'],['ta+']],[['nu'],['ta-']]]"
#TChipChimStauSnu.off.condition =
#TChipChimStauSnu.on.fuzzycondition ="Csim([[['ta-'],['nu']],[['nu'],['ta+']]],[[['ta+'],['nu']],[['nu'],['ta-']]],[[['ta+'],['nu']],[['ta-'],['nu']]],[[['nu'],['ta+']],[['nu'],['ta-']]])"
#TChipChimStauSnu.off.fuzzycondition =
#
##+++++++ next mass plane block ++++++++++++++
#TChipChimStauSnu050 = TChipChimStauSnu.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
##----limit source----
#TChipChimStauSnu050.obsUpperLimit.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
##----exclusion source----
#TChipChimStauSnu050.obsExclusion.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimStauSnu050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
##----global url settings ----
#TChipChimStauSnu050.dataUrl =
#TChipChimStauSnu050.histoDataUrl =
#TChipChimStauSnu050.exclusionDataUrl =
##----figure----
#TChipChimStauSnu050.figure = 'Fig.(aux) 11a'
#TChipChimStauSnu050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-14/fig_07b.png'
##----limit url settings ----
#TChipChimStauSnu050.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304288/d28'
#TChipChimStauSnu050.expUpperLimit.dataUrl =
##----exclusion url settings ----
#TChipChimStauSnu050.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304288/d20'
#TChipChimStauSnu050.obsExclusionM1.dataUrl =
#TChipChimStauSnu050.obsExclusionP1.dataUrl =
#TChipChimStauSnu050.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1304288/d19'
#TChipChimStauSnu050.expExclusionM1.dataUrl =
#TChipChimStauSnu050.expExclusionP1.dataUrl =

databaseCreator.create()

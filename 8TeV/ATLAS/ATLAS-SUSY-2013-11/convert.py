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
info = MetaInfoInput('ATLAS-SUSY-2013-11')
info.comment = 'TChiWW being investigated'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP05(2014)071'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/'
#info.superseded_by = 
info.arxiv = 'http://arxiv.org/abs/1403.5294'
info.contact = '?'
info.prettyname = 'ATLAS dilepton'
info.supersedes = 'ATLAS-CONF-2013-049'

#+++++++ next txName block ++++++++++++++
TChiWZ = TxNameInput('TChiWZ')
#TChiWZ.on.checked =
#TChiWZ.off.checked =
TChiWZ.on.constraint ="[[['W']],[['Z']]]"
#TChiWZ.off.constraint =
TChiWZ.on.condition ="None"
#TChiWZ.off.condition =
TChiWZ.on.fuzzycondition ="None"
#TChiWZ.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiWZ = TChiWZ.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWZ.obsUpperLimit.setSource( "orig/limit_TChiWZ.txt", "txt", objectName = None, index = None )
#TChiWZ.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiWZ.obsExclusion.setSource( "orig/exclusion_TChiWZ.txt", "txt", objectName = None, index = None )
#TChiWZ.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWZ.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiWZ.expExclusion.setSource( "orig/expectedexclusion_TChiWZ.txt", "txt", objectName = None, index = None )
#TChiWZ.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWZ.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiWZ.dataUrl =
#TChiWZ.histoDataUrl =
#TChiWZ.exclusionDataUrl =
#----figure----
TChiWZ.figure = 'Fig.(aux) 19b'
TChiWZ.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/fig_07a.png'
#----limit url settings ----
TChiWZ.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d64'
#TChiWZ.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiWZ.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d17'
#TChiWZ.obsExclusionM1.dataUrl =
#TChiWZ.obsExclusionP1.dataUrl =
TChiWZ.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d18'
#TChiWZ.expExclusionM1.dataUrl =
#TChiWZ.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TChipChimSlepSnu = TxNameInput('TChipChimSlepSnu')
#TChipChimSlepSnu.on.checked =
#TChipChimSlepSnu.off.checked =
TChipChimSlepSnu.on.constraint ="[[['L-'],['nu']],[['nu'],['L+']]] + [[['L+'],['nu']],[['nu'],['L-']]] + [[['L+'],['nu']],[['L-'],['nu']]] + [[['nu'],['L+']],[['nu'],['L-']]]"
#TChipChimSlepSnu.off.constraint =
TChipChimSlepSnu.on.condition ="[[['L-'],['nu']],[['nu'],['L+']]] ~ [[['L+'],['nu']],[['nu'],['L-']]], [[['L-'],['nu']],[['nu'],['L+']]] ~ [[['L+'],['nu']],[['L-'],['nu']]], [[['L-'],['nu']],[['nu'],['L+']]] ~ [[['nu'],['L+']],[['nu'],['L-']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['ta-'],['nu']],['nu'],['L+']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['L-'],['nu']],[['nu'],['ta+']]], [[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['ta+'],['nu']],[['nu'],['L-']]], [[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['L+'],['nu']],[['nu'],['ta-']]], [[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['ta+'],['nu']],[['L-'],['nu']]], [[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['L+'],['nu']],[['ta-'],['nu']]], [[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['ta+']],[['nu'],[L-']]], [[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['L+']],[['nu'],[ta-']]], [[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['e-'],['nu']],[['nu'],['L+']]], [[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['L-'],['nu']],[['nu'],['e+']]], [[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['e+'],['nu']],[['nu'],['L-']]],[[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['L+'],['nu']],[['nu'],['e-']]],[[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['e+'],['nu']],[['L-'],['nu']]],[[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['L+'],['nu']],[['e-'],['nu']]],[[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['e+']],[['nu'],['L-']]], [[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['L+']],[['nu'],['e-']]]"
#TChipChimSlepSnu.off.condition =
TChipChimSlepSnu.on.fuzzycondition ="Csim([[['L-'],['nu']],[['nu'],['L+']]],[[['L+'],['nu']],[['nu'],['L-']]],[[['L+'],['nu']],[['L-'],['nu']]],[[['nu'],['L+']],[['nu'],['L-']]]); Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['ta-'],['nu']],[['nu'],['L+']]]); Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['L-'],['nu']],[['nu'],['ta+']]]); Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.*[[['ta+'],['nu']],[['nu'],['L-']]]); Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.* [[['L+'],['nu']],[['nu'],['ta-']]]); Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['ta+'],['nu']],[['L-'],['nu']]]); Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['L+'],['nu']],[['ta-'],['nu']]]); Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['ta+']],[['nu'],[L-']]]); Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['L+']],[['nu'],[ta-']]]); Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['e-'],['nu']],[['nu'],['L+']]]); Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['L-'],['nu']],[['nu'],['e+']]]); Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.*[[['e+'],['nu']],[['nu'],['L-']]]); Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.* [[['L+'],['nu']],[['nu'],['e-']]]); Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['e+'],['nu']],[['L-'],['nu']]]); Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['L+'],['nu']],[['e-'],['nu']]]); Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['e+']],[['nu'],[L-']]]); Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['L+']],[['nu'],[e-']]])"
#TChipChimSlepSnu.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChipChimSlepSnu050 = TChipChimSlepSnu.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChipChimSlepSnu050.obsUpperLimit.setSource( "orig/limit_TChipChimSlepSnu050.txt", "txt", objectName = None, index = None )
#TChipChimSlepSnu050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChipChimSlepSnu050.obsExclusion.setSource( "orig/exclusion_TChipChimSlepSnu050.txt", "txt", objectName = None, index = None )
#TChipChimSlepSnu050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChipChimSlepSnu050.expExclusion.setSource( "orig/expectedexclusion_TChipChimSlepSnu050.txt", "txt", objectName = None, index = None )
#TChipChimSlepSnu050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChipChimSlepSnu050.dataUrl =
#TChipChimSlepSnu050.histoDataUrl =
#TChipChimSlepSnu050.exclusionDataUrl =
#----figure----
TChipChimSlepSnu050.figure = 'Fig.(aux) 19a'
TChipChimSlepSnu050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/fig_05.png'
#----limit url settings ----
TChipChimSlepSnu050.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d63'
#TChipChimSlepSnu050.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChipChimSlepSnu050.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d12'
#TChipChimSlepSnu050.obsExclusionM1.dataUrl =
#TChipChimSlepSnu050.obsExclusionP1.dataUrl =
TChipChimSlepSnu050.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d13'
#TChipChimSlepSnu050.expExclusionM1.dataUrl =
#TChipChimSlepSnu050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TChiWW = TxNameInput('TChiWW')
#TChiWW.on.checked =
#TChiWW.off.checked =
TChiWW.on.constraint ="[[['W+']],[['W-']]]"
#TChiWW.off.constraint =
TChiWW.on.condition ="None"
#TChiWW.off.condition =
TChiWW.on.fuzzycondition ="None"
#TChiWW.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiWW = TChiWW.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWW.obsUpperLimit.setSource( "orig/limit_TChiWW.txt", "txt", objectName = None, index = None )
#TChiWW.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiWW.obsExclusion.setSource( "orig/exclusion_TChiWW.txt", "txt", objectName = None, index = None )
#TChiWW.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWW.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiWW.expExclusion.setSource( "orig/expectedexclusion_TChiWW.txt", "txt", objectName = None, index = None )
#TChiWW.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWW.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiWW.dataUrl =
#TChiWW.histoDataUrl =
#TChiWW.exclusionDataUrl =
#----figure----
TChiWW.figure = 'Fig.(aux) 18'
TChiWW.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/figaux_18.png'
#----limit url settings ----
TChiWW.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d62'
#TChiWW.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiWW.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d14'
#TChiWW.obsExclusionM1.dataUrl =
#TChiWW.obsExclusionP1.dataUrl =
#TChiWW.expExclusion.dataUrl =
#TChiWW.expExclusionM1.dataUrl =
#TChiWW.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TSlepSlep = TxNameInput('TSlepSlep')
#TSlepSlep.on.checked =
#TSlepSlep.off.checked =
TSlepSlep.on.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
#TSlepSlep.off.constraint =
TSlepSlep.on.condition ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
#TSlepSlep.off.condition =
TSlepSlep.on.fuzzycondition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
#TSlepSlep.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TSlepSlep = TSlepSlep.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TSlepSlep.obsUpperLimit.unit = 'fb'
TSlepSlep.obsUpperLimit.setSource( "orig/limit_TSlepSlep.txt", "txt", objectName = None, index = None )
#TSlepSlep.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TSlepSlep.obsExclusion.setSource( "orig/exclusion_TSlepSlep.txt", "txt", objectName = None, index = None )
#TSlepSlep.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TSlepSlep.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TSlepSlep.expExclusion.setSource( "orig/expectedexclusion_TSlepSlep.txt", "txt", objectName = None, index = None )
#TSlepSlep.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TSlepSlep.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TSlepSlep.dataUrl =
#TSlepSlep.histoDataUrl =
#TSlepSlep.exclusionDataUrl =
#----figure----
TSlepSlep.figure = 'Fig.(aux) 20c'
TSlepSlep.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-11/figaux_20c.png'
#----limit url settings ----
TSlepSlep.obsUpperLimit.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d67'
#TSlepSlep.expUpperLimit.dataUrl =
#----exclusion url settings ----
TSlepSlep.obsExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d25'
#TSlepSlep.obsExclusionM1.dataUrl =
#TSlepSlep.obsExclusionP1.dataUrl =
TSlepSlep.expExclusion.dataUrl = 'http://hepdata.cedar.ac.uk/view/ins1286761/d26'
#TSlepSlep.expExclusionM1.dataUrl =
#TSlepSlep.expExclusionP1.dataUrl =

databaseCreator.create()

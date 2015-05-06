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
info = MetaInfoInput('ATLAS-CONF-2013-036')
info.comment = 'will be superseded by SUSY_2013_36'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-036/'
#info.supersededBy = 
#info.arxiv = 
#info.contact = 
info.prettyName = 'ATLAS multileptons'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TChiChiSlepSlep = TxNameInput('TChiChiSlepSlep')
TChiChiSlepSlep.on.checked ="VM"
#TChiChiSlepSlep.off.checked =
TChiChiSlepSlep.on.constraint ="[[['l+'],['l-']],[['l+'],['l-']]]+[[['l-'],['l+']],[['l-'],['l+']]]+[[['l+'],['l-']],[['l-'],['l+']]]"
#TChiChiSlepSlep.off.constraint =
TChiChiSlepSlep.on.conditionDescription ="[[['l+'],['l-']],[['l+'],['l-']]] ~ [[['l-'],['l+']],[['l-'],['l+']]], 2.*[[['l+'],['l-']],[['l+'],['l-']]] ~ [[['l+'],['l-']],[['l-'],['l+']]], [[['mu+'],['mu-']],[['e+'],['e-']]] ~ 2.*[[['mu+'],['mu-']],[['mu+'],['mu-']]], [[['mu+'],['mu-']],[['e+'],['e-']]] ~ 2.*[[['e+'],['e-']],[['e+'],['e-']]], [[['mu-'],['mu+']],[['e-'],['e+']]] ~ 2.*[[['e-'],['e+']],[['e-'],['e+']]], [[['mu-'],['mu+']],[['e-'],['e+']]] ~ 2.*[[['mu-'],['mu+']],[['mu-'],['mu+']]], [[['mu+'],['mu-']],[['e-'],['e+']]] ~ 2.*[[['e+'],['e-']],[['e-'],['e+']]], [[['mu+'],['mu-']],[['e-'],['e+']]] ~ 2.*[[['mu+'],['mu-']],[['mu-'],['mu+']]]"
#TChiChiSlepSlep.off.conditionDescription =
TChiChiSlepSlep.on.condition ="Csim([[['l+'],['l-']],[['l+'],['l-']]],[[['l-'],['l+']],[['l-'],['l+']]],0.5*[[['l+'],['l-']],[['l-'],['l+']]]); Csim([[['mu+'],['mu-']],[['e+'],['e-']]],2.*[[['mu+'],['mu-']],[['mu+'],['mu-']]],2.*[[['e+'],['e-']],[['e+'],['e-']]]); Csim([[['mu-'],['mu+']],[['e-'],['e+']]],2.*[[['e-'],['e+']],[['e-'],['e+']]],2.*[[['mu-'],['mu+']],[['mu-'],['mu+']]]); Csim([[['mu+'],['mu-']],[['e-'],['e+']]],[[['e+'],['e-']],[['e-'],['e+']]],[[['mu+'],['mu-']],[['mu-'],['mu+']]])"
#TChiChiSlepSlep.off.condition =

#+++++++ next mass plane block ++++++++++++++
TChiChiSlepSlepD080 = TChiChiSlepSlep.addMassPlane(motherMass = x+80., interMass0 = x+80.-y, lspMass = x)
TChiChiSlepSlepD080.setBranch_1(motherMass = x+80., interMass0 = x+80.-y, lspMass = x)
TChiChiSlepSlepD080.setBranch_2(motherMass = x+75., interMass0 = x+80.-y, lspMass = x)
#----limit source----
TChiChiSlepSlepD080.obsUpperLimit.setSource( 'orig/TChiChiSlepSlepD080.txt', 'txt', objectName = None, index = None )
TChiChiSlepSlepD080.obsUpperLimit.unit = 'fb'
#TChiChiSlepSlepD080.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChiSlepSlepD080.obsExclusion.setSource( 'orig/TChiChiSlepSlepD080_excl.txt', 'txt' )
#TChiChiSlepSlepD080.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlepD080.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlepD080.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlepD080.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlepD080.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiChiSlepSlepD080.dataUrl =
#TChiChiSlepSlepD080.histoDataUrl =
#TChiChiSlepSlepD080.exclusionDataUrl =
#----figure----
TChiChiSlepSlepD080.figure = 'Fig.(aux) 1a'
TChiChiSlepSlepD080.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-036/figaux_01a.png'
#----limit url settings ----
#TChiChiSlepSlepD080.obsUpperLimit.dataUrl =
#TChiChiSlepSlepD080.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChiSlepSlepD080.obsExclusion.dataUrl =
#TChiChiSlepSlepD080.obsExclusionM1.dataUrl =
#TChiChiSlepSlepD080.obsExclusionP1.dataUrl =
#TChiChiSlepSlepD080.expExclusion.dataUrl =
#TChiChiSlepSlepD080.expExclusionM1.dataUrl =
#TChiChiSlepSlepD080.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
TChiChiSlepSlep050 = TChiChiSlepSlep.addMassPlane(motherMass = y+x, interMass0 = 0.5*(y+x+x), lspMass = x)
#----limit source----
TChiChiSlepSlep050.obsUpperLimit.setSource( 'orig/TChiChiSlepSlep050.txt', 'txt', objectName = None, index = None )
TChiChiSlepSlep050.obsUpperLimit.unit = 'fb'
#TChiChiSlepSlep050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChiSlepSlep050.obsExclusion.setSource( 'orig/TChiChiSlepSlep050_excl.txt', 'txt' )
#TChiChiSlepSlep050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlep050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlep050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlep050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChiSlepSlep050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiChiSlepSlep050.dataUrl =
#TChiChiSlepSlep050.histoDataUrl =
#TChiChiSlepSlep050.exclusionDataUrl =
#----figure----
TChiChiSlepSlep050.figure = 'Fig.(aux) 1b'
TChiChiSlepSlep050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-036/fig_07b.png'
#----limit url settings ----
#TChiChiSlepSlep050.obsUpperLimit.dataUrl =
#TChiChiSlepSlep050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChiSlepSlep050.obsExclusion.dataUrl =
#TChiChiSlepSlep050.obsExclusionM1.dataUrl =
#TChiChiSlepSlep050.obsExclusionP1.dataUrl =
#TChiChiSlepSlep050.expExclusion.dataUrl =
#TChiChiSlepSlep050.expExclusionM1.dataUrl =
#TChiChiSlepSlep050.expExclusionP1.dataUrl =

databaseCreator.create()

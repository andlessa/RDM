#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt, txname.txt, twiki.txt and sms.py.

.. moduleauthor:: Michael Traub <michael.traub@gmx.at>

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
from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y


#+++++++ global info block ++++++++++++++
info = MetaInfo('ATLAS-CONF-2013-028')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-028/'
info.superseded_by = 'ATLAS-SUSY-2013-14'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS hadronic stau'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TChiChipmStauL = TxName('TChiChipmStauL')
TChiChipmStauL.on.checked ="AL"
#TChiChipmStauL.off.checked =
TChiChipmStauL.on.constraint ="2.*([[['nu'],['ta']],[['ta+'],['ta-']]] + [[['ta'],['nu']],[['ta+'],['ta-']]]+[[['nu'],['ta']],[['ta-'],['ta+']]] + [[['ta'],['nu']],[['ta-'],['ta+']]])"
#TChiChipmStauL.off.constraint =
TChiChipmStauL.on.condition ="[[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['ta'],['nu']],[['ta+'],['ta-']]],[[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['nu'],['ta']],[['ta-'],['ta+']]], [[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['ta'],['nu']],[['ta-'],['ta+']]]"
#TChiChipmStauL.off.condition =
TChiChipmStauL.on.fuzzycondition ="Csim([[['nu'],['ta']],[['ta+'],['ta-']]],[[['ta'],['nu']],[['ta+'],['ta-']]],[[['nu'],['ta']],[['ta-'],['ta+']]],[[['ta'],['nu']],[['ta-'],['ta+']]])"
#TChiChipmStauL.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmStauL050 = TChiChipmStauL.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChiChipmStauL050.obsUpperLimit.setSource( "orig/TChiChipmStauL.txt", "txt" )
#TChiChipmStauL050.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#TChiChipmStauL050.obsExclusion.setSource( path, type, object = None, index = None )
#TChiChipmStauL050.obsExclusionM1.setSource( path, type, object = None, index = None )
#TChiChipmStauL050.obsExclusionP1.setSource( path, type, object = None, index = None )
#TChiChipmStauL050.expExclusion.setSource( path, type, object = None, index = None )
#TChiChipmStauL050.expExclusionM1.setSource( path, type, object = None, index = None )
#TChiChipmStauL050.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#TChiChipmStauL050.dataUrl =
#TChiChipmStauL050.histoDataUrl =
#TChiChipmStauL050.exclusionDataUrl =
#----figure----
TChiChipmStauL050.figure = 'Fig.(aux) 8a'
TChiChipmStauL050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-028/figaux_08a.png'
#----limit url settings ----
#TChiChipmStauL050.obsUpperLimit.dataUrl = 
#TChiChipmStauL050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChipmStauL050.obsExclusion.dataUrl =
#TChiChipmStauL050.obsExclusionM1.dataUrl =
#TChiChipmStauL050.obsExclusionP1.dataUrl =
#TChiChipmStauL050.expExclusion.dataUrl =
#TChiChipmStauL050.expExclusionM1.dataUrl =
#TChiChipmStauL050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TChipChimStauSnu = TxName('TChipChimStauSnu')
TChipChimStauSnu.on.checked ="A"
#TChipChimStauSnu.off.checked =
TChipChimStauSnu.on.constraint ="[[['ta-'],['nu']],[['nu'],['ta+']]] + [[['ta+'],['nu']],[['nu'],['ta-']]] + [[['ta+'],['nu']],[['ta-'],['nu']]] + [[['nu'],['ta+']],[['nu'],['ta-']]]"
#TChipChimStauSnu.off.constraint =
TChipChimStauSnu.on.condition ="[[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['ta+'],['nu']],[['nu'],['ta-']]], [[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['ta+'],['nu']],[['ta-'],['nu']]] ,[[['ta-'],['nu']],[['nu'],['ta+']]] ~ [[['nu'],['ta+']],[['nu'],['ta-']]]"
#TChipChimStauSnu.off.condition =
TChipChimStauSnu.on.fuzzycondition ="Csim([[['ta-'],['nu']],[['nu'],['ta+']]],[[['ta+'],['nu']],[['nu'],['ta-']]],[[['ta+'],['nu']],[['ta-'],['nu']]],[[['nu'],['ta+']],[['nu'],['ta-']]])"
#TChipChimStauSnu.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChipChimStauSnu050 = TChipChimStauSnu.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChipChimStauSnu050.obsUpperLimit.setSource( "orig/TChipChimStauSnu.txt", "txt" )
#TChipChimStauSnu050.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#TChipChimStauSnu050.obsExclusion.setSource( path, type, object = None, index = None )
#TChipChimStauSnu050.obsExclusionM1.setSource( path, type, object = None, index = None )
#TChipChimStauSnu050.obsExclusionP1.setSource( path, type, object = None, index = None )
#TChipChimStauSnu050.expExclusion.setSource( path, type, object = None, index = None )
#TChipChimStauSnu050.expExclusionM1.setSource( path, type, object = None, index = None )
#TChipChimStauSnu050.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#TChipChimStauSnu050.dataUrl =
#TChipChimStauSnu050.histoDataUrl =
#TChipChimStauSnu050.exclusionDataUrl =
#----figure----
TChipChimStauSnu050.figure = 'Fig.(aux) 9a'
TChipChimStauSnu050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-028/figaux_09a.png'
#----limit url settings ----
#TChipChimStauSnu050.obsUpperLimit.dataUrl =
#TChipChimStauSnu050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChipChimStauSnu050.obsExclusion.dataUrl =
#TChipChimStauSnu050.obsExclusionM1.dataUrl =
#TChipChimStauSnu050.obsExclusionP1.dataUrl =
#TChipChimStauSnu050.expExclusion.dataUrl =
#TChipChimStauSnu050.expExclusionM1.dataUrl =
#TChipChimStauSnu050.expExclusionP1.dataUrl =

databaseCreator.create()
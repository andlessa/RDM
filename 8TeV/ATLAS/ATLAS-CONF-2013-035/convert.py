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
info = MetaInfo('ATLAS-CONF-2013-035')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-035/'
info.superseded_by = 'ATLAS-SUSY-2013-12'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS trilepton weakinos'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TChiWZ = TxName('TChiWZ')
TChiWZ.on.checked ="VM"
TChiWZ.off.checked ="VM"
TChiWZ.on.constraint ="[[['W']],[['Z']]]"
TChiWZ.off.constraint ="71.*([[['mu+','mu-']],[['l','nu']]] + [[['e+','e-']],[['l','nu']]])"
TChiWZ.on.condition ="None"
TChiWZ.off.condition ="[[['mu+','mu-']],[['l','nu']]] > [[['e+','e-']],[['l','nu']]]"
TChiWZ.on.fuzzycondition ="None"
TChiWZ.off.fuzzycondition ="Cgtr([[['mu+','mu-']],[['l','nu']]],[[['e+','e-']],[['l','nu']]])"

#+++++++ next mass plane block ++++++++++++++
TChiWZ = TChiWZ.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWZ.obsUpperLimit.setSource( "orig/TChiWZ.txt", "txt" )
#TChiWZ.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
TChiWZ.obsExclusion.setSource( "orig/TChiWZ_exc.dat", "txt")
#TChiWZ.obsExclusionM1.setSource( path, type, object = None, index = None )
#TChiWZ.obsExclusionP1.setSource( path, type, object = None, index = None )
#TChiWZ.expExclusion.setSource( path, type, object = None, index = None )
#TChiWZ.expExclusionM1.setSource( path, type, object = None, index = None )
#TChiWZ.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#TChiWZ.dataUrl =
#TChiWZ.histoDataUrl =
#TChiWZ.exclusionDataUrl =
#----figure----
TChiWZ.figure = 'Fig.(aux) 1b'
TChiWZ.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-035/figaux_01b.png'
#----limit url settings ----
TChiWZ.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-035/figaux_01b_PRELIMINARY.data'
#TChiWZ.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiWZ.obsExclusion.dataUrl =
#TChiWZ.obsExclusionM1.dataUrl =
#TChiWZ.obsExclusionP1.dataUrl =
#TChiWZ.expExclusion.dataUrl =
#TChiWZ.expExclusionM1.dataUrl =
#TChiWZ.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TChiChipmSlepL = TxName('TChiChipmSlepL')
TChiChipmSlepL.on.checked ="VM"
#TChiChipmSlepL.off.checked =
TChiChipmSlepL.on.constraint ="2.*([[['L'],['L']],[['L'],['nu']]] + [[['L'],['L']],[['nu'],['L']]])"
#TChiChipmSlepL.off.constraint =
TChiChipmSlepL.on.condition ="[[['L'],['L']],[['L'],['nu']]] ~ [[['L'],['L']],[['nu'],['L']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['ta'],['ta']],[['nu'],['L']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['ta'],['ta']],[['L'],['nu']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['ta']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['ta'],['nu']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['e'],['e']],[['nu'],['L']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['e'],['e']],[['L'],['nu']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['e']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['e'],['nu']]]"
#TChiChipmSlepL.off.condition =
TChiChipmSlepL.on.fuzzycondition ="Csim([[['L'],['L']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['ta'],['ta']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['ta'],['ta']],[['L'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['ta']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['ta'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['e'],['e']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['e'],['e']],[['L'],['nu']]]); Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['e']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['e'],['nu']]])"
#TChiChipmSlepL.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL050 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChiChipmSlepL050.obsUpperLimit.setSource( "orig/TChiChipmSlepL.txt", 'txt' )
TChiChipmSlepL050.obsUpperLimit.unit = 'fb'
#TChiChipmSlepL050.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#TChiChipmSlepL050.obsExclusion.setSource( path, type, object = None, index = None )
#TChiChipmSlepL050.obsExclusionM1.setSource( path, type, object = None, index = None )
#TChiChipmSlepL050.obsExclusionP1.setSource( path, type, object = None, index = None )
#TChiChipmSlepL050.expExclusion.setSource( path, type, object = None, index = None )
#TChiChipmSlepL050.expExclusionM1.setSource( path, type, object = None, index = None )
#TChiChipmSlepL050.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#TChiChipmSlepL050.dataUrl =
#TChiChipmSlepL050.histoDataUrl =
#TChiChipmSlepL050.exclusionDataUrl =
#----figure----
TChiChipmSlepL050.figure = 'Fig.(aux) 1a'
TChiChipmSlepL050.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-035/figaux_01a.png'
#----limit url settings ----
TChiChipmSlepL050.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-035/figaux_01a_PRELIMINARY.data'
#TChiChipmSlepL050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChipmSlepL050.obsExclusion.dataUrl =
#TChiChipmSlepL050.obsExclusionM1.dataUrl =
#TChiChipmSlepL050.obsExclusionP1.dataUrl =
#TChiChipmSlepL050.expExclusion.dataUrl =
#TChiChipmSlepL050.expExclusionM1.dataUrl =
#TChiChipmSlepL050.expExclusionP1.dataUrl =

databaseCreator.create()
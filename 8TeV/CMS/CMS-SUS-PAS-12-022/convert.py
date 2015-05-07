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
info = MetaInfoInput('CMS-SUS-PAS-12-022')
# info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '9.2'
##info.publication = 
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS12022'
info.supersededBy = 'CMS-SUS-13-006 (more data)'
#info.arxiv = 
info.contact = 'Benjamin Hooberman <hooberman@gmail.com>, Lesya Shchutska <lesya.shchutska@cern.ch>'
info.prettyName = 'weakinos'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TChiWZ = TxNameInput('TChiWZ')
TChiWZ.on.checked ="A"
#TChiWZ.off.checked =
TChiWZ.on.constraint ="[[['W']],[['Z']]]"
#TChiWZ.off.constraint =
TChiWZ.on.conditionDescription ="None"
#TChiWZ.off.condition =
TChiWZ.on.condition ="None"
#TChiWZ.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiWZ = TChiWZ.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWZ.obsUpperLimit.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 2 )
TChiWZ.obsUpperLimit.unit = 'fb'
# TChiWZ.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiWZ.obsExclusion.setSource( "orig/exclusion_TChiWZ.root", "canvas", objectName = "interpret", index = 8 )
"""
TChiWZ.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiWZ.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiWZ.expExclusion.setSource( path, filetype, objectName = None, index = None )
TChiWZ.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiWZ.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TChiWZ.dataUrl =
TChiWZ.histoDataUrl =
TChiWZ.exclusionDataUrl =
#----figure----
TChiWZ.figure =
TChiWZ.figureUrl =
#----limit url settings ----
TChiWZ.obsUpperLimit.dataUrl =
TChiWZ.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiWZ.obsExclusion.dataUrl =
TChiWZ.obsExclusionM1.dataUrl =
TChiWZ.obsExclusionP1.dataUrl =
TChiWZ.expExclusion.dataUrl =
TChiWZ.expExclusionM1.dataUrl =
TChiWZ.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
TChiChipmStauStau = TxNameInput('TChiChipmStauStau')
TChiChipmStauStau.on.checked ="A"
#TChiChipmStauStau.off.checked =
TChiChipmStauStau.on.constraint ="[[['ta'],['ta']],[['nu'],['ta']]]"
#TChiChipmStauStau.off.constraint =
TChiChipmStauStau.on.conditionDescription ="None"
#TChiChipmStauStau.off.condition =
TChiChipmStauStau.on.condition ="None"
#TChiChipmStauStau.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmStauStau050 = TChiChipmStauStau.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChiChipmStauStau050.obsUpperLimit.setSource( "orig/exclusion_TChiStauSnu_0_5.root", "canvas", objectName = "interpret", index = 2 )
# TChiChipmStauStau050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmStauStau050.obsExclusion.setSource( "orig/exclusion_TChiStauSnu_0_5.root", "canvas", objectName = "interpret", index = 8 )
#TChiChipmStauStau050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauStau050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauStau050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauStau050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmStauStau050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiChipmStauStau050.dataUrl =
#TChiChipmStauStau050.histoDataUrl =
#TChiChipmStauStau050.exclusionDataUrl =
#----figure----
TChiChipmStauStau050.figure = "Fig. 17"
TChiChipmStauStau050.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChiStauSnu_0_5.pdf"
#----limit url settings ----
##TChiChipmStauStau050.obsUpperLimit.dataUrl =
#TChiChipmStauStau050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChipmStauStau050.obsExclusion.dataUrl =
#TChiChipmStauStau050.obsExclusionM1.dataUrl =
#TChiChipmStauStau050.obsExclusionP1.dataUrl =
#TChiChipmStauStau050.expExclusion.dataUrl =
#TChiChipmStauStau050.expExclusionM1.dataUrl =
#TChiChipmStauStau050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TSlepSlep = TxNameInput('TSlepSlep')
TSlepSlep.on.checked ="A"
#TSlepSlep.off.checked =
TSlepSlep.on.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
#TSlepSlep.off.constraint =
TSlepSlep.on.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
#TSlepSlep.off.condition =
TSlepSlep.on.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
#TSlepSlep.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TSlepSlep = TSlepSlep.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TSlepSlep.obsUpperLimit.setSource( "orig/exclusion_TSlepSlep.root", "canvas", objectName = "interpret", index = 2 )
TSlepSlep.obsUpperLimit.unit = 'fb'
## TSlepSlep.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TSlepSlep.obsExclusion.setSource( "orig/exclusion_TSlepSlep.root","canvas", objectName = "interpret", index = 8 )
"""
TSlepSlep.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TSlepSlep.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TSlepSlep.expExclusion.setSource( path, filetype, objectName = None, index = None )
TSlepSlep.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TSlepSlep.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TSlepSlep.dataUrl =
TSlepSlep.histoDataUrl =
TSlepSlep.exclusionDataUrl =
"""
#----figure----
TSlepSlep.figure = "Fig. 21"
TSlepSlep.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TSlepSlep.pdf"
"""
#----limit url settings ----
TSlepSlep.obsUpperLimit.dataUrl =
TSlepSlep.expUpperLimit.dataUrl =
#----exclusion url settings ----
TSlepSlep.obsExclusion.dataUrl =
TSlepSlep.obsExclusionM1.dataUrl =
TSlepSlep.obsExclusionP1.dataUrl =
TSlepSlep.expExclusion.dataUrl =
TSlepSlep.expExclusionM1.dataUrl =
TSlepSlep.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
TChiChipmSlepStau = TxNameInput('TChiChipmSlepStau')
TChiChipmSlepStau.on.checked ="A"
#TChiChipmSlepStau.off.checked =
TChiChipmSlepStau.on.constraint ="[[['L'],['L']],[['nu'],['ta']]]"
#TChiChipmSlepStau.off.constraint =
TChiChipmSlepStau.on.conditionDescription ="[[['L'],['L']],[['nu'],['ta']]] > 2.7*[[['ta'],['ta']],[['nu'],['ta']]],[[['L'],['L']],[['nu'],['ta']]] > 2.7*[[['e'],['e']],[['nu'],['ta']]]"
#TChiChipmSlepStau.off.condition =
TChiChipmSlepStau.on.condition ="Cgtr([[['L'],['L']],[['nu'],['ta']]],3.*[[['ta'],['ta']],[['nu'],['ta']]]);Cgtr([[['L'],['L']],[['nu'],['ta']]],3.*[[['e'],['e']],[['nu'],['ta']]])"
#TChiChipmSlepStau.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau095 = TChiChipmSlepStau.addMassPlane(motherMass = x, interMass0 = x*0.95 + (1. - 0.95)*y, lspMass = y)
#----limit source----
TChiChipmSlepStau095.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = 
        "interpret", index = 2 )
# TChiChipmSlepStau095.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepStau095.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_95.root", "canvas", objectName = "interpret", index = 8 )
"""
TChiChipmSlepStau095.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau095.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau095.expExclusion.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau095.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau095.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TChiChipmSlepStau095.dataUrl =
TChiChipmSlepStau095.histoDataUrl =
TChiChipmSlepStau095.exclusionDataUrl =
#----figure----
"""
TChiChipmSlepStau095.figure = "Fig. 16a"
TChiChipmSlepStau095.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChiSlepSnu_2a_0_05.pdf"
#----limit url settings ----
"""
TChiChipmSlepStau095.obsUpperLimit.dataUrl =
TChiChipmSlepStau095.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau095.obsExclusion.dataUrl =
TChiChipmSlepStau095.obsExclusionM1.dataUrl =
TChiChipmSlepStau095.obsExclusionP1.dataUrl =
TChiChipmSlepStau095.expExclusion.dataUrl =
TChiChipmSlepStau095.expExclusionM1.dataUrl =
TChiChipmSlepStau095.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau050 = TChiChipmSlepStau.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChiChipmSlepStau050.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 2 )
# TChiChipmSlepStau050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepStau050.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_5.root", "canvas", objectName = "interpret", index = 8 )
"""
TChiChipmSlepStau050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau050.expExclusion.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TChiChipmSlepStau050.dataUrl =
TChiChipmSlepStau050.histoDataUrl =
TChiChipmSlepStau050.exclusionDataUrl =
#----figure----
TChiChipmSlepStau050.figure =
TChiChipmSlepStau050.figureUrl =
#----limit url settings ----
TChiChipmSlepStau050.obsUpperLimit.dataUrl =
TChiChipmSlepStau050.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau050.obsExclusion.dataUrl =
TChiChipmSlepStau050.obsExclusionM1.dataUrl =
TChiChipmSlepStau050.obsExclusionP1.dataUrl =
TChiChipmSlepStau050.expExclusion.dataUrl =
TChiChipmSlepStau050.expExclusionM1.dataUrl =
TChiChipmSlepStau050.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepStau005 = TChiChipmSlepStau.addMassPlane(motherMass = x, interMass0 = x*0.05 + (1. - 0.05)*y, lspMass = y)
#----limit source----
TChiChipmSlepStau005.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 2 )
#TChiChipmSlepStau005.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepStau005.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2a_0_05.root", "canvas", objectName = "interpret", index = 8 )
"""
TChiChipmSlepStau005.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau005.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau005.expExclusion.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau005.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepStau005.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TChiChipmSlepStau005.dataUrl =
TChiChipmSlepStau005.histoDataUrl =
TChiChipmSlepStau005.exclusionDataUrl =
#----figure----
"""
TChiChipmSlepStau005.figure = "Fig. 16a"
TChiChipmSlepStau005.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChiSlepSnu_2a_0_05.pdf"
"""
#----limit url settings ----
TChiChipmSlepStau005.obsUpperLimit.dataUrl =
TChiChipmSlepStau005.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepStau005.obsExclusion.dataUrl =
TChiChipmSlepStau005.obsExclusionM1.dataUrl =
TChiChipmSlepStau005.obsExclusionP1.dataUrl =
TChiChipmSlepStau005.expExclusion.dataUrl =
TChiChipmSlepStau005.expExclusionM1.dataUrl =
TChiChipmSlepStau005.expExclusionP1.dataUrl =
"""

#+++++++ next txName block ++++++++++++++
TChiChipmSlepL = TxNameInput('TChiChipmSlepL')
TChiChipmSlepL.on.checked ="A"
#TChiChipmSlepL.off.checked =
TChiChipmSlepL.on.constraint ="2.*([[['L'],['L']],[['L'],['nu']]] + [[['L'],['L']],[['nu'],['L']]])"
#TChiChipmSlepL.off.constraint =
TChiChipmSlepL.on.conditionDescription ="[[['L'],['L']],[['L'],['nu']]] ~ [[['L'],['L']],[['nu'],['L']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['ta'],['ta']],[['nu'],['L']]],[[['L'],['L']],[['L'],['nu']]] > 2.7*[[['ta'],['ta']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['ta']]],[[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['ta'],['nu']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['e'],['e']],[['nu'],['L']]],[[['L'],['L']],[['L'],['nu']]] > 2.7*[[['e'],['e']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['e']]],[[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['e'],['nu']]]"
#TChiChipmSlepL.off.condition =
TChiChipmSlepL.on.condition ="Csim([[['L'],['L']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['ta'],['ta']],[['nu'],['L']]]);Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['ta'],['ta']],[['L'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['ta']]]);Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['ta'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['e'],['e']],[['nu'],['L']]]);Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['e'],['e']],[['L'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['e']]]);Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['e'],['nu']]])"
#TChiChipmSlepL.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL005 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = x*0.05 + (1. - 0.05)*y, lspMass = y)
#----limit source----
TChiChipmSlepL005.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2i_0_05.root", "canvas", objectName = "interpret", index = 2 )
# TChiChipmSlepL005.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL005.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2i_0_05.root", "canvas", objectName = "interpret", index = 8 )
"""
TChiChipmSlepL005.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepL005.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepL005.expExclusion.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepL005.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
TChiChipmSlepL005.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
TChiChipmSlepL005.dataUrl =
TChiChipmSlepL005.histoDataUrl =
TChiChipmSlepL005.exclusionDataUrl =
#----figure----
TChiChipmSlepL005.figure =
TChiChipmSlepL005.figureUrl =
#----limit url settings ----
TChiChipmSlepL005.obsUpperLimit.dataUrl =
TChiChipmSlepL005.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiChipmSlepL005.obsExclusion.dataUrl =
TChiChipmSlepL005.obsExclusionM1.dataUrl =
TChiChipmSlepL005.obsExclusionP1.dataUrl =
TChiChipmSlepL005.expExclusion.dataUrl =
TChiChipmSlepL005.expExclusionM1.dataUrl =
TChiChipmSlepL005.expExclusionP1.dataUrl =
"""

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL095 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = x*0.95 + (1. - 0.95)*y, lspMass = y)
#----limit source----
TChiChipmSlepL095.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2i_0_95.root", "canvas", objectName = "interpret", index = 2 )
# TChiChipmSlepL095.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL095.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2i_0_95.root", "canvas", objectName = "interpret", index = 8 )
#TChiChipmSlepL095.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiChipmSlepL095.dataUrl =
#TChiChipmSlepL095.histoDataUrl =
#TChiChipmSlepL095.exclusionDataUrl =
#----figure----
TChiChipmSlepL095.figure = "Fig. 15b" 
TChiChipmSlepL095.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChiSlepSnu_2i_0_95.pdf"
#----limit url settings ----
#TChiChipmSlepL095.obsUpperLimit.dataUrl =
#TChiChipmSlepL095.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChipmSlepL095.obsExclusion.dataUrl =
#TChiChipmSlepL095.obsExclusionM1.dataUrl =
#TChiChipmSlepL095.obsExclusionP1.dataUrl =
#TChiChipmSlepL095.expExclusion.dataUrl =
#TChiChipmSlepL095.expExclusionM1.dataUrl =
#TChiChipmSlepL095.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL050 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChiChipmSlepL050.obsUpperLimit.setSource( "orig/exclusion_TChiSlepSnu_2i_0_5.root", "canvas", objectName = "interpret", index = 2 )
# TChiChipmSlepL050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiChipmSlepL050.obsExclusion.setSource( "orig/exclusion_TChiSlepSnu_2i_0_5.root", "canvas", objectName = "interpret", index = 8 )
#TChiChipmSlepL050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmSlepL050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmSlepL050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChiChipmSlepL050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiChipmSlepL050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiChipmSlepL050.dataUrl =
#TChiChipmSlepL050.histoDataUrl =
#TChiChipmSlepL050.exclusionDataUrl =
#----figure----
TChiChipmSlepL050.figure = "Fig. 14"
TChiChipmSlepL050.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChiSlepSnu_2i_0_5.pdf"
#----limit url settings ----
#TChiChipmSlepL050.obsUpperLimit.dataUrl =
#TChiChipmSlepL050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiChipmSlepL050.obsExclusion.dataUrl =
#TChiChipmSlepL050.obsExclusionM1.dataUrl =
#TChiChipmSlepL050.obsExclusionP1.dataUrl =
#TChiChipmSlepL050.expExclusion.dataUrl =
#TChiChipmSlepL050.expExclusionM1.dataUrl =
#TChiChipmSlepL050.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
TChipChimSlepSnu = TxNameInput('TChipChimSlepSnu')
TChipChimSlepSnu.on.checked ="A"
#TChipChimSlepSnu.off.checked =
TChipChimSlepSnu.on.constraint ="[[['L-'],['nu']],[['nu'],['L+']]] + [[['L+'],['nu']],[['nu'],['L-']]] + [[['L+'],['nu']],[['L-'],['nu']]] + [[['nu'],['L+']],[['nu'],['L-']]]"
#TChipChimSlepSnu.off.constraint =
TChipChimSlepSnu.on.conditionDescription ="[[['L-'],['nu']],[['nu'],['L+']]] ~ [[['L+'],['nu']],[['nu'],['L-']]],[[['L-'],['nu']],[['nu'],['L+']]] ~ [[['L+'],['nu']],[['L-'],['nu']]],[[['L-'],['nu']],[['nu'],['L+']]] ~ [[['nu'],['L+']],[['nu'],['L-']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['ta-'],['nu']],['nu'],['L+']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['L-'],['nu']],[['nu'],['ta+']]],[[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['ta+'],['nu']],[['nu'],['L-']]],[[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['L+'],['nu']],[['nu'],['ta-']]],[[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['ta+'],['nu']],[['L-'],['nu']]],[[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['L+'],['nu']],[['ta-'],['nu']]],[[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['ta+']],[['nu'],[L-']]],[[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['L+']],[['nu'],[ta-']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['e-'],['nu']],[['nu'],['L+']]],[[['L-'],['nu']],[['nu'],['L+']]] > 2.7*[[['L-'],['nu']],[['nu'],['e+']]],[[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['e+'],['nu']],[['nu'],['L-']]],[[['L+'],['nu']],[['nu'],['L-']]] > 2.7*[[['L+'],['nu']],[['nu'],['e-']]], [[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['e+'],['nu']],[['L-'],['nu']]],[[['L+'],['nu']],[['L-'],['nu']]] > 2.7*[[['L+'],['nu']],[['e-'],['nu']]], [[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['e+']],[['nu'],['L-']]],[[['nu'],['L+']],[['nu'],['L-']]] > 2.7*[[['nu'],['L+']],[['nu'],['e-']]]"
#TChipChimSlepSnu.off.condition =
TChipChimSlepSnu.on.condition ="Csim([[['L-'],['nu']],[['nu'],['L+']]],[[['L+'],['nu']],[['nu'],['L-']]],[[['L+'],['nu']],[['L-'],['nu']]],[[['nu'],['L+']],[['nu'],['L-']]]);Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['ta-'],['nu']],[['nu'],['L+']]]);Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['L-'],['nu']],[['nu'],['ta+']]]);Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.*[[['ta+'],['nu']],[['nu'],['L-']]]);Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.* [[['L+'],['nu']],[['nu'],['ta-']]]);Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['ta+'],['nu']],[['L-'],['nu']]]);Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['L+'],['nu']],[['ta-'],['nu']]]);Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['ta+']],[['nu'],[L-']]]);Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['L+']],[['nu'],[ta-']]]);Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['e-'],['nu']],[['nu'],['L+']]]);Cgtr([[['L-'],['nu']],[['nu'],['L+']]],3.*[[['L-'],['nu']],[['nu'],['e+']]]);Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.*[[['e+'],['nu']],[['nu'],['L-']]]);Cgtr([[['L+'],['nu']],[['nu'],['L-']]],3.* [[['L+'],['nu']],[['nu'],['e-']]]);Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['e+'],['nu']],[['L-'],['nu']]]);Cgtr([[['L+'],['nu']],[['L-'],['nu']]],3.*[[['L+'],['nu']],[['e-'],['nu']]]);Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['e+']],[['nu'],[L-']]]);Cgtr([[['nu'],['L+']],[['nu'],[L-']]],3.*[[['nu'],['L+']],[['nu'],[e-']]])"
#TChipChimSlepSnu.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TChipChimSlepSnu050 = TChipChimSlepSnu.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#----limit source----
TChipChimSlepSnu050.obsUpperLimit.setSource( "orig/exclusion_TChipmSlepSnu.root", "canvas", objectName = "interpret", index = 2 )
# TChipChimSlepSnu050.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChipChimSlepSnu050.obsExclusion.setSource( "orig/exclusion_TChipmSlepSnu.root", "canvas", objectName = "interpret", index = 8 )
#TChipChimSlepSnu050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChipChimSlepSnu050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChipChimSlepSnu050.dataUrl =
#TChipChimSlepSnu050.histoDataUrl =
#TChipChimSlepSnu050.exclusionDataUrl =
#----figure----
TChipChimSlepSnu050.figure = "Fig. 20"
TChipChimSlepSnu050.figureUrl = "https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS12022/exclusion_TChipmSlepSnu.pdf"
#----limit url settings ----
#TChipChimSlepSnu050.obsUpperLimit.dataUrl =
#TChipChimSlepSnu050.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChipChimSlepSnu050.obsExclusion.dataUrl =
#TChipChimSlepSnu050.obsExclusionM1.dataUrl =
#TChipChimSlepSnu050.obsExclusionP1.dataUrl =
#TChipChimSlepSnu050.expExclusion.dataUrl =
#TChipChimSlepSnu050.expExclusionM1.dataUrl =
#TChipChimSlepSnu050.expExclusionP1.dataUrl =

databaseCreator.create()

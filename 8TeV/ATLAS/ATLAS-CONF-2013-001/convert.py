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
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-CONF-2013-001')
info.comment = 'suberseding vesrion is published'
info.sqrts = '8.0'
info.private = False
info.lumi = '12.8'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-001/'
info.superseded_by = 'ATLAS-SUSY-2013-05'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS W_{off} stop'
#info.supersedes = 
info.implemented_by = 'MT'

#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
#T6bbWW.on.checked =
T6bbWW.off.checked ="AL"
T6bbWW.on.constraint = "[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="[[['b'],['L','nu']],[['b'],['L','nu']]] + [[['b'],['L','nu']],[['b'],['jet','jet']]] + [[['b'],['jet','jet']],[['b'],['jet','jet']]]"
#T6bbWW.on.condition =
T6bbWW.off.condition ="None"
#T6bbWW.on.fuzzycondition =
T6bbWW.off.fuzzycondition ="None"

#+++++++ next mass plane block ++++++++++++++
T6bbWWD020 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y + 20.0, lspMass = y)
#----limit source----
T6bbWWD020.obsUpperLimit.setSource( "orig/T6bbWWoff.txt", "txt" )
#T6bbWWD020.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T6bbWWD020.obsExclusion.setSource( "orig/T6bbWW20GeV_excl.txt", "txt")
#T6bbWWD020.obsExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD020.obsExclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWD020.expExclusion.setSource( path, type, object = None, index = None )
#T6bbWWD020.expExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD020.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWD020.dataUrl =
#T6bbWWD020.histoDataUrl =
#T6bbWWD020.exclusionDataUrl =
#----figure----
T6bbWWD020.figure ='Fig.(aux) 7'
T6bbWWD020.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-001/figaux_07.png'
#----limit url settings ----
#T6bbWWD020.obsUpperLimit.dataUrl =
#T6bbWWD020.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWD020.obsExclusion.dataUrl =
#T6bbWWD020.obsExclusionM1.dataUrl =
#T6bbWWD020.obsExclusionP1.dataUrl =
#T6bbWWD020.expExclusion.dataUrl =
#T6bbWWD020.expExclusionM1.dataUrl =
#T6bbWWD020.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWD005 = T6bbWW.addMassPlane(motherMass = x, interMass0 = y + 5.0, lspMass = y)
#----limit source----
T6bbWWD005.obsUpperLimit.setSource( "orig/T2bb.txt", "txt" )
#T6bbWWD005.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T6bbWWD005.obsExclusion.setSource( "orig/T6bbWW5GeV_excl.txt", "txt")
#T6bbWWD005.obsExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD005.obsExclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWD005.expExclusion.setSource( path, type, object = None, index = None )
#T6bbWWD005.expExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD005.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWD005.dataUrl =
#T6bbWWD005.histoDataUrl =
#T6bbWWD005.exclusionDataUrl =
#----figure----
T6bbWWD005.figure ='Fig.(aux) 6'
T6bbWWD005.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-001/figaux_06.png'
#----limit url settings ----
#T6bbWWD005.obsUpperLimit.dataUrl =
#T6bbWWD005.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6bbWWD005.obsExclusion.dataUrl =
#T6bbWWD005.obsExclusionM1.dataUrl =
#T6bbWWD005.obsExclusionP1.dataUrl =
#T6bbWWD005.expExclusion.dataUrl =
#T6bbWWD005.expExclusionM1.dataUrl =
#T6bbWWD005.expExclusionP1.dataUrl =

databaseCreator.create()

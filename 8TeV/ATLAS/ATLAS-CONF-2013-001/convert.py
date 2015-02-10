#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create info.txt,sms.py,sms.root and newSms.py.

"""
import sys
import os
sys.path.append(os.path.abspath('../../../../smodels-utils'))
from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfo('ATLAS-CONF-2013-001')
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
T6bbWW = TxName('T6bbWW')
#T6bbWW.on.checked =
T6bbWW.off.checked ="AL"
T6bbWW.on.constraint = "[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="[[['b'],['L','nu']],[['b'],['L','nu']]] + [[['b'],['L','nu']],[['b'],['jet','jet']]] + [[['b'],['jet','jet']],[['b'],['jet','jet']]]"
#T6bbWW.on.condition =
T6bbWW.off.condition ="None"
#T6bbWW.on.fuzzycondition =
T6bbWW.off.fuzzycondition ="None"

#+++++++ next mass plane block ++++++++++++++
T6bbWWD020 = T6bbWW.addMassPlane(motherMass = x, interMass = y + 20.0, lspMass = y)
#----limit source----
T6bbWWD020.limit.setSource( "orig/T6bbWWoff.txt", "txt" )
#T6bbWWD020.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T6bbWWD020.exclusion.setSource( path, type, object = None, index = None )
#T6bbWWD020.exclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD020.exclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWD020.expectedExclusion.setSource( path, type, object = None, index = None )
#T6bbWWD020.expectedExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD020.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWD020.dataUrl =
#T6bbWWD020.histoDataUrl =
#T6bbWWD020.exclusionDataUrl =
#----figure----
T6bbWWD020.figure ='Fig.(aux) 7'
T6bbWWD020.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-001/figaux_07.png'
#----limit url settings ----
#T6bbWWD020.limit.dataUrl =
#T6bbWWD020.expectedlimit.dataUrl =
#----exclusion url settings ----
#T6bbWWD020.exclusion.dataUrl =
#T6bbWWD020.exclusionM1.dataUrl =
#T6bbWWD020.exclusionP1.dataUrl =
#T6bbWWD020.expectedExclusion.dataUrl =
#T6bbWWD020.expectedExclusionM1.dataUrl =
#T6bbWWD020.expectedExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWD005 = T6bbWW.addMassPlane(motherMass = x, interMass = y + 5.0, lspMass = y)
#----limit source----
T6bbWWD005.limit.setSource( "orig/T2bb.txt", "txt" )
#T6bbWWD005.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T6bbWWD005.exclusion.setSource( path, type, object = None, index = None )
#T6bbWWD005.exclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD005.exclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWD005.expectedExclusion.setSource( path, type, object = None, index = None )
#T6bbWWD005.expectedExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWD005.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWD005.dataUrl =
#T6bbWWD005.histoDataUrl =
#T6bbWWD005.exclusionDataUrl =
#----figure----
T6bbWWD005.figure ='Fig.(aux) 6'
T6bbWWD005.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-001/figaux_06.png'
#----limit url settings ----
#T6bbWWD005.limit.dataUrl =
#T6bbWWD005.expectedlimit.dataUrl =
#----exclusion url settings ----
#T6bbWWD005.exclusion.dataUrl =
#T6bbWWD005.exclusionM1.dataUrl =
#T6bbWWD005.exclusionP1.dataUrl =
#T6bbWWD005.expectedExclusion.dataUrl =
#T6bbWWD005.expectedExclusionM1.dataUrl =
#T6bbWWD005.expectedExclusionP1.dataUrl =

databaseCreator.create()
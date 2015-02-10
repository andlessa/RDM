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
info = MetaInfo('ATLAS-CONF-2012-166')
info.comment = 'superseding publication contain more Data'
info.sqrts = '8.0'
info.private = False
info.lumi = '13.0'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-166/'
info.superseded_by = 'ATLAS-CONF-2013-037'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS leptonic stop'
#info.supersedes = 
info.implemented_by = 'MT'

#+++++++ next txName block ++++++++++++++
T2tt = TxName('T2tt')
T2tt.on.checked ="AL"
#T2tt.off.checked =
T2tt.on.constraint ="[[['t']],[['t']]]"
#T2tt.off.constraint =
T2tt.on.condition ="None"
#T2tt.off.condition =
T2tt.on.fuzzycondition ="None"
#T2tt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T2tt = T2tt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T2tt.limit.setSource( "orig/T2tt.txt", "txt" )
#T2tt.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T2tt.exclusion.setSource( 'orig/exclusion_T2tt.txt', 'txt')
#T2tt.exclusionM1.setSource( path, type, object = None, index = None )
#T2tt.exclusionP1.setSource( path, type, object = None, index = None )
#T2tt.expectedExclusion.setSource( path, type, object = None, index = None )
#T2tt.expectedExclusionM1.setSource( path, type, object = None, index = None )
#T2tt.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T2tt.dataUrl =
#T2tt.histoDataUrl =
#T2tt.exclusionDataUrl =
#----figure----
T2tt.figure = 'Fig.(aux) 3'
T2tt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-166//figaux_03.png'
#----limit url settings ----
#T2tt.limit.dataUrl =
#T2tt.expectedlimit.dataUrl =
#----exclusion url settings ----
#T2tt.exclusion.dataUrl =
#T2tt.exclusionM1.dataUrl =
#T2tt.exclusionP1.dataUrl =
#T2tt.expectedExclusion.dataUrl =
#T2tt.expectedExclusionM1.dataUrl =
#T2tt.expectedExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T6bbWW = TxName('T6bbWW')
T6bbWW.on.checked ="AL"
#T6bbWW.off.checked =
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="3.5*([[['b'],['L','nu']],[['b'],['jet','jet']]])"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="[[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','ta','nu']],[['b','jet','jet']]], [[['b','L','nu']],[['b','jet','jet']]] > 2.7* [[['b','e','nu']],[['b','jet','jet']]]"
T6bbWW.on.fuzzycondition ="None"
T6bbWW.off.fuzzycondition ="Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['ta','nu']],[['b'],['jet','jet']]]);Cgtr([[['b'],['L','nu']],[['b'],['jet','jet']]],3.*[[['b'],['e','nu']],[['b'],['jet','jet']]])"

#+++++++ next mass plane block ++++++++++++++
T6bbWWC150 = T6bbWW.addMassPlane(motherMass = x, interMass = 150.0, lspMass = y)
#----limit source----
T6bbWWC150.limit.setSource( "orig/T6bbWWC150.txt", "txt")
#T6bbWWC150.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T6bbWWC150.exclusion.setSource( path, type, object = None, index = None )
#T6bbWWC150.exclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWC150.exclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWC150.expectedExclusion.setSource( path, type, object = None, index = None )
#T6bbWWC150.expectedExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWC150.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWC150.dataUrl =
#T6bbWWC150.histoDataUrl =
#T6bbWWC150.exclusionDataUrl =
#----figure----
T6bbWWC150.figure = 'Fig.(aux) 4'
T6bbWWC150.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-166//figaux_04.png'
#----limit url settings ----
#T6bbWWC150.limit.dataUrl =
#T6bbWWC150.expectedlimit.dataUrl =
#----exclusion url settings ----
#T6bbWWC150.exclusion.dataUrl =
#T6bbWWC150.exclusionM1.dataUrl =
#T6bbWWC150.exclusionP1.dataUrl =
#T6bbWWC150.expectedExclusion.dataUrl =
#T6bbWWC150.expectedExclusionM1.dataUrl =
#T6bbWWC150.expectedExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6bbWWx200 = T6bbWW.addMassPlane(motherMass = x, interMass = y * 2.0, lspMass = y)
#----limit source----
T6bbWWx200.limit.setSource( "orig/T6bbWWx2.txt", 'txt' )
#T6bbWWx200.expectedlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T6bbWWx200.exclusion.setSource( path, type, object = None, index = None )
#T6bbWWx200.exclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWx200.exclusionP1.setSource( path, type, object = None, index = None )
#T6bbWWx200.expectedExclusion.setSource( path, type, object = None, index = None )
#T6bbWWx200.expectedExclusionM1.setSource( path, type, object = None, index = None )
#T6bbWWx200.expectedExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6bbWWx200.dataUrl =
#T6bbWWx200.histoDataUrl =
#T6bbWWx200.exclusionDataUrl =
#----figure----
T6bbWWx200.figure = 'Fig.(aux) 5'
T6bbWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-166//figaux_05.png'
#----limit url settings ----
#T6bbWWx200.limit.dataUrl =
#T6bbWWx200.expectedlimit.dataUrl =
#----exclusion url settings ----
#T6bbWWx200.exclusion.dataUrl =
#T6bbWWx200.exclusionM1.dataUrl =
#T6bbWWx200.exclusionP1.dataUrl =
#T6bbWWx200.expectedExclusion.dataUrl =
#T6bbWWx200.expectedExclusionM1.dataUrl =
#T6bbWWx200.expectedExclusionP1.dataUrl =

databaseCreator.create()
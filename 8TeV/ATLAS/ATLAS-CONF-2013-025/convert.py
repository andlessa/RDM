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
info = MetaInfo('ATLAS-CONF-2013-025')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-025/'
info.superseded_by = 'ATLAS-SUSY-2013-08' 
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS heavy stop'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T6ZZtt = TxName('T6ZZtt')
T6ZZtt.on.checked ="AL"
#T6ZZtt.off.checked =
T6ZZtt.on.constraint ="[[['Z'],['t']],[['Z'],['t']]]"
#T6ZZtt.off.constraint =
T6ZZtt.on.condition ="None"
#T6ZZtt.off.condition =
T6ZZtt.on.fuzzycondition ="None"
#T6ZZtt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T6ZZttD180 = T6ZZtt.addMassPlane(motherMass = x, interMass = y + 180.0, lspMass = y)
#----limit source----
T6ZZttD180.obsUpperLimit.setSource( "orig/T6ZZttD180.txt", "txt" )
T6ZZttD180.obsUpperLimit.unit = 'fb'
#T6ZZttD180.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T6ZZttD180.obsExclusion.setSource( "orig/exclusion_T6ZZttD180.txt", "svg" )
T6ZZttD180.obsExclusionM1.setSource( "orig/exclusionm1_T6ZZttD180.txt", "svg" )
T6ZZttD180.obsExclusionP1.setSource( "orig/exclusionp1_T6ZZttD180.txt", "svg" )
#T6ZZttD180.expExclusion.setSource( path, type, object = None, index = None )
#T6ZZttD180.expExclusionM1.setSource( path, type, object = None, index = None )
#T6ZZttD180.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6ZZttD180.dataUrl =
#T6ZZttD180.histoDataUrl =
#T6ZZttD180.exclusionDataUrl =
#----figure----
T6ZZttD180.figure = 'Figure 10'
T6ZZttD180.figureUrl ='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-025/figaux_10.png'
#----limit url settings ----
#T6ZZttD180.obsUpperLimit.dataUrl =
#T6ZZttD180.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6ZZttD180.obsExclusion.dataUrl =
#T6ZZttD180.obsExclusionM1.dataUrl =
#T6ZZttD180.obsExclusionP1.dataUrl =
#T6ZZttD180.expExclusion.dataUrl =
#T6ZZttD180.expExclusionM1.dataUrl =
#T6ZZttD180.expExclusionP1.dataUrl =

databaseCreator.create()

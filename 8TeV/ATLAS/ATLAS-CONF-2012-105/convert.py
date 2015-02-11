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
info = MetaInfo('ATLAS-CONF-2012-105')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '5.8'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-105/'
#info.superseded_by = 
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS SS'
#info.supersedes = 
info.implemented_by = 'MT'

#+++++++ next txName block ++++++++++++++
T1tttt = TxName('T1tttt')
T1tttt.on.checked ="AL"
#T1tttt.off.checked =
T1tttt.on.constraint ="[[['t+','t-']],[['t+','t-']]]"
#T1tttt.off.constraint =
T1tttt.on.condition ="None"
#T1tttt.off.condition =
T1tttt.on.fuzzycondition ="None"
#T1tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tttt.obsUpperLimit.setSource( 'orig/T1tttt.txt', 'txt', )
T1tttt.obsUpperLimit.unit = 'fb'
#T1tttt.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
#T1tttt.obsExclusion.setSource( path, type, object = None, index = None )
#T1tttt.obsExclusionM1.setSource( path, type, object = None, index = None )
#T1tttt.obsExclusionP1.setSource( path, type, object = None, index = None )
#T1tttt.expExclusion.setSource( path, type, object = None, index = None )
#T1tttt.expExclusionM1.setSource( path, type, object = None, index = None )
#T1tttt.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T1tttt.dataUrl =
#T1tttt.histoDataUrl =
#T1tttt.exclusionDataUrl =
#----figure----
T1tttt.figure = 'Fig. 3'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2012-105/fig_03.png'
#----limit url settings ----
#T1tttt.obsUpperLimit.dataUrl =
#T1tttt.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T1tttt.obsExclusion.dataUrl =
#T1tttt.obsExclusionM1.dataUrl =
#T1tttt.obsExclusionP1.dataUrl =
#T1tttt.expExclusion.dataUrl =
#T1tttt.expExclusionM1.dataUrl =
#T1tttt.expExclusionP1.dataUrl =

databaseCreator.create()


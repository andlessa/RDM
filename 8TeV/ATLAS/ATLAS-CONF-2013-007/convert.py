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
info = MetaInfo('ATLAS-CONF-2013-007')
info.comment = 'A technical problem has been found in the pseudo-experiments used to make Table 4 in the conference note of March 1.'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.7'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/'
info.superseded_by = 'ATLAS-SUSY-2013-09'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS SS+b'
#info.supersedes = 
info.implemented_by = 'MT'

#+++++++ next txName block ++++++++++++++
T6ttWW = TxName('T6ttWW')
T6ttWW.on.checked ='VM'
#T6ttWW.off.checked =
T6ttWW.on.constraint ="[[['t+'],['W-']],[['t+'],['W-']]]+[[['t-'],['W+']],[['t-'],['W+']]]+[[['t+'],['W-']],[['t-'],['W+']]]"
T6ttWW.off.constraint = 'not yet assigned'
T6ttWW.on.condition ="None"
T6ttWW.off.condition = 'not yet assigned'
T6ttWW.on.fuzzycondition ="None"
T6ttWW.off.fuzzycondition = 'not yet assigned'

#+++++++ next mass plane block ++++++++++++++
T6ttWWLSP060 = T6ttWW.addMassPlane(motherMass = x, interMass = y, lspMass = 60.0)
#----limit source----
T6ttWWLSP060.obsUpperLimit.setSource( 'orig/T6ttWWLSP060.txt', 'txt' )
T6ttWWLSP060.obsUpperLimit.unit = 'fb'
#T6ttWWLSP060.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T6ttWWLSP060.obsExclusion.setSource( 'orig/exclusion_T6ttWWLSP060.txt', 'svg' )
T6ttWWLSP060.obsExclusionM1.setSource( 'orig/exclusionm1_T6ttWWLSP060.txt', 'svg' )
T6ttWWLSP060.obsExclusionP1.setSource( 'orig/exclusionp1_T6ttWWLSP060.txt', 'svg' )
#T6ttWWLSP060.expExclusion.setSource( path, type, object = None, index = None )
#T6ttWWLSP060.expExclusionM1.setSource( path, type, object = None, index = None )
#T6ttWWLSP060.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6ttWWLSP060.dataUrl =
#T6ttWWLSP060.histoDataUrl =
#T6ttWWLSP060.exclusionDataUrl =
#----figure----
T6ttWWLSP060.figure = 'Fig. 15a'
T6ttWWLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_15a.png'
#----limit url settings ----
#T6ttWWLSP060.obsUpperLimit.dataUrl =
#T6ttWWLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6ttWWLSP060.obsExclusion.dataUrl =
#T6ttWWLSP060.obsExclusionM1.dataUrl =
#T6ttWWLSP060.obsExclusionP1.dataUrl =
#T6ttWWLSP060.expExclusion.dataUrl =
#T6ttWWLSP060.expExclusionM1.dataUrl =
#T6ttWWLSP060.expExclusionP1.dataUrl =

#+++++++ next mass plane block ++++++++++++++
T6ttWWx200 = T6ttWW.addMassPlane(motherMass = x, interMass = y * 2.0, lspMass = y)
#----limit source----
T6ttWWx200.obsUpperLimit.setSource( 'orig/T6ttWWx200.txt', 'txt' )
T6ttWWx200.obsUpperLimit.unit = 'fb'
#T6ttWWx200.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T6ttWWx200.obsExclusion.setSource( 'orig/exclusion_T6ttWWx200.txt', 'svg' )
T6ttWWx200.obsExclusionM1.setSource( 'orig/exclusionm1_T6ttWWx200.txt', 'svg' )
T6ttWWx200.obsExclusionP1.setSource( 'orig/exclusionp1_T6ttWWx200.txt', 'svg' )
#T6ttWWx200.expExclusion.setSource( path, type, object = None, index = None )
#T6ttWWx200.expExclusionM1.setSource( path, type, object = None, index = None )
#T6ttWWx200.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T6ttWWx200.dataUrl =
#T6ttWWx200.histoDataUrl =
#T6ttWWx200.exclusionDataUrl =
#----figure----
T6ttWWx200.figure = 'Fig. 15b'
T6ttWWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_15b.png'
#----limit url settings ----
#T6ttWWx200.obsUpperLimit.dataUrl =
#T6ttWWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T6ttWWx200.obsExclusion.dataUrl =
#T6ttWWx200.obsExclusionM1.dataUrl =
#T6ttWWx200.obsExclusionP1.dataUrl =
#T6ttWWx200.expExclusion.dataUrl =
#T6ttWWx200.expExclusionM1.dataUrl =
#T6ttWWx200.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1tttt = TxName('T1tttt')
T1tttt.on.checked ="VM"
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
T1tttt.obsUpperLimit.setSource( 'orig/T1tttt.txt', 'txt' )
T1tttt.obsUpperLimit.unit = 'fb'
#T1tttt.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T1tttt.obsExclusion.setSource( 'orig/exclusion_T1tttt.txt', 'svg' )
T1tttt.obsExclusionM1.setSource( 'orig/exclusionm1_T1tttt.txt', 'svg' )
T1tttt.obsExclusionP1.setSource( 'orig/exclusionp1_T1tttt.txt', 'svg' )
#T1tttt.expExclusion.setSource( path, type, object = None, index = None )
#T1tttt.expExclusionM1.setSource( path, type, object = None, index = None )
#T1tttt.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T1tttt.dataUrl =
#T1tttt.histoDataUrl =
#T1tttt.exclusionDataUrl =
#----figure----
T1tttt.figure = 'Fig. 8a'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_08a.png'
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

#+++++++ next txName block ++++++++++++++
T5tttt = TxName('T5tttt')
T5tttt.on.checked ="VM"
#T5tttt.off.checked =
T5tttt.on.constraint ="[[['t+'],['t-']],[['t+'],['t-']]]+[[['t-'],['t+']],[['t-'],['t+']]]+[[['t+'],['t-']],[['t-'],['t+']]]"
#T5tttt.off.constraint =
T5tttt.on.condition ="None"
#T5tttt.off.condition =
T5tttt.on.fuzzycondition ="None"
#T5tttt.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T5ttttLSP060 = T5tttt.addMassPlane(motherMass = x, interMass = y, lspMass = 60.0)
#----limit source----
T5ttttLSP060.obsUpperLimit.setSource( 'orig/T5ttttLSP060.txt', 'txt' )
T5ttttLSP060.obsUpperLimit.unit = 'fb'
#T5ttttLSP060.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T5ttttLSP060.obsExclusion.setSource( 'orig/exclusion_T5ttttLSP060.txt', 'svg' )
T5ttttLSP060.obsExclusionM1.setSource( 'orig/exclusionm1_T5ttttLSP060.txt', 'svg' )
T5ttttLSP060.obsExclusionP1.setSource( 'orig/exclusionp1_T5ttttLSP060.txt', 'svg' )
#T5ttttLSP060.expExclusion.setSource( path, type, object = None, index = None )
#T5ttttLSP060.expExclusionM1.setSource( path, type, object = None, index = None )
#T5ttttLSP060.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T5ttttLSP060.dataUrl =
#T5ttttLSP060.histoDataUrl =
#T5ttttLSP060.exclusionDataUrl =
#----figure----
T5ttttLSP060.figure = 'Fig. 9'
T5ttttLSP060.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_09.png'
#----limit url settings ----
#T5ttttLSP060.obsUpperLimit.dataUrl =
#T5ttttLSP060.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T5ttttLSP060.obsExclusion.dataUrl =
#T5ttttLSP060.obsExclusionM1.dataUrl =
#T5ttttLSP060.obsExclusionP1.dataUrl =
#T5ttttLSP060.expExclusion.dataUrl =
#T5ttttLSP060.expExclusionM1.dataUrl =
#T5ttttLSP060.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T1tbtb = TxName('T1tbtb')
T1tbtb.on.checked ="VM"
#T1tbtb.off.checked =
T1tbtb.on.constraint ="[[['t','b']],[['t','b']]]"
#T1tbtb.off.constraint =
T1tbtb.on.condition ="None"
#T1tbtb.off.condition =
T1tbtb.on.fuzzycondition ="None"
#T1tbtb.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
T1tbtb = T1tbtb.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
T1tbtb.obsUpperLimit.setSource( 'orig/T1tbtb.txt', 'txt' )
T1tbtb.obsUpperLimit.unit = 'fb'
#T1tbtb.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T1tbtb.obsExclusion.setSource( 'orig/exclusion_T1tbtb.txt', 'svg' )
T1tbtb.obsExclusionM1.setSource( 'orig/exclusionm1_T1tbtb.txt', 'svg' )
T1tbtb.obsExclusionP1.setSource( 'orig/exclusionp1_T1tbtb.txt', 'svg' )
#T1tbtb.expExclusion.setSource( path, type, object = None, index = None )
#T1tbtb.expExclusionM1.setSource( path, type, object = None, index = None )
#T1tbtb.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T1tbtb.dataUrl =
#T1tbtb.histoDataUrl =
#T1tbtb.exclusionDataUrl =
#----figure----
T1tbtb.figure = 'Fig. 11'
T1tbtb.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_11.png'
#----limit url settings ----
#T1tbtb.obsUpperLimit.dataUrl =
#T1tbtb.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T1tbtb.obsExclusion.dataUrl =
#T1tbtb.obsExclusionM1.dataUrl =
#T1tbtb.obsExclusionP1.dataUrl =
#T1tbtb.expExclusion.dataUrl =
#T1tbtb.expExclusionM1.dataUrl =
#T1tbtb.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++
T5WW = TxName('T5WW')
T5WW.on.checked ="VM"
#T5WW.off.checked =
T5WW.on.constraint ="[[['jet','jet'],['W']],[['jet','jet'],['W']]]"
T5WW.off.constraint = 'not yet assigned'
T5WW.on.condition ="None"
T5WW.off.condition = 'not yet assigned'
T5WW.on.fuzzycondition ="None"
T5WW.off.fuzzycondition = 'not yet assigned'

#+++++++ next mass plane block ++++++++++++++
T5WWx200 = T5WW.addMassPlane(motherMass = x, interMass = y * 2.0, lspMass = y)
#----limit source----
T5WWx200.obsUpperLimit.setSource( 'orig/T5WWx200.txt', 'txt' )
T5WWx200.obsUpperLimit.unit = 'fb'
#T5WWx200.expUpperLimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T5WWx200.obsExclusion.setSource( 'orig/exclusion_T5WWx200.txt', 'svg' )
T5WWx200.obsExclusionM1.setSource( 'orig/exclusionm1_T5WWx200.txt', 'svg' )
T5WWx200.obsExclusionP1.setSource( 'orig/exclusionp1_T5WWx200.txt', 'svg' )
#T5WWx200.expExclusion.setSource( path, type, object = None, index = None )
#T5WWx200.expExclusionM1.setSource( path, type, object = None, index = None )
#T5WWx200.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T5WWx200.dataUrl =
#T5WWx200.histoDataUrl =
#T5WWx200.exclusionDataUrl =
#----figure----
T5WWx200.figure = 'Fig. 13'
T5WWx200.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-007/fig_13.png'
#----limit url settings ----
#T5WWx200.obsUpperLimit.dataUrl =
#T5WWx200.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T5WWx200.obsExclusion.dataUrl =
#T5WWx200.obsExclusionM1.dataUrl =
#T5WWx200.obsExclusionP1.dataUrl =
#T5WWx200.expExclusion.dataUrl =
#T5WWx200.expExclusionM1.dataUrl =
#T5WWx200.expExclusionP1.dataUrl =

databaseCreator.create()
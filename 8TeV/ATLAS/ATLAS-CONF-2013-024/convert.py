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
info = MetaInfoInput('ATLAS-CONF-2013-024')
info.comment = 'will be superseded by SUSY_2013_16'
info.sqrts = '8.0'
info.private = False
info.lumi = '21.0'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-024/'
#info.superseded_by = 
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS hadronic stop'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
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
T2tt.obsUpperLimit.setSource( "orig/fig3_aux_ATLAS-CONF-2013-024.txt", 'txt')
#T2tt.expUpperlimit.setSource( path, type, object = None, index = None )
#----exclusion source----
T2tt.obsExclusion.setSource( "orig/exclusion_T2tt.txt", 'txt')
#T2tt.obsExclusionM1.setSource( path, type, object = None, index = None )
#T2tt.obsExclusionP1.setSource( path, type, object = None, index = None )
#T2tt.expExclusion.setSource( path, type, object = None, index = None )
#T2tt.expExclusionM1.setSource( path, type, object = None, index = None )
#T2tt.expExclusionP1.setSource( path, type, object = None, index = None )
#----global url settings ----
#T2tt.dataUrl =
#T2tt.histoDataUrl =
#T2tt.exclusionDataUrl =
#----figure----
T2tt.figure = 'Fig.(aux) 3'
T2tt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-024/figaux_03.png'
#----limit url settings ----
#T2tt.obsUpperLimit.dataUrl =
#T2tt.expUpperLimit.dataUrl =
#----exclusion url settings ----
#T2tt.obsExclusion.dataUrl =
#T2tt.obsExclusionM1.dataUrl =
#T2tt.obsExclusionP1.dataUrl =
#T2tt.expExclusion.dataUrl =
#T2tt.expExclusionM1.dataUrl =
#T2tt.expExclusionP1.dataUrl =

databaseCreator.create()

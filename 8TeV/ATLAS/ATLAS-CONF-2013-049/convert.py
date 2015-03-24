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
info = MetaInfoInput('ATLAS-CONF-2013-049')
#info.comment = 
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
#info.publication = 
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-049/ https://cds.cern.ch/record/1547565'
info.superseded_by = 'ATLAS-SUSY-2013-11'
#info.arxiv = 
#info.contact = 
info.prettyname = 'ATLAS OS e/\mu'
#info.supersedes = 

#+++++++ next txName block ++++++++++++++
TSlepSlep = TxNameInput('TSlepSlep')
TSlepSlep.on.checked ="VM"
#TSlepSlep.off.checked =
TSlepSlep.on.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
#TSlepSlep.off.constraint =
TSlepSlep.on.condition ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
#TSlepSlep.off.condition =
TSlepSlep.on.fuzzycondition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
#TSlepSlep.off.fuzzycondition =

#+++++++ next mass plane block ++++++++++++++
TSlepSlep = TSlepSlep.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TSlepSlep.obsUpperLimit.setSource( "orig/TSlepSlep.txt", "txt", objectName = None, index = None )
TSlepSlep.obsUpperLimit.unit = 'fb'
#TSlepSlep.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TSlepSlep.obsExclusion.setSource( "orig/TSlepSlep_exc.dat", "txt", objectName = None, index = None )
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
TSlepSlep.figure = 'Fig.(aux) 16a'
TSlepSlep.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-049/fig_08c.png'
#----limit url settings ----
TSlepSlep.obsUpperLimit.dataUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-049/figaux_16a_PRELIMINARY.data'
"""
TSlepSlep.expUpperLimit.dataUrl =
#----exclusion url settings ----
TSlepSlep.obsExclusion.dataUrl =
TSlepSlep.obsExclusionM1.dataUrl =
TSlepSlep.obsExclusionP1.dataUrl =
TSlepSlep.expExclusion.dataUrl =
TSlepSlep.expExclusionM1.dataUrl =
TSlepSlep.expExclusionP1.dataUrl =
"""

databaseCreator.create()

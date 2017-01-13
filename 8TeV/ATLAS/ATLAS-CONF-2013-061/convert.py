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
info = MetaInfoInput('ATLAS-CONF-2013-061')
info.comment = 'Superseeded by ATLAS-SUSY-2013-18 but publication has fewer topologies, e.g. T1btbt result will be lost'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.1'
info.publication = 'http://cds.cern.ch/record/1557778'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-061/'
#info.supersededBy = 'ATLAS-SUSY-2013-18'
#info.arxiv =
#info.contact =
info.prettyName = 'ATLAS three b-jets'
#info.supersedes =

#+++++++ next txName block ++++++++++++++
T1bbbb = TxNameInput('T1bbbb')
T1bbbb.on.checked ="VM"
T1bbbb.on.constraint = "[[['b','b']],[['b','b']]]"
T1bbbb.on.conditionDescription ="None"
T1bbbb.on.condition ="None"

T1bbbb = T1bbbb.addMassPlane(motherMass = x, lspMass = y)
T1bbbb.obsUpperLimit.setSource( 'orig/Fig12a.txt', 'txt' )
T1bbbb.obsUpperLimit.unit = 'fb'
T1bbbb.obsExclusion.setSource( 'orig/exclusion_T1bbbb.txt', 'txt' )
T1bbbb.figure = 'Fig. 12a'
T1bbbb.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-061/fig_12a.png'

#+++++++ next txName block ++++++++++++++
T1tttt = TxNameInput('T1tttt')
T1tttt.on.checked ="VM"
T1tttt.on.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.on.conditionDescription ="None"
T1tttt.on.condition ="None"

T1tttt = T1tttt.addMassPlane(motherMass = x, lspMass = y)
T1tttt.obsUpperLimit.setSource( 'orig/Fig12b.txt', 'txt' )
T1tttt.obsUpperLimit.unit = 'fb'
T1tttt.obsExclusion.setSource( 'orig/exclusion_T1tttt.txt', 'txt' )
T1tttt.figure = 'Fig. 12b'
T1tttt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-061/fig_12b.png'

#+++++++ next txName block ++++++++++++++
T1btbt = TxNameInput('T1btbt')
T1btbt.on.checked ="VM"
T1btbt.on.constraint = "[[['t','b']],[['t','b']]]"
T1btbt.on.conditionDescription ="None"
T1btbt.on.condition ="None"

T1btbt = T1btbt.addMassPlane(motherMass = x, lspMass = y)
T1btbt.obsUpperLimit.setSource( 'orig/Fig12c.txt', 'txt' )
T1btbt.obsUpperLimit.unit = 'fb'
T1btbt.obsExclusion.setSource( 'orig/exclusion_T1tbtb.txt', 'txt' )
T1btbt.figure = 'Fig. 12c'
T1btbt.figureUrl = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-061/fig_12c.png'

databaseCreator.create()

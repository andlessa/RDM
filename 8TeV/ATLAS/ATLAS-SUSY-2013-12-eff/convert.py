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
info = MetaInfoInput('ATLAS-SUSY-2013-12')
info.comment = 'They give Acceptance and Efficiency, not multiplied.'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP04(2014)169'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-12/'
#info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1402.7029'
#info.contact =
info.prettyName = 'ATLAS trilepton inc Wh decay'
info.supersedes = 'ATLAS-CONF-2013-035; CONF-2012-154'


#+++++++ next txName block ++++++++++++++
TChiChipmStauL = TxNameInput('TChiChipmStauL')
#TChiChipmStauL.on.checked =
#TChiChipmStauL.off.checked =
TChiChipmStauL.on.constraint ="2.*([[['nu'],['ta']],[['ta+'],['ta-']]] + [[['ta'],['nu']],[['ta+'],['ta-']]]+[[['nu'],['ta']],[['ta-'],['ta+']]] + [[['ta'],['nu']],[['ta-'],['ta+']]])"
#TChiChipmStauL.off.constraint =
TChiChipmStauL.on.conditionDescription ="[[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['ta'],['nu']],[['ta+'],['ta-']]],[[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['nu'],['ta']],[['ta-'],['ta+']]], [[['nu'],['ta']],[['ta+'],['ta-']]] ~ [[['ta'],['nu']],[['ta-'],['ta+']]]"
#TChiChipmStauL.off.conditionDescription =
TChiChipmStauL.on.condition ="Csim([[['nu'],['ta']],[['ta+'],['ta-']]],[[['ta'],['nu']],[['ta+'],['ta-']]],[[['nu'],['ta']],[['ta-'],['ta+']]],[[['ta'],['nu']],[['ta-'],['ta+']]])"
#TChiChipmStauL.off.condition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmStauL050 = TChiChipmStauL.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)


TChiChipmStauL050.efficiencyMap.setSource("orig/SR2taua_stauL.txt", "txt",  objectName = "orig/SR2taua_stauL.txt", index = None, dataset="SR2tauaStauL" )
TChiChipmStauL050.efficiencyMap.setStatistics ( observedN=6, expectedBG=6.9, bgError=0.8 )  #check asymmetric error
TChiChipmStauL050.obsExclusion.setSource( "orig/exc_stauL_obs.txt", "txt", objectName = None, index = None )
TChiChipmStauL050.expExclusion.setSource( "orig/exc_stauL_expected.txt", "txt", objectName = None, index = None )
TChiChipmStauL050.obsExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d22"
TChiChipmStauL050.expExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d23"

databaseCreator.create()









#+++++++ next txName block ++++++++++++++
TChiChipmSlepL = TxNameInput('TChiChipmSlepL')
#TChiChipmSlepL.on.checked =
#TChiChipmSlepL.off.checked =
TChiChipmSlepL.on.constraint ="2.*([[['L'],['L']],[['L'],['nu']]] + [[['L'],['L']],[['nu'],['L']]])"
#TChiChipmSlepL.off.constraint =
TChiChipmSlepL.on.conditionDescription ="[[['L'],['L']],[['L'],['nu']]] ~ [[['L'],['L']],[['nu'],['L']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['ta'],['ta']],[['nu'],['L']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['ta'],['ta']],[['L'],['nu']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['ta']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['ta'],['nu']]],[[['L'],['L']],[['nu'],['L']]] > 2.7*[[['e'],['e']],[['nu'],['L']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['e'],['e']],[['L'],['nu']]], [[['L'],['L']],[['nu'],['L']]] > 2.7*[[['L'],['L']],[['nu'],['e']]], [[['L'],['L']],[['L'],['nu']]] > 2.7*[[['L'],['L']],[['e'],['nu']]]"
#TChiChipmSlepL.off.conditionDescription =
TChiChipmSlepL.on.condition ="Csim([[['L'],['L']],[['L'],['nu']]],[[['L'],['L']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['ta'],['ta']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['ta'],['ta']],[['L'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['ta']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['ta'],['nu']]]);Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['e'],['e']],[['nu'],['L']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['e'],['e']],[['L'],['nu']]]); Cgtr([[['L'],['L']],[['nu'],['L']]],3.*[[['L'],['L']],[['nu'],['e']]]); Cgtr([[['L'],['L']],[['L'],['nu']]],3.*[[['L'],['L']],[['e'],['nu']]])"
#TChiChipmSlepL.off.condition =

#+++++++ next mass plane block ++++++++++++++
TChiChipmSlepL050 = TChiChipmSlepL.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)

TChiChipmSlepL050.efficiencyMap.setSource("orig/SR0taua_slepL.txt", "txt",  objectName = "orig/SR0taua_slepL.txt", index = None, dataset="SR0tauaSlepL-bin20" )
TChiChipmSlepL050.efficiencyMap.setStatistics ( observedN=0, expectedBG=0.29, bgError=0.17 )  #check asymmetric error
TChiChipmSlepL050.obsExclusion.setSource( "orig/exc_slepL_obs.txt", "txt", objectName = None, index = None )
TChiChipmSlepL050.expExclusion.setSource( "orig/exc_slepL_expected.txt", "txt", objectName = None, index = None )
TChiChipmSlepL050.obsExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d18"
TChiChipmSlepL050.expExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d19"
databaseCreator.create(True)




'''

#+++++++ next txName block ++++++++++++++
TChiWH = TxNameInput('TChiWH')
#TChiWH.on.checked =
#TChiWH.off.checked =
TChiWH.on.constraint ="[[['W']],[['higgs']]]"
#TChiWH.off.constraint =
TChiWH.on.conditionDescription ="None"
#TChiWH.off.conditionDescription =
TChiWH.on.condition ="None"
#TChiWH.off.condition =
#----limit url settings ----
#T1bbbb.expUpperLimit.dataUrl =

#+++++++ next mass plane block ++++++++++++++
TChiWH = TChiWH.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWH.efficiencyMap.setSource("orig/SR2taub_WH.txt", "txt",  objectName = "orig/SR2taub_WH.txt", index = None, dataset="SR2taubWH" )
TChiWH.efficiencyMap.setStatistics ( observedN=5, expectedBG=7.2, bgError=0.7 )  #check asymmetric error



#----global url settings ----
#TChiWH.dataUrl =
#TChiWH.histoDataUrl =
#TChiWH.exclusionDataUrl =
#----figure----
#----limit url settings ----
#TChiWH.obsUpperLimit.dataUrl =
#TChiWH.expUpperLimit.dataUrl =
#----exclusion url settings ----
#TChiWH.obsExclusionM1.dataUrl =
#TChiWH.obsExclusionP1.dataUrl =
#TChiWH.expExclusionM1.dataUrl =
#TChiWH.expExclusionP1.dataUrl =

#+++++++ next txName block ++++++++++++++

TChiWZ = TxNameInput('TChiWZ')
#TChiWZ.on.checked =
#TChiWZ.off.checked =
TChiWZ.on.constraint ="[[['W']],[['Z']]]"
TChiWZ.off.constraint ="71.*([[['mu+','mu-']],[['l','nu']]] + [[['e+','e-']],[['l','nu']]])"
TChiWZ.on.conditionDescription ="None"
TChiWZ.off.conditionDescription ="[[['mu+','mu-']],[['l','nu']]] > [[['e+','e-']],[['l','nu']]]"
TChiWZ.on.condition ="None"
TChiWZ.off.condition ="Cgtr([[['mu+','mu-']],[['l','nu']]],[[['e+','e-']],[['l','nu']]])"
TChiWZ = TChiWZ.addMassPlane(motherMass = x, lspMass = y)

#----limit source----
TChiWZ.efficiencyMap.setSource("orig/SR0taua_WZ.txt", "txt",  objectName = "orig/SR0taua_WH.txt", index = None, dataset="SR0tauaWZ" )
TChiWZ.efficiencyMap.setStatistics ( observedN=3, expectedBG=4.6, bgError=1.5 )  #check asymmetric error






#+++++++ next txName block ++++++++++++++
TChiWZ = TxNameInput('TChiWZ')
#TChiWZ.on.checked =
#TChiWZ.off.checked =
TChiWZ.on.constraint ="[[['W']],[['Z']]]"
TChiWZ.off.constraint ="71.*([[['mu+','mu-']],[['l','nu']]] + [[['e+','e-']],[['l','nu']]])"
TChiWZ.on.conditionDescription ="None"
TChiWZ.off.conditionDescription ="[[['mu+','mu-']],[['l','nu']]] > [[['e+','e-']],[['l','nu']]]"
TChiWZ.on.condition ="None"
TChiWZ.off.condition ="Cgtr([[['mu+','mu-']],[['l','nu']]],[[['e+','e-']],[['l','nu']]])"

#+++++++ next mass plane block ++++++++++++++
TChiWZ = TChiWZ.addMassPlane(motherMass = x, lspMass = y)
#----limit source----
TChiWZ.obsUpperLimit.setSource( "orig/TChiWZ.txt", "txt", objectName = None, index = None )
#TChiWZ.expUpperlimit.setSource( path, filetype, objectName = None, index = None )
#----exclusion source----
TChiWZ.obsExclusion.setSource( "orig/exc_tchiwz_obs.txt", "txt", objectName = None, index = None )
#TChiWZ.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWZ.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
TChiWZ.expExclusion.setSource( "orig/exc_tchiwz_expected.txt", "txt", objectName = None, index = None )
#TChiWZ.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#TChiWZ.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
#TChiWZ.dataUrl =
#TChiWZ.histoDataUrl =
#TChiWZ.exclusionDataUrl =
#----figure----
TChiWZ.figure = "fig 7b"
TChiWZ.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-12/fig_07b.png"
#----limit url settings ----
#TChiWZ.obsUpperLimit.dataUrl =
#TChiWZ.expUpperLimit.dataUrl =
#----exclusion url settings ----
TChiWZ.obsExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d20"
#TChiWZ.obsExclusionM1.dataUrl =
#TChiWZ.obsExclusionP1.dataUrl =
TChiWZ.expExclusion.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1282905/d21"
#TChiWZ.expExclusionM1.dataUrl =
#TChiWZ.expExclusionP1.dataUrl =
'''


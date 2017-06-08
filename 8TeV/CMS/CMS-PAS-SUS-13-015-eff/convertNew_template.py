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
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
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
if args.smodelsPath:
    sys.path.append(os.path.abspath(args.smodelsPath))

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-PAS-SUS-13-015')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13015'
info.sqrts = 8
info.lumi = 19.4
info.private = False
info.publication ='http://cds.cern.ch/record/1635353/files/SUS-13-015-pas.pdf'
info.comment ='PAS so no arxiv publication - only cds.cern; whenever the error on the expected SM background is asymmetric for some signal regions, the largest value is used'


BEGIN_AUXILIARY_BLOCK
datasetShortStr = {
"pTmiss200_Nb1" : 'eff_baseline',
"pTmiss350_Nb1" : 'eff_baseline_2b',
"pTmiss200_Nb2" : 'eff_highMET',
"pTmiss350_Nb2" : 'eff_highMET_2b'
}
END_AUXILIARY_BLOCK


BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T2tt = dataset.addTxName('T2tt')
T2tt.constraint = "[[['t']],[['t']]]"
T2tt.conditionDescription ="None"
T2tt.condition = None
T2tt.massConstraint = None
T2tt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T2ttoff = dataset.addTxName('T2ttoff')
T2ttoff.constraint ="[[['W','b']],[['W','b']]]"
T2ttoff.conditionDescription =None
T2ttoff.condition = None
T2ttoff.massConstraint = [['dm <= 169.']]*2
T2ttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane([[x,y]]*2)
T2tt_1.figure = 'Fig. 11'
T2tt_1.figureUrl = $$
T2tt_1.addSource('obsExclusion','orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_obsExclOneTimesProspino')
T2tt_1.addSource('obsExclusionM1','orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino')
T2tt_1.addSource('obsExclusionP1','orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino')
T2tt_1.addSource('expExclusion','orig/CMS-SUS-13-015_from_cMacro.root', 'root',   objectName = 'combined_expExclOneTimesProspino')
T2tt_1.addSource('expExclusionM1','orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclMinusSysErrProspino')
T2tt_1.addSource('expExclusionP1','orig/CMS-SUS-13-015_from_cMacro.root', 'root', objectName = 'combined_obsExclPlusSysErrProspino')
T2tt_1.addSource('efficiencyMap','orig/$datasetShortStr$.root', 'root', objectName = '$datasetShortStr$')
T2tt_1.efficiencyMap.dataUrl = $$
T2ttoff.addMassPlane(T2tt_1)
END_BLOCK_TO_FILL

databaseCreator.create()

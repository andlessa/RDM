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
info = MetaInfoInput('CMS-SUS-13-007')
info.url ='https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13007'
info.sqrts = 8
info.lumi = 19.3
info.prettyName = 'e/\mu DP'
info.private = False
info.arxiv = 'http://arxiv.org/abs/arXiv:1311.4937'
info.contact ='Loukas Gouskos <loukas.gouskos@cern.ch>, Markus Stoye <Markus.Stoye@cern.ch>'
info.publication = 'http://www.sciencedirect.com/science/article/pii/S037026931400255X'
info.comment = 'Only two mass planes for T5tttt; implemented Delta Phi method'
info.implementedBy = 'Federico Ambrogi'


BEGIN_AUXILIARY_BLOCK
datasetShortStr = {
"mu250Nb2" : 'mu-250-sig-Nb2',
"mu250Nb3" : 'mu-250-sig-Nb3',
"mu350Nb2" : 'mu-350-sig-Nb2',
"mu350Nb3" : 'mu-350-sig-Nb3',
"mu450Nb2" : 'mu-450-sig-Nb2',
"mu450Nb3" : 'mu-450-sig-Nb3',
"el250Nb2" : 'el-250-sig-Nb2',
"el250Nb3" : 'el-250-sig-Nb3',
"el350Nb2" : 'el-350-sig-Nb2',
"el350Nb3" : 'el-350-sig-Nb3',
"el450Nb2" : 'el-450-sig-Nb2',
"el450Nb3" : 'el-450-sig-Nb3'
}
END_AUXILIARY_BLOCK

BEGIN_BLOCK_TO_FILL
#+++++++ dataset block ++++++++++++++
dataset = DataSetInput($datasetFolder$)
dataset.setInfo(dataType = 'efficiencyMap', dataId = $dataset$, observedN = $observedN$, expectedBG = $expectedBG$ , bgError = $bgError$)
#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.constraint = "[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription = None
T1tttt.condition = None
T1tttt.massConstraint = None
T1tttt.source = 'CMS'
#+++++++ next txName block ++++++++++++++
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.constraint ="[[['b','W','b','W']],[['b','W','b','W']]]"
T1ttttoff.conditionDescription = None
T1ttttoff.condition = None
T1ttttoff.massConstraint = [['dm <= 338.0']]*2
T1ttttoff.source = 'CMS'
#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane([[x,y]]*2)
T1tttt_1.figure = $$
T1tttt_1.figureUrl = $$
T1tttt_1.addSource('obsExclusion', 'orig/T1tttt_excl.txt', 'txt' )
T1tttt_1.addSource('efficiencyMap', 'orig/EffxAcc_Smoothed_DPhi_Paper_Dec2013.root', 'root', objectName = 'EffxAcc-ISR-T1tttt-EffxAcc-ISR-MG_$datasetShortStr$')
T1tttt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/edit/CMSPublic/EffxAcc?topicparent=CMSPublic.PhysicsResultsSUS13007;nowysiwyg=1'
T1ttttoff.addMassPlane(T1tttt_1)
END_BLOCK_TO_FILL

databaseCreator.create()

#!/usr/bin/env python3

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
    type = str )
argparser.add_argument ('-smodelsPath', '--smodelsPath',
    help = 'path to the package smodels_utils',\
    type = str )
argparser.add_argument ('-no', '--noUpdate',
    help = 'do not update the lastUpdate field.',\
    action= "store_true" )
argparser.add_argument ('-r', '--resetValidation',
    help = 'reset the validation flag',\
    action= "store_true" )

args = argparser.parse_args()

if args.noUpdate:
    os.environ["SMODELS_NOUPDATE"]="1"

if args.resetValidation:
    os.environ["SMODELS_RESETVALIDATION"]="1"

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
info = MetaInfoInput('CMS-EXO-13-006')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-13-006/index.html'
info.sqrts = 8
info.lumi = 18.8
info.prettyName ='hscp search'
info.private = False
info.arxiv = 'https://arxiv.org/abs/1502.02522'
info.contact ='Andre Lessa <lessa.a.p@gmail.com>; Jan Heisig <heisig@physik.rwth-aachen.de>; SModelS'
info.publication ='https://cds.cern.ch/record/1987723/files/arXiv:1502.02522.pdf'
info.comment ='Search for long-lived charged particles implemented in arXiv:1509.00473. For the topologies with mixed MET-HSCP branches, the MET branch is irrelevant and wildcards are used.'
info.supersedes =''

#++Define list of datasets++
datasetNames = ['c000','c100','c200','c300']
observedNs = [42,7,0,0]
expectedBGs = [44.,5.6,0.56,0.09]
bgErrors = [9.,1.1,0.11,0.02]
#SR Upper limits from arxiv:1502.02522 (Table 2). Note that the SR UL are given by obs_UL*eff (from the table)
obsUpperLimits = ['1.02*fb','0.45*fb','0.17*fb','0.16*fb']
#SR Expected Upper limits from arxiv:1502.02522 (Table 2). Note that the SR UL are given by exp_UL*eff (from the table)
expUpperLimits = ['1.09*fb','0.37*fb','0.22*fb','0.17*fb']


for i,name in enumerate(datasetNames):
#+++++++ dataset block ++++++++++++++
    dataset = DataSetInput(name)
    dataset.setInfo(dataType = 'efficiencyMap', dataId = name,
            observedN=observedNs[i], expectedBG=expectedBGs[i], bgError=bgErrors[i],
            upperLimit = obsUpperLimits[i], expectedUpperLimit = expUpperLimits[i])

    #+++++++ txnames ++++++++++++++++++++
    #+++++++ next txName block ++++++++++++++
    """
    HSCPM1 = dataset.addTxName('THSCPM1Disp')
    HSCPM1.checked =''
    HSCPM1.constraint = "[[],[]]"
    HSCPM1.condition =None
    HSCPM1.finalState = ['HSCP','HSCP']
    HSCPM1.massConstraints = None
    HSCPM1.dataUrl = None
    HSCPM1.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    #plane = HSCPM1.addMassPlane([[x],[x]])
    # plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/effmap_M1_stau_8TeV_mre'+name+'.dat'], dataFormats=['txt'])
    plane = HSCPM1.addMassPlane([[(x,y)],[(x,y)]])
    plane.setSources(dataLabels= ['efficiencyMap','obsExclusion'],
                    dataFiles=['orig/efficiencies_M1.txt','orig/exclusion_line.txt'], 
                    coordinates = [ { x: 0, y: 1, 'value': 2+i }, None ],
                    units = [ None, ('GeV', 'ns') ],
                    dataFormats=['txt','txt'])
    #+++++++ next txName block ++++++++++++++
    """
    HSCPM1b = dataset.addTxName('THSCPM1b')
    HSCPM1b.checked =''
    HSCPM1b.constraint = "[[],[]]"
    HSCPM1b.condition =None
    HSCPM1b.finalState = ['HSCP','HSCP']
    HSCPM1b.massConstraints = None
    HSCPM1b.dataUrl = None
    HSCPM1b.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    #plane = HSCPM1.addMassPlane([[x],[x]])
    # plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/effmap_M1_stau_8TeV_mre'+name+'.dat'], dataFormats=['txt'])
    plane = HSCPM1b.addMassPlane([[(x,y)],[(x,y)]])
    plane.setSources(dataLabels= ['efficiencyMap','obsExclusion'],
                    dataFiles=['orig/efficiencies_HSCPM1b.txt','orig/exclusion_line.txt'], 
                    coordinates = [ { x: 0, y: 1, 'value': 2+i }, None ],
                    units = [ None, ('GeV', 'ns') ],
                    dataFormats=['txt','txt'])
    HSCPM3 = dataset.addTxName('THSCPM3')
    HSCPM3.checked =''
    HSCPM3.constraint = "[[['*']],[['*']]]"  ##Here '*' represents any (single) even particle
    HSCPM3.condition =None
    HSCPM3.conditionDescription =None
    HSCPM3.finalState = ['HSCP','HSCP']
    HSCPM3.massConstraints = None
    HSCPM3.dataUrl = None
    HSCPM3.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM3.addMassPlane([[(x,y),z],[(x,y),z]])
    plane.setSources(dataLabels= ['efficiencyMap'],
            dataFiles=['orig/efficiencies_HSCPM3.txt'], dataFormats=['txt'])
    #+++++++ next txName block ++++++++++++++
    """
    HSCPM5 = dataset.addTxName('THSCPM5')
    HSCPM5.checked =''
    HSCPM5.constraint = "[[['*'],['*']],[['*'],['*']]]" ##Here '*' represents any (single) even particle
    HSCPM5.condition =None
    HSCPM5.conditionDescription =None
    HSCPM5.finalState = ['HSCP','HSCP']
    HSCPM5.massConstraints = None
    HSCPM5.dataUrl = None
    HSCPM5.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM5.addMassPlane([[x,y,z]]*2)
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/eff_HSCPM5_'+name+'.txt'], dataFormats=['txt'])
    #+++++++ next txName block ++++++++++++++
    HSCPM7 = dataset.addTxName('THSCPM7')
    HSCPM7.checked =''
    HSCPM7.constraint = "[[['*']],[['*'],['*']]]" ##Here '*' represents any (single) even particle
    HSCPM7.condition =None
    HSCPM7.conditionDescription =None
    HSCPM7.finalState = ['HSCP','HSCP']
    HSCPM7.massConstraints = None
    HSCPM7.dataUrl = None
    HSCPM7.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM7.addMassPlane([[x,z],[x,y,z]])
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/eff_HSCPM7_'+name+'.txt'], dataFormats=['txt'])
    #+++++++ next txName block ++++++++++++++
    HSCPM8 = dataset.addTxName('THSCPM8')
    HSCPM8.checked =''
    HSCPM8.constraint = "[[['*','*']],[['*','*']]]" ##Here '*','*' represents any pair of even particles
    HSCPM8.condition =None
    HSCPM8.conditionDescription =None
    HSCPM8.finalState = ['HSCP','HSCP']
    HSCPM8.massConstraints = None
    HSCPM8.dataUrl = None
    HSCPM8.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM8.addMassPlane([[x,y],[x,y]])
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/eff_HSCPM8_'+name+'.txt'], dataFormats=['txt'])
    """
    #+++++++ next txName block ++++++++++++++
    HSCPM2 = dataset.addTxName('THSCPM2b')
    HSCPM2.checked =''
    HSCPM2.constraint = "[[*],[]]" ##Here [*] represents one branch with any list of vertices
    HSCPM2.condition =None
    HSCPM2.conditionDescription =None
    HSCPM2.finalState = ['MET','HSCP']
    HSCPM2.massConstraints = None
    HSCPM2.dataUrl = None
    HSCPM2.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM2.addMassPlane([['*'],[(x,y)]]) ##Here ['*'] represents a mass array with any length
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/efficiencies_HSCPM2.txt'], dataFormats=['txt'])
    #+++++++ next txName block ++++++++++++++
    HSCPM4 = dataset.addTxName('THSCPM4')
    HSCPM4.checked =''
    HSCPM4.constraint = "[[*],[['*']]]" ##Here [*] represents one branch with any list of vertices
    HSCPM4.condition =None
    HSCPM4.conditionDescription =None
    HSCPM4.finalState = ['MET','HSCP']
    HSCPM4.massConstraints = None
    HSCPM4.dataUrl = None
    HSCPM4.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM4.addMassPlane([['*'],[(x,y),z]]) ##Here ['*'] represents a mass array with any length
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/efficiencies_HSCPM4.txt'], dataFormats=['txt'])
    """
    #+++++++ next txName block ++++++++++++++
    HSCPM6 = dataset.addTxName('THSCPM6')
    HSCPM6.checked =''
    HSCPM6.constraint = "[[*],[['*'],[ '*']]]" ##Here [*] represents one branch with any list of vertices
    HSCPM6.condition =None
    HSCPM6.conditionDescription =None
    HSCPM6.finalState = ['MET','HSCP']
    HSCPM6.massConstraints = None
    HSCPM6.dataUrl = None
    HSCPM6.source = 'SModelS'
    #+++++++ next mass plane block ++++++++++++++
    plane = HSCPM6.addMassPlane([['*'],[x,y,z]]) ##Here ['*'] represents a mass array with any length
    plane.setSources(dataLabels= ['efficiencyMap'],dataFiles=['orig/eff_HSCPM6_'+name+'.txt'], dataFormats=['txt'])
    """

databaseCreator.create()


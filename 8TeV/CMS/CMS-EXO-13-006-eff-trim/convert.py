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
    type = str, default = os.path.expanduser('~/smodels-utils') )
argparser.add_argument ('-smodelsPath', '--smodelsPath',
    help = 'path to the package smodels_utils',\
    type = str, default = os.path.expanduser('~/smodels') )
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

utilsPath = args.utilsPath
sys.path.append(os.path.abspath(os.path.expanduser(utilsPath)))
sys.path.append(os.path.abspath(os.path.expanduser(args.smodelsPath)))


from smodels_utils.dataPreparation.inputObjects import MetaInfoInput,DataSetInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.massPlaneObjects import x, y, z, w

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-EXO-13-006-trim')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/EXO-13-006/index.html'
info.sqrts = 8
info.lumi = 18.8
info.prettyName ='hscp search'
info.private = False
info.arxiv = 'https://arxiv.org/abs/1502.02522'
info.contact ='SModelS'
info.Leff_inner = 1e-3
info.Leff_outer = 7.0
info.publication ='https://cds.cern.ch/record/1987723/files/arXiv:1502.02522.pdf'
info.comment ='Search for long-lived charged particles implemented in arXiv:1509.00473. For the topologies with mixed MET-HSCP branches, the MET branch is irrelevant and wildcards are used. The topologies THSCPM1b and THSCPM2b refer to staus, while in 1509.00473 charginos were used. All topologies do not include intermediate BSM states in the production process. The THSCPM5, THSCPM6 and THSCPM7 topologies do not include width information'
info.supersedes =''
particlesFile = os.path.abspath('../../../databaseParticles.py')

#++Define list of datasets++
datasetNames = ['c000','c100','c200','c300']
observedNs = [42,7,0,0]
expectedBGs = [44.,5.6,0.56,0.09]
bgErrors = [9.,1.1,0.11,0.02]
#SR Upper limits from arxiv:1502.02522 (Table 2). Note that the SR UL are given by obs_UL*eff (from the table)
obsUpperLimits = ['1.02*fb','0.45*fb','0.17*fb','0.16*fb']
#SR Expected Upper limits from arxiv:1502.02522 (Table 2). Note that the SR UL are given by exp_UL*eff (from the table)
expUpperLimits = ['1.09*fb','0.37*fb','0.22*fb','0.17*fb']


#Txname data:
txnames = {
    'THSCPM1b' : {'constraint' : "[[],[]]", 'finalState' : ['HSCP','HSCP'], 'massPlane' : [[(x,w)]]*2,
                        'coordinates' : [{x: 0, w:1, 'value' : 2}]},
    'THSCPM2b' : {'constraint' : "[['*'],[]]", 'finalState' : ['MET','HSCP'], 'massPlane' : [['*'],[(x,w)]],
                        'coordinates' : [{x: 0, w:1, 'value' : 2}]},
    'THSCPM3' : {'constraint' : "[[['*']],[['*']]]", 'finalState' : ['HSCP','HSCP'], 'massPlane' : [[x,(y,w)]]*2,
                        'coordinates' : [{x: 0, y:1, w: 2, 'value' : 3}]},
    'THSCPM4' : {'constraint' : "[[*],[['*']]]", 'finalState' : ['MET','HSCP'], 'massPlane' : [['*'],[x,(y,w)]],
                        'coordinates' : [{x: 0, y:1, w: 2, 'value' : 3}]},
    'THSCPM5' : {'constraint' :"[[['*'],['*']],[['*'],['*']]]", 'finalState' : ['HSCP','HSCP'], 'massPlane' : [[x,y,z]]*2,
                        'coordinates' : [{x: 0, y:1, z: 2, 'value' : 4}]},
    'THSCPM6' : {'constraint' : "[[*],[['*'],[ '*']]]", 'finalState' : ['MET','HSCP'], 'massPlane' : [['*'],[x,y,z]],
                        'coordinates' : [{x: 0, y:1, z: 2, 'value' : 4}]},
   'THSCPM7' : {'constraint' :  "[[['*'],['*']],[['*']]]", 'finalState' : ['HSCP','HSCP'], 'massPlane' : [[x,y,z],[x,z]],
                        'coordinates' : [{x: 0, y:1, z: 2, 'value' : 4}]},
    'THSCPM8' : {'constraint' : "[[['*','*']],[['*','*']]]", 'finalState' : ['HSCP','HSCP'], 'massPlane' : [[x,(y,w)]]*2,
                        'coordinates' : [{x: 0, y:1, w: 2, 'value' : 3}]},
   'THSCPM9' : {'constraint' : "[[*],[['*','*']]]", 'finalState' : ['MET','HSCP'], 'massPlane' : [['*'],[x,(y,w)]],
                        'coordinates' : [{x: 0, y:1, w: 2, 'value' : 3}]}
}


for idataset,name in enumerate(datasetNames):
#+++++++ dataset block ++++++++++++++
    dataset = DataSetInput(name)
    dataset.setInfo(dataType = 'efficiencyMap', dataId = name,
            observedN=observedNs[idataset], expectedBG=expectedBGs[idataset], bgError=bgErrors[idataset],
            upperLimit = obsUpperLimits[idataset])

    #+++++++ txnames ++++++++++++++++++++
    for tx in txnames:
        #+++++++ next txName block ++++++++++++++
        Txname = dataset.addTxName(tx)
        Txname.checked =''
        Txname.constraint = txnames[tx]['constraint']
        Txname.condition =None
        Txname.finalState = txnames[tx]['finalState']
        Txname.massConstraints = None
        Txname.dataUrl = None
        Txname.source = 'SModelS'
        Txname.setParticlesFromFile(particlesFile)
        #+++++++ next mass plane block ++++++++++++++
        plane = Txname.addMassPlane(txnames[tx]['massPlane'])

        if not w  in txnames[tx]['coordinates'][0]:
            dataFile = 'orig/%s_efficiencyMaps_%s_noWidth.dat' %(tx,name) #Use maps without width info
        else:
            dataFile = 'orig/%s_efficiencyMaps_%s_trimmedwidth.dat' %(tx,name)
        plane.setSources(dataLabels= ['efficiencyMap'],
                    dataFiles=[dataFile],
                    coordinates = txnames[tx]['coordinates'],
                    dataFormats=['txt'])
        #++++++ add axes for validation (only for THSCPM1b) ++++
        if 'validation axes' in txnames[tx]:
            plane.axes = txnames[tx]['validation axes']

databaseCreator.create()

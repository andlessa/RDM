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
type = str)
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
help = 'path to the package smodels_utils',\
type = str)
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



#+++++++ Datasets info ++++++++++++++
datasetsInfo = [
{'dataId': 'SRA mCT250', 'dataType': 'efficiencyMap', 'observedN': '14', 'expectedUpperLimit': '0.517*fb', 'folder': 'data-cut2', 'expectedBG': '15.8', 'bgError': '2.8', 'upperLimit': '0.45*fb'},
{'dataId': 'SRA mCT200', 'dataType': 'efficiencyMap', 'observedN': '48', 'expectedUpperLimit': '0.914*fb', 'folder': 'data-cut1', 'expectedBG': '39.0', 'bgError': '6.0', 'upperLimit': '1.3*fb'},
{'dataId': 'SRB', 'dataType': 'efficiencyMap', 'observedN': '65', 'expectedUpperLimit': '1.31*fb', 'folder': 'data-cut5', 'expectedBG': '64.0', 'bgError': '10.0', 'upperLimit': '1.3*fb'},
{'dataId': 'SRA mCT150', 'dataType': 'efficiencyMap', 'observedN': '102', 'expectedUpperLimit': '1.63*fb', 'folder': 'data-cut0', 'expectedBG': '94.0', 'bgError': '13.0', 'upperLimit': '1.9*fb'},
{'dataId': 'SRA mCT300', 'dataType': 'efficiencyMap', 'observedN': '7', 'expectedUpperLimit': '0.309*fb', 'folder': 'data-cut3', 'expectedBG': '5.9', 'bgError': '1.1', 'upperLimit': '0.37*fb'},
{'dataId': 'SRA mCT350', 'dataType': 'efficiencyMap', 'observedN': '3', 'expectedUpperLimit': '0.235*fb', 'folder': 'data-cut4', 'expectedBG': '2.5', 'bgError': '0.6', 'upperLimit': '0.26*fb'}
]

#+++++++ Constraints info ++++++++++++++
constraintsDict = {
"T2gg" : "[[['jet']],[['jet']]]",
"T1" : "[[['jet','jet']],[['jet','jet']]]",
"T1bbbb" : "[[['b','b']],[['b','b']]]",
"T5btbt" : "[[['b'],['t']],[['b'],['t']]]",
"T1bbqq" : "[[['b','b']],[['jet','jet']]]",
"T5bbbt" : "[[['b'],['b']],[['b'],['t']]]",
"T1bbbt" : "[[['b','b']],[['b','t']]]",
"TGQbtq" : "[[['b','t']],[['jet']]]",
"TGQ" : "[[['jet']],[['jet','jet']]]",
"TGQqtt" : "[[['jet']],[['t+','t-']]]",
"T2tt" : "[[['t']],[['t']]]",
"T5tttt" : "[[['t+'],['t-']],[['t+'],['t-']]]+[[['t-'],['t+']],[['t-'],['t+']]]",
"T1btqq" : "[[['b','t']],[['jet','jet']]]",
"T1btbt" : "[[['b','t']],[['b','t']]]",
"T1tttt" : "[[['t+','t-']],[['t+','t-']]]",
"T2" : "[[['jet']],[['jet']]]",
"T5tbtb" : "[[['t'],['b']],[['t'],['b']]]",
"T5tbtt" : "[[['t'],['b']],[['t+'],['t-']]]+[[['t'],['b']],[['t-'],['t+']]]",
"TGQbbq" : "[[['b','b']],[['jet']]]",
"T2bt" : "[[['b']],[['t']]]",
"T1bbtt" : "[[['b','b']],[['t+','t-']]]",
"T5bbbb" : "[[['b'],['b']],[['b'],['b']]]",
"T1qqtt" : "[[['jet','jet']],[['t+','t-']]]",
"T1bttt" : "[[['b','t']],[['t+','t-']]]",
"T2bb" : "[[['b']],[['b']]]"
}

#+++++++ Figure info ++++++++++++++
figure={}
figure["T1"]='fig_07a.pdf'
figureUrl={}
figureUrl["T1"]='https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-047/fig_07a.pdf'


#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-CONF-2013-053')
info.comment = 'created from fastlim-1.0; superseded by ATLAS-SUSY-2013-05, fastlim maps contain more topologies for ATLAS-CONF-2013-053. Topologies included here are, T1, T1bbbb, T1bbbt, T1bbqq, T1bbtt, T1btbt, T1btqq, T1bttt, T1qqtt, T1tttt, T2, T2bb, T2bt, T2tt, T5bbbb, T5bbbt, T5btbt, T5tbtb, T5tbtt, T5tttt, TGQ, TGQbbq, TGQbtq, TGQQtt.'
info.lastUpdate = '2016/08/16'
info.implementedBy = 'WW'
info.sqrts = '8*TeV'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/CONFNOTES/ATLAS-CONF-2013-053/'
info.contact = 'fastlim'
info.lumi = '20.1/fb'


for dt in datasetsInfo:
    folder = dt.pop('folder')
    dataset = DataSetInput(folder)        
    dataset.setInfo(**dt)
    origDir = os.path.basename(folder)+"-orig/"
    for i in os.listdir(origDir):
        if i[-5:]!=".effi": continue
        txname=i[:-5]
        tmp = dataset.addTxName(txname)
        tmp.constraint = constraintsDict[txname]
        tmp.conditionDescription=None
        tmp.condition = None
        tmp.source = 'Fastlim-v1.0'
        tmp.dataUrl = None
        if i[:2] in [ "T5", "T6" ]:
            tmp_1 = tmp.addMassPlane([[x,y,z]]*2)
            tmp_1.addSource('efficiencyMap', origDir+'%s.effi' % txname, 'effi')
        else:
            tmp_1 = tmp.addMassPlane([[x,y]]*2)
            tmp_1.addSource('efficiencyMap', origDir+'%s.effi' % txname, 'effi')
        if os.path.exists(origDir+'%s_excl.dat' % txname):
            tmp_1.addSource('obsExclusion', origDir+'%s_excl.dat' % txname, 'txt')
        if txname in figure:
            tmp_1.figure = figure[txname]
        if txname in figureUrl:
            tmp_1.figureUrl = figureUrl[txname]
databaseCreator.create()


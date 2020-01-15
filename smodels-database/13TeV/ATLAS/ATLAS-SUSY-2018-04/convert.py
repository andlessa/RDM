#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: used to create info.txt and the <txname>.txt files.

"""
import sys
import os
import argparse

argparser = argparse.ArgumentParser(description =  
'create info.txt, txname.txt, twiki.txt and sms.py')
argparser.add_argument ('-utilsPath', '--utilsPath', 
help = 'path to the package smodels_utils',\
type = str )
argparser.add_argument ('-smodelsPath', '--smodelsPath', 
help = 'path to the package smodels_utils',\
type = str )
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
info 				= MetaInfoInput('ATLAS-SUSY-2018-04')
info.url 			= 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/'
info.sqrts 			= 13
info.lumi 			= 139
info.prettyName 	= 'hadronic tau + MET'
info.private 		= False
info.arxiv 			= 'arXiv:1911.06660'
info.contact 		= 'ATLAS collaboration'
info.publication 	= 'pending'



TStauStau = {
'name' 		 : 'TStauStau',
'info' 		 :{'figure' 		: 'Fig.1a', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2018-04/figaux_01a.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1765529?version=1&table=X-section U.L 1'},
'sources'	 :{'upLimit'		: 'orig/HEPData-ins1765529-v1-X-section_U.L_1.csv',
			   'obsExcl'		: 'orig/HEPData-ins1765529-v1-Exclusion_contour_1_Obs.csv'},
'constraint' : "[[['ta+']],[['ta-']]]",
'massPlane'  : 2*[[x, y]]}

DATA = [TStauStau]

#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

for TX in DATA:
	#+++++++ next txName block ++++++++++++++
	newTx 							= dataset.addTxName(TX['name'])
	newTx.checked 					= 'False'
	newTx.constraint 				= TX['constraint']
	newTx.conditionDescription 		= None
	newTx.condition 				= None
	newTx.source 					= 'ATLAS'
	#+++++++ next mass plane block ++++++++++++++
	newPlane 						= newTx.addMassPlane(TX['massPlane'])
	newPlane.figure 				= TX['info']['figure']
	newPlane.figureUrl 				= TX['info']['figureUrl']
	newPlane.dataUrl 				= TX['info']['dataUrl']
	newPlane.setSources(dataLabels 	= ['obsExclusion', 'upperLimits'],
					dataFiles 		= [TX['sources']['obsExcl'], TX['sources']['upLimit']],
					units			= [ None, 'pb' ],
                 	dataFormats 	= ['csv', 'csv'])

databaseCreator.create()

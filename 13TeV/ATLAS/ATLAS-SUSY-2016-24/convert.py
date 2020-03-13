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
info = MetaInfoInput('ATLAS-SUSY-2016-24')
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/'
info.sqrts = 13
info.lumi = 36.1
info.prettyName = '2+ leptons (e,mu) + jets + Etmiss'
info.private = False
info.arxiv =  'https://arxiv.org/abs/1803.02762'
info.contact = 'atlas-phys-susy-conveners@cern.ch'
info.publication = 'https://link.springer.com/article/10.1140/epjc/s10052-018-6423-7'

TChipChimSlepSlepAll = {
'name' 		 : 'TChipChimSlepSlepAll',
'info' 		 :{'figure' 		: 'Fig.8a', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08a.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table78'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_13.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_14.csv',
			   'upLimit'		: 'orig/HEPData-ins1658902-v1-Table_78.csv'},
#'constraint' : "0.5*([[['nu'],['L+']],[['nu'],['L-']]]+[[['nu'],['L-']],[['nu'],['L+']]])",
'constraint' : "[[['nu'],['L+']],[['nu'],['L-']]]",
'massPlane'  : 2*[[x, 0.5*(x+y), y]]}

TSlepSlepAll = {
'name' 		 : 'TSlepSlepAll',
'info' 		 :{'figure' 		: 'Fig.8b', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08b.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table79'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_15.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_16.csv',
			   'upLimit'		: 'orig/HEPData-ins1658902-v1-Table_79.csv'},
#'constraint' : "[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]",
'constraint' : "[[['l']],[['l']]]", #"[[['l+']],[['l-']]]"
'massPlane'  : 2*[[x, y]]}

TChiChipmSlepL = {
'name' 		 : 'TChiChipmSlepL',
'info' 		 :{'figure' 		: 'Fig.8c', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08c.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table80'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_17.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_18.csv',
			   'upLimit'		: 'orig/HEPData-ins1658902-v1-Table_80.csv'},
#'constraint' : "0.5*([[['L+'],['L-']],[['L'],['nu']]] + [[['L+'],['L-']],[['nu'],['L']]] + [[['L-'],['L+']],[['L'],['nu']]] + [[['L-'],['L+']],[['nu'],['L']]])", #war auf 2.*
'constraint' : "2.0*([[['L+'],['L-']],[['L'],['nu']]] + [[['L+'],['L-']],[['nu'],['L']]] + [[['L-'],['L+']],[['L'],['nu']]] + [[['L-'],['L+']],[['nu'],['L']]])",
'massPlane'  : 2*[[x, 0.5*(x+y), y]]}

TChiWZ = {
'name' 		 : 'TChiWZ',
'info' 		 :{'figure' 		: 'Fig.8d', 
			   'figureUrl' 		: 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2016-24/fig_08d.png', 
			   'dataUrl' 		: 'https://www.hepdata.net/record/ins1658902?version=1&table=Table81'},
'sources'	 :{'expExcl'		: 'orig/HEPData-ins1658902-v1-Table_19.csv',
			   'obsExcl'		: 'orig/HEPData-ins1658902-v1-Table_20.csv',
			   'upLimit'		: 'orig/HEPData-ins1658902-v1-Table_81.csv'},
'constraint' : "[[['W']],[['Z']]]",
'massPlane'  : 2*[[x, y]]}

DATA = [TChipChimSlepSlepAll, TSlepSlepAll, TChiChipmSlepL, TChiWZ]

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
	newPlane.setSources(dataLabels 	= ['expExclusion', 'obsExclusion', 'upperLimits'],
					dataFiles 		= [TX['sources']['expExcl'], TX['sources']['obsExcl'], TX['sources']['upLimit']],
					units			= [ None, None, 'fb' ],
				 	coordinates 	= [ {x: 0, y: 1, 'value': None}, {x: 0, y: 1, 'value': None},  {x : 1, y: 0, 'value' :2} ],
                 	dataFormats 	= ['csv', 'csv', 'csv'])

databaseCreator.create()

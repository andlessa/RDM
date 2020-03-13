#!/usr/bin/env python3

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
help = 'path to smodels',\
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

databaseCreator.ncpus = 1


#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-17-009')
info.url = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/'
info.sqrts = 13
info.lumi = 35.9
info.prettyName = 'leptons + Etmiss'
info.private = False
info.arxiv = ''
info.contact = ''
info.publication = ''
info.comment = ''


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)



#+++++++ next txName block ++++++++++++++
TSlepSlep = dataset.addTxName('TSlepSlep')
TSlepSlep.checked =""
TSlepSlep.constraint ="[[['e+']],[['e-']]]+[[['mu+']],[['mu-']]]"
TSlepSlep.conditionDescription ="[[['mu+']],[['mu-']]] > [[['e+']],[['e-']]]"
TSlepSlep.condition ="Cgtr([[['mu+']],[['mu-']]],[[['e+']],[['e-']]])"
TSlepSlep.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_1 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlep_1.figure = "Fig. 5a"
TSlepSlep_1.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-a.png"
TSlepSlep_1.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-a.root'
TSlepSlep_1.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_005-a.root', 'orig/CMS-SUS-17-009_Figure_005-a.root','orig/CMS-SUS-17-009_Figure_005-a.root', 'orig/CMS-SUS-17-009_Figure_005-a.root','orig/CMS-SUS-17-009_Figure_005-a.root', 'orig/CMS-SUS-17-009_Figure_005-a.root','orig/CMS-SUS-17-009_Figure_005-a.root', 'orig/CMS-SUS-17-009_Figure_005-a.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])

'''
#+++++++ next mass plane block ++++++++++++++
TSlepSlep_2 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlep_2.figure = "Fig. 5b"
TSlepSlep_2.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-b.png"
TSlepSlep_2.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-b.root'
TSlepSlep_2.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])


#+++++++ next mass plane block ++++++++++++++
TSlepSlep_3 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlep_3.figure = "Fig. 5c"
TSlepSlep_3.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-c.png"
TSlepSlep_3.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_005-c.root'
TSlepSlep_3.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_005-c.root', 'orig/CMS-SUS-17-009_Figure_005-c.root','orig/CMS-SUS-17-009_Figure_005-c.root', 'orig/CMS-SUS-17-009_Figure_005-c.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])
 
 
 
 
 
#+++++++ next txName block ++++++++++++++
#TSlepSlepE = dataset.addTxName('TSlepSlep')
#TSlepSlepE.checked =""
#TSlepSlepE.constraint ="[[['e+']],[['e-']]]"
#TSlepSlepE.conditionDescription =None
#TSlepSlepE.condition =None
#TSlepSlepE.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
TSlepSlepE_1 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepE_1.constraint ="[[['e+']],[['e-']]]"
TSlepSlepE_1.conditionDescription =None
TSlepSlepE_1.condition =None
TSlepSlepE_1.figure = "Fig. 6a"
TSlepSlepE_1.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-a.png"
TSlepSlepE_1.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-a.root'
TSlepSlepE_1.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1','upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_006-a.root', 'orig/CMS-SUS-17-009_Figure_006-a.root','orig/CMS-SUS-17-009_Figure_006-a.root', 'orig/CMS-SUS-17-009_Figure_006-a.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])




#+++++++ next mass plane block ++++++++++++++
TSlepSlepE_2 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepE_2.constraint ="[[['e+']],[['e-']]]"
TSlepSlepE_2.conditionDescription =None
TSlepSlepE_2.condition =None
TSlepSlepE_2.figure = "Fig. 6b"
TSlepSlepE_2.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-b.png"
TSlepSlepE_2.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-b.root'
TSlepSlepE_2.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1','upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_006-b.root', 'orig/CMS-SUS-17-009_Figure_006-b.root','orig/CMS-SUS-17-009_Figure_006-b.root', 'orig/CMS-SUS-17-009_Figure_006-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])


#+++++++ next mass plane block ++++++++++++++
TSlepSlepE_3 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepE_3.constraint ="[[['e+']],[['e-']]]"
TSlepSlepE_3.conditionDescription =None
TSlepSlepE_3.condition =None
TSlepSlepE_3.figure = "Fig. 6c"
TSlepSlepE_3.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-c.png"
TSlepSlepE_3.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_006-c.root'
TSlepSlepE_3.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1','upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_006-c.root', 'orig/CMS-SUS-17-009_Figure_006-c.root','orig/CMS-SUS-17-009_Figure_006-c.root', 'orig/CMS-SUS-17-009_Figure_006-c.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16]) 
 
 
#+++++++ next mass plane block ++++++++++++++
TSlepSlepmu_1 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepmu_1.constraint ="[[['mu+']],[['mu-']]]"
TSlepSlepmu_1.conditionDescription =None
TSlepSlepmu_1.condition =None
TSlepSlepmu_1.figure = "Fig. 7a"
TSlepSlepmu_1.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-a.png"
TSlepSlepmu_1.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-a.root'
TSlepSlepmu_1.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1','upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_007-a.root', 'orig/CMS-SUS-17-009_Figure_007-a.root','orig/CMS-SUS-17-009_Figure_007-a.root', 'orig/CMS-SUS-17-009_Figure_007-a.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16]) 
 
 
#+++++++ next mass plane block ++++++++++++++
TSlepSlepmu_2 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepmu_2.constraint ="[[['mu+']],[['mu-']]]"
TSlepSlepmu_2.conditionDescription =None
TSlepSlepmu_2.condition =None
TSlepSlepmu_2.figure = "Fig. 7b"
TSlepSlepmu_2.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-b.png"
TSlepSlepmu_2.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-b.root'
TSlepSlepmu_2.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1','upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_007-b.root', 'orig/CMS-SUS-17-009_Figure_007-b.root','orig/CMS-SUS-17-009_Figure_007-b.root', 'orig/CMS-SUS-17-009_Figure_007-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])


#+++++++ next mass plane block ++++++++++++++
TSlepSlepmu_3 = TSlepSlep.addMassPlane(2*[[x, y]])
TSlepSlepmu_3.constraint ="[[['mu+']],[['mu-']]]"
TSlepSlepmu_3.conditionDescription =None
TSlepSlepmu_3.condition =None
TSlepSlepmu_3.figure = "Fig. 7c"
TSlepSlepmu_3.figureUrl = "https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-c.png"
TSlepSlepmu_3.dataUrl = 'https://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-17-009/CMS-SUS-17-009_Figure_007-c.root'
TSlepSlepmu_3.setSources(dataLabels= ['obsExclusion', 'expExclusion','expExclusionP1','expExclusionM1','obsExclusionP1','obsExclusionM1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/CMS-SUS-17-009_Figure_007-c.root', 'orig/CMS-SUS-17-009_Figure_007-c.root','orig/CMS-SUS-17-009_Figure_007-c.root', 'orig/CMS-SUS-17-009_Figure_007-c.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root','orig/CMS-SUS-17-009_Figure_005-b.root', 'orig/CMS-SUS-17-009_Figure_005-b.root'],
                 dataFormats= ['root', 'root','root', 'root','root', 'root','root', 'root'],objectNames= ['gr_obs_smoothed;1','gr_exp_smoothed;1','gr_ep1s_smoothed;1','gr_em1s_smoothed;1','gr_op1s_smoothed;1','gr_om1s_smoothed;1','obs_xs0;1','exp_xs0;1'],units= [None,None,None,None,None,None,'fb','fb'],
                    indices= [1,2,3,4,7,8,10,16])  
 
''' 
 
databaseCreator.create()

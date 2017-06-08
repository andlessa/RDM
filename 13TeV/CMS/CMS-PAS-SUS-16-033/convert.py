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
    utilsPath = '../../../../smodels-utils'
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
info = MetaInfoInput('CMS-PAS-SUS-16-033')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
info.sqrts = 13
info.lumi = 35.9
info.prettyName = 'MHT'
info.private = False
info.arxiv = 'http://arxiv.org/abs/1704.07781'
info.contact = ''
info.publication = ''
info.comment = ''


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++ next txName block ++++++++++++++
T1bbbb = dataset.addTxName('T1bbbb')
T1bbbb.checked = ''
T1bbbb.constraint = "[[['b','b']],[['b','b']]]"
T1bbbb.conditionDescription = None
T1bbbb.condition = None
T1bbbb.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T1bbbb_1 = T1bbbb.addMassPlane(2*[[x, y]])
T1bbbb_1.figure = 'Fig.12-b'
T1bbbb_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.png'
T1bbbb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T1bbbb_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1bbbb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1bbbb_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1bbbb_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/T1bbbb.root', 'orig/T1bbbb.root','orig/T1bbbb.root','orig/T1bbbb.root','orig/T1bbbb.root','orig/T1bbbb.root','orig/T1bbbb.root','orig/T1bbbb.root' ],
                 dataFormats= ['root', 'root', 'root', 'root', 'root', 'root', 'root','root'],objectNames= ['ExpLim', 'ExpLimSdn', 'ExpLimSup', 'ObsLim', 'ObsLimSdn', 'ObsLimSup', 'MassScan2D','MassScan2DExp'])


#+++++++ next txName block ++++++++++++++
T1tttt = dataset.addTxName('T1tttt')
T1tttt.checked = ''
T1tttt.constraint =  "[[['t','t']],[['t','t']]]"
T1tttt.conditionDescription = None
T1tttt.condition = None
T1tttt.source = "CMS"
T1tttt.massConstraint = None
T1ttttoff = dataset.addTxName('T1ttttoff')
T1ttttoff.checked = ''
T1ttttoff.constraint = "[[['b','W','b','W']],[['b','W','b','W']]]"
T1ttttoff.conditionDescription = None
T1ttttoff.condition = None
T1ttttoff.massConstraint = [['dm <= 338.0'], ['dm <= 338.0']]
T1ttttoff.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T1tttt_1 = T1tttt.addMassPlane(2*[[x, y]])
T1tttt_1.figure = 'Fig.12-a'
T1tttt_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.png'
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T1tttt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1tttt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1tttt_1.exclusionDataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-a.root'
T1tttt_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/T1tttt.root', 'orig/T1tttt.root', 'orig/T1tttt.root', 'orig/T1tttt.root', 'orig/T1tttt.root', 'orig/T1tttt.root', 'orig/T1tttt.root','orig/T1tttt.root' ],
                 dataFormats= ['root','root', 'root', 'root', 'root', 'root', 'root', 'root'],objectNames= ['ExpLim', 'ExpLimSdn', 'ExpLimSup', 'ObsLim', 'ObsLimSdn', 'ObsLimSup', 'MassScan2D','MassScan2DExp'])
T1ttttoff.addMassPlane(T1tttt_1)

#+++++++ next txName block ++++++++++++++
T1 = dataset.addTxName('T1')
T1.checked =''
T1.constraint = "[[['jet','jet']],[['jet','jet']]]"
T1.conditionDescription = None
T1.condition = None
T1.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T1_1 = T1.addMassPlane(2*[[x, y]])
T1_1.figure = 'Fig.8-c'
T1_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-c.png'
T1_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T1_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-c.root'
T1_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-c.root'
T1_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_012-c.root'
T1_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                 dataFiles= ['orig/T1.root', 'orig/T1.root','orig/T1.root','orig/T1.root','orig/T1.root','orig/T1.root','orig/T1.root','orig/T1.root'],
                 dataFormats= ['root','root', 'root', 'root', 'root', 'root', 'root', 'root'],objectNames= ['ExpLim', 'ExpLimSdn', 'ExpLimSup', 'ObsLim', 'ObsLimSdn', 'ObsLimSup', 'MassScan2D','MassScan2DExp'])



#+++++++ next txName block ++++++++++++++
T2tt = dataset.addTxName('T2tt')
T2tt.checked = ''
T2tt.constraint =  "[[['t']],[['t']]]"
T2tt.conditionDescription = None
T2tt.condition = None
T2tt.source = "CMS"
T2tt.massConstraint = [['dm >= 169.0']]*2 #Use only on-shell data to avoid interpolation in the removed data band
T2ttoff = dataset.addTxName('T2ttoff')
T2ttoff.checked = ''
T2ttoff.constraint = "[[['b','W']],[['b','W']]]"
T2ttoff.conditionDescription = None
T2ttoff.condition = None
T2ttoff.massConstraint = [['dm <= 169.0'], ['dm <= 169.0']]
T2ttoff.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(2*[[x, y]])
T2tt_1.figure = 'Fig.12-a'
T2tt_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-a.png'
T2tt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T2tt_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-a.root'
T2tt_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-a.root'
T2tt_1.exclusionDataUrl =  'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-a.root'
T2tt_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                    dataFiles= ['orig/T2tt_fix.root', 'orig/T2tt_fix.root','orig/T2tt_fix.root','orig/T2tt_fix.root','orig/T2tt_fix.root','orig/T2tt_fix.root','orig/T2tt_fix.root','orig/T2tt_fix.root'],
                    dataFormats= ['root','root', 'root', 'root', 'root', 'root', 'root', 'root'],objectNames= ['ExpLim2', 'ExpLimSdn2', 'ExpLimSup2', 'ObsLim2', 'ObsLimSdn2', 'ObsLimSup2', 'MassScan2D_fix','MassScan2DExp'])
T2ttoff.addMassPlane(T2tt_1)


#+++++++ next txName block ++++++++++++++
T2bb = dataset.addTxName('T2bb')
T2bb.checked = ''
T2bb.constraint = "[[['b']],[['b']]]"
T2bb.conditionDescription = None
T2bb.condition = None
T2bb.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T2bb_1 = T2bb.addMassPlane(2*[[x, y]])
T2bb_1.figure = 'Fig.12-b'
T2bb_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-b.png'
T2bb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T2bb_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-b.root'
T2bb_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-b.root'
T2bb_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-b.root'
T2bb_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                    dataFiles= ['orig/T2bb.root', 'orig/T2bb.root','orig/T2bb.root','orig/T2bb.root','orig/T2bb.root','orig/T2bb.root','orig/T2bb.root','orig/T2bb.root'],
                    dataFormats= ['root','root', 'root', 'root', 'root', 'root', 'root', 'root'],objectNames= ['ExpLim', 'ExpLimSdn', 'ExpLimSup', 'ObsLim', 'ObsLimSdn', 'ObsLimSup', 'MassScan2D','MassScan2DExp'])





#+++++++ next txName block ++++++++++++++
T2 = dataset.addTxName('T2')
T2.checked = ''
T2.constraint = "[[['jet']],[['jet']]]"
T2.conditionDescription = None
T2.condition = None
T2.source = "CMS"
#+++++++ next mass plane block ++++++++++++++
T2_1 = T2.addMassPlane(2*[[x, y]])
T2_1.figure = 'Fig.12-b'
T2_1.figureUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-c.png'
T2_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/index.html'
T2_1.histoDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-c.root'
T2_1.dataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-c.root'
T2_1.exclusionDataUrl = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-16-033/CMS-SUS-16-033_Figure_013-c.root'
T2_1.setSources(dataLabels= ['expExclusion', 'expExclusionM1', 'expExclusionP1', 'obsExclusion', 'obsExclusionM1', 'obsExclusionP1', 'upperLimits','expectedUpperLimits'],
                  dataFiles= ['orig/T2.root', 'orig/T2.root','orig/T2.root','orig/T2.root','orig/T2.root','orig/T2.root','orig/T2.root','orig/T2.root'],
                  dataFormats= ['root', 'root', 'root', 'root', 'root', 'root', 'root','root'],objectNames= ['ExpLim2', 'ExpLimSdn2', 'ExpLimSup2', 'ObsLim2', 'ObsLimSdn2', 'ObsLimSup2', 'MassScan2D','MassScan2DExp'])



databaseCreator.create()

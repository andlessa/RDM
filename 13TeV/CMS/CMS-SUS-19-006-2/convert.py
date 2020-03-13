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



#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-19-006')
info.url = 'http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/index.html'
info.sqrts = 13
info.lumi = 137
info.prettyName = '0L + jets + Etmiss'
info.private = False
info.arxiv = '1908.04722'
info.contact = 'cms-phys-conveners-sus@cern.ch'
info.publication = 'JHEP 10 (2019) 244, http://dx.doi.org/10.1007/JHEP10(2019)244'


#+++++++ dataset block ++++++++++++++
dataset = DataSetInput('data')
dataset.setInfo(dataType = 'upperLimit', dataId = None)

#+++++++txName block++++++++++++++++++++
T1tttt=dataset.addTxName('T1tttt')
T1tttt.checked='no'
T1tttt.constraint="[[['t','t']],[['t','t']]]"
T1tttt.condition=None
T1tttt.conditionDescription = None
T1tttt.source="CMS"
T1tttt.massConstraint=[['dm>=338.0'],['dm>=338.0']]

T1ttttoff=dataset.addTxName('T1ttttoff')
T1ttttoff.checked='no'
T1ttttoff.constraint="[[['b','W','b','W']],[['b','W','b','W']]]"
T1ttttoff.condition=None
T1ttttoff.source="CMS"
T1ttttoff.massConstraint=[['160 < dm < 338.0'], ['160 < dm < 338.0']]

#++++++next mass plane block+++++++++

T1tttt_1 = T1tttt.addMassPlane(2*[[x,y]])
T1tttt_1.figure='Fig. 13-a'
T1tttt_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-a.png'
T1tttt_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-a.root'
T1tttt_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-a.root'
T1tttt_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-a.root'
T1tttt_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root','orig/CMS-SUS-19-006_Figure_013-a.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])
T1ttttoff.addMassPlane(T1tttt_1)

#+++++txName block +++++++++++++++++

T1bbbb=dataset.addTxName('T1bbbb')
T1bbbb.checked='no'
T1bbbb.constraint="[[['b','b']],[['b','b']]]"
T1bbbb.condition=None
T1bbbb.conditionDescription = None
T1bbbb.source="CMS"

#++++++next mass plane block+++++++++

T1bbbb_1 = T1bbbb.addMassPlane(2*[[x,y]])
T1bbbb_1.figure='Fig. 12-b'
T1bbbb_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-b.png'
T1bbbb_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-b.root'
T1bbbb_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-b.root'
T1bbbb_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-b.root'
T1bbbb_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root','orig/CMS-SUS-19-006_Figure_013-b.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])

#+++++txName block +++++++++++++++++

T1=dataset.addTxName('T1')
T1.checked='no'
T1.constraint="[[['jet','jet']],[['jet','jet']]]"
T1.condition=None
T1.conditionDescription = None
T1.source="CMS"

#++++++next mass plane block+++++++++

T1_1 = T1.addMassPlane(2*[[x,y]])
T1_1.figure='Fig. 13-c'
T1_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-c.png'
T1_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-c.root'
T1_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-c.root'
T1_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_013-c.root'
T1_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root','orig/CMS-SUS-19-006_Figure_013-c.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])

#+++++txName block +++++++++++++++++

T2tt=dataset.addTxName('T2tt')
T2tt.checked='no'
T2tt.constraint="[[['t']],[['t']]]"
T2tt.condition=None
T2tt.conditionDescription = None
T2tt.massConstraint=[['dm>169'],['dm>169']]
T2tt.source="CMS"

T2ttoff=dataset.addTxName('T2ttoff')
T2ttoff.checked='no'
T2ttoff.constraint="[[['b','W']],[['b','W']]]"
T2ttoff.condition=None
T2ttoff.conditionDescription=None
T2ttoff.massConstraint=[['80<dm<169'],['80<dm<169']]
T2ttoff.source="CMS"
#++++++next mass plane block+++++++++

T2tt_1 = T2tt.addMassPlane(2*[[x,y]])
T2tt_1.figure='Fig. 14-a'
T2tt_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-a.png'
T2tt_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-a.root'
T2tt_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-a.root'
T2tt_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-a.root'
T2tt_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root','orig/CMS-SUS-19-006_Figure_014-a.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])

T2ttoff.addMassPlane(T2tt_1)

#+++++txName block +++++++++++++++++

T2bb=dataset.addTxName('T2bb')
T2bb.checked='no'
T2bb.constraint="[[['b']],[['b']]]"
T2bb.condition=None
T2bb.conditionDescription = None
T2bb.source="CMS"

#++++++next mass plane block+++++++++

T2bb_1 = T2bb.addMassPlane(2*[[x,y]])
T2bb_1.figure='Fig. 14-b'
T2bb_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-b.png'
T2bb_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-b.root'
T2bb_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-b.root'
T2bb_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-b.root'
T2bb_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root','orig/CMS-SUS-19-006_Figure_014-b.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])


#+++++txName block +++++++++++++++++

T2=dataset.addTxName('T2')
T2.checked='no'
T2.constraint="[[['jet']],[['jet']]]"
T2.condition=None
T2.conditionDescription = None
T2.source="CMS"

#++++++next mass plane block+++++++++

T2_1 = T2.addMassPlane(2*[[x,y]])
T2_1.figure='Fig. 14-c'
T2_1.figureUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-c.png'
T2_1.dataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-c.root'
T2_1.histoDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-c.root'
T2_1.exclusionDataUrl='http://cms-results.web.cern.ch/cms-results/public-results/publications/SUS-19-006/CMS-SUS-19-006_Figure_014-c.root'
T2_1.setSources(dataLabels=['expExclusion','expExclusionM1','expExclusionP1','obsExclusion','obsExclusionM1','obsExclusionP1','upperLimits'],
                    dataFiles=['orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root','orig/CMS-SUS-19-006_Figure_014-c.root'],
                    dataFormats=['root','root','root','root','root','root','root'],objectNames=['ExpLim;1','ExpLimSdn;1','ExpLimSup;1','ObsLim;1','ObsLimSdn;1','ObsLimSup;1','MassScan2D;1'],units=[None,None,None,None,None,None,'pb'])



databaseCreator.create()

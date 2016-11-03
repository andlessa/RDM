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
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('CMS-SUS-13-011')
info.url = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
info.sqrts = 8
info.lumi = 19.5
info.prettyName = 'leptonic stop'
info.private = False
info.arxiv = 'arXiv:1308.1586v2'
info.contact = 'Benjamin Hooberman <hooberman@gmail.com>, Mariarosaria DAlfonso <dalfonso@mail.cern.ch>'
info.publication = 'http://link.springer.com/article/10.1140%2Fepjc%2Fs10052-013-2677-2'
info.comment = ''
info.supersedes ='CMS-PAS-SUS-12-023'
info.supersededBy =''

#+++++++ next txName block ++++++++++++++
T2tt = TxNameInput('T2tt')
T2tt.on.checked =''
T2tt.off.checked =''
T2tt.on.constraint = "[[['t']],[['t']]]"
T2tt.off.constraint ="[[['W','b']],[['W','b']]]"
T2tt.on.conditionDescription ="None"
T2tt.off.conditionDescription ="None"
T2tt.on.condition = None
T2tt.off.condition = None
#T2tt.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T2tt_1 = T2tt.addMassPlane(motherMass = x, lspMass = y )
#----figure----
T2tt_1.figure = '20a'
T2tt_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/fig20a.pdf'
#----limit source----
T2tt_1.obsUpperLimit.setSource( 'orig/topneutralino_cutbased.root', 'root', objectName = 'xsec_upperlimit', index = None )
#T2tt_1.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T2tt_1.obsExclusion.setSource( 'orig/T2tt_exclusion.dat', 'txt', objectName = None, index = None )
#T2tt_1.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusion.setSource( 'orig/topneutralino_cutbased.root', 'root', objectName = 'expected_exclusion', index = None )
#T2tt_1.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T2tt_1.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T2tt_1.dataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
#----limit url settings ----
T2tt_1.histoDataUrl = 'https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSUS13011'
T2tt_1.obsUpperLimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.root'
#T2tt_1.expUpperlimit.dataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.root'
#----exclusion url settings ----
T2tt_1.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.C'
T2tt_1.obsExclusion.dataUrl = ''
T2tt_1.obsExclusionM1.dataUrl =''
T2tt_1.obsExclusionP1.dataUrl =''
T2tt_1.expExclusion.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/topneutralino_cutbased.C'
T2tt_1.expExclusionM1.dataUrl =''
T2tt_1.expExclusionP1.dataUrl =''



#+++++++ next txName block ++++++++++++++
T6bbWW = TxNameInput('T6bbWW')
T6bbWW.on.checked =''
T6bbWW.off.checked =''
T6bbWW.on.constraint ="[[['b'],['W']],[['b'],['W']]]"
T6bbWW.off.constraint ="2.3*([[['b'],['L','nu']],[['b'],['jet','jet']]])"
T6bbWW.on.conditionDescription = "None"
T6bbWW.off.conditionDescription ="None"
T6bbWW.on.condition ="None"
T6bbWW.off.condition ="None"
#T6bbWW.branchingRatio =

#+++++++ next mass plane block ++++++++++++++
T6bbWW_1 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x*0.5 + (1. - 0.5)*y, lspMass = y)
#T6bbWW_1.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_1.figure = '10c'
T6bbWW_1.figureUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/fig10c.pdf'
#----limit source----
T6bbWW_1.obsUpperLimit.setSource( 'orig/bottomchargino_x50_BDT.root', "root", objectName = 'xsec_upperlimit', index = None )
#T6bbWW050.expUpperlimit.s
#----exclusion source----
T6bbWW_1.obsExclusion.setSource( 'orig/Obs_BDT_x05.txt', "txt", objectName = None, index = None ) # TODO check!
#T6bbWW050.obsExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWW050.obsExclusionP1.setSource( path, filetype, objectName = None, index = None )
#T6bbWW050.expExclusion.setSource( path, filetype, objectName = None, index = None )
#T6bbWW050.expExclusionM1.setSource( path, filetype, objectName = None, index = None )
#T6bbWW050.expExclusionP1.setSource( path, filetype, objectName = None, index = None )
#----global url settings ----
T6bbWW_1.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/'
#----limit url settings ----
T6bbWW_1.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x50_cutbased.root'
T6bbWW_1.obsUpperLimit.dataUrl =''
T6bbWW_1.expUpperLimit.dataUrl =''
#----exclusion url settings ----
T6bbWW_1.exclusionDataUrl ='https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x50_cutbased.root'
#T6bbWW_1.obsExclusion.dataUrl =
#T6bbWW_1.obsExclusionM1.dataUrl =
#T6bbWW_1.obsExclusionP1.dataUrl =
#T6bbWW_1.expExclusion.dataUrl =
#T6bbWW_1.expExclusionM1.dataUrl =
#T6bbWW_1.expExclusionP1.dataUrl =


#+++++++ next mass plane block ++++++++++++++
T6bbWW_2 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x*0.25 + (1. - 0.25)*y, lspMass = y)
#T6bbWW_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_2.figure ='10b'
T6bbWW_2.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/fig10b.pdf'
#----limit source----
T6bbWW_2.obsUpperLimit.setSource( 'orig/bottomchargino_x25_BDT.root', "root", objectName = 'xsec_upperlimit', index = None )
#T6bbWW_2.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_2.obsExclusion.setSource( 'orig/Obs_BDT_x025.txt', "txt", objectName = None, index = None )
#T6bbWW_2.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_2.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/'
#----limit url settings ----
T6bbWW_2.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x25_BDT.root'
T6bbWW_2.obsUpperLimit.dataUrl =''
T6bbWW_2.expUpperLimit.dataUrl =''
#----exclusion url settings ----
T6bbWW_2.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x25_BDT.root'
#T6bbWW_2.obsExclusion.dataUrl =
#T6bbWW_2.obsExclusionM1.dataUrl =
#T6bbWW_2.obsExclusionP1.dataUrl =
#T6bbWW_2.expExclusion.dataUrl =
#T6bbWW_2.expExclusionM1.dataUrl =
#T6bbWW_2.expExclusionP1.dataUrl =


#+++++++ next mass plane block ++++++++++++++
T6bbWW_3 = T6bbWW.addMassPlane(motherMass = x, interMass0 = x*0.75 + (1. - 0.75)*y, lspMass = y)
#T6bbWW_2.setBranch_2(motherMass = , interMass0 = , lspMass = )
#----figure----
T6bbWW_3.figure = '10d'
T6bbWW_3.figureUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/fig10d.pdf'
#----limit source----
T6bbWW_3.obsUpperLimit.setSource( 'orig/bottomchargino_x75_BDT.root', "root", objectName = 'xsec_upperlimit', index = None )
#T6bbWW_3.expUpperLimit.setSource( path, type, objectName = None, index = None )
#----exclusion source----
T6bbWW_3.obsExclusion.setSource( 'orig/Obs_BDT_x075.txt', "txt", objectName = None, index = None )

#T6bbWW_2.obsExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.obsExclusionP1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusion.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionM1.setSource( path, type, objectName = None, index = None )
#T6bbWW_2.expExclusionP1.setSource( path, type, objectName = None, index = None )
#----global url settings ----
T6bbWW_3.dataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/'
#----limit url settings ----
T6bbWW_3.histoDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x75_BDT.root'
T6bbWW_3.obsUpperLimit.dataUrl =''
T6bbWW_3.expUpperLimit.dataUrl =''
#----exclusion url settings ----
T6bbWW_3.exclusionDataUrl = 'https://twiki.cern.ch/twiki/pub/CMSPublic/PhysicsResultsSUS13011/bottomchargino_x75_BDT.root'
#T6bbWW_2.obsExclusion.dataUrl =
#T6bbWW_2.obsExclusionM1.dataUrl =
#T6bbWW_2.obsExclusionP1.dataUrl =
#T6bbWW_2.expExclusion.dataUrl =
#T6bbWW_2.expExclusionM1.dataUrl =
#T6bbWW_2.expExclusionP1.dataUrl =

databaseCreator.create()


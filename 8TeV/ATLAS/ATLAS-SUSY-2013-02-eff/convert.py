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
args = argparser.parse_args()

if args.utilsPath:
    utilsPath = args.utilsPath
else:
    databaseRoot = '../../../'
    sys.path.append(os.path.abspath(databaseRoot))
    from utilsPath import utilsPath
    utilsPath = databaseRoot + utilsPath

sys.path.append(os.path.abspath(utilsPath))
from smodels_utils.dataPreparation.inputObjects import TxNameInput, MetaInfoInput
from smodels_utils.dataPreparation.databaseCreation import databaseCreator
from smodels_utils.dataPreparation.origPlotObjects import x, y

#+++++++ global info block ++++++++++++++
info = MetaInfoInput('ATLAS-SUSY-2013-02')
info.comment = 'T5WWLSP060 and T6WWLSP060 originally have xvalue on y-axes, changed by us to M2'
info.sqrts = '8.0'
info.private = False
info.lumi = '20.3'
info.publication = 'http://link.springer.com/article/10.1007/JHEP09%282014%29176'
info.url = 'https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/'
#info.supersededBy =
info.arxiv = 'http://arxiv.org/abs/1405.7875'
#info.contact =
info.prettyName =  "jets and met"
info.supersedes = 'ATLAS-CONF-2013-047'



#+++++++        T2     ++++++++++++++
T2m = TxNameInput('T2')
#T2.on.checked =
#T2.off.checked =
T2m.on.constraint ="[[['jet']],[['jet']]]"
#T2.off.constraint =
T2m.on.conditionDescription ="None"
#T2.off.conditionDescription =
T2m.on.condition ="None"
#T2.off.condition =

#+++++++ next mass plane block ++++++++++++++
T2 = T2m.addMassPlane(motherMass = x, lspMass = y)

T2.figure = "figaux_15b"
T2.efficiencyMap.setSource("orig/T2_SR2jl.dat","txt", objectName = "T2_SR2jl.dat", index = None , dataset = "SR2jl")
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_15b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d106"

T2.efficiencyMap.setStatistics( observedN = 12315, expectedBG = 13000 , bgError = 1000)
T2.obsExclusion.setSource("orig/exclusion_T2.txt", "txt", objectName=None, index=None )

databaseCreator.create()


T2.figure = "figaux_16b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_16b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d109"

T2.efficiencyMap.setSource("orig/T2_SR2jm.dat","txt", objectName = "T2_SR2jm.dat", index = None , dataset = "SR2jm")
T2.efficiencyMap.setStatistics( observedN = 715, expectedBG = 760 , bgError = 50 )

databaseCreator.create(True)



T2.figure = "figaux_17b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_17b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d112"

T2.efficiencyMap.setSource("orig/T2_SR2jt.dat","txt", objectName = "T2_SR2jt.dat", index = None , dataset = "SR2jt")
T2.efficiencyMap.setStatistics( observedN = 133, expectedBG = 125 , bgError = 10 )

databaseCreator.create(True)

T2.figure = "figaux_18b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_18b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d115" 

T2.efficiencyMap.setSource("orig/T2_SR2jW.dat","txt", objectName = "T2_SR2jW.dat", index = None , dataset = "SR2jW")
T2.efficiencyMap.setStatistics( observedN = 0, expectedBG = 2.3 , bgError = 1.4 )

databaseCreator.create(True)


T2.figure = "figaux_19b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_19b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d118"

T2.efficiencyMap.setSource("orig/T2_SR3j.dat","txt", objectName = "T2_SR3j.dat", index = None , dataset = "SR3j")
T2.efficiencyMap.setStatistics( observedN = 7, expectedBG = 5 , bgError = 1.2 )

databaseCreator.create(True)



T2.figure = "figaux_20b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_20b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d121"

T2.efficiencyMap.setSource("orig/T2_SR4jW.dat","txt", objectName = "T2_SR4jW.dat", index = None , dataset = "SR4jW")
T2.efficiencyMap.setStatistics( observedN = 16, expectedBG = 14 , bgError = 4 )

databaseCreator.create(True)





T2.figure = "figaux_21b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_21b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d124"

T2.efficiencyMap.setSource("orig/T2_SR4jl-.dat","txt", objectName = "T2_SR4jl-.dat", index = None , dataset = "SR4jl-")
T2.efficiencyMap.setStatistics( observedN = 2169, expectedBG = 2120 , bgError = 110 )

databaseCreator.create(True)

T2.figure = "figaux_22b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_22b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d127"

T2.efficiencyMap.setSource("orig/T2_SR4jl.dat","txt", objectName = "T2_SR4jl.dat", index = None , dataset = "SR4jl")
T2.efficiencyMap.setStatistics( observedN = 608, expectedBG = 630 , bgError = 50 )

databaseCreator.create(True)

T2.figure = "figaux_23b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_23b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d130"

T2.efficiencyMap.setSource("orig/T2_SR4jm.dat","txt", objectName = "T2_SR4jm.dat", index = None , dataset = "SR4jm")
T2.efficiencyMap.setStatistics( observedN = 24, expectedBG = 37 , bgError = 6 )

databaseCreator.create(True)

T2.figure = "figaux_24b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_24b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d133"

T2.efficiencyMap.setSource("orig/T2_SR4jt.dat","txt", objectName = "T2_SR4jt.dat", index = None , dataset = "SR4jt")
T2.efficiencyMap.setStatistics( observedN = 0, expectedBG = 2.5 , bgError = 1.0 )

databaseCreator.create(True)





T2.figure = "figaux_25b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_25b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d136"

T2.efficiencyMap.setSource("orig/T2_SR5j.dat","txt", objectName = "T2_SR5j.dat", index = None , dataset = "SR5j")
T2.efficiencyMap.setStatistics( observedN = 121, expectedBG = 126 , bgError = 13 )

databaseCreator.create(True)




T2.figure = "figaux_26b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_26b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d139"

T2.efficiencyMap.setSource("orig/T2_SR6jl.dat","txt", objectName = "T2_SR6jl.dat", index = None , dataset = "SR6jl")
T2.efficiencyMap.setStatistics( observedN = 121, expectedBG = 111 , bgError = 11 )

databaseCreator.create(True)





T2.figure = "figaux_27b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_27b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d142"

T2.efficiencyMap.setSource("orig/T2_SR6jm.dat","txt", objectName = "T2_SR6jm.dat", index = None , dataset = "SR6jm")
T2.efficiencyMap.setStatistics( observedN = 39, expectedBG = 33 , bgError = 6 )

databaseCreator.create(True)





T2.figure = "figaux_28b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_28b.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d145"

T2.efficiencyMap.setSource("orig/T2_SR6jt.dat","txt", objectName = "T2_SR6jt.dat", index = None , dataset = "SR6jt")
T2.efficiencyMap.setStatistics( observedN = 5, expectedBG = 5.2 , bgError = 1.4 )

databaseCreator.create(True)



T2.figure = "figaux_29b"
T2.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_29.png"
T2.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d148"

T2.efficiencyMap.setSource("orig/T2_SR6jt+.dat","txt", objectName = "T2_SR6jt+.dat", index = None , dataset = "SR6jt+")
T2.efficiencyMap.setStatistics( observedN = 6, expectedBG = 4.9 , bgError = 1.6 )

databaseCreator.create(True)



##### T1 ########



T1 = TxNameInput('T1')
#T1.on.checked =
#T1.off.checked =
T1.on.constraint ="[[['jet','jet']],[['jet','jet']]]"
#T1.off.constraint =
T1.on.conditionDescription ="None"
#T1.off.conditionDescription =
T1.on.condition ="None"
#T1.off.condition =

#+++++++ next mass plane block ++++++++++++++
T1 = T1.addMassPlane(motherMass = x, lspMass = y)

T1.figure = "figaux_31b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_31b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d152"

T1.efficiencyMap.setSource("orig/T1_SR2jl.dat","txt", objectName = "T1_SR2jl.dat", index = None , dataset = "SR2jl")
T1.efficiencyMap.setStatistics( observedN = 12315, expectedBG = 13000 , bgError = 1000)

databaseCreator.create(True)


T1.figure = "figaux_32b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_32b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d155"

T1.efficiencyMap.setSource("orig/T1_SR2jm.dat","txt", objectName = "T1_SR2jm.dat", index = None , dataset = "SR2jm")
T1.efficiencyMap.setStatistics( observedN = 715, expectedBG = 760 , bgError = 50 )

databaseCreator.create(True)



T1.figure = "figaux_33b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_33b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d158"

T1.efficiencyMap.setSource("orig/T1_SR2jt.dat","txt", objectName = "T1_SR2jt.dat", index = None , dataset = "SR2jt")
T1.efficiencyMap.setStatistics( observedN = 133, expectedBG = 125 , bgError = 10 )

databaseCreator.create(True)

T1.figure = "figaux_34b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_34b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d161"

T1.efficiencyMap.setSource("orig/T1_SR2jW.dat","txt", objectName = "T1_SR2jW.dat", index = None , dataset = "SR2jW")
T1.efficiencyMap.setStatistics( observedN = 0, expectedBG = 2.3 , bgError = 1.4 )

databaseCreator.create(True)


T1.figure = "figaux_35b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_35b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d164"

T1.efficiencyMap.setSource("orig/T1_SR3j.dat","txt", objectName = "T1_SR3j.dat", index = None , dataset = "SR3j")
T1.efficiencyMap.setStatistics( observedN = 7, expectedBG = 5 , bgError = 1.2 )

databaseCreator.create(True)



T1.figure = "figaux_36b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_36b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d167"

T1.efficiencyMap.setSource("orig/T1_SR4jW.dat","txt", objectName = "T1_SR4jW.dat", index = None , dataset = "SR4jW")
T1.efficiencyMap.setStatistics( observedN = 16, expectedBG = 14 , bgError = 4 )

databaseCreator.create(True)





T1.figure = "figaux_37b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_37b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d170"

T1.efficiencyMap.setSource("orig/T1_SR4jl-.dat","txt", objectName = "T1_SR4jl-.dat", index = None , dataset = "SR4jl-")
T1.efficiencyMap.setStatistics( observedN = 2169, expectedBG = 2120 , bgError = 110 )

databaseCreator.create(True)





T1.figure = "figaux_38b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_38b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d173"

T1.efficiencyMap.setSource("orig/T1_SR4jl.dat","txt", objectName = "T1_SR4jl.dat", index = None , dataset = "SR4jl")
T1.efficiencyMap.setStatistics( observedN = 608, expectedBG = 630 , bgError = 50 )

databaseCreator.create(True)






T1.figure = "figaux_39b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_39b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d176"

T1.efficiencyMap.setSource("orig/T1_SR4jm.dat","txt", objectName = "T1_SR4jm.dat", index = None , dataset = "SR4jm")
T1.efficiencyMap.setStatistics( observedN = 24, expectedBG = 37 , bgError = 6 )

databaseCreator.create(True)






T1.figure = "figaux_40b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_40b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d179"

T1.efficiencyMap.setSource("orig/T1_SR4jt.dat","txt", objectName = "T1_SR4jt.dat", index = None , dataset = "SR4jt")
T1.efficiencyMap.setStatistics( observedN = 0, expectedBG = 2.5 , bgError = 1.0 )

databaseCreator.create(True)





T1.figure = "figaux_41b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_41b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d182"

T1.efficiencyMap.setSource("orig/T1_SR5j.dat","txt", objectName = "T1_SR5j.dat", index = None , dataset = "SR5j")
T1.efficiencyMap.setStatistics( observedN = 121, expectedBG = 126 , bgError = 13 )

databaseCreator.create(True)




T1.figure = "figaux_42b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_42b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d185"

T1.efficiencyMap.setSource("orig/T1_SR6jl.dat","txt", objectName = "T1_SR6jl.dat", index = None , dataset = "SR6jl")
T1.efficiencyMap.setStatistics( observedN = 121, expectedBG = 111 , bgError = 11 )

databaseCreator.create(True)





T1.figure = "figaux_43b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_43b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d188"

T1.efficiencyMap.setSource("orig/T1_SR6jm.dat","txt", objectName = "T1_SR6jm.dat", index = None , dataset = "SR6jm")
T1.efficiencyMap.setStatistics( observedN = 39, expectedBG = 33 , bgError = 6 )

databaseCreator.create(True)





T1.figure = "figaux_44b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_44b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d191"

T1.efficiencyMap.setSource("orig/T1_SR6jt.dat","txt", objectName = "T1_SR6jt.dat", index = None , dataset = "SR6jt")
T1.efficiencyMap.setStatistics( observedN = 5, expectedBG = 5.2 , bgError = 1.4 )

databaseCreator.create(True)



T1.figure = "figaux_45b"
T1.figureUrl = "https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/SUSY-2013-02/figaux_45b.png"
T1.dataUrl = "http://hepdata.cedar.ac.uk/view/ins1298722/d194"

T1.efficiencyMap.setSource("orig/T1_SR6jt+.dat","txt", objectName = "T1_SR6jt+.dat", index = None , dataset = "SR6jt+")
T1.efficiencyMap.setStatistics( observedN = 6, expectedBG = 4.9 , bgError = 1.6 )

databaseCreator.create(True)




#!/usr/bin/env python

"""
.. module:: convert
   :synopsis: uesed to create a new database entry.

.. moduleauthor:: Michael Traub <michael.traub@gmx.at>

"""   

import os
import sys
import argparse
import types
sys.path.append(os.path.abspath('../smodels-utils'))
from smodels_utils.helper.txDecays import TxDecay

def head():
    block =\
    '#!/usr/bin/env python\n' +\
    '\n' +\
    '"""\n' +\
    '.. module:: convert\n' +\
    '   :synopsis: uesed to create info.txt,sms.py,sms.root and newSms.py.\n' +\
    '\n' +\
    '"""\n' +\
    'import sys\n' +\
    'import os\n' +\
    "sys.path.append(os.path.abspath('../../../../smodels-utils'))\n" +\
    'from smodels_utils.dataPreparation.inputObjects import TxName, MetaInfo\n' +\
    'from smodels_utils.dataPreparation.databaseCreation import databaseCreator\n' +\
    'from smodels_utils.dataPreparation.origPlotObjects import x, y\n'
    return block

def infoBlock(experiment, ID, sqrts): 
    block =\
    "\n" +\
    "#+++++++ global info block ++++++++++++++" +\
    "\n" +\
    "info = MetaInfo('%s-%s')\n" %(experiment, ID) +\
    'info.url =\n' +\
    'info.sqrts = %s\n' %sqrts +\
    'info.lumi = \n' +\
    'info.prettyname =\n' +\
    'info.private =\n' +\
    'info.arxiv = \n' +\
    'info.contact =\n' +\
    'info.publication =\n' +\
    'info.comment =\n' +\
    'info.supersedes =\n' +\
    'info.superseded_by =\n' +\
    'info.implemented_by =\n' 
    return block

def txNameBlock(txName):

    block =\
    "\n" +\
    "#+++++++ next txName block ++++++++++++++" +\
    "\n" +\
    "%s = TxName('%s')\n" %(txName, txName) +\
    "%s.on.checked =\n" %txName +\
    "%s.off.checked =\n" %txName +\
    "%s.on.constraint =\n" %txName +\
    "%s.off.constraint =\n" %txName +\
    "%s.on.condition =\n" %txName +\
    "%s.off.condition =\n" %txName +\
    "%s.on.fuzzycondition =\n" %txName +\
    "%s.off.fuzzycondition =\n" %txName 
    return block
    
def planeBlock(planeName):
    
    block =\
    "#----figure----\n" +\
    "%s.figure =\n" %planeName +\
    "%s.figureUrl =\n" %planeName +\
    "#----limit source----\n" +\
    "%s.obsUpperLimit.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.expUpperLimit.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "#----exclusion source----\n" +\
    "%s.obsExclusion.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.obsExclusionM1.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.obsExclusionP1.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.expExclusion.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.expExclusionM1.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "%s.expExclusionP1.setSource( path, type, objectName = None, index = None )\n" %planeName +\
    "#----global url settings ----\n" +\
    "%s.dataUrl =\n" %planeName +\
    "#----limit url settings ----\n" +\
    "%s.histoDataUrl =\n" %planeName +\
    "%s.obsUpperLimit.dataUrl =\n" %planeName +\
    "%s.expUpperlimit.dataUrl =\n" %planeName +\
    "#----exclusion url settings ----\n" +\
    "%s.exclusionDataUrl =\n" %planeName +\
    "%s.obsExclusion.dataUrl =\n" %planeName +\
    "%s.obsExclusionM1.dataUrl =\n" %planeName +\
    "%s.obsExclusionP1.dataUrl =\n" %planeName +\
    "%s.expExclusion.dataUrl =\n" %planeName +\
    "%s.expExclusionM1.dataUrl =\n" %planeName +\
    "%s.expExclusionP1.dataUrl =\n" %planeName 
    return block
    
def addMassPlane_singleDecay(txName, planeName):
    
    block =\
    "\n" +\
    "#+++++++ next mass plane block ++++++++++++++" +\
    "\n" +\
    "%s = %s.addMassPlane(motherMass = , lspMass = )\n" \
    %(planeName, txName)
    return block
    
def addMassPlane_multiDecay(txName, planeName):

    block =\
    "\n" +\
    "#+++++++ next mass plane block ++++++++++++++" +\
    "\n" +\
    "%s = %s.addMassPlane(motherMass = , interMass = , lspMass = )\n"\
    %(planeName, txName)
    return block
    
def food():

    return "databaseCreator.create()"
    
    
def SqrtsAsInteger(sqrts):

    check = sqrts.split('*')
    if len(check) == 2:
        if not check[1].strip() == 'TeV': return False
    try:
        check[0] = float(check[0])
        if not check[0] % 1 == 0.: return False
    except:
        return False
    return int(check[0])

    
    
def checkPath(path, exit = False):
    if os.path.exists(path):
        if exit == True:
            m = 'path: %s already exist.\n' %path
            m = m + 'Please check directory or remove it manually'
            print m
            sys.exit()
        return
    print 'creating path: %s' %path
    os.makedirs(path)
        
        
def createPath(sqrts, experiment, ID):
    
    path = './%sTeV' %sqrts
    checkPath(path)
    path = path + '/%s' %experiment
    checkPath(path)
    path = path + '/%s-%s' %(experiment, ID)
    checkPath(path, exit = True)
    os.makedirs(path + '/orig')
    return path
    
    
def createTxNameDict(txNames):
    
    txNameDict = {}
    txNames = txNames.split(',')
    for txName in txNames:
        txName = txName.strip()
        if not '[' in txName and not ']' in txName:
            planes = None
        else:
            planes = txName[txName.find('[')+1: txName.find(']')]
            planes = planes.strip()
            try:
                planes = int(planes)
            except ValueError:
                m = 'to predefine number of mass planes'
                m  = m + 'use the syntax txName(number as int)'
                print m
                sys.exit()
            txName = txName[:txName.find('[')]
            txName.strip()
        txNameDict[txName] = planes
    return txNameDict
    
    
def checkTxNameDict(txNameDict):

    for txName in txNameDict:
        txDecay = TxDecay(txName)
        if not txDecay:
            m = '%s is no known txName !!\n'  %txName
            m = m + 'make shure there are no typos in the txName\n'
            m = m + 'or add the txName to the decay Dict at helper/txDecays.py'
            print m
            sys.exit()
        interPart = txDecay.intermediateParticles
        if not interPart:
            if txNameDict[txName] and txNameDict[txName] > 1:
                m = '%s have no intermediate partice\n' %txName
                m = m + 'set addional mass planes to 1'
                print m
                txNameDict[txName] = None
        if interPart and not txNameDict[txName]:
            m = '%s have intermediate partices' %txName 
            m = m + ',but addional mass planes not set\n' 
            m = m + 'set addional mass planes to 1'
            print m
            txNameDict[txName] = 1
    return txNameDict
        
        
def main(experiment, ID, sqrts, txNames):
    

    txNameDict = createTxNameDict(txNames)  
    txNameDict = checkTxNameDict(txNameDict)
    sqrts = SqrtsAsInteger(sqrts)
    if not sqrts:
        print 'sqrts must be an integer or integer*TeV'
        sys.exit()
    path = createPath(sqrts, experiment, ID)
    contend = head()
    contend = contend + infoBlock(experiment, ID, sqrts)
    for txName, planes in txNameDict.iteritems():
        contend = contend + txNameBlock(txName)
        if not planes:
            plane = '%s_%s' %(txName, 1)
            contend = contend + addMassPlane_singleDecay(txName, plane)
            contend = contend + planeBlock(plane)
            continue
        for i in range(planes):
            i += 1
            plane = '%s_%s' %(txName, i)
            contend = contend + addMassPlane_multiDecay(txName, plane)
            contend = contend + planeBlock(plane)
    contend = contend + '\n' + food()
    convertPath = path + '/convert.py'
    convert = open(path + '/convert.py','w')
    print 'creating file: %s' %convertPath
    convert.write(contend)
    convert.close

if __name__ == '__main__':
    
    argparser = argparse.ArgumentParser(description = \
    'Produces a template for implimentation of new publication')
    
    argparser.add_argument ('-id', '--ID', \
    help = 'full name of the paper',\
    type = types.StringType)
    
    argparser.add_argument ('-sqrts', '--sqrts', \
    help = 'center of mass energy',\
    type = types.StringType)
    
    argparser.add_argument ('-txNames', '--txNames', \
    help = 'list of txNames, separated by comma, addional numbers of mass planes in brackets ', \
    type = types.StringType)
    
    argparser.add_argument ('-CMS', '--cms', \
    help = 'experiment must be CMS or ATLAS ', \
    action = "store_true")
    
    argparser.add_argument ('-ATLAS', '--atlas', \
    help = 'experiment must be CMS or ATLAS ', \
    action = "store_true")
    
    args = argparser.parse_args()
    
    if args.cms and args.atlas:
        print 'publication can only belong to one experiment'
        sys.exit()
    if not args.cms and not args.atlas:
        print 'no experiment, use -ATLAS or -CMS'
        sys.exit()
    if args.cms: experiment = 'CMS'
    if args.atlas: experiment = 'ATLAS'
    if not args.ID:
        print 'no id, use -id to set'
        sys.exit()
    if not args.sqrts:
        print 'no sqrts, use -sqrts to set'
        sys.exit()
    if not args.txNames:
        print 'no txNames, use -txNames to set'
        sys.exit()
        

    main(experiment, args.ID, args.sqrts, args.txNames)


    
        
        


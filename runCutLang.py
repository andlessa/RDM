#!/usr/bin/env python3

"""Simple code for running CutLang using the output of Delphes."""


#First tell the system where to find the modules:
import sys,os,glob,shutil
from ufo2slha.configParserWrapper import ConfigParserExt
import logging
import subprocess
import time,datetime
import multiprocessing
import tempfile
import pyslha

FORMAT = '%(levelname)s in %(module)s.%(funcName)s() in %(lineno)s: %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def RunAll(parserDict):
    """
    Runs Pythia 8, Delphes and CutLang using the parameters given in parser.

    :param parser: ConfigParser object with all the parameters needed.
    """

    t0 = time.time()
    parser = ConfigParserExt()
    parser.read_dict(parserDict)

    #Get cleanning option:
    doClean = parser.get("options","clean")

    #Get input file and define output files
    inFile = os.path.abspath(parser.get("options","inputFile"))
    outFolder = os.path.abspath(parser.get("options","outputFolder"))
    if not os.path.isdir(outFolder):
        os.makedirs(outFolder)
    hepmcfile = os.path.basename(inFile)
    hepmcfile = hepmcfile.split('.lhe')[0]+'.hepmc'
    hepmcfile = os.path.join(outFolder,hepmcfile)
    rootfile = os.path.join(outFolder,hepmcfile.replace('.hepmc','.root'))

    #Run Pythia 8
    logger.info('Running Pythia 8')
    cfgfile = os.path.abspath(parser.get("Pythia8","cfgfile"))
    pythia8exe = os.path.abspath(parser.get("Pythia8","pythia8exe"))
    pythiaRun = runPythia8(inFile,cfgfile,hepmcfile,pythia8exe)
    if not pythiaRun or not os.path.isfile(hepmcfile):
        logger.error("Error running Pythia 8")
        return "Run for file %s failed" %(inFile)
    logger.info(pythiaRun)

    #Run Delphes
    logger.info('Running Delphes')
    delphescard = os.path.abspath(parser.get("Delphes","delphescard"))
    delphesexe = os.path.abspath(parser.get("Delphes","delphesexe"))
    delphesRun = runDelphes(hepmcfile,delphescard,rootfile,delphesexe)
    if not pythiaRun  or not os.path.isfile(rootfile):
        logger.error("Error running Delphes")
        return "Run for file %s failed" %(inFile)
    logger.info(delphesRun)

    #Run CutLang
    logger.info('Running CutLang')
    adlFile = os.path.abspath(parser.get("CutLang","analysisFile"))
    cutlangexe = os.path.abspath(parser.get("CutLang","cutlangexe"))
    cutlangRun = RunCutLang(rootfile,adlfile,cutlangexe)
    if not cutlangRun:
        logger.error("Error running CutLang")
        return "Run for file %s failed" %(inFile)
    logger.info(cutlangRun)

    if doClean:
        logger.debug("Removing files %s and %s" %(hepmcfile,rootfile))
        os.remove(hepmcfile)
        os.remove(rootfile)
    now = datetime.datetime.now()

    return "Run for file %s done at %s (total run time = %1.2f min)" %(inFile,
                        now.strftime("%Y-%m-%d %H:%M"),(time.time()-t0)/60.)

def runPythia8(lhefile,cfgfile,hepmcfile,pythia8exe):
    """
    Runs Pythia 8 for a given input LHE file and store the Pythia 8 events in HepMC format.

    :param lhefile: Name of LHE input file
    :param cfgfile: Pythia8 configuration file
    :param hepmcfile: Name of output (HepMC) file
    :param pythia8exe: Name of pythia 8 executable
    """

    if not os.path.isfile(pythia8exe):
        logger.error("Pythia executable %s not found. Try running make." %pythia8exe)
        return None

    if not os.path.isfile(lhefile):
        logger.error("LHE input file %s not found." %lhefile)
        return None

    if not os.path.isfile(cfgfile):
        logger.error("Pythia configuration file %s not found." %cfgfile)
        return None

    if os.path.isfile(hepmcfile):
        logger.info("File %s already exists. It will be overwriten." %hepmcfile)
        os.remove(hepmcfile)

    run = subprocess.Popen('%s -f %s -c %s -o %s' %(pythia8exe,lhefile,cfgfile,hepmcfile)
                       ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    output,errorMsg= run.communicate()
    logger.debug('Pythia 8 error:\n %s \n' %errorMsg)
    logger.debug('Pythia 8 output:\n %s \n' %output)
    now = datetime.datetime.now()

    return "Finished running Pythia at %s" %(now.strftime("%Y-%m-%d %H:%M"))

def runDelphes(hepmcfile,delphescard,rootfile,delphesexe):
    """
    Runs Delphes for a given HepMC file and store output in a ROOT file.

    :param hepmcfile: Name of HepMC input file
    :param delphescard: Delphes configuration file
    :param rootfile: Name of output (ROOT) file
    :param delphesexe: Name of Delphes executable
    """

    if not os.path.isfile(delphesexe):
        logger.error("Delphes executable %s not found. Is Delphes installed?" %delphesexe)
        return None

    if not os.path.isfile(hepmcfile):
        logger.error("HepMC input file %s not found." %hepmcfile)
        return None

    if not os.path.isfile(delphescard):
        logger.error("Delphes card %s not found." %delphescard)
        return None

    if os.path.isfile(rootfile):
        logger.info("File %s already exists. It will be overwriten." %rootfile)
        os.remove(rootfile)

    run = subprocess.Popen('%s %s %s %s' %(delphesexe,delphescard,rootfile,hepmcfile)
                       ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    output,errorMsg= run.communicate()
    logger.debug('Delphes error:\n %s \n' %errorMsg)
    logger.debug('Delphes output:\n %s \n' %output)
    now = datetime.datetime.now()

    return "Finished running Delphes at %s" %(now.strftime("%Y-%m-%d %H:%M"))

def RunCutLang(rootfile,adlfile,cutlangexe):
    """
    Run CutLang for the input ROOT file

    :param rootfile: Name of ROOT input file
    :param adlfile: Analysis file
    :param cutlangexe: Name of CutLang script
    """

    ftype = "DELPHES"

    if not os.path.isfile(cutlangexe):
        logger.error("CutLang script %s not found." %cutlangexe)
        return None

    if not os.path.isfile(adlFile):
        logger.error("ADL file %s not found." %adlFile)
        return None

    cutLangFolder = os.path.dirname(cutlangexe)
    cutlang_script = os.path.basename(cutlangexe)

    #Run CutLang
    run = subprocess.Popen('%s %s %s -i %s' %(cutlang_script,rootfile,ftype,adlFile)
                       ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                       cwd=cutLangFolder)
    output,errorMsg= run.communicate()
    logger.debug('CutLang error:\n %s \n' %errorMsg)
    logger.debug('CutLang output:\n %s \n' %output)

    now = datetime.datetime.now()

    return "Finished running CutLang at %s" %(now.strftime("%Y-%m-%d %H:%M"))


def main(parfile,verbose):
    """
    Submit parallel jobs using the parameter file.

    :param parfile: name of the parameter file.
    :param verbose: level of debugging messages.
    """
    level = args.verbose.lower()
    levels = { "debug": logging.DEBUG, "info": logging.INFO,
               "warn": logging.WARNING,
               "warning": logging.WARNING, "error": logging.ERROR }
    if not level in levels:
        logger.error ( "Unknown log level ``%s'' supplied!" % level )
        sys.exit()
    logger.setLevel(level = levels[level])

    parser = ConfigParserExt()
    ret = parser.read(parfile)
    if ret == []:
        logger.error( "No such file or directory: '%s'" % parfile)
        sys.exit()

    if not parser.has_option('options', 'input'):
        logger.error("An input file or folder must be defined.")
        sys.exit()
    else:
        inputF = parser.get('options','input')
        if os.path.isfile(inputF):
            inputFiles = [os.path.abspath(inputF)]
        elif "*" in inputF:
            inputFiles = [os.path.abspath(f) for f in glob.glob(inputF)]
        elif os.path.isdir(inputF):
            inputFiles = [os.path.abspath(os.path.join(inputF,f))
                          for f in os.listdir(inputF)
                          if os.path.isfile(os.path.join(inputF, f))]
        else:
            logger.error("Input format %s not accepted" %inputF)
            sys.exit()

    parserList = []
    for f in inputFiles:
        newParser = ConfigParserExt()
        newParser.read_dict(parser.toDict(raw=True))
        newParser.set("options","inputFile",f)
        parserList.append(newParser)

    ncpus = int(parser.get("options","ncpu"))
    if ncpus  < 0:
        ncpus =  multiprocessing.cpu_count()
    ncpus = min(ncpus,len(parserList))
    pool = multiprocessing.Pool(processes=ncpus)
    children = []
    #Loop over parsers and submit jobs
    logger.info("Submitting %i jobs over %i cores" %(len(parserList),ncpus))
    for newParser in parserList:
        logger.debug("Submitting job for file %s"
                    %(newParser.get("options","inputFile")))
        parserDict = newParser.toDict(raw=False) #Must convert to dictionary for pickling
        p = pool.apply_async(RunAll, args=(parserDict,))
        children.append(p)
        time.sleep(2)


    #Wait for jobs to finish:
    output = [p.get() for p in children]
    for out in output:
        print(out)

if __name__ == "__main__":

    import argparse
    ap = argparse.ArgumentParser( description=
            "Run CutLang for ROOT file created by Delphes." )
    ap.add_argument('-p', '--parfile', default='cutlang_parameters.ini',
            help='path to the parameters file. Default is cutlang_parameters.ini')
    ap.add_argument('-v', '--verbose', default='error',
            help='verbose level (debug, info, warning or error). Default is error')


    t0 = time.time()

    args = ap.parse_args()

    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))

#!/usr/bin/env python3

"""
Simple code for computing the combined upper limit for a given signal over several signal regions (bins).

It assumes the simplified likelihood framework, using
the covariant matrix for all signal regions.
"""

from simplifiedLikelihoods import Data, UpperLimitComputer
import sys, os
import numpy as np
import logging
import multiprocessing
FORMAT = '%(levelname)s in %(module)s.%(funcName)s() in %(lineno)s: %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def addCombinedRTo(checkmateOutput,deltas_rel=0.2):
    """
    Compute the combined limit for CMS-SUS-16-032 using the
    data from CheckMate output (total_results.txt). Add the result as a new line
    in the output with the combined r-value assuming zero signal uncertainty (robs)
    and 20% uncertainty (robscons).

    :param checkmateOutput: CheckMate output file (total_results.txt)
    :param deltas_rel: Relative uncertainty for the number of signal events.

    :return: True if succesful, False otherwise
    """

    # Specify the ordering of the signal regions as used in the covariance matrix for CMS-SUS-16-032
    SRsNC = ['HT_200_MCT_150', 'HT_1000_MCT_150', 'HT_1000_MCT_250', 'HT_1000_MCT_350',
     'HT_1000_MCT_450', 'HT_1000_MCT_600', 'HT_1000_MCT_800', 'HT_200_MCT_250',
     'HT_200_MCT_350', 'HT_200_MCT_450', 'HT_500_MCT_150', 'HT_500_MCT_250', 'HT_500_MCT_350',
     'HT_500_MCT_450', 'HT_500_MCT_600']

    SRsC = ['1b_ETmiss_250', '2b_ETmiss_500', '2b_ETmiss_500_HT_100', '1c_ETmiss_250',
     '1c_ETmiss_300', '1c_ETmiss_500', '1c_ETmiss_750', '1c_ETmiss_1000', '2c_ETmiss_250',
     '2c_ETmiss_250_HT_100', '2c_ETmiss_300', '1b_ETmiss_300', '2c_ETmiss_300_HT_100',
     '2c_ETmiss_500', '2c_ETmiss_500_HT_100', '2c_ETmiss_750', '2c_ETmiss_750_HT_100',
     'NSV_ETmiss_250', 'NSV_ETmiss_300', 'NSV_ETmiss_500', 'NSV_ETmiss_750', 'NSV_ETmiss_1000',
     '1b_ETmiss_500', '0b_ETmiss_300', '0b_ETmiss_500', '0b_ETmiss_750', '0b_ETmiss_1000',
     '0b_ETmiss_1250', '1b_ETmiss_750', '1b_ETmiss_1000', '2b_ETmiss_250',
     '2b_ETmiss_250_HT_100', '2b_ETmiss_300', '2b_ETmiss_300_HT_100']

    # Get covariance matrix for non-compressed signal regions:
    covNC = CovarianceHandler(filename = './CMS_data/CMS-SUS-16-032_Figure-aux_003.root',
                            histoname = 'Canvas_1/Cov', max_datasets=None,
                            aggregate = None , triangular=True)
    # Get covariance matrix for compressed signal regions:
    covC = CovarianceHandler(filename = './CMS_data/CMS-SUS-16-032_Figure-aux_004.root',
                            histoname = 'Canvas_1/Cov', max_datasets=None,
                            aggregate = None , triangular=True)
    # Get singal regions info
    SRs = np.genfromtxt('./CMS_data/cms_sus_16_032_SRs.txt',names=True,dtype=None,encoding='utf-8')
    SRdict = dict([[pt['sr'],pt] for pt in SRs])

    if not os.path.isfile(checkmateOutput):
        print("Files %s not found" %checkmateOutput)
        return False

    # Get CMS-SUS-16-032 data:
    data = np.genfromtxt(checkmateOutput,names=True,
            dtype=None,encoding=None)
    #Remove combined line, if exists:
    data = np.delete(data,np.where((data['analysis'] == 'cms_sus_16_032') & (data['sr'] == 'Combined')))
    data = np.delete(data,np.where((data['analysis'] == 'cms_sus_16_032') & (data['sr'] == 'Combined_comp')))
    data = np.delete(data,np.where((data['analysis'] == 'cms_sus_16_032') & (data['sr'] == 'Combined_noncomp')))
    cmsData = data[np.where(data['analysis'] == 'cms_sus_16_032')]
    # If the analysis is not found, return
    if len(cmsData) == 0:
        return False

    #Add combination of non-compressed signal regions:
    cov = covNC
    SRs = SRsNC
    robsComb_NC = getCombinedR(cmsData,cov,SRs,deltas_rel=0.0,SRdict=SRdict,expected=False)
    rexpComb_NC = getCombinedR(cmsData,cov,SRs,deltas_rel=0.0,SRdict=SRdict,expected=True)
    #Reproduce CheckMATE computation of conservative robs using an estimate of the signal
    #uncertainty effect:
    robsconComb_NC = robsComb_NC*(1.0-1.64*deltas_rel)

    #Add combination of compressed signal regions:
    cov = covC
    SRs = SRsC
    robsComb_C = getCombinedR(cmsData,cov,SRs,deltas_rel=0.0,SRdict=SRdict,expected=False)
    rexpComb_C = getCombinedR(cmsData,cov,SRs,deltas_rel=0.0,SRdict=SRdict,expected=True)
    #Reproduce CheckMATE computation of conservative robs using an estimate of the signal
    #uncertainty effect:
    robsconComb_C = robsComb_C*(1.0-1.64*deltas_rel)


    ilast = max([i for i,pt in enumerate(data) if pt['analysis'] == 'cms_sus_16_032'])
    pt_NC = data[ilast].copy()
    pt_C = data[ilast].copy()
    for name in data.dtype.names:
        if name == 'sr':
            pt_NC[name] = 'Combined_noncomp'
            pt_C[name]= 'Combined_comp'
        elif name == 'robs':
            pt_NC[name] = robsComb_NC
            pt_C[name]= robsComb_C
        elif name == 'robscons':
            pt_NC[name] = robsconComb_NC
            pt_C[name]= robsconComb_C
        elif name == 'rexp':
            pt_NC[name] = rexpComb_NC
            pt_C[name]= rexpComb_C
        elif name == 'analysis':
            pt_NC[name] = 'cms_sus_16_032'
            pt_C[name] = 'cms_sus_16_032'
        else:
            pt_NC[name] = 0.0
            pt_C[name] = 0.0

    dataNew = np.insert(data,ilast+1,pt_NC)
    dataNew = np.insert(dataNew,ilast+2,pt_C)

    #Add combined result to total_results.txt:
    analysisSize = str(max([len(pt['analysis']) for pt in dataNew])+2)
    srsSize = str(max([len(pt['sr']) for pt in dataNew])+2)
    other = 9
    header = ''
    fmt = []
    for name in dataNew.dtype.names:
        if name == 'analysis':
            header += '%-'+analysisSize+'s'
            fmt.append('%-'+analysisSize+'s')
        elif name == 'sr':
            header += '%-'+srsSize+'s'
            fmt.append('%-'+srsSize+'s')
        else:
            l = max(other,len(name))+2
            header += '%-'+str(l)+'s'
            fmt.append('%1.3e'+' '*(l-10))

    header = header %dataNew.dtype.names

    np.savetxt(checkmateOutput,dataNew,header=header,fmt = fmt)

    return True


def getCombinedR(data,cov,orderSRs,deltas_rel=0.,SRdict=None, expected=False):
    """
    Compute a combined r-value using the covariance matrix.

    :param data: 2-d numpy array with number of observed events (obs),
                 number of signal events (s),
                 number of expected background events (bkg) for each
                 signal region (sr)
    :param cov: covariace matrix (CovarianceHandler object)
    :param orderSRs: lists of SR strings in the same order used
                     for the covariance matrix
    :param deltas_rel: Relative uncertainty for the number of signal events.
    :param SR_dict: Optional dictionary containing the number of observed events ('obs') and
                    expected events ('bkg') for each signal region. If not defined, this information
                    will assume to be defined in data.

    :return: Combined r-value (sum(nsig)/ul_combined)
    """
    nobs = [0]*len(orderSRs)
    nsig = [0]*len(orderSRs)
    bg = [0]*len(orderSRs)
    # Get ordered data for the specified SRs
    for pt in data:
        if not pt['sr'] in orderSRs:
            continue
        i = orderSRs.index(pt['sr'])
        nsig[i] = pt['s']
        if SRdict is None:
            nobs[i] = int(pt['obs'])
            bg[i] = pt['bkg']
        else:
            nobs[i] = int(SRdict[pt['sr']]['obs'])
            bg[i] = SRdict[pt['sr']]['bkg']

    #In case no SRs are found:
    if sum(nsig) == 0:
        return 0.0

    #Compute the combined upper limit
    ul = getCombinedUpperLimitFor(nobs, bg, nsig,
                    cov.covariance, deltas_rel, expected)

    #Compute the new r-value:
    r = sum(nsig)/ul

    return r


def getCombinedUpperLimitFor(nobs, bg, nsig, cov, deltas_rel=0.2, expected=False):
    """
    Get combined upper limit.

    :param nobs: list of observed events in each signal region. The list
                    should obey the ordering in the covariance matrix.
    :param bg: list of expected BG events in each signal region. The list
                    should obey the ordering in the covariance matrix.
    :param nsig: list of signal events in each signal region. The list
                    should be consistent with the covariance matrix.
    :param deltas_rel: relative uncertainty in signal (float). Default value is 20%.
    :returns: upper limit on the number of signal events summed over all signal regions
    """
    computer = UpperLimitComputer(ntoys=10000)

    ulObs = computer.ulSigma(Data(observed=nobs, backgrounds=bg, covariance=cov,
                                 third_moment=None, nsignal=nsig, deltas_rel=deltas_rel),
                           marginalize=False, expected=expected)

    return ulObs



class CovarianceHandler:
    """Basic class to handle convariance matrices."""

    def __init__ ( self, filename, histoname, max_datasets=None,
                   aggregate = None , triangular=False):
        """Load the covariance matrix from ROOT file."""
        import ROOT
        f=ROOT.TFile(filename)
        h=self.getHistogram(f, histoname)
        xaxis = h.GetXaxis()
        self.n=h.GetNbinsX()+1
        if max_datasets:
            self.n=min(max_datasets+1,self.n)
        self.datasetOrder = []
        self.covariance = []
        self.blinded_regions = []
        for i in range ( 1, self.n ):
            if i in self.blinded_regions:
                continue
            self.datasetOrder.append(xaxis.GetBinLabel(i))
            row = []
            for j in range ( 1, self.n ):
                if j in self.blinded_regions:
                    continue
                el = h.GetBinContent(i,j)
                if i==j and el < 1e-4:
                   print( "variance in the covariance matrix at position %d has a very small (%g) value" % (i,el) )
                   el = 1e-4
                row.append(el)
            self.covariance.append(row)

        if aggregate != None:
            ## aggregate the stuff
            self.aggregateThis(aggregate)

        if triangular:
            c = np.array(self.covariance)
            if (np.triu(c) == c).all() or (np.tril(c) == c).all():
                self.covariance = c + c.transpose() - np.diag(np.diag(c))
                self.covariance = self.covariance.tolist()
        self.checkCovarianceMatrix()

    def computeAggCov(self, agg1, agg2 ):
        """Compute the covariance between agg1 and agg2."""
        C=0.
        for i in agg1:
            for j in agg2:
                C+=self.covariance[i-1][j-1]
        return C

    def checkCovarianceMatrix( self ):
        """Quick check if the covariance matrix is invertible."""
        from simplifiedLikelihoods import Data
        n=len(self.covariance)
        m=Data( [0.]*n, [0.]*n, self.covariance )
        # print( "Check %d-dim covariance matrix for positive definiteness." % n)
        try:
            I=(m.covariance)**(-1)
        except Exception as e:
            print( "Inversion failed. %s" % e)
            sys.exit()
        try:
            from scipy import stats
            l=stats.multivariate_normal.logpdf([0.]*n,mean=[0.]*n,cov=m.covariance)
        except Exception as e:
            import numpy
            print( "computation of logpdf failed: %s" % e )
            print( "the diagonal reads: %s " % ( numpy.diag ( m.covariance ) ) )
            sys.exit()

    def getHistogram( self, f, histoname ):
        """Retrieve histogram.

        :param f: filehandle
        """
        h=f.Get ( histoname )
        if h: return h
        if not "/" in histoname:
            print( "cannot find %s in %s" % (histoname, f.GetName()))
            sys.exit()
        tokens = histoname.split("/")
        if not len(tokens)==2:
            print("cannot interpret histoname %s in %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        c= f.Get ( tokens[0] )
        if not c:
            print( "cannot retrieve %s from %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        if c.ClassName() == "TCanvas":
            h=c.GetPrimitive ( tokens[1] )
            if h: return h
            print( "cannot retrieve %s from %s" % \
                            ( histoname, f.name ) )
            sys.exit()
        print( "cannot interpret %s in %s" % \
                        ( histoname, f.name ) )
        sys.exit()

if __name__ == "__main__":

    import argparse
    ap = argparse.ArgumentParser( description=
            "Compute combined limit and add to checkmate output" )
    ap.add_argument('-f', '--file', required = True,
            help='CheckMate output file (total_result.txt) or folder containing total_result.txt files')
    ap.add_argument('-n', '--ncpu', required = False, default = 1, type = int,
            help='Number of jobs to run (if running over multiple files)')
    ap.add_argument('-v', '--verbose', default='error',
            help='verbose level (debug, info, warning or error). Default is error')

    args = ap.parse_args()
    level = args.verbose.lower()
    levels = { "debug": logging.DEBUG, "info": logging.INFO,
               "warn": logging.WARNING,
               "warning": logging.WARNING, "error": logging.ERROR }
    if not level in levels:
        logger.error ( "Unknown log level ``%s'' supplied!" % level )
        sys.exit()
    logger.setLevel(level = levels[level])



    import time
    t0 = time.time()

    #Get number of files:
    if os.path.isfile(args.file):
        files = [os.path.abspath(args.file)]
    elif os.path.isdir(args.file):
        files = []
        for root, dirs, fnames in os.walk(args.file):
            for f in fnames:
                if f == 'total_results.txt':
                     files.append(os.path.abspath(os.path.join(root, f)))
                     break
    if not files:
        logger.warning("No files found.")
        sys.exit()

    ncpus = args.ncpu
    if ncpus  < 0:
        ncpus =  multiprocessing.cpu_count()
    ncpus = min(ncpus,len(files))

    pool = multiprocessing.Pool(processes=ncpus)
    children = []
    #Loop over parsers and submit jobs
    logger.info("Submitting %i jobs over %i cores" %(len(files),ncpus))
    for f in files:
        logger.debug("Submitting job for file %s" %f)
        p = pool.apply_async(addCombinedRTo, args=(f,))
        children.append(p)
        time.sleep(0.01)

    #Wait for jobs to finish:
    output = [p.get() for p in children]
    print("Done in %3.2f min" %((time.time()-t0)/60.))
